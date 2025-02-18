import logging
import argparse
from pathlib import Path
import shutil
import subprocess

import gt2gpx
import geocode

log = logging.getLogger(__name__)


def _parse_arguments():
    parser = argparse.ArgumentParser(description="Automated GPS Toolchain")
    parser.add_argument(
        "photos_path", help="Path of the directory containing the photos"
    )
    parser.add_argument("--backup", "-b", dest="backup_path", help="Backup path")
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_const",
        const=logging.DEBUG,
        default=logging.INFO,
        help="Display debugging information in the output",
    )
    parser.add_argument(
        "--skip-download",
        "-s",
        action="store_true",
        help="Skip GPS track download and use existing GPX file",
    )

    return parser.parse_args()


def _generate_gpx_filename(photos_path: Path) -> Path:
    filename = photos_path.name
    if not filename:
        raise Exception("Unable to compute filename from photo path")
    # Add extension
    filename = filename + ".gpx"

    full_filename = photos_path.joinpath(filename)
    return full_filename


def _download_track(destination_file: Path) -> None:
    # Connection
    log.info("Downloading track...")
    connection = gt2gpx.connections.get_connection(
        gt2gpx.connections.CONNECTION_TYPE_USB
    )
    gt2gpx.download_track(connection, destination_file)
    log.info("Downloaded GPS track to: %s", destination_file)


def _backup(source_file: Path, backup_path: str) -> None:
    if backup_path and source_file:
        filename = source_file.name
        backup_file = Path(backup_path).joinpath(filename)
        if backup_file.exists():
            raise Exception("Backup for GPX track already exists")

        shutil.copy2(source_file, backup_file)
        log.info("Backup done to: %s", backup_file)
    else:
        log.info("Backup skipped")


def _geotag_photos(gpx_file: Path, photos_path: Path) -> None:
    # ORF
    # exiftool -geotag "$GPX_FILE" '-geotime<${DateTimeUTC}+00:00' -P *.ORF -srcfile %d%f.xmp -srcfile @ -o %d%f.xmp
    result = subprocess.run(
        " ".join(
            [
                "exiftool",
                "-geotag",
                '"' + str(gpx_file) + '"',
                "'-geotime<${DateTimeUTC}+00:00'",
                "-P",
                "*.ORF",
                "-srcfile",
                "%d%f.xmp",
                "-srcfile",
                "@",
                "-o",
                "%d%f.xmp",
            ]
        ),
        cwd=photos_path,
        capture_output=True,
        shell=True,
    )
    log.info(result)
    # result.check_returncode()
    log.info(result.stdout)

    # DNG with camera set to UTC timezone
    # exiftool -geotag "$GPX_FILE" '-geotime<${DateTimeOriginal}+00:00' -P *.DNG -srcfile %d%f.xmp -srcfile @ -o %d%f.xmp
    result = subprocess.run(
        " ".join(
            [
                "exiftool",
                "-geotag",
                '"' + str(gpx_file) + '"',
                "'-geotime<${DateTimeOriginal}+00:00'",
                "-P",
                "*.DNG",
                "-srcfile",
                "%d%f.xmp",
                "-srcfile",
                "@",
                "-o",
                "%d%f.xmp",
            ]
        ),
        cwd=photos_path,
        capture_output=True,
        shell=True,
    )
    log.info(result)
    # result.check_returncode()
    log.info(result.stdout)

    return


def _reverse_geocode(photos_path: Path) -> None:
    files_to_list = str(photos_path.joinpath("*.xmp"))
    geocode.geocode_files([files_to_list])
    log.info("Finished geocoding")


def main() -> None:
    arguments = _parse_arguments()
    logging.basicConfig(level=arguments.verbose)
    photos_path = Path(arguments.photos_path)

    dest_gpx = _generate_gpx_filename(photos_path)
    
    if arguments.skip_download:
        if not dest_gpx.exists():
            raise Exception(f"GPX file not found at expected location: {dest_gpx}")
        log.info("Using existing GPX file: %s", dest_gpx)
    else:
        if dest_gpx.exists():
            raise Exception("GPX track already exists")
        _download_track(dest_gpx)
        
    _backup(dest_gpx, arguments.backup_path)
    _geotag_photos(dest_gpx, photos_path)
    _reverse_geocode(photos_path)


if __name__ == "__main__":
    main()

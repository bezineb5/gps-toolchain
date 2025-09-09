# Automatic geotagging

## Features
This simple script helps me to geotag my photos easily. The key features are:
* Downloads GPS tracks from an iGotU device
* Converts NMEA files to GPX format
* Geotag the photos with the track. Currently, it looks for ORF (Olympus raw files) and DNG files but the script can be adapted to other file formats. It stores the metadata in a sidecar XMP file.
* Reverse geocode the photos

## Dependencies
The script requires the following Python packages:
* `gt2gpx` - for downloading GPS tracks from iGotU devices
* `geocode` - for reverse geocoding photos
* `nmea2gpx` - for converting NMEA files to GPX format

External dependencies:
* `exiftool` - for reading and writing photo metadata

## How to use
```
usage: autogps.py [-h] [--backup BACKUP_PATH] [--verbose] [--nmea-input NMEA_INPUT] [--skip-download] photos_path

Automated GPS Toolchain

positional arguments:
  photos_path           Path of the directory containing the photos

optional arguments:
  -h, --help            show this help message and exit
  --backup BACKUP_PATH, -b BACKUP_PATH
                        Backup path
  --nmea-input NMEA_INPUT
                        Path of the NMEA file(s) to convert to GPX. This can be a file pattern to convert multiple files in one go. they will be processed in alphabetical order.
  --skip-download, -s   Skip GPS track download and use existing GPX file
  --verbose, -v         Display debugging information in the output
```

Examples:
```
# Basic usage with iGotU device
python3 autogps.py --backup /my/backup/dir /path/to/my/vacation-photos

# Using NMEA files instead of iGotU device
python3 autogps.py --nmea-input "*.nmea" --backup /my/backup/dir /path/to/my/vacation-photos

# Skip download and use existing GPX file
python3 autogps.py --skip-download --backup /my/backup/dir /path/to/my/vacation-photos
```

It will create a GPX file named "vacation-photos.gpx" in /path/to/my/vacation-photos, with a copy in /my/backup/dir. All ORF and DNG files in /path/to/my/vacation-photos will be geotagged and will have the address in the metadata, stored in a sidecar XMP file.

## Capture One scripts
In the script directory of this repository, there are 2 scripts to make it easier to use in Capture One 11 (Mac OS only):
* Clear GPS content: clears the content of the iGotU device
* Geotag for GPS: calls the script to geotag an entire session. You have to select an image first, so that the script knows where the images are located on the disk. To enable backup, set the variable "backupPath" to your backup directory.

## Build wheel

First, install the build tools:
```
pip install build
```

Then build the wheel:
```
python3 -m build
```

## Install wheel
```
pip install dist/gps_toolchain-0.3-py3-none-any.whl
```

## Run
```
python3 autogps.py --backup /my/backup/dir /path/to/my/vacation-photos
```
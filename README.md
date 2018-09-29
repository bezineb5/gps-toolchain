# Automatic geotagging

## Features
This simple script helps me to geotag my photos easily. The key features are:
* Downloads GPS tracks from an iGotU device
* Geotag the photos withthe track. Currently, it looks for ORF (Olympus raw files) but the script can be adapted to other file formats. It stored the metadata in a sidecar XMP file.
* Reverse geocode the photos

## How to use
```
usage: autogps.py [-h] [--backup BACKUP_PATH] [--verbose] photos_path

Automated GPS Toolchain

positional arguments:
  photos_path           Path of the directory containing the photos

optional arguments:
  -h, --help            show this help message and exit
  --backup BACKUP_PATH, -b BACKUP_PATH
                        Backup path
```

Example:
```
python3 autogps.py --backup /my/backup/dir /path/to/my/vacation-photos
```

It will create a GPX file named "vacation-photos.gpox" in /path/to/my/vacation-photos, with a copy in /my/backup/dir. All ORF files in /path/to/my/vacation-photos will be geotagged and will have the address  in the metadata, soted in a sidecar XMP file.

## Capture One scripts
In the script directory of this repository, there are 2 scripts to make it easier to use in Capture One 11 (Mac OS only):
* Clear GPS content: clears the content of the iGotU device
* Geotag for GPS: calls the script to geotag an entire session. You have to select an image first, so that the script knows where the images are located on the disk. To enable backup, set the variable "backupPath" to your backup directory.
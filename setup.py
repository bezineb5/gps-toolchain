# gps-toolchain <https://github.com/bezineb5/gps-toolchain>
# Copyright 2018 Benjamin Bezine

# This file is part of gps-toolchain.
#
# gps-toolchain is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the licence, or
# (at your option) any later version, or the BSD licence.
#
# gps-toolchain is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENCE for more details.

from distutils.core import setup

setup(name="gps-toolchain",
      version="0.1",
      description="Reverse geocoding library for photos",
      license="MIT",
      author="Benjamin Bezine",
      url="https://github.com/bezineb5/gps-toolchain",
      install_requires=[
      ],
      dependency_links=[
        "git+ssh://git@github.com/bezineb5/reverse-geocoder.git",
        "git+ssh://git@github.com/bezineb5/pygotu.git",
      ],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
          "Programming Language :: Python :: 3.5",
          "Topic :: Multimedia"],
      py_modules=["autogps"])

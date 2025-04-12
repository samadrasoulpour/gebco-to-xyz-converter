# GEBCO NetCDF to XYZ Converter

A Python tool to convert GEBCO bathymetry data from NetCDF format to XYZ format compatible with MIKE by DHI software.

## Features

- Converts GEBCO NetCDF files to simple XYZ format
- Option to filter only negative values (depths) or include all elevations
- Command line interface for easy integration in workflows

## Installation

1. Clone this repository:
>> git clone https://github.com/yourusername/gebco-to-xyz.git
>> cd gebco-to-xyz
   
3. Install requirements:
>> pip install -r requirements.txt

## Usage
Basic conversion (only negative/depth values):
>> python -m gebco_to_xyz.converter input.nc output.xyz

Include all elevation values (positive and negative):
>> python -m gebco_to_xyz.converter input.nc output.xyz --include-positive
## Requirements
Python 3.6+
netCDF4
numpy



import numpy as np
import netCDF4
from pathlib import Path


def convert_gebco_to_xyz(input_file, output_file, filter_positive=True):
    """
    Convert GEBCO NetCDF file to XYZ format.
    
    Args:
        input_file (str): Path to input NetCDF file
        output_file (str): Path to output XYZ file
        filter_positive (bool): If True, only outputs negative values (depths)
    """
    try:
        # Open NetCDF file
        with netCDF4.Dataset(input_file) as dataset:
            print("File metadata:")
            print(dataset)
            
            # Extract variables
            lat = dataset.variables['lat'][:]
            lon = dataset.variables['lon'][:]
            elev = dataset.variables['elevation'][:]
            
            # Convert to numpy arrays
            x = np.array(lon)
            y = np.array(lat)
            z = np.array(elev)
            
            # Write to XYZ file
            with open(output_file, 'w') as f:
                for i in range(len(x)):
                    for j in range(len(y)):
                        if not filter_positive or z[j, i] < 0:
                            f.write(f"{x[i]} {y[j]} {z[j, i]}\n")
            
        print(f"Conversion successful. Output saved to {output_file}")
        
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        raise


if __name__ == "__main__":
    import argparse
    
    # Set up command line interface
    parser = argparse.ArgumentParser(
        description="Convert GEBCO NetCDF bathymetry data to XYZ format for MIKE by DHI"
    )
    parser.add_argument("input", help="Input NetCDF file path")
    parser.add_argument("output", help="Output XYZ file path")
    parser.add_argument("--include-positive", action="store_true",
                      help="Include positive elevation values (default: only negative/depth values)")
    
    args = parser.parse_args()
    
    # Run conversion
    convert_gebco_to_xyz(
        input_file=args.input,
        output_file=args.output,
        filter_positive=not args.include_positive
    )

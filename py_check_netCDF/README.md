Script to check if a netCDF file conforms to the [ATOMIX](https://wiki.app.uib.no/atomix/) standard.

Usage
-----

A netCDF file can be checked by invoking the script with the filename of the netCDF file, for example:

    python atomix_netcdf_check.py MSS_Baltic.nc

All options
-----------

An overview about all options can be listed by:

    python python3 atomix_netcdf_check.py -h


This will display the options

    Welcome to atomix_netcdf_check version 0.6
    usage: atomix_netcdf_check.py [-h] [--verbose] [--metadata] [--variables] [--datalevel DATALEVEL]
                                  [--required REQUIRED] [--print_variables]
                                  [filename]
    
    positional arguments:
      filename              The netCDF filename to be checked
    
    options:
      -h, --help            show this help message and exit
      --verbose, -v         Verbosity, can be added multiple times, if argument is not called: loglevel=INFO, once:
                            both missing and found variables are printed, twice: loglevel=DEBUG
      --metadata            Add if metadata shall be checked
      --variables           Add if variables shall be checked
      --datalevel DATALEVEL
                            List of datalevel to be checked, if not set, all level will be checked, equal to
                            --datalevel="L1_converted,L2_cleaned,L3_spectra,L4_dissipation"
      --required REQUIRED   List of requirement levels to be checked, if not set, all level will be checked, equal to
                            --required="required,highly-recommended,optional"
      --print_variables     Prints the ATOMIX structure to the command line in a csv format


CSV list of netCDF Dimensions, Variables and Metadata
-----------------------------------------------------

To print a csv formatted output of the dimensions, variables and metadata call

    atomix_netcdf_check.py --print_variables

The output can be for example read with a spreadsheat program.

Files
-----
[atomix_netcdf_check.py](./atomix_netcdf_check.py) Atomix netCDF check script 

[atomix_structure.py](./atomix_structure.py) Atomix data structure definition 


Limitations
-----------
Version 0.6 does not support required either/or variables, an [example](https://wiki.app.uib.no/atomix/index.php?title=Level_3_data_(shear_probes)) are ACC or VIB variables, defined as N_***_SENSORS in the specification.
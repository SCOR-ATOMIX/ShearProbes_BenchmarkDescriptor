"""
Python software to check Atomix netCDF files for consistency

author(s): Peter Holtermann (peter.holtermann@io-warnemuende.de)


This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or any
later version.

"""

import logging
import sys
import os
import argparse
import netCDF4
from atomix_structure import atomix_structure


version= '0.6'
# Setup logging module
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger('atomix')




def atomix_atomix_structure_csv(req_levels=['required','highly-recommended','optional']):
    """
        Prints the atomix structure in a csv format

        Returns:

    """

    print('ATOMIX Version:\n{:s}\n'.format(atomix_structure['info']['version']))
    print('ATOMIX Version description:\n{:s}\n'.format(atomix_structure['info']['version_description']))
    print('================ Dimensions =================')
    for dlevel in atomix_structure['datalevels'].keys():
        datalevel = atomix_structure['datalevels'][dlevel]
        # DIMENSIONS
        DIMENSIONS = datalevel['DIMENSIONS']
        print('------')
        for dimname in DIMENSIONS:
            print(' "{:s}" , "{:s}" , "{:s}"'.format(dimname,dlevel,DIMENSIONS[dimname]['description']))

    print('================ Variables =================')
    for dlevel in atomix_structure['datalevels'].keys():
        # Print the Variables
        datalevel = atomix_structure['datalevels'][dlevel]
        VARIABLES = datalevel['VARIABLES']
        print('------')
        for req in req_levels:
            for varname in VARIABLES:
                var = VARIABLES[varname]
                # print(var,varname)
                if var['required'] == req:  # Check if the requirement level fits
                    stdname = var['standard_name']
                    units = var['units']
                    dims = ''
                    for d in var['DIMENSIONS']:
                        #print('var',varname,'d',d)
                        dims += d['name'] + ';'

                    dims = dims[:-1]
                    print('"{:s}","{:s}","{:s}","{:s}","{:s}","{:s}"'.format(varname,dlevel,req,stdname,units,dims))


def atomix_check_requirements_variables(nc, datalevel = None, req_levels=['required','highly-recommended','optional'], plot_found = False):
    """
    Checks if the netCDF file fulfills the requirements of an Atomix netCDF file.

    Returns:

    """
    funcname = 'atomix_check_requirements_variables():'
    groups_atomix = list(atomix_structure['datalevels'].keys())
    if datalevel is None:
        groups = list(atomix_structure['datalevels'].keys())
    else:
        groups = datalevel

    groups_found = []
    for g in nc.groups.keys():
        flag_check = False
        flag_atomix_standard = g in groups_atomix
        if g in groups:
            flag_check = True
            groups_found.append(g)

        logger.info(' Found datalevel {:s} which is ATOMIX standard: {:s} and will be checked: {:s}'.format(g,str(flag_atomix_standard),str(flag_check)))

    #logger.debug(funcname + ' Found {:d} ATOMIX level of data {:s}'.format(len(groups_found),str(groups_found)))
    for req_level in req_levels:
       req_str = ' ================Checking variables with requirement: {:s}================='.format(req_level)
       logger.info(req_str)
       # Fill a dictionary with the requirements of variables
       variable_required = {}
       for g in groups:
           variable_required[g] = []
           for var in atomix_structure['datalevels'][g]['VARIABLES'].keys():
               req = atomix_structure['datalevels'][g]['VARIABLES'][var]['required']
               if req_level in req:
                   variable_required[g].append(var)
               #else:
               #    try: # Check if there are XOR variables
               #        xor_vars = atomix_structure['datalevels'][g]['VARIABLES'][var]['required']['XOR']
               #    except:
               #        xor_vars = None
               #    if xor_vars is not None:
               #        print('Variable is not existing, checking ')
               #    print('fdf')

       # Check requirements
       variables_req_found = {}
       variables_req_notfound = {}
       variables_req_notfound_but_or_existing = {}
       for g in groups_found:
           infostr = ' ----------------{:s}-------------------'.format(g)
           infostr += '-' * (len(req_str) - len(infostr))
           logger.info(infostr)
           if len(variable_required[g]) == 0:
              logger.info(' Lev. {:s}\t No {:s} variables specified by ATOMIX'.format(g, req_level))
           else:
              variables_req_found[g] = []
              variables_req_notfound[g] = []
              variables_req_notfound_but_or_existing[g] = []
              # Loop over all variables in the netCDF group g
              for var in nc.groups[g].variables.keys():
                  flag_atomix_standard = False
                  if var in variable_required[g]:
                      flag_atomix_standard = True
                      variables_req_found[g].append(var)
                      if plot_found:
                          logger.info(' Lev. {:s}\t Variable found {:s}'.format(g, var))

              # Check the variable that have not been found
              for var_atomix in variable_required[g]:
                  # Check if we have variables that could be as well used
                  try:
                      or_variables = atomix_structure['datalevels'][g]['VARIABLES'][var_atomix]['OR_VARIABLES'] # Check if there is an OR possibility
                  except:
                      or_variables = None

                  #print('Test',var_atomix,or_variables)
                  flag_variable_found = (var_atomix in variables_req_found[g])                      
                  if not(flag_variable_found) and (or_variables is None):
                      variables_req_notfound[g].append(var_atomix)
                  elif or_variables is not None: # Check if an "or" variable is existing
                      print('Or variables')

                      flag_or_variable_found = False
                      for var_atomix_or in or_variables:
                          if var_atomix_or in variables_req_found[g]:
                              flag_or_variable_found = True
                              break

                      if flag_variable_found == False:
                          if flag_or_variable_found == True:                              
                              variables_req_notfound_but_or_existing[g].append( [var_atomix, var_atomix_or] )
                          else:
                              variables_req_notfound[g].append(var_atomix)                                  

                      print('Or variables list',variables_req_notfound_but_or_existing[g])

              if len(variables_req_notfound[g]) == 0:
                  logger.info(' Lev. {:s}\t ALL {:s} variables found'.format(g, req_level))
                  #logger.debug(funcname + ' Lev. {:s}\t ALL {:s} variables found: {:s}'.format(g, req_level, str(variables_req_found[g])))
              else:
                  logger.info(' Lev. {:s}\t MISSING variables:'.format(g, req_level))
                  for var in variables_req_notfound[g]:
                      logger.info(' Lev. {:s}\t Variable NOT found {:s}'.format(g, var))
                  for var in variables_req_notfound_but_or_existing[g]:
                      logger.info(' Lev. {:s}\t Variable NOT found {:s} but optional variable existing {:s}'.format(g, var[0], var[1]))


                  #logger.info(funcname + ' Group: {:s}: MISSING {:s} variables: {:s} '.format(g, req_level, str(variables_req_notfound[g])))
                  #logger.info(funcname + ' Group: {:s}: {:s} variables found: {:s}'.format(g, req_level, str(variables_req_found[g])))

def atomix_check_requirements_metadata(nc, req_levels=['required', 'optional'], plot_found = False):
    """
    Checks if the netCDF file fulfills the requirements of an Atomix netCDF file.

    Returns:

    """
    funcname = 'atomix_check_requirements_metadata():'
    metadata_check = {}

    for req_level in req_levels:
        meta_str = ' ================Checking metadata ({:s})================='.format(req_level)
        logger.info(meta_str)
        for metadata_entry in atomix_structure['metadata'].keys():
            required = atomix_structure['metadata'][metadata_entry]['required']
            #print('metadata', metadata_entry,required,req_levels,required in req_levels)
            if required in req_level:
                try: # Try to find attribute in netcdf file
                    attr = getattr(nc,metadata_entry)
                    flag_has_attr = True
                    flag_has_attr_str = 'ok'
                except Exception as e: # Not found
                    flag_has_attr = False
                    flag_has_attr_str = 'missing'
                    #print(e)

                if (plot_found and flag_has_attr) or not(flag_has_attr):
                    logger.info(' Parameter: {:s}: {:s}'.format(metadata_entry,flag_has_attr_str))

                metadata_check[metadata_entry] = flag_has_attr

    logger.debug(funcname)




if __name__ == '__main__':
    config_help_filename = 'The netCDF filename to be checked'
    config_help_verbose = 'Verbosity, can be added multiple times, if argument is not called: loglevel=INFO, once: both missing and found variables are printed, twice: loglevel=DEBUG'
    config_help_metadata = 'Add if metadata shall be checked'
    config_help_variables = 'Add if variables shall be checked'
    config_help_datalevel = 'List of datalevel to be checked, if not set, all level will be checked, equal to --datalevel="L1_converted,L2_cleaned,L3_spectra,L4_dissipation"'
    config_help_required = 'List of requirement levels to be checked, if not set, all level will be checked, equal to --required="required,highly-recommended,optional"'
    config_help_print = 'Prints the ATOMIX structure to the command line in a csv format'
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', help = config_help_filename)
    parser.add_argument('--verbose', '-v', action='count', help = config_help_verbose)
    parser.add_argument('--metadata', action='store_true', help = config_help_metadata)
    parser.add_argument('--variables', action='store_true', help = config_help_variables)
    parser.add_argument('--datalevel', help = config_help_datalevel)
    parser.add_argument('--required', help = config_help_required)
    parser.add_argument('--print_variables', action='store_true', help = config_help_print)

    print('Welcome to atomix_netcdf_check version {:s}'.format(version))
    args = parser.parse_args()
    plot_found = False
    logging_level = logging.INFO
    if (args.verbose is None):
        print('Logging level: INFO')
        logging_level = logging.INFO
    elif (args.verbose == 1):
        plot_found = True
    elif (args.verbose == 2):
        plot_found = True
        print('Logging level: DEBUG')
        logging_level = logging.DEBUG

    logger.setLevel(logging_level)

    # What do we want to check?
    if args.metadata == False and args.variables == False: # None of the two set, check both in an onset of preemptive obedience.
        flag_metadata = True
        flag_variables = True
    else:
        flag_metadata = args.metadata
        flag_variables = args.variables


    if args.datalevel is None:
        datalevel_str = 'L1_converted,L2_cleaned,L3_spectra,L4_dissipation'
    else:
        datalevel_str = args.datalevel

    datalevel = datalevel_str.replace(' ','').split(',')

    if args.required is None:
        required_str = 'required,highly-recommended,optional'
    else:
        required_str = args.required

    required = required_str.replace(' ','').split(',')

    filename = args.filename
    #print('Checking variables of {:s}'.format(filename.split('/')[-1]))

    if filename is not None:
        nc = netCDF4.Dataset(filename)
        if flag_variables:
            atomix_check_requirements_variables(nc, datalevel = datalevel, req_levels=required, plot_found = plot_found)
        if flag_metadata:
            atomix_check_requirements_metadata(nc, req_levels = required, plot_found = plot_found)
    else:
        #print('Print variables',args.print_variables)
        if args.print_variables == True:
            atomix_atomix_structure_csv()




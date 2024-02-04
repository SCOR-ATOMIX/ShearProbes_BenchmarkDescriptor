"""
Python software to check Atomix netCDF files for consistency

author(s): Peter Holtermann (peter.holtermann@io-warnemuende.de)


This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or any
later version.

"""

# Structure from Atomix webpage https://wiki.app.uib.no/atomix/index.php (version from the 02. Nov.2023)
atomix_structure = {}
atomix_structure['info'] = {}
atomix_structure['info']['version'] = '1.0'
atomix_structure['info']['version_description'] = 'ATOMIX structure as defined in the Article "ATOMIX benchmark datasets for dissipation rate measurements using shear probes"'
atomix_structure['metadata'] = {}
atomix_structure['datalevels'] = {}


atomix_structure['datalevels']['L1_converted']   = {'DIMENSIONS':{}, 'VARIABLES':{}, 'description':'Timeseries in physical units: Full resolution data in physical units'}
atomix_structure['datalevels']['L2_cleaned']     = {'DIMENSIONS':{}, 'VARIABLES':{}, 'description': 'Quality-controlled and segmented timeseries: Full resolution cleaned and despiked parameters from level 1, subdivided in individual sections'}
atomix_structure['datalevels']['L3_spectra']     = {'DIMENSIONS':{}, 'VARIABLES':{}, 'description': 'Spectra: Raw and cleaned spectra' }
atomix_structure['datalevels']['L4_dissipation'] = {'DIMENSIONS':{}, 'VARIABLES':{}, 'description': 'Dissipation (varepsilon) estimates : Dissipation estimates and corresponding quality parameter as time series'}

# Level1 data
levelname = 'L1_converted'
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'] = {'description':'Length of the record from turbulence (fast) data channels'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_XYZ'] = {'description':'Length of the record from slow data channels (if different from fast), add only if necessary'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] = {'description':'Number of shear channels (shear sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']   = {'description':'Number of acc channels (acc sensors), add only if sensor exists'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']   = {'description':'Number of vib channels (vib sensors), add only if sensor exists'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GRADT_SENSORS'] = {'description':'Number of channels/sensors of type GRADT, add only if sensor exists'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GRADC_SENSORS'] = {'description':'Number of channels/sensors of type GRADC, add only if sensor exists'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_CNDC_SENSORS']  = {'description':'Number of channels/sensors of type C, add only if sensor exists'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_XYZ_SENSORS']   = {'description':'Number of XYZ channels (sensors), add only if sensor exists'}


atomix_structure['datalevels'][levelname]['VARIABLES']['TIME'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['standard_name'] = 'time'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['units'] = 'CF-Conventions compatible offset'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['standard_name'] = '[sea_]water_velocity_shear'
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['units'] = 's-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['standard_name'] = 'platform_speed_wrt_[sea_]water'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['units'] ='m s-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['VIB'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['standard_name'] = 'platform_vibration'
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['units'] ='-'
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PRES'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['standard_name'] = '[sea_]water_pressure'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['units'] = 'dbar'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['TEMP'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TEMP']['standard_name'] = '[sea_]water_temperature'
atomix_structure['datalevels'][levelname]['VARIABLES']['TEMP']['units'] = 'degree_Celsius'
atomix_structure['datalevels'][levelname]['VARIABLES']['TEMP']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]
varname = 'ACC'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'platform_acceleration'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='m s-2'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']]
varname = 'ROLL'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'platform_roll_angle'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='degree'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]
varname = 'PITCH'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'platform_pitch_angle'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='degree'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]
varname = 'GRADT'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'derivative_of_[sea_]water_temperature_wrt_X'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='degree_Celcius m-1'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GRADT_SENSORS']]
varname = 'GRADC'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'derivative_of_[sea_]water_conductivity_wrt_X'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='-'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GRADC_SENSORS']]
varname = 'CNDC'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = '[sea_]water_electrical_conductivity (water_electrical_conductivity)'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='S m-1'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_CNDC_SENSORS']]

# End Level1 data

# Level2 data
levelname = 'L2_cleaned'
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'] = {'description':'Length of the record from turbulence (fast) data channels'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] = {'description':'Number of shear channels (shear sensors)' }
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']   = {'description':'Number of acc channels (acc sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']   = {'description':'Number of vib channels (vib sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_XYZ_SENSORS']   = {'description':'Number of other channels/sensors'}

atomix_structure['datalevels'][levelname]['VARIABLES']['TIME'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['standard_name'] = 'time'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['units'] = 'CF-Conventions compatible offset'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['standard_name'] = 'unique_identifier_for_each_section_of_data_from_timeseries'
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['standard_name'] = '[sea_]water_velocity_shear'
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['units'] = 's-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['standard_name'] = 'platform_speed_wrt_[sea_]water'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['units'] ='m s-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['ACC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC']['standard_name'] = 'platform_acceleration'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC']['units'] ='m s-2'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['VIB'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['standard_name'] = 'platform_vibration'
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['units'] =''
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']]

# End Level 2 data


# Level3 data
levelname = 'L3_spectra'
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']    = {'description':'Length of the record of average times of spectral segments'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER']    = {'description':'Length of the wavenumber array' }
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] = {'description':'Number of shear channels (shear sensors)' }
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']   = {'description':'Number of acc channels (acc sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']   = {'description':'Number of vib channels (vib sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_XYZ_SENSORS']   = {'description':'Number of other channels/sensors'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SH_ACC_SPEC']   = {'description':'Number of shear-vibration cross spectra'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SH_VIB_SPEC']   = {'description':'Number of shear-acceleration cross spectra'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GLOBAL_VALUES'] = {'description':'Dimension for 1 data point (for the entire analysis)'}


atomix_structure['datalevels'][levelname]['VARIABLES']['TIME'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['standard_name'] = 'time'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['units'] = 'CF-Conventions compatible offset'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['standard_name'] = 'unique_identifier_for_each_section_of_data_from_timeseries'
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['standard_name'] = 'platform_speed_wrt_[sea_]water'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['units'] ='m s-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC']['standard_name'] = 'shear_probe_spectrum'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC']['units'] = 's-2 cpm-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] ]

atomix_structure['datalevels'][levelname]['VARIABLES']['KCYC'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['KCYC']['standard_name'] = 'cyclic_wavenumber'
atomix_structure['datalevels'][levelname]['VARIABLES']['KCYC']['units'] = 'cpm'
atomix_structure['datalevels'][levelname]['VARIABLES']['KCYC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'] ]

atomix_structure['datalevels'][levelname]['VARIABLES']['DOF'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['DOF']['standard_name'] = 'degrees_of_freedom_of_spectrum'
atomix_structure['datalevels'][levelname]['VARIABLES']['DOF']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['DOF']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GLOBAL_VALUES']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC_CLEAN'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC_CLEAN']['standard_name'] = 'shear_probe_spectrum_clean'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC_CLEAN']['units'] = 's-2 cpm-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC_CLEAN']['DIMENSIONS']  = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] ]

atomix_structure['datalevels'][levelname]['VARIABLES']['N_FFT_SEGMENTS'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['N_FFT_SEGMENTS']['standard_name'] = 'number_of_fft_segments'
atomix_structure['datalevels'][levelname]['VARIABLES']['N_FFT_SEGMENTS']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['N_FFT_SEGMENTS']['DIMENSIONS']  = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GLOBAL_VALUES']]

atomix_structure['datalevels'][levelname]['VARIABLES']['N_VIB_SENSORS'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['N_VIB_SENSORS']['standard_name'] = 'number_of_vibration_sensors_used_for_cleaning_spectra'
atomix_structure['datalevels'][levelname]['VARIABLES']['N_VIB_SENSORS']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['N_VIB_SENSORS']['DIMENSIONS']  = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GLOBAL_VALUES']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SPEC_STD'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SPEC_STD']['standard_name'] = 'standard_deviation_uncertainty_of_shear_spectrum'
atomix_structure['datalevels'][levelname]['VARIABLES']['SPEC_STD']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['SPEC_STD']['DIMENSIONS']  = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GLOBAL_VALUES']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PRES'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['standard_name'] = '[sea_]water_pressure'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['units'] = 'dbar'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['ACC_SPEC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC_SPEC']['standard_name'] = 'acceleration_sensor_spectrum'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC_SPEC']['units'] = 'm2 s-4 cpm-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC_SPEC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS'] ]

atomix_structure['datalevels'][levelname]['VARIABLES']['VIB_SPEC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB_SPEC']['standard_name'] = 'vibration_sensor_spectrum'
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB_SPEC']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB_SPEC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS'] ]

atomix_structure['datalevels'][levelname]['VARIABLES']['SH_VIB_SPEC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_VIB_SPEC']['standard_name'] = 'shear_and_vibration_cross-spectral_matrix'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_VIB_SPEC']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_VIB_SPEC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SH_ACC_SPEC'] ]

atomix_structure['datalevels'][levelname]['VARIABLES']['SH_ACC_SPEC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_ACC_SPEC']['standard_name'] = 'shear_and_acceleration_cross-spectral_matrix'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_ACC_SPEC']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_ACC_SPEC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SH_VIB_SPEC'] ]

# End Level 3 data

# Level4 data
levelname = 'L4_dissipation'
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'] = {'description':'Length of the record of average times of spectral segments'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] = {'description':'Number of shear channels (shear sensors)'}

atomix_structure['datalevels'][levelname]['VARIABLES']['TIME'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['standard_name'] = 'time'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['units'] = 'CF-Conventions compatible offset'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['standard_name'] = 'unique_identifier_for_each_section_of_data_from_timeseries'
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['standard_name'] = 'platform_speed_wrt_[sea_]water'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['units'] ='m s-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI']['standard_name'] = 'specific_turbulent_kinetic_energy_dissipation_in_water'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI']['units'] ='W kg-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FINAL'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FINAL']['standard_name'] = 'specific_turbulent_kinetic_energy_dissipation_in_water'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FINAL']['units'] ='W kg-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FINAL']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['KMAX'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['KMAX']['standard_name'] = 'maximum_wavenumber_used_for_estimating_ turbulent_kinetic_energy_dissipation'
atomix_structure['datalevels'][levelname]['VARIABLES']['KMAX']['units'] ='cpm'
atomix_structure['datalevels'][levelname]['VARIABLES']['KMAX']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['N_S'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['N_S']['standard_name'] = 'number_of_spectral_points_used_for_estimating_turbulent_kinetic_energy_dissipation'
atomix_structure['datalevels'][levelname]['VARIABLES']['N_S']['units'] ='-'
atomix_structure['datalevels'][levelname]['VARIABLES']['N_S']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FLAGS'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FLAGS']['standard_name'] = 'dissipation_qc_flags'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FLAGS']['units'] ='-'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FLAGS']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['METHOD'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['METHOD']['standard_name'] = 'method_used_for_estimating_ turbulent_kinetic_energy_dissipation'
atomix_structure['datalevels'][levelname]['VARIABLES']['METHOD']['units'] ='-'
atomix_structure['datalevels'][levelname]['VARIABLES']['METHOD']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PRES'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['standard_name'] = 'water_pressure'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['units'] = 'dbar'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['KVISC'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['KVISC']['standard_name'] = 'kinematic_viscosity_of_water'
atomix_structure['datalevels'][levelname]['VARIABLES']['KVISC']['units'] = 'm2 s-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['KVISC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['FOM'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['FOM']['standard_name'] = 'figure_of_merit'
atomix_structure['datalevels'][levelname]['VARIABLES']['FOM']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['FOM']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_STD'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_STD']['standard_name'] = 'expected_standard_deviation_of_the_ logarithm_of_the_dissipation_estimate'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_STD']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_STD']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['MAD'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['MAD']['standard_name'] = 'mean_absolute_deviation'
atomix_structure['datalevels'][levelname]['VARIABLES']['MAD']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['MAD']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['VAR_RESOLVED'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['VAR_RESOLVED']['standard_name'] = 'variance_resolved'
atomix_structure['datalevels'][levelname]['VARIABLES']['VAR_RESOLVED']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['VAR_RESOLVED']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['KMIN'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['KMIN']['standard_name'] = 'minimum_wavenumber_used_for_estimating_ turbulent_kinetic_energy_dissipation'
atomix_structure['datalevels'][levelname]['VARIABLES']['KMIN']['units'] ='cpm'
atomix_structure['datalevels'][levelname]['VARIABLES']['KMIN']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['DESPIKE_FRACTION_SH'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['DESPIKE_FRACTION_SH']['standard_name'] = 'fraction_of_shear_data_modified_by_despiking_algorithm'
atomix_structure['datalevels'][levelname]['VARIABLES']['DESPIKE_FRACTION_SH']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['DESPIKE_FRACTION_SH']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['DESPIKE_PASS_COUNT_SH'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['DESPIKE_PASS_COUNT_SH']['standard_name'] = 'number_of_despike_passes_for_shear_probes'
atomix_structure['datalevels'][levelname]['VARIABLES']['DESPIKE_PASS_COUNT_SH']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['DESPIKE_PASS_COUNT_SH']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]


# Metadata
parameter = 'title'
description = 'A comprehensive title for the dataset including the time and location aspect'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'authors'
description = 'Names of authors'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'summary'
description = 'An abstract describing the dataset'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'comment'
description = 'Supplementary technical details about the collecting and processing of the dataset'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'platform_type'
description = 'The platform from which the data are collected. From the SeaVoX Platform Categories (L06) list, e.g. sub-surface mooring, research vessel, sub-surface glider'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'source'
description = 'The instrument used for collecting the data. For example, vertical microstructure profiler, VMP2000 SN009.'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'date_created'
description = 'The date on which the data were created, yyyy-mm-ddTHH:MM:SSZ'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'date_update'
description = 'The date on which the data were last modified, yyyy-mm-ddTHH:MM:SSZ'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'time_reference_year'
description = 'Year for time reference'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'time_coverage_start'
description = 'Time of the first data point in the dataset, yyyy-mm-ddTHH:MM:SSZ'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'time_coverage_end'
description = 'Time of the last data point in the dataset, yyyy-mm-ddTHH:MM:SSZ'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_lat_min'
description = 'Southern bound of data, decimal degrees, negative for South'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_lat_max'
description = 'Northern bound of data, decimal degrees, negative for South'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_lon_min'
description = 'Western bound of data, decimal degrees, negative for West'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_lon_max'
description = 'Eastern bound of data, decimal degrees, negative for West'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'fs_fast'
description = 'Sampling frequency for fast (turbulence) channels'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'fs_slow'
description = 'Sampling frequency for slow channels (if exist). Alternative names could be, e.g., fs_ctd'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'profiling_direction'
description = 'Direction along which the section was collected, e.g., horizontal, vertical, or glide'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'fft_length'
description = 'Length of the Fast Fourier transform segments (in data points; note, fft_lengths_sec in seconds is optional)'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'diss_length'
description = 'Length of data (in data points) used for each dissipation estimate'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'overlap'
description = 'Length of overlap (in data points) in diss_length'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'goodman'
description = 'Flag for the vibration coherent noise removal using the Goodman algorithm. 0=not applied; 1=applied'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'HP_cut'
description = 'the high-pass filter cutoff frequency in Hz. Can be zero for no filtering'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

#parameter = 'num_fft_segments'
#description = 'number of FFT segments'
#required = 'required'
#atomix_structure['metadata'][parameter] = {}
#atomix_structure['metadata'][parameter]['description'] = description
#atomix_structure['metadata'][parameter]['required'] = required

parameter = 'conventions'
description = 'A comma-separated list of the conventions that are followed by the dataset. e.g., CF-1.6, ACDD-1.3, ATOMIX'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'history'
description = 'Provides an audit trail for modifications to the original data; e.g., Version 1'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'data_mode'
description = 'D #(D)elayed'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required
# End Metadata required
# Metadata optional
parameter = 'fft_length_sec'
description = 'Length of the Fast Fourier transform segments in seconds'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'diss_length_sec'
description = 'Dissipation estimate data length in seconds'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'overlap_sec'
description = 'Length of overlap (in seconds) in diss_length_sec'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'f_AA'
description = 'The anti-aliasing frequency in Hz'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'FOM_limit'
description = 'Figure of merit limit for quality assurance. Typically, 1.15'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'diss_ratio_limit'
description = 'The limit to identify anomalously large disagreement between dissipation estimates from probes. The magnitude of the difference of the natural logarithm of two dissipation estimates should be smaller than diss_ratio_limit times std log eps. Typically, 2.77'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'despike_shear_fraction_limit'
description = 'The maximum allowed fraction of data (of each diss_length_sec length segment) removed by de-spiking. Typically, 0.05'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'despike_shear_iterations_limit'
description = 'The maximum number of allowed iterations of de-spiking when producing the L2 shear probe data (one value per section). Typically 8'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'variance_resolved_limit'
description = 'The minimum fraction of variance resolved in an estimate by spectral integration. Typically 0.6'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'f_limit'
description = 'The upper limit to exclude frequencies that have contamination. Typically infinity'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'fit_2_isr'
description = 'Dissipation threshold for using the method of fitting in the inertial subrange. Typically 10−5 W kg−1'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'area'
description = 'The region where the data were collected, e.g., Arctic Ocean, Barents Sea'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_vertical_min'
description = 'Further refinement of the geospatial bounding box. Vertical minimum in m'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_vertical_max'
description = 'Further refinement of the geospatial bounding box. Vertical maximum in m'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_vertical_positive'
description = 'Direction of positive vertical: down, up'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'institution'
description = 'The name of the institution principally responsible for originating this data'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'principal_investigator'
description = 'Name of the principal investigator who created the data'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'contact'
description = 'Name of the contact person'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'project_name'
description = 'The scientific project that produced the data'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'cruise'
description = 'The name or number of the research cruise'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'vessel'
description = 'The name of the research vessel'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'references'
description = 'A list of related references'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'keywords'
description = 'A comma separated list of key words and phrases'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'creator_name'
description = 'The data creators name'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'creator_email'
description = 'The data creators email'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'creator_url'
description = 'The data creators URL'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'acknowledgement'
description = 'Acknowledgement of various type of support for the project that produced this data'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'station_name'
description = 'The name of the station where data were collected'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'license'
description = 'Provide the URL to a standard or specific license, e.g, http://creativecommons.org/licenses/by/4.0/, Freely Distributed, or None'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

#parameter = 'spectral_model'
#description = 'e.g., Nasmyth, Lueck or Panchev-Kesich'
#required = 'optional'
#atomix_structure['metadata'][parameter] = {}
#atomix_structure['metadata'][parameter]['description'] = description
#atomix_structure['metadata'][parameter]['required'] = required

#parameter = 'spectrum_std'
#description = 'statistical uncertainty (standard deviation) of the natural logarithm of spectrum of shear'
#required = 'optional'
#atomix_structure['metadata'][parameter] = {}
#atomix_structure['metadata'][parameter]['description'] = description
#atomix_structure['metadata'][parameter]['required'] = required

#parameter = 'num_vibration_goodman'
#description = 'number of vibration or acceleration time series used to clean the shear spectrum'
#required = 'optional'
#atomix_structure['metadata'][parameter] = {}
#atomix_structure['metadata'][parameter]['description'] = description
#atomix_structure['metadata'][parameter]['required'] = required

#parameter = 'eps_remove_top_meters'
#description = 'if applicable, upper meters removed from dissipation estimates (e.g., because of ship)'
#required = 'optional'
#atomix_structure['metadata'][parameter] = {}
#atomix_structure['metadata'][parameter]['description'] = description
#atomix_structure['metadata'][parameter]['required'] = required

# Add the dimensionname as name entry to the structure
for levelname in atomix_structure['datalevels'].keys():
    for dimname in atomix_structure['datalevels'][levelname]['DIMENSIONS'].keys():
        atomix_structure['datalevels'][levelname]['DIMENSIONS'][dimname]['name'] = dimname

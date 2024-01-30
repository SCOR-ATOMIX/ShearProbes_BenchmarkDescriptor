

# Structure from Atomix webpage https://wiki.app.uib.no/atomix/index.php (version from the 02. Nov.2023)
atomix_structure = {}
atomix_structure['info'] = {}
atomix_structure['info']['atomix_version'] = 'copy of the structure found in the ATOMIX-Wiki at 02. Nov. 2023'
atomix_structure['metadata'] = {}
atomix_structure['datalevels'] = {}


atomix_structure['datalevels']['L1_converted']   = {'DIMENSIONS':{}, 'VARIABLES':{}, 'description':'Timeseries in physical units: Full resolution data in physical units'}
atomix_structure['datalevels']['L2_cleaned']     = {'DIMENSIONS':{}, 'VARIABLES':{}, 'description': 'Quality-controlled and segmented timeseries: Full resolution cleaned and despiked parameters from level 1, subdivided in individual sections'}
atomix_structure['datalevels']['L3_spectra']     = {'DIMENSIONS':{}, 'VARIABLES':{}, 'description': 'Spectra: Raw and cleaned spectra' }
atomix_structure['datalevels']['L4_dissipation'] = {'DIMENSIONS':{}, 'VARIABLES':{}, 'description': 'Dissipation (varepsilon) estimates : Dissipation estimates and corresponding quality parameter as time series'}

# Level1 data
levelname = 'L1_converted'
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'] = {'description':'length of the record from turbulence (fast) data channels'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_XYZ'] = {'description':'length of the record from sensor XYZ'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] = {'description':'number of shear channels (shear sensors)' }
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']   = {'description':'number of acc channels (acc sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']   = {'description':'number of vib channels (vib sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GRADT_SENSORS']   = {'description':'number of channels/sensors of type GRADT'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GRADC_SENSORS']   = {'description':'number of channels/sensors of type GRADC'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_CNDC_SENSORS']   = {'description':'number of channels/sensors of type C'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_XYZ_SENSORS']   = {'description':'number of channels/sensors of type XYZ'}


atomix_structure['datalevels'][levelname]['VARIABLES']['TIME'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['standard_name'] = 'time'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['units'] = 'CF-Conventions compatible offset'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['standard_name'] = 'sea_water_velocity_shear'
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['units'] = 's-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['standard_name'] = 'platform_speed_wrt_sea_water'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['units'] ='m s-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['ACC'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC']['standard_name'] = 'platform_acceleration'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC']['units'] ='m s-2'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['VIB'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['standard_name'] = 'platform_vibration'
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['units'] =''
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PRES'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['standard_name'] = 'water_pressure'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['units'] = 'dbar'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['TEMP'] = {'required':'highly-recommended'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TEMP']['standard_name'] = 'water_pressure'
atomix_structure['datalevels'][levelname]['VARIABLES']['TEMP']['units'] = 'degree_Celsius'
atomix_structure['datalevels'][levelname]['VARIABLES']['TEMP']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]
varname = 'ACC'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'platform_acceleration'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='m s-2'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']]
varname = 'VIB'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'platform_vibration'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] =''
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']]
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
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'derivative_of_seawater_temperature_wrt_X'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='degree_Celcius m-1'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GRADT_SENSORS']]
varname = 'GRADC'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'derivative_of_seawater_conductivity_wrt_X'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='Typically not calibrated'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GRADC_SENSORS']]
varname = 'CNDC'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['standard_name'] = 'sea_water_electrical_conductivity (water_electrical_conductivity)'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['units'] ='S m-1'
atomix_structure['datalevels'][levelname]['VARIABLES'][varname]['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_CNDC_SENSORS']]

# End Level1 data

# Level2 data
levelname = 'L2_cleaned'
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'] = {'description':'length of the record from turbulence (fast) data channels'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] = {'description':'number of shear channels (shear sensors)' }
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']   = {'description':'number of acc channels (acc sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']   = {'description':'number of vib channels (vib sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_XYZ_SENSORS']   = {'description':'number of other channels/sensors'}

atomix_structure['datalevels'][levelname]['VARIABLES']['TIME'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['standard_name'] = 'time'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['units'] = 'CF-Conventions compatible offset'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['standard_name'] = 'unique_identifier_for_each_section_of_data_from_timeseries'
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['units'] = ''
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['standard_name'] = 'sea_water_velocity_shear'
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['units'] = 's-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['SHEAR']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['standard_name'] = 'platform_speed_wrt_sea_water'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['units'] ='m s-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME']]

atomix_structure['datalevels'][levelname]['VARIABLES']['ACC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC']['standard_name'] = 'platform_acceleration'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC']['units'] ='m s-2'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['VIB'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['standard_name'] = 'platform_vibration'
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['units'] =''
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']]

# End Level 2 data


# Level3 data
levelname = 'L3_spectra'
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']    = {'description':'length of the record of average times of spectral segments. This also equals time of dissipation estimates. '}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER']    = {'description':'length of the wavenumber array' }
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] = {'description':'number of shear channels (shear sensors)' }
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS']   = {'description':'number of acc channels (acc sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS']   = {'description':'number of vib channels (vib sensors)'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_XYZ_SENSORS']   = {'description':'number of other channels/sensors'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SH_ACC_SPEC']   = {'description':'number of shear and acc sensor combinations: N_SHEAR_SENSORS * N_ACC_SENSORS'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SH_VIB_SPEC']   = {'description':'number of shear and vib sensor combinations: N_SHEAR_SENSORS * N_VIB_SENSORS'}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_GLOBAL_VALUES'] = {'description':'Dimension for 1 data point (for the entire analysis)'}


atomix_structure['datalevels'][levelname]['VARIABLES']['TIME'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['standard_name'] = 'time'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['units'] = 'CF-Conventions compatible offset'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['standard_name'] = 'unique_identifier_for_each_section_of_data_from_timeseries'
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['units'] = ''
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['standard_name'] = 'platform_speed_wrt_sea_water'
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
atomix_structure['datalevels'][levelname]['VARIABLES']['DOF']['units'] = ''
atomix_structure['datalevels'][levelname]['VARIABLES']['DOF']['DIMENSIONS'] = [1]

atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC_CLEAN'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC_CLEAN']['standard_name'] = 'shear_probe_spectrum_clean'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC_CLEAN']['units'] = 's-2 cpm-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC_CLEAN']['DIMENSIONS']  = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] ]
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_SPEC_CLEAN']['comment'] = 'SH_SPEC_CLEAN must be included in the file if these spectra were used to compute EPS'

atomix_structure['datalevels'][levelname]['VARIABLES']['PRES'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['standard_name'] = 'water_pressure'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['units'] = 'dbar'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['ACC_SPEC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC_SPEC']['standard_name'] = 'acceleration_sensor_spectrum'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC_SPEC']['units'] = 'm2 s-4 cpm-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['ACC_SPEC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_ACC_SENSORS'] ]

atomix_structure['datalevels'][levelname]['VARIABLES']['VIB_SPEC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB_SPEC']['standard_name'] = 'vibration_sensor_spectrum'
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB_SPEC']['units'] = ''
atomix_structure['datalevels'][levelname]['VARIABLES']['VIB_SPEC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_VIB_SENSORS'] ]

atomix_structure['datalevels'][levelname]['VARIABLES']['SH_VIB_SPEC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_VIB_SPEC']['standard_name'] = 'shear_and_vibration_cross-spectral_matrix'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_VIB_SPEC']['units'] = ''
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_VIB_SPEC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SH_ACC_SPEC'] ]

atomix_structure['datalevels'][levelname]['VARIABLES']['SH_ACC_SPEC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_ACC_SPEC']['standard_name'] = 'shear_and_acceleration_cross-spectral_matrix'
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_ACC_SPEC']['units'] = ''
atomix_structure['datalevels'][levelname]['VARIABLES']['SH_ACC_SPEC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_WAVENUMBER'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SH_VIB_SPEC'] ]

# End Level 3 data

# Level4 data
levelname = 'L4_dissipation'
atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'] = {'description':'length of the record of average times of spectral segments. This also equals time of dissipation estimates. '}
atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS'] = {'description':'length of the wavenumber array' }

atomix_structure['datalevels'][levelname]['VARIABLES']['TIME'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['standard_name'] = 'time'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['units'] = 'CF-Conventions compatible offset'
atomix_structure['datalevels'][levelname]['VARIABLES']['TIME']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['standard_name'] = 'unique_identifier_for_each_section_of_data_from_timeseries'
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['units'] = ''
atomix_structure['datalevels'][levelname]['VARIABLES']['SECTION_NUMBER']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['standard_name'] = 'platform_speed_wrt_sea_water'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['units'] ='m s-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['PSPD_REL']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI']['standard_name'] = 'specific_turbulent_kinetic_energy_dissipation _in_water'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI']['units'] ='W kg-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FINAL'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FINAL']['standard_name'] = 'specific_turbulent_kinetic_energy_dissipation _in_water'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FINAL']['units'] ='W kg-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_FINAL']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['KMIN'] = {'required':'required'}
atomix_structure['datalevels'][levelname]['VARIABLES']['KMIN']['standard_name'] = 'minimum_wavenumber_used_for_estimating_ turbulent_kinetic_energy_dissipation'
atomix_structure['datalevels'][levelname]['VARIABLES']['KMIN']['units'] ='cpm'
atomix_structure['datalevels'][levelname]['VARIABLES']['KMIN']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

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

atomix_structure['datalevels'][levelname]['VARIABLES']['PRES'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['standard_name'] = 'water_pressure'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['units'] = 'dbar'
atomix_structure['datalevels'][levelname]['VARIABLES']['PRES']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['KVISC'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['KVISC']['standard_name'] = 'kinematic_viscosity_of_water'
atomix_structure['datalevels'][levelname]['VARIABLES']['KVISC']['units'] = 'm2 s-1'
atomix_structure['datalevels'][levelname]['VARIABLES']['KVISC']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA']]

atomix_structure['datalevels'][levelname]['VARIABLES']['FOM'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['FOM']['standard_name'] = 'figure_of_merit'
atomix_structure['datalevels'][levelname]['VARIABLES']['FOM']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['FOM']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['MAD'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['MAD']['standard_name'] = 'mean_absolute_deviation'
atomix_structure['datalevels'][levelname]['VARIABLES']['MAD']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['MAD']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['VAR_RESOLVED'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['VAR_RESOLVED']['standard_name'] = 'variance_resolved'
atomix_structure['datalevels'][levelname]['VARIABLES']['VAR_RESOLVED']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['VAR_RESOLVED']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_STD'] = {'required':'optional'}
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_STD']['standard_name'] = 'expected_standard_deviation_of_the_ logarithm_of_the_dissipation_estimate'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_STD']['units'] = '-'
atomix_structure['datalevels'][levelname]['VARIABLES']['EPSI_STD']['DIMENSIONS'] = [atomix_structure['datalevels'][levelname]['DIMENSIONS']['TIME_SPECTRA'],atomix_structure['datalevels'][levelname]['DIMENSIONS']['N_SHEAR_SENSORS']]

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
description = 'e.g., Vertical micostructure profiler data from cruise XXX'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'summary'
description = 'required by ACDD'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'comment'
description = 'required by CF'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'platform_type'
description = 'research vessel, sub-surface glider etc'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'creation_time'
description = 'netCDF file creation time (required by CF-Standard). Format: yyyy-mm-ddTHH:MM:SSZ'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'date_created'
description = 'same as "creation time". Format: yyyy-mm-ddTHH:MM:SSZ'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'date_update'
description = 'Time of the latest revision: Format: yyyy-mm-ddTHH:MM:SSZ'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'time_reference_year'
description = 'year for time reference'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'fs_fast'
description = 'sampling frequency for fast channels (or fast_ctd or similar if such records are included)'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'fs_slow'
description = 'sampling frequency for slow channels'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'profiling_direction'
description = 'horizontal, vertical, glide'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'fft_length'
description = 'Length (in data points) of fft_length (note, fft_lengths_sec in seconds is optional)'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'diss_length'
description = 'Length (in data points) of dissipation estimate'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'overlap'
description = 'Overlap of dissipation estimates (diss_length, in data points)'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'num_fft_segments'
description = 'number of FFT segments'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'goodman'
description = '0=not applied; 1=applied'
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

parameter = 'conventions'
description = 'CF-1.6, ACDD-1.3, ATOMIX'
required = 'required'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'history'
description = 'Version 1'
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
description = 'seconds'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'diss_length_sec'
description = 'seconds'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'overlap_sec'
description = 'seconds'
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
description = 'Figure of Merit limit, non-dimensional. If absent the FOM QC-flag is not set. Typically, 1.15'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'diss_ratio_limit'
description = 'non-dimensional, if absent the dissipation ration QC-flag is not set. Typically, 2.77'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'despike_shear_fraction_limit'
description = 'non-dimensional, if absent the de-spike fraction QC-flag is not set. Typically, 0.05.'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'despike_shear_iterations_limit'
description = 'non-dimensional, if absent the de-spike iteration passes QC-flag is not set. Typically 8.'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'variance_resolved_limit'
description = 'threshold for the minimum percent of variance resolved in a shear spectrum. Typically 50%.'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'spectral_model'
description = 'e.g., Nasmyth, Lueck or Panchev-Kesich'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'spectrum_std'
description = 'statistical uncertainty (standard deviation) of the natural logarithm of spectrum of shear'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'num_vibration_goodman'
description = 'number of vibration or acceleration time series used to clean the shear spectrum'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'f_limit'
description = 'upper limit to exclude frequencies that have contaminations. Typically infinity.'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'fit_2_isr'
description = 'dissipation threshold to use the method of fitting to the inertial subrange. Typically 10-5 W/kg.'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'eps_remove_top_meters'
description = 'if applicable, upper meters removed from dissipation estimates (e.g., because of ship)'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'area'
description = 'e.g., Arctic Ocean, Barents Sea'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_lat_min'
description = 'latitude minimum of data'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_lat_max'
description = 'latitude maximum of data'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_lon_min'
description = 'longitude minimum of data'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_lon_max'
description = 'longitude maximum of data'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_vertical_min'
description = '0'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_vertical_max'
description = 'in m'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'geospatial_vertical_positive'
description = 'down, up'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'time_coverage_start'
description = 'yyyy-mm-ddTHH:MM:SSZ'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'time_coverage_end'
description = 'yyyy-mm-ddTHH:MM:SSZ'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'institution'
description = 'e.g. University of Bergen'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'principal_investigator'
description = 'Name of Principal Investigator'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'authors'
description = 'Names of authors'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'contact'
description = 'email address of corresponding author (usually principal investigator)'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'project_name'
description = 'name of project for which the data was collected'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'cruise'
description = 'name of cruise from which the data was collected'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'vessel'
description = 'name of vessel from which the data was collected'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'source'
description = 'From the SeaVoX Platform Categories vocabulary (L06) list, e.g.  “subsurface mooring”, ”ship”, ""sub-surface gliders"", ""autonomous underwater vehicle"" (CF)'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'references'
description = 'key references'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'keywords'
description = 'relevant keywords describing data e.g. shear probes'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'creator_name'
description = 'name of person who generated the file'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'creator_email'
description = 'email address of person who generated the file'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'creator_url'
description = 'website address of the creator'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'acknowledgement'
description = 'acknowledgements for this data. e.g. this could include crew of ship or funders'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

parameter = 'station_name'
description = 'name of station'
required = 'optional'
atomix_structure['metadata'][parameter] = {}
atomix_structure['metadata'][parameter]['description'] = description
atomix_structure['metadata'][parameter]['required'] = required

# Add the dimensionname as name entry to the structure
for levelname in atomix_structure['datalevels'].keys():
    for dimname in atomix_structure['datalevels'][levelname]['DIMENSIONS'].keys():
        atomix_structure['datalevels'][levelname]['DIMENSIONS'][dimname]['name'] = dimname
def _CI_Density(field, data):
  dens = data[('enzo', 'CI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('CI_Density_cgs', function=_CI_Density, units='g/cm**3',
                        force_override = True)
# #

def _NI_Density(field, data):
  dens = data[('enzo', 'NI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('NI_Density_cgs', function=_NI_Density, units='g/cm**3',
                        force_override = True)

# #

def _OI_Density(field, data):
  dens = data[('enzo', 'OI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('OI_Density_cgs', function=_OI_Density, units='g/cm**3',
                        force_override = True)

def _MgI_Density(field, data):
  dens = data[('enzo', 'MgI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('MgI_Density_cgs', function=_MgI_Density, units='g/cm**3',
                        force_override = True)

def _SiI_Density(field, data):
  dens = data[('enzo', 'SiI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('SiI_Density_cgs', function=_SiI_Density, units='g/cm**3',
                        force_override = True)

def _FeI_Density(field, data):
  dens = data[('enzo', 'FeI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('FeI_Density_cgs', function=_FeI_Density, units='g/cm**3',
                        force_override = True)

def _YI_Density(field, data):
  dens = data[('enzo', 'YI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('YI_Density_cgs', function=_YI_Density, units='g/cm**3',
                        force_override = True)

def _LaI_Density(field, data):
  dens = data[('enzo', 'LaI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('LaI_Density_cgs', function=_LaI_Density, units='g/cm**3',
                        force_override = True)

def _BaI_Density(field, data):
  dens = data[('enzo', 'BaI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('BaI_Density_cgs', function=_BaI_Density, units='g/cm**3',
                        force_override = True)

def _EuI_Density(field, data):
  dens = data[('enzo', 'EuI_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('EuI_Density_cgs', function=_EuI_Density, units='g/cm**3',
                        force_override = True)


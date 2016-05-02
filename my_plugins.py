def _metal_fraction(field, data):
  metal_dens = data[('enzo', 'Metal_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field('metal_gas_fraction', function = _metal_fraction, units='dimensionless')



def _C_Fraction(field, data):
  metal_dens = data[('enzo', 'C_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','C_Gas_Fraction'), function = _C_Fraction, units='dimensionless')


def _O_Fraction(field, data):
  metal_dens = data[('enzo', 'O_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','O_Gas_Fraction'), function = _O_Fraction, units='dimensionless')

def _N_Fraction(field, data):
  metal_dens = data[('enzo', 'N_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','N_Gas_Fraction'), function = _N_Fraction, units='dimensionless')

def _Mg_Fraction(field, data):
  metal_dens = data[('enzo', 'Mg_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field('Mg_Gas_Fraction', function = _Mg_Fraction, units='dimensionless')

def _Si_Fraction(field, data):
  metal_dens = data[('enzo', 'Si_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field('Si_Gas_Fraction', function = _Si_Fraction, units='dimensionless')

def _Fe_Fraction(field, data):
  metal_dens = data[('enzo', 'Fe_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','Fe_Gas_Fraction'), function = _Fe_Fraction, units='dimensionless')


def _Ba_Fraction(field, data):
  metal_dens = data[('enzo', 'Ba_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field('Ba_Gas_Fraction', function = _Ba_Fraction, units='dimensionless')

def _La_Fraction(field, data):
  metal_dens = data[('enzo', 'La_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field('La_Gas_Fraction', function = _La_Fraction, units='dimensionless')

def _Y_Fraction(field, data):
  metal_dens = data[('enzo', 'Y_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field('Y_Gas_Fraction', function = _Y_Fraction, units='dimensionless')

def _Eu_Fraction(field, data):
  metal_dens = data[('enzo', 'Eu_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field('Eu_Gas_Fraction', function = _Eu_Fraction, units='dimensionless')


# ---------------------------------------------------
  

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


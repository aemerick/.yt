
#def _jeans_length(field,data):
 #   if data.has_field_parameter("Gamma"):
  #      gamma = data.get_field_parameter('Gamma')
   # else:
    #    gamma = 1.6667

#    gamma = 1.6667
#    mu    = 1.3
#    T     = data['temperature'].convert_to_units('K')
#    c_s_squared = const.kboltz * gamma * T / (mu * const.mp)

#    L = c_s_squared * np.pi / const.G / data['density']

#    L = np.sqrt(L)

#    return L.convert_to_units('cm')

#yt.add_field('jeans_length', function=_jeans_length, units='cm', force_override=True)
#add_field(('all','jl'), function=_jeans_length, units='cm', force_override=True)


# ---------------------------------------------------------------------------
#
# Fields for testing Enzo individual star SF scheme (A. Emerick)
# as postprocessing step
# ---------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# Chemical species densities meant to me used with enzo data 
#
# ----------------------------------------------------------------------------
def _metal_fraction(field, data):

  try:
      metal_dens = data[('enzo', 'Metal_Density')].value
  except:
      try:
          metal_dens = data[('enzo', 'metallicity')].value
      except:
          metal_dens = data[('enzo', 'Metallicity')].value

  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','metal_fraction'), function = _metal_fraction, units='dimensionless')


def _C_Fraction(field, data):
  metal_dens = data[('enzo', 'C_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','C_Fraction'), function = _C_Fraction, units='dimensionless')


def _O_Fraction(field, data):
  metal_dens = data[('enzo', 'O_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','O_Fraction'), function = _O_Fraction, units='dimensionless')

def _N_Fraction(field, data):
  metal_dens = data[('enzo', 'N_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','N_Fraction'), function = _N_Fraction, units='dimensionless')

def _Mg_Fraction(field, data):
  metal_dens = data[('enzo', 'Mg_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','Mg_Fraction'), function = _Mg_Fraction, units='dimensionless')

def _Si_Fraction(field, data):
  metal_dens = data[('enzo', 'Si_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','Si_Fraction'), function = _Si_Fraction, units='dimensionless')

def _S_Fraction(field, data):
  metal_dens = data[('enzo', 'S_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','S_Fraction'), function = _Si_Fraction, units='dimensionless')


def _Fe_Fraction(field, data):
  metal_dens = data[('enzo', 'Fe_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','Fe_Fraction'), function = _Fe_Fraction, units='dimensionless')

def _Ni_Fraction(field, data):
  metal_dens = data[('enzo', 'Ni_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','Ni_Fraction'), function = _Fe_Fraction, units='dimensionless')


def _Ba_Fraction(field, data):
  metal_dens = data[('enzo', 'Ba_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','Ba_Fraction'), function = _Ba_Fraction, units='dimensionless')

def _La_Fraction(field, data):
  metal_dens = data[('enzo', 'La_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','La_Fraction'), function = _La_Fraction, units='dimensionless')

def _Y_Fraction(field, data):
  metal_dens = data[('enzo', 'Y_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','Y_Fraction'), function = _Y_Fraction, units='dimensionless')

def _Eu_Fraction(field, data):
  metal_dens = data[('enzo', 'Eu_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','Eu_Fraction'), function = _Eu_Fraction, units='dimensionless')


# ---------------------------------------------------
  

def _CI_Density(field, data):
  dens = data[('enzo', 'C_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('C_Density_cgs', function=_CI_Density, units='g/cm**3',
                        force_override = True)
# #

def _NI_Density(field, data):
  dens = data[('enzo', 'N_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('N_Density_cgs', function=_NI_Density, units='g/cm**3',
                        force_override = True)

# #

def _OI_Density(field, data):
  dens = data[('enzo', 'O_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('O_Density_cgs', function=_OI_Density, units='g/cm**3',
                        force_override = True)

def _MgI_Density(field, data):
  dens = data[('enzo', 'Mg_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('Mg_Density_cgs', function=_MgI_Density, units='g/cm**3',
                        force_override = True)

def _SiI_Density(field, data):
  dens = data[('enzo', 'Si_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('Si_Density_cgs', function=_SiI_Density, units='g/cm**3',
                        force_override = True)

def _FeI_Density(field, data):
  dens = data[('enzo', 'Fe_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('Fe_Density_cgs', function=_FeI_Density, units='g/cm**3',
                        force_override = True)

def _NiI_Density(field, data):
  dens = data[('enzo', 'Ni_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('Ni_Density_cgs', function=_NiI_Density, units='g/cm**3',
                        force_override = True)


def _YI_Density(field, data):
  dens = data[('enzo', 'Y_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('Y_Density_cgs', function=_YI_Density, units='g/cm**3',
                        force_override = True)

def _LaI_Density(field, data):
  dens = data[('enzo', 'La_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('La_Density_cgs', function=_LaI_Density, units='g/cm**3',
                        force_override = True)

def _BaI_Density(field, data):
  dens = data[('enzo', 'Ba_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('Ba_Density_cgs', function=_BaI_Density, units='g/cm**3',
                        force_override = True)

def _EuI_Density(field, data):
  dens = data[('enzo', 'Eu_Density')].value
  dens = dens * data.ds.mass_unit / data.ds.length_unit**3
  dens = dens.convert_to_cgs()

  return dens

add_field('Eu_Density_cgs', function=_EuI_Density, units='g/cm**3',
                        force_override = True)
# ---------------------------------------------------------------------------


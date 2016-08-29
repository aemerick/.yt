from yt import units as u 
import numpy as np 



def _H_ionization_fraction(field,data):
    return data['H_p1_number_density'] / (data['H_number_density'] + data['H_p1_number_density'])
add_field(('gas','H_ionization_fraction'), function=_H_ionization_fraction, units='dimensionless')

def _He_p1_ionization_fraction(field,data):
    return data['He_p1_number_density'] / (data['He_number_density'] + data['He_p1_number_density'] + data['He_p2_number_density'])
add_field(('gas','He_p1_ionization_fraction'), function=_He_p1_ionization_fraction, units='dimensionless')

def _He_p2_ionization_fraction(field,data):
    return data['He_p2_number_density'] / (data['He_number_density'] + data['He_p1_number_density'] + data['He_p2_number_density'])
add_field(('gas','He_p2_ionization_fraction'), function=_He_p2_ionization_fraction, units='dimensionless')


# define a efficiency parameter field here for FUV heating
#def _FUV_heating_efficiency(field,data):

#    m = data[('all','birth_mass')].value
#    Z = data[('all','metallicity_fraction')].value
#    xp = data[('all','particle_position_x')].convert_to_units('cm').value
#    yp = data[('all','particle_position_y')].convert_to_units('cm').value
#    zp = data[('all','particle_position_z')].convert_to_units('cm').value

#    m = m[0] 
#    Z = Z[0]
#    xp = data.ds.domain_center[0].convert_to_units('cm')
#    yp = xp
#    zp = xp

#    m = 20.0
#    Z = 0.01
#    star = isp.individual_star( m, Z=Z)

#    L = star.FUV * 4.0 * np.pi * star._R**2
#    L = L * u.erg / u.s

#    rsqr = ( xp - data['x'])**2 +\
#           ( yp - data['y'])**2 +\
#           ( zp - data['z'])**2
#    rsqr = rsqr.convert_to_units('cm**2')


#    G = L / (4.0 * np.pi * rsqr) / 1.59E-3
#    G = G.value # should be unitless

#    T = data['temperature'].value
#    n_e = data['El_number_density'].convert_to_units('cm**(-3)').value

#    e = 4.92E-2 / ( 1.0 + 4.0E-3 * (G * T**(0.5) / n_e)**(0.73)) +\
#        3.7E-2 * (1.0E-4 * T)**(0.7) / (1.0 + 2.0E-4 * ((G * T**0.5)/n_e))

#    return e * data['temperature']/data['temperature'] # force dimensionless units

#add_field(('gas','fuv_efficiency'), function =_FUV_heating_efficiency, units='dimensionless')

def _Pe_heating_total_rate(field, data):
  gamma = (data[('gas','pe_heating_cgs')])
                             
  return (gamma / data[('gas','H_number_density')]).convert_to_units('erg/s')

add_field(('gas','pe_total_rate'), function=_Pe_heating_total_rate, units='erg/s')


def _Pe_heating(field, data):
  gamma = data[('enzo','Pe_heating_rate')]

  gamma = gamma * data.ds.mass_unit / data.ds.length_unit**3 * data.ds.velocity_unit**2 / data.ds.time_unit

  gamma = gamma.convert_to_units('erg/s/cm**3')
    
  return gamma

add_field(('enzo','Pe_heating_rate'), function = _Pe_heating, units='erg/s/cm**3', force_override=True)


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

def _metal_mass(field, data):

  try:
      metal_dens = data[('enzo', 'Metal_Density')].value
  except:
      try:
          metal_dens = data[('enzo', 'metallicity')].value
      except:
          metal_dens = data[('enzo', 'Metallicity')].value

  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  mass = metal_dens * data['cell_volume']
  mass = mass.convert_to_units('Msun')

  return mass
add_field(('gas','metal_mass'), function = _metal_mass, units='Msun')

def _metal_number_density(field, data):

  try:
      metal_dens = data[('enzo', 'Metal_Density')].value
  except:
      try:
          metal_dens = data[('enzo', 'metallicity')].value
      except:
          metal_dens = data[('enzo', 'Metallicity')].value

  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  n = metal_dens / ( 16.0 * u.amu)
  n = n.convert_to_cgs()

  return n
add_field(('gas','Metal_Number_Density'), function = _metal_number_density, units='cm**(-3)')



def _C_Fraction(field, data):
  metal_dens = data[('enzo', 'C_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','C_Fraction'), function = _C_Fraction, units='dimensionless')

def _C_Number_Density(field, data):
    metal_dens = data[('enzo', 'C_Density')].value
    metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
    metal_dens = metal_dens.convert_to_cgs()

    n = metal_dens / (12.0107 * u.amu)
    n = n.convert_to_cgs()

    return n
add_field(('gas','C_Number_Density'), function = _C_Number_Density, units='cm**(-3)')
	
def _O_Fraction(field, data):
  metal_dens = data[('enzo', 'O_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','O_Fraction'), function = _O_Fraction, units='dimensionless')

def _O_Number_Density(field, data):
    metal_dens = data[('enzo', 'O_Density')].value
    metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
    metal_dens = metal_dens.convert_to_cgs()

    n = metal_dens / (15.9994 * u.amu)
    n = n.convert_to_cgs()          

    return n
add_field(('gas','O_Number_Density'), function = _O_Number_Density, units='cm**(-3)')


def _N_Fraction(field, data):
  metal_dens = data[('enzo', 'N_Density')].value
  metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
  metal_dens = metal_dens.convert_to_cgs()

  dens = data[('enzo','Density')].convert_to_units('g/cm**3')

  fraction = metal_dens / dens

  return fraction
add_field(('gas','N_Fraction'), function = _N_Fraction, units='dimensionless')

def _N_Number_Density(field, data):
    metal_dens = data[('enzo', 'N_Density')].value
    metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
    metal_dens = metal_dens.convert_to_cgs()

    n = metal_dens / (14.0067 * u.amu)
    n = n.convert_to_cgs()

    return n
add_field(('gas','N_Number_Density'), function = _N_Number_Density, units='cm**(-3)')


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

def _Fe_Number_Density(field, data):
    metal_dens = data[('enzo', 'Fe_Density')].value
    metal_dens = metal_dens * data.ds.mass_unit / data.ds.length_unit**3
    metal_dens = metal_dens.convert_to_cgs()

    n = metal_dens / (55.845 * u.amu)
    n = n.convert_to_cgs()

    return n
add_field(('gas','Fe_Number_Density'), function = _Fe_Number_Density, units='cm**(-3)')

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


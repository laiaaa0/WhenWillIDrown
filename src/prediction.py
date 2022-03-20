
# Global sea level rise is due to thermal expansion and mass increase
#https://sealevel.nasa.gov/understanding-sea-level/global-sea-level/overview

# Key indicator : 
# Steric height 
#https://sealevel.nasa.gov/understanding-sea-level/key-indicators/steric-height

# Ocean mass
# https://sealevel.nasa.gov/understanding-sea-level/key-indicators/ocean-mass


# Checked on 20 March 2022
OCEAN_MASS_RATE_OF_CHANGE = 2.1
STERIC_MASS_RATE_OF_CHANGE = 1.2
MEAN_SEA_LEVEL_RATE_OF_CHANGE = 3.4

def sea_level_rise(year):
    """
    Return sea level rise in millimeters based on the year
    """

    years_since_1992 = year - 1992
    if years_since_1992 < 0:
        return None
    S = (OCEAN_MASS_RATE_OF_CHANGE+STERIC_MASS_RATE_OF_CHANGE)*years_since_1992

    return S 

def year_sea_level_will_reach(elevation):
    """
    Invert sea_level_rise function, return the year where the water will reach the elevation
    """
    if elevation<0:
        return None
    years_from_1992 = elevation/(OCEAN_MASS_RATE_OF_CHANGE+STERIC_MASS_RATE_OF_CHANGE)

    return 1992+years_from_1992




# Oher interesting articles
#Grinsted, A. and Christensen, J. H.: The transient sensitivity of sea level rise, Ocean Sci., 17, 181–186, https://doi.org/10.5194/os-17-181-2021, 2021.
#https://os.copernicus.org/articles/17/181/2021/

from prediction import year_sea_level_will_reach
import location

def drown_time(longitude, latitude):
    elevation_m = location.elevation(longitude, latitude)
    elevation_mm = elevation_m*1000
    year = year_sea_level_will_reach(elevation_mm)
    return round(year)

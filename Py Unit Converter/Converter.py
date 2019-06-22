from Distance import *

# Distance Units
KILOMETER = "km"
MILE = "mi"
METER = "m"
MILIMETER = "mm"

# Speed Units
KILOMETER_PER_HOUR = "kph"
MILE_PER_HOUR = "miph"
METER_PER_HOUR = "mph"
METER_PER_SECOND = "mps"

# Volume Units
GALLON = "gal"
LITER = "l"

# Pressure Units
KILO_PASCAL = "kpa"
POUNDS_PER_SQUARE_INCH = "psi"
MILIMETER_MERCURY = "mmhg"
BAR = "bar"

# Fuel Economy unit
KILOMETER_PER_GALLON = "kpg"
KILOMETER_PER_LITER = "kpl"
MILE_PER_GALLON = "mipg"
MILE_PER_LITER = "mipl"
METER_PER_GALLON = "mpg"
METER_PER_LITER = "mpl"

# Temperature Unit
CELCIUS = "C"
FAHRENHEINT = "F"
KELVIN = "K"

# Latitude and Longitude format
DEGREES_MINUTES_SECONDS = "dms"
DEGREES_MINUTES = "dmm"
DECIMAL_DEGREES = "dd"


def Convert_Speed(self, parameter_list):
    try:
        pass
    except Exception as e:
        pass

def Convert_Coordinates(self, parameter_list):
    try:
        pass
    except Exception as e:
        pass

def Convert_Volume(self, parameter_list):
    try:
        pass
    except Exception as e:
        pass

def Convert_Pressure(self, parameter_list):
    try:
        pass
    except Exception as e:
        pass

def Convert_Distance(self, value, unitIn, unitOut ):
    try:
        if unitIn == unitOut:
            return value
        if unitIn == METER and unitOut = KILOMETER:
            return Distance_Converter.ConvertToKilometersFromMeters(value)
        if unitIn == METER and unitOut = MILE:
            return Distance_Converter.ConvertToMilesFromMeters(value)
        if unitIn == MILE and unitOut = METER:
            return Distance_Converter.ConvertToMetersFromMiles(value)
        if unitIn == MILE and unitOut = KILOMETER:
            return Distance_Converter.ConvertToKilometersFromMiles(value)
        if unitIn == KILOMETER and unitOut = MILE:
            return Distance_Converter.ConvertToMilessFromKilometers(value)
        if unitIn == KILOMETER and unitOut = METER:
            return Distance_Converter.ConvertToMetersFromKilometers(value)
        if unitIn == MILIMETER and unitOut = MILE:
            return Distance_Converter.ConvertToMilesFromMillimeters(value)
        if unitIn == MILIMETER and unitOut = KILOMETER:
            return Distance_Converter.ConvertToKilometersFromMillimeters(value)
        if unitIn == MILIMETER and unitOut = METER:
            return Distance_Converter.ConvertToMetersFromMillimeters(value)
    except Exception as e:
        return "Error: " + e

def Convert_Consumption(self, parameter_list):
    try:
        pass
    except Exception as e:
        pass

def Convert_Temperature(self, parameter_list):
    try:
        pass
    except Exception as e:
        pass
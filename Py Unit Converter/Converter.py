from Distance import Distance_Converter
from Speed import Speed_Converter
from Volume import Volume_Converter
from Temperature import Temperature_Converter
# Distance Units
KILOMETER = "km"
MILE = "mi"
METER = "m"
MILIMETER = "mm"

# Speed Units
KILOMETER_PER_HOUR = "kph"
KILOMETER_PER_SECOND = "kps"
MILE_PER_HOUR = "miph"
MILE_PER_SECOND = "mips"
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


def Convert_Speed(self, value, unitIn, unitOut):
    try:
        if unitIn == unitOut:
            return value
        elif unitIn == MILE_PER_HOUR and unitOut == KILOMETER_PER_HOUR:
            return Speed_Converter.ConvertToKPHFromMIPH(value)
        elif unitIn == METER_PER_HOUR and unitOut == KILOMETER_PER_HOUR :
            return Speed_Converter.ConvertToKPHFromMPH(value)
        elif unitIn == MILE_PER_SECOND and unitOut == KILOMETER_PER_HOUR :
            return Speed_Converter.ConvertToKPHFromMIPS(value)
        elif unitIn == METER_PER_SECOND and unitOut == KILOMETER_PER_HOUR :
            return Speed_Converter.ConvertToKPHFromMPS(value)

        elif unitIn == KILOMETER_PER_HOUR and unitOut == METER_PER_HOUR:
            return Speed_Converter.ConvertToMPHFromKPH(value)
        elif unitIn == MILE_PER_HOUR and unitOut == METER_PER_HOUR :
            return Speed_Converter.ConvertToMPHFromMIPH(value)
        elif unitIn == KILOMETER_PER_SECOND and unitOut == METER_PER_HOUR :
            return Speed_Converter.ConvertToMPHFromKPS(value)
        elif unitIn == MILE_PER_SECOND and unitOut == METER_PER_HOUR :
            return Speed_Converter.ConvertToMPHFromMIPS(value)
        
        elif unitIn == KILOMETER_PER_HOUR and unitOut == MILE_PER_HOUR:
            return Speed_Converter.ConvertToMIPHFromKPH(value)
        elif unitIn == METER_PER_HOUR and unitOut == MILE_PER_HOUR:
            return Speed_Converter.ConvertToMIPHFromMPH(value)
        elif unitIn == KILOMETER_PER_SECOND and unitOut == MILE_PER_HOUR:
            return Speed_Converter.ConvertToMIPHFromKPS(value)
        elif unitIn == METER_PER_SECOND and unitOut == MILE_PER_HOUR:
            return Speed_Converter.ConvertToMIPHFromMPS(value)
    except Exception as e:
        return "Error : " + e

def Convert_Coordinates(self, value, unitIn, unitOut):
    try:
        pass
    except Exception as e:
        pass

def Convert_Volume(self, value, unitIn, unitOut):
    try:
        if unitIn == unitOut:
            return value
        elif unitIn == LITER and unitOut == GALLON:
            return Volume_Converter.ConvertToGallonFromLiter(value)
        elif unitIn == GALLON and unitOut == LITER:
            return Volume_Converter.ConvertToLiterFromGallon(value)
    except Exception as e:
        return "Error: " + e

def Convert_Pressure(self, value, unitIn, unitOut):
    try:
        pass
    except Exception as e:
        pass

def Convert_Distance(self, value, unitIn, unitOut):
    try:
        if unitIn == unitOut:
            return value
        elif unitIn == METER and unitOut == KILOMETER:
            return Distance_Converter.ConvertToKilometersFromMeters(value)
        elif unitIn == METER and unitOut == MILE:
            return Distance_Converter.ConvertToMilesFromMeters(value)
        elif unitIn == MILE and unitOut == METER:
            return Distance_Converter.ConvertToMetersFromMiles(value)
        elif unitIn == MILE and unitOut == KILOMETER:
            return Distance_Converter.ConvertToKilometersFromMiles(value)
        elif unitIn == KILOMETER and unitOut == MILE:
            return Distance_Converter.ConvertToMilessFromKilometers(value)
        elif unitIn == KILOMETER and unitOut == METER:
            return Distance_Converter.ConvertToMetersFromKilometers(value)
        elif unitIn == MILIMETER and unitOut == MILE:
            return Distance_Converter.ConvertToMilesFromMillimeters(value)
        elif unitIn == MILIMETER and unitOut == KILOMETER:
            return Distance_Converter.ConvertToKilometersFromMillimeters(value)
        elif unitIn == MILIMETER and unitOut == METER:
            return Distance_Converter.ConvertToMetersFromMillimeters(value)
    except Exception as e:
        return "Error: " + e

def Convert_Consumption(self, value, unitIn, unitOut):
    try:
        pass
    except Exception as e:
        pass

def Convert_Temperature(self, value, unitIn, unitOut):
    try:
        if unitIn == unitOut:
            return value
        elif unitIn == FAHRENHEINT and unitOut == CELCIUS:
            return Temperature_Converter.ConvertToCelsiusFromFahrenheint(value)
        elif unitIn == KELVIN and unitOut == CELCIUS:
            return Temperature_Converter.ConvertToCelsiusFromKelvin(value)
        elif unitIn == CELCIUS and unitOut == FAHRENHEINT:
            return Temperature_Converter.ConvertToFahrenheintFromCelsius(value)
        elif unitIn == KELVIN and unitOut == FAHRENHEINT:
            return Temperature_Converter.ConvertToFahrenheintFromKelvin(value)
        elif unitIn == CELCIUS and unitOut == KELVIN:
            return Temperature_Converter.ConvertToKelvinFromCelsius(value)
        elif unitIn == FAHRENHEINT and unitOut == KELVIN:
            return Temperature_Converter.ConvertToKelvinFromFahrenheint(value)
    except Exception as e:
        return "Error: " + e
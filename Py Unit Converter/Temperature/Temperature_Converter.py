
# Convert any to Celcius
def ConvertToCelsiusFromFahrenheint(value):
    try:
        return (value - 32) * (5/9)
    except Exception as e:
        return "Error Converting: " + e

def ConvertToCelsiusFromKelvin(value):
    try:
        return value - 273.15
    except Exception as e:
        return "Error Converting: " + e


# Convert any to Fahrenheint
def ConvertToFahrenheintFromCelsius(value):
    try:
        return (value * 9/5) + 32
    except Exception as e:
        return "Error q Converting: " + e

def ConvertToFahrenheintFromKelvin(value):
    try:
        return ((value - 273.15) * 9/5) + 32
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Kelvin
def ConvertToKelvinFromCelsius(value):
    try:
        return value + 273.15
    except Exception as e:
        return "Error q Converting: " + e

def ConvertToKelvinFromFahrenheint(value):
    try:
        return ((value - 32) * 5/9) + 273.15
    except Exception as e:
        return "Error Converting: " + e        

# Convert any to Celcius
def ConvertToCelsiusFromFahrenheint(self, value):
    try:
        return (value − 32) × 5/9
    except Exception as e:
        return "Error Converting: " + e

def ConvertToCelsiusFromKelvin(self, value):
    try:
        return value - 273.15
    except Exception as e:
        return "Error Converting: " + e


# Convert any to Fahrenheint
def ConvertToFahrenheintFromCelsius(self, value):
    try:
        return (value × 9/5) + 32
    except Exception as e:
        return "Error q Converting: " + e

def ConvertToFahrenheintFromKelvin(self, value):
    try:
        return ((value − 273.15) × 9/5) + 32
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Kelvin
def ConvertToKelvinFromCelsius(self, value):
    try:
        return value + 273.15
    except Exception as e:
        return "Error q Converting: " + e

def ConvertToKelvinFromFahrenheint(self, value):
    try:
        return ((value − 32) × 5/9) + 273.15
    except Exception as e:
        return "Error Converting: " + e        
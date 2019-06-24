

# Convert any to Meters
def ConvertToMetersFromKilometers(value):
    try:
        return (value*1000)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToMetersFromMiles(value):
    try:
        return (value*1609.344)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToMetersFromMillimeters(value):
    try:
        return (value/1000)
    except Exception as e:
        return ("Error converting: " + e)

# Convert any to Kilometers
def ConvertToKilometersFromMeters(value):
    try:
        return (value/1000)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToKilometersFromMiles(value):
    try:
        return (value*1.609)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToKilometersFromMillimeters(value):
    try:
        return (value*100000)
        
    except Exception as e:
        return ("Error converting: " + e)

# Convert any to Miles
def ConvertToMilesFromMeters(value):
    try:
        return (value/1.609)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToMilessFromKilometers(value):
    try:
        return (value/1.609)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToMilesFromMillimeters(value):
    try:
        return (value*1609000)
    except Exception as e:
        return ("Error converting: " + e)

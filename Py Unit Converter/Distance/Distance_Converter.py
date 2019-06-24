

# Convert any to Meters
def ConvertToMetersFromKilometers(self, value):
    try:
        return (value*1000)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToMetersFromMiles(self, value):
    try:
        return (value*1609.344)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToMetersFromMillimeters(self, value):
    try:
        return (value/1000)
    except Exception as e:
        return ("Error converting: " + e)

# Convert any to Kilometers
def ConvertToKilometersFromMeters(self, value):
    try:
        return (value/1000)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToKilometersFromMiles(self, value):
    try:
        return (value*1.609)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToKilometersFromMillimeters(self, value):
    try:
        return (value*100000)
        
    except Exception as e:
        return ("Error converting: " + e)

# Convert any to Miles
def ConvertToMilesFromMeters(self, value):
    try:
        return (value/1.609)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToMilessFromKilometers(self, value):
    try:
        return (value/1.609)
    except Exception as e:
        return ("Error converting: " + e)

def ConvertToMilesFromMillimeters(self, value):
    try:
        return (value*1609000)
    except Exception as e:
        return ("Error converting: " + e)

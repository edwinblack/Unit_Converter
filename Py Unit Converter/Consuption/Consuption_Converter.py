
# Convert any to Kilometer per Allon
def ConvertToKPGFromMIPG(value):
    try:
        return value * 1.609
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPGFromMPG(value):
    try:
        return value * 1000
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPGFromKPL(value):
    try:
        return value * 3.785
    except Exception as e:
        return "Error coneting: " + e

def ConvertToKPGFromMIPL(value):
    try:
        return value *  6.090065
    except Exception as e:
        return "Error coneting: " + e

def ConvertToKPGFromMPL(value):
    try:
        return value / 264.172
    except Exception as e:
        return "Error coneting: " + e

# Convert any to Miles per gallon
def ConvertToMIPGFromKPG(value):
    try:
        return value / 1.609
    except Exception as e:
        return "Error coneting: " + e

def ConvertToMIPGFromMPG(value):
    try:
        return value * 1609
    except Exception as e:
        return "Error coneting: " + e

def ConvertToMIPGFromKPL(value):
    try:
        return value * 2.352
    except Exception as e:
        return "Error coneting: " + e

def ConvertToMIPGFromMIPL(value):
    try:
        return value * 3.785
    except Exception as e:
        return "Error coneting: " + e

def ConvertToMIPGFromMPL(value):
    try:
        return value / 425.144
    except Exception as e:
        return "Error coneting: " + e

# Convert any to Meter per liter
def ConvertToMPLFromKPG(value):
    try:
        return value * 264.172
    except Exception as e:
        return "Error coneting: " + e

def ConvertToMPLFromMIPG(value):
    try:
        return value * 425.099075297
    except Exception as e:
        return "Error coneting: " + e

def ConvertToMPLFromMPG(value):
    try:
        return value / 3.785
    except Exception as e:
        return "Error coneting: " + e

def ConvertToMPLFromKPL(value):
    try:
        return value * 1000
    except Exception as e:
        return "Error coneting: " + e

def ConvertToMPLFromMIPL(value):
    try:
        return value * 1609
    except Exception as e:
        return "Error coneting: " + e
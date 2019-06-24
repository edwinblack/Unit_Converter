import traceback
# Convert any to Kilometer per Hour
def ConvertToKPHFromMPH(value):
    try:
        return value/1000
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPHFromMIPH(value):
    try:
        return value * 1.609
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPHFromMPS(value):
    try:
        return value * 3.6
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPHFromMIPS(value):
    try:
        return value * 5793.638
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Meters per Hour
def ConvertToMPHFromKPH(value):
    try:
        return value*1000
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMPHFromMIPH(value):
    try:
        return value * 1609
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMPHFromKPS(value):
    try:
        return value * 3600000
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMPHFromMIPS(value):
    try:
        return value * 5793624
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Mile per Hour
def ConvertToMIPHFromKPH(value):
    try:
        return value / 1.609
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMIPHFromMPH(value):
    try:
        return value / 1609.344
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMIPHFromKPS(value):
    try:
        return value / 5793.638
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMIPHFromMPS(value):
    try:
        return value * 2.237
    except Exception as e:
        return "Error Converting: " + e
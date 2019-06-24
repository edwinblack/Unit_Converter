import traceback
# Convert any to Kilometer per Hour
def ConvertToKPHFromMPH(self, value):
    try:
        return value/1000
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPHFromMIPH(self, value):
    try:
        return value * 1.609
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPHFromMPS(self, value):
    try:
        return value * 3.6
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPHFromMIPS(self, value):
    try:
        return value * 5793.638
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Meters per Hour
def ConvertToMPHFromKPH(self, value):
    try:
        return value*1000
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMPHFromMIPH(self, value):
    try:
        return value * 1609
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMPHFromKPS(self, value):
    try:
        return value * 3600000
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMPHFromMIPS(self, value):
    try:
        return value * 5793624
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Mile per Hour
def ConvertToMIPHFromKPH(self, value):
    try:
        return value / 1.609
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMIPHFromMPH(self, value):
    try:
        return value / 1609.344
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMIPHFromKPS(self, value):
    try:
        return value / 5793.638
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMIPHFromMPS(self, value):
    try:
        return value * 2.237
    except Exception as e:
        return "Error Converting: " + e
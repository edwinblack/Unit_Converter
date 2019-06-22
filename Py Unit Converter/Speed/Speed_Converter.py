import traceback
# Convert any to Kilometer per Hour
def ConvertKPHFromMPH(self, value):
    try:
        return value/1000
    except Exception as e:
        return "Error Converting: " + traceback.print_exception()

def ConvertToKPHFromMIPH(self, value):
    try:
        return value * 1.609
    except Exception as e:
        return "Error Converting: " + traceback.print_exception()

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
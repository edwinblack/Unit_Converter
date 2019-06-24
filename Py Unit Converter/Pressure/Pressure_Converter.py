
# Convert any to KPA
def ConvertToKPAFromPSI(self, value):
    try:
        return value * 6.895
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPAFromMMHG(self, value):
    try:
        return value / 7.501
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPAFromBAR(self, value):
    try:
        return value * 100
    except Exception as e:
        return "Error Converting: " + e

# Convert any to MMHG
def ConvertToKPAFromPSI(self, value):
    try:
        return value * 6.895
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPAFromMMHG(self, value):
    try:
        return value / 7.501
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPAFromBAR(self, value):
    try:
        return value * 100
    except Exception as e:
        return "Error Converting: " + e
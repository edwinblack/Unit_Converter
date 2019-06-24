
# Convert any to KPA
def ConvertToKPAFromPSI(value):
    try:
        return value * 6.895
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPAFromMMHG(value):
    try:
        return value / 7.501
    except Exception as e:
        return "Error Converting: " + e

def ConvertToKPAFromBAR(value):
    try:
        return value * 100
    except Exception as e:
        return "Error Converting: " + e

# Convert any to MMHG
def ConvertToMMHGFromPSI(value):
    try:
        return value * 51.715
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMMHGFromKPA(value):
    try:
        return value * 7.501
    except Exception as e:
        return "Error Converting: " + e

def ConvertToMMHGFromBAR(value):
    try:
        return value * 750.062
    except Exception as e:
        return "Error Converting: " + e

# Convert any to PsI
def ConvertToPSIFromMMHG(value):
    try:
        return value / 51.715
    except Exception as e:
        return "Error Converting: " + e

def ConvertToPSIFromKPA(value):
    try:
        return value / 6.895
    except Exception as e:
        return "Error Converting: " + e

def ConvertToPSIFromBAR(value):
    try:
        return value * 14.504
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Bar
def ConvertToBARFromMMHG(value):
    try:
        return value / 750.062
    except Exception as e:
        return "Error Converting: " + e

def ConvertToBARFromKPA(value):
    try:
        return value / 100
    except Exception as e:
        return "Error Converting: " + e

def ConvertToBARFromPSI(value):
    try:
        return value / 14.504
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Gallon
def ConvertToGallonFromLiter(value):
    try:
        return value / 3.785
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Liter
def ConvertToLiterFromGallon(value):
    try:
        return value * 3.785
    except Exception as e:
        return "Error Converting: " + e
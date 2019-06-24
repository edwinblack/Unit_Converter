
# Convert any to Degrees Minutes Seconds
def ConvertToDMSFromDD(value):
    try:
        grades = int(value)
        minutes = int((value - grades) * 60)
        seconds = (value - grades - minutes/60) * 3600
        valueString = str(grades) + "° " + str(minutes) + "' " + str(seconds) + "''" 
        return{
            "grades": grades,
            "minutes":minutes,
            "seconds":seconds,
            "valueString":valueString
        }
    except Exception as e:
        return "Error Converting: " + e

def ConvertToDMSFromDMM(value):
    try:
        value = value.split(",")
        grades = int(value[0])
        minutes = int(value[1])
        seconds = int(value[1] - minutes)/60 * 3600
        valueString = str(grades) + "° " + str(minutes) + "' " + str(seconds) + "''" 
        return{
            "grades": grades,
            "minutes":minutes,
            "seconds":seconds,
            "valueString":valueString
        }
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Degrees Minutes
def ConvertToDMMFromDD(value):
    try:
        grades = int(value)
        minutes = int((value - grades) * 60)
        valueString = str(grades) + "° " + str(minutes) + "'" 
        return{
            "grades": grades,
            "minutes":minutes,
            "valueString":valueString
        }
    except Exception as e:
        return "Error Converting: " + e

def ConvertToDMMFromDMS(value):
    try:
        value = value.split(",")
        grades = int(value[0])
        minutes = int(value[1])
        minutes += int(value[2] / 3600) * 60
        valueString = str(grades) + "° " + str(minutes) + "'"
        return{
            "grades": grades,
            "minutes":minutes,
            "valueString":valueString
        }
    except Exception as e:
        return "Error Converting: " + e

# Convert any to Decimal Degrees
def ConvertToDDFromDMS(value):
    try:
        value = value.split(",")
        grades = value[0]
        grades += int(value[1] / 60)
        grades += (value[2] / 3600) * 60
        valueString = str(grades) + "°"
        return{
            "grades": grades,
            "valueString":valueString
        }
    except Exception as e:
        return "Error Converting: " + e

def ConvertToDDFromDMM(value):
    try:
        value = value.split(",")
        grades = int(value[0])
        grades += int(value[1] / 60)
        valueString = str(grades) + "°"
        return{
            "grades": grades,
            "valueString":valueString
        }
    except Exception as e:
        return "Error Converting: " + e
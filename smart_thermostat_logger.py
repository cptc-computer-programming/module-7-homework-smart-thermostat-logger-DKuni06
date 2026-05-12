MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100

COLD_LIMIT = 68
WARM_LIMIT = 76
COLD_COUNT = 0
WARM_COUNT = 0

#ask user for number of tempurature readings and validate the amount
temp_reading_count = int(input("How many Tempurature readings do you want to enter? "))
while temp_reading_count <= 0:
    print("Error: Amount of readings must be greater than 0")
    temp_reading_count = int(input("Please enter a positive value. "))

#creates a list of the temp readings
#had to look up how to save the inputted values and found the dictionary(?) clause
#avg temp value was incorrect so I looked it up and the dictionary clause would not be helpful here,
#i needed the list clause instead
temp_readings = []
# OLD CODE: temp_readings = {}

#requests temp for amount of temp readings inputted
for i in range(1, temp_reading_count + 1):
    temp_reading = int(input(f"Enter temperature reading {i}: "))
    
    #check if the reading is in valid range and save value if so
    #OLD CODE:
    #if temp_reading in range(MIN_VALID_TEMP, MAX_VALID_TEMP + 1):
    #    temp_readings[temp_reading] = temp_reading

    #checks if temp entered is withing valid ranges
    while temp_reading not in range(MIN_VALID_TEMP, MAX_VALID_TEMP + 1):
        print("Error: Temperature must be between 40 and 100 degrees." )
        temp_reading = int(input(f"Enter temperature reading {i}: "))
    
    #adds valid tempurature to the readings list
    temp_readings.append(temp_reading)

    #count temps below or above temp comfort range
    if temp_reading < COLD_LIMIT:
        COLD_COUNT += 1
    elif temp_reading > WARM_LIMIT:
        WARM_COUNT += 1

#calculate the avg of the temps entered
temp_avg = sum(temp_readings) / temp_reading_count

#display summary
print("Smart Thermostat Summary")
print("------------------------")
print(f"Average tempurature: {temp_avg:.1f}")
print(f"Readings below comfort range ({COLD_LIMIT} degrees): {COLD_COUNT}")
print(f"Readings above comfort range ({WARM_LIMIT} degrees): {WARM_COUNT}")
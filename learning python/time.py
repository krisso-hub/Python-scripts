import time

currentTime = time.time()

totalSeconds = int(currentTime)

currentSeconds = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinutes = totalMinutes % 60

totalHours = totalMinutes // 60

currentHour = totalHours % 60

# current time in GMT

print("current time is  :",currentHour, "hours :", currentMinutes, "minutes:", currentSeconds, "seconds")

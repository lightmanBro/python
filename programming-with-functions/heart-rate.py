""""
Name: Omotoso David
Project: Minimum and maximum heart rate calculation.
 'when you physically excercise to strengthen your heart, you shpuld maintain your heart rate within a range for at least 20 minutes. To find that range, subtract your age from 220. This difference is your maximum heart rate per minute. Your heart simply will not beat faster than this maximum (220 - age).
 when excercising to strengthen your heart, you should keep your heart rate between 65% and maximum of 85% of your heart rate."
"""""


userAge = int(input('What is your age?  '))

heartRate = 220 - userAge
maxHeartRate = heartRate * 0.85
minHeartRate = heartRate * 0.65
result = f'when you excercise to strengthen your heart, you should keep your heart rate between {minHeartRate:.0f} and {maxHeartRate:.0f} beats per minute '
print(result)
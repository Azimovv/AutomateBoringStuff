# simple stopwatch program

import time

# Display program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. '
      'Press Ctrl-C to quit')

input()  # press ENTER to begin
print('Started...')
startTime = time.time()  # first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'Lap #{lapNum}: {totalTime} ({lapTime})', end='')
        lapNum += 1
        lastTime = time.time()  # reset last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying
    print('\nDone')
import subprocess
# All lines can be run through the command prompt
# Merely a demonstration of what can be done with subprocess

# Open calculator
subprocess.Popen('C:\\Windows\\System32\\calc.exe')

# Open paint
paintProc = subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')
paintProc.poll() == None  # returns True if process is running when called
paintProc.wait()  # Doesn't return until MS Paint closes
paintProc.poll()  # Returns exit code if process is terminated when called

# Passing command line args
subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\Users\\Sunny\\hello.txt'])

# Running other Python scripts
subprocess.Popen(['C:\\Users\\Sunny\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe',
                  'C:\\Users\\Sunny\\PycharmProjects\\Learn\\GettingStarted\\class_challenge.py'])

# Opening files with default applications
with open('hello.txt', 'w') as fileObj:
    fileObj.write('Hello world')
subprocess.Popen(['start', 'hello.txt'], shell=True)
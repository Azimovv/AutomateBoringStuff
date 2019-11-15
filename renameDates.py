# Rename filenames with American style date format (MM-DD-YYYY) to
# European style format (DD-MM-YYYY)

import shutil, os, re

# Create regex that matches files with American format
datePattern = re.compile(r"^(.*?)"              # all text before date
                         r"((0|1)?\d)-"         # one or two digits for month
                         r"((0|1|2|3)?\d)-"     # one or two digits for day
                         r"((19|20)\d\d)"       # four digits for year
                         r"(.*?)$",             # all text after the date
                         re.VERBOSE)

# Loop over files in working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get full, absolute file path
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename files
    print(f"Renaming {amerFilename} to {euroFilename}...")
    shutil.move(amerFilename, euroFilename)
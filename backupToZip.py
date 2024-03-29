# Copies folder and contents into ZIP file with incremental filename

import zipfile, os

def backupToZip(folder):
    # Backup entire contents of folder into ZIP file

    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out filename the code should use based on what files exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # Create the ZIP file
    print(f"Creating {zipFilename}...")
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk folder tree and compress files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")
        # Add current folder to ZIP file
        backupZip.write(foldername)

        # Add all the files in folder to ZIP file
        for filename in filenames:
            newBase / os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip')
                continue  # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("Done.")


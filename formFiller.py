#  Fills in a form automatically
#  Specifically this form: https://autbor.com/form

import pyautogui, time

submitAnotherLink = (691, 509)
formData = [
    {'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
     'robocop': 4, 'comments': 'Tell Bob I said hi.'},
    {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
     'comments': 'n/a'},
    {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
     'robocop': 1, 'comments': 'Please take the puppets out of the '
                               'break room.'},
    {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
     'robocop': 5, 'comments': 'Protect the innocent. Serve the public '
                               'trust. Uphold the law.'},
    ]

pyautogui.PAUSE = 0.5
pyautogui.alert("Ensure the browser window is active and the form is loaded", "IMPORTANT")

for person in formData:
    # Give the user a chance to kill the script
    if pyautogui.confirm("The script is about to run, continue?") == 'Cancel':
        break
    time.sleep(5)

    print(f"Entering {person['name']}'s info...")
    pyautogui.write(['\t', '\t'])

    # Fill out the Name field
    pyautogui.write(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field
    pyautogui.write(person['fear'] + '\t')

    # Fill out the Source of a Wizard Powers field
    if person['source'] == 'wand':
        pyautogui.write(['down', 'enter', '\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.5)

    # Fill out the RoboCop field
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t'], 0.5)

    # Fill out the Additional Comments field
    pyautogui.write(person['comments'] + '\t')

    # Click submit button
    time.sleep(0.5)  # Wait for the button to activate
    pyautogui.press('enter')

    # Wait until form page has loaded
    print('Submitted form')
    time.sleep(5)

    # Click the submit another response link
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
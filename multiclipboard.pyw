# Saves and loads text to the clipboard
# Usage: py.exe multiclipboard.pyw save <keyword>  - Saves to keyword
#        py.exe multiclipboard.pyw <keyword> - Loads keyword to clipboard
#        py.exe multiclipboard.pyw list - Loads all keywords to clipboard
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipbboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
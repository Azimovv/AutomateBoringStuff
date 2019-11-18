# Open several google search results

import requests, sys, webbrowser, bs4

print("Googling...")  # Display text while downloading Google page
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search results links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open browser tab for each result
linkElems = soup.select('.bkWMgd a')
print(linkElems)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open("https://google.com" + linkElems[i].get('href'))
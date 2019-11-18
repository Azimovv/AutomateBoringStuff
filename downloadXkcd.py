# Downloads every single xkcd comic

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)  # Where to store comics

while not url.endswith('#'):
    # Download the page
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print("Could not find comic image")
    else:
        comicUrl = comicElem[0].get('src')
        # Download image
        print(f"Downloading image {comicUrl}...")
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save image to ./xkcd
        with open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') as fileObj:
            for chunk in res.iter_content(100000):
                fileObj.write(chunk)

    # Get prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print("Done")
import os
import requests
from bs4 import BeautifulSoup

# Create a directory to save the images if it doesn't exist
if not os.path.exists('comics'):
    os.makedirs('comics')

for i in range(1, 10):
    try:
        url = f'https://xkcd.com/{i}/'  # Update the URL to fetch comics from different pages
        print("Fetching URL:", url)
        page = requests.get(url).content
        soup = BeautifulSoup(page, 'html.parser')
        image = soup.select_one('#comic img')['src']
        print("Image URL:", image)
        with open(os.path.join('comics', os.path.basename(image)), 'wb') as f:
            image_url = 'https:' + image
            print("Fetching Image URL:", image_url)
            f.write(requests.get(image_url).content)
    except Exception as e:
        print("Error:", e)
        continue

print('Done')

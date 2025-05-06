import requests
from bs4 import BeautifulSoup
import csv
import time

def crawl(url, max_depth=2, output_file='output.csv'):
    visited = set()
    results = []

    def _crawl(current_url, depth):
        if depth > max_depth or current_url in visited:
            return
        visited.add(current_url)
        
        try:
            response = requests.get(current_url, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to fetch {current_url}: {e}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title'
        results.append({'url': current_url, 'title': title})

        for link in soup.find_all('a', href=True):
            next_url = link['href']
            if not next_url.startswith('http'):
                next_url = requests.compat.urljoin(current_url, next_url)
            _crawl(next_url, depth + 1)
            time.sleep(1)

    _crawl(url, 0)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

crawl('https://vishal1227.blogspot.com/2020/09/welcome-to-my-blogs.html')


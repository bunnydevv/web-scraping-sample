import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.select('.athing'):
        title = item.select_one('.storylink').text
        link = item.select_one('.storylink')['href']
        subtext = item.find_next_sibling('.subtext')

        points = subtext.select_one('.score').text.split()[0] if subtext.select_one('.score') else '0'
        author = subtext.select_one('.hnuser').text if subtext.select_one('.hnuser') else 'unknown'
        comments = subtext.select_one('a[href^="item?id="]').text.split()[0] if subtext.select_one('a[href^="item?id="]') else '0'

        articles.append({
            'title': title,
            'link': link,
            'points': points,
            'author': author,
            'comments': comments
        })
    return articles

if __name__ == "__main__":
    for article in scrape_hacker_news():
        print(f"{article['title']} ({article['link']}) - {article['points']} points by {article['author']} | {article['comments']} comments")

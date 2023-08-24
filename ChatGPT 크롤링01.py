#ChatGPT 크롤링01.py

import requests
from bs4 import BeautifulSoup

def crawl_naver_search_results(search_keyword):
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    results = []
    
    blog_cards = soup.find_all('li', class_='sh_blog_top')
    for card in blog_cards:
        blog_name = card.find('a', class_='sh_blog_title').text
        blog_address = card.find('a', class_='url').get('href')
        posting_date = card.find('dd', class_='txt_inline').text
        
        results.append({
            'blog_name': blog_name,
            'blog_address': blog_address,
            'posting_date': posting_date
        })
    
    return results

if __name__ == "__main__":
    search_keyword = input("Enter the search keyword: ")
    search_results = crawl_naver_search_results(search_keyword)
    
    for result in search_results:
        print("Blog Name:", result['blog_name'])
        print("Blog Address:", result['blog_address'])
        print("Posting Date:", result['posting_date'])
        print("=" * 50)

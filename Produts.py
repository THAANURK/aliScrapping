from selenium import webdriver
import pickle
import time
import csv

driver = webdriver.Chrome('/Users/prasunsarkar/Downloads/chromedrivers')
driver.get("https://aliexpress.com")
cookies = pickle.load(open("cookies.pickle", "rb"))


fd = open('/Users/prasunsarkar/Downloads/document.csv', 'a')
writer = csv.writer(open("/Users/prasunsarkar/Desktop/AliSample.csv", 'a',encoding='utf-8'))

for cookie in cookies:
    driver.add_cookie(cookie)


def extract_product_urls_from_list_page(list_page_url):
    driver.get(list_page_url)
    time.sleep(5)
    cats = driver.find_elements_by_css_selector('span.title')

    all_links = set()
    for ind, cat in enumerate(cats):
        print(cat.text)
        try:
            cat.click()
        except Exception:
            continue
        if ind == 0:
            items = driver.find_elements_by_class_name('item-desc')
            links = [item.get_attribute('href') for item in items]
        else:
            items = driver.find_elements_by_css_selector('div.title > a')
            links = [item.get_attribute('href') for item in items]
        for link in links:
            all_links.add(link)
            print(all_links)
        time.sleep(2)
        writer.writerow([all_links])
    return all_links

if __name__ == '__main__':
    extract_product_urls_from_list_page('https://sale.aliexpress.com/__pc/bestselling.htm')
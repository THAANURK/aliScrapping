fk_path = 'https://www.flipkart.com"
from selenium import webdriver
browser = webdriver.Chrome('/home/subhasis/chromedriver')
browser.get(fk_path)
browser.find_element_by_xpath("//span[@class='_1EPkIx']/span").click() # Mimick clicking on 'Read More'
[p.click() for p in browser.find_elements_by_xpath("//span[@class='_1EPkIx']/span")] # Expand all 'Read More' buttons
browser.find_element_by_xpath("//div[@class='_3DCdKt']//div[@class='qwjRop']/div").text # Extract texts from respective Xpaths (1st review)


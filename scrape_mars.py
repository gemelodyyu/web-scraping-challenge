from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import requests


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

    
def scrape():
    browser = init_browser()
    mars = {}

    # NASA Mars News
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
 
    first_news = soup.select_one('ul.item_list, li.slide')

    news_title = first_news.find('div', class_= 'content_title').get_text()
    news_p = first_news.find('div', class_= 'article_teaser_body').get_text()


    # JPL Mars Space Images - Featured Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    full_image_button = browser.find_by_id("full_image")
    full_image_button.click()

    more_info_element = browser.links.find_by_partial_text("more info")
    more_info_element.click()

    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")
 
    image_url = image_soup.select_one("figure.lede a img").get("src")
    
    featured_image_url = f"https://www.jpl.nasa.gov{image_url}"


    # Mars Facts
    url = "https://space-facts.com/mars/"

    tables = pd.read_html(url)

    facts_df = tables[0]
    facts_df.columns=["Description","Mars"]
    facts_df.set_index("Description", inplace = True)

    html_table = facts_df.to_html(classes="table table_striped")
    

    # Mars Hemispheres
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    hemisphere_image_urls = []

    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
        hemisphere = {}
        
        browser.find_by_css("a.product-item h3")[item].click()
        
        sample_element = browser.find_link_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]
        
        hemisphere["title"] = browser.find_by_css("h2.title").text
        
        hemisphere_image_urls.append(hemisphere)
        
        browser.back()


    mars["news_title"] = news_title
    mars["news_paragraph"] = news_p
    mars["featured_image"] = featured_image_url
    mars["facts"] = html_table
    mars["hemisphere"] = hemisphere_image_urls

    browser.quit()

    return mars 

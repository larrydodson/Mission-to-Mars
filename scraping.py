
# Module 10, Mission to Mars Challenge
# Import Splinter,  BeautifulSoup, Pandas, and datetime
from splinter import Browser, browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
import time
import requests
import pymongo

def scrape_all():
    # Initiate headless driver for deployment (initialize the browser)
    browser = Browser("chrome", executable_path="chromedriver", headless=False)
    # set news title and paragraph variables 
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary (create data dictionary)
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "weather": mars_weather(browser),
        "hemisphere_title": title,
        "hemispheres": hemisphere_image_urls,
        "last_modified": dt.datetime.now()
    }
    # Stop webdriver and return scraped data
    browser.quit()
    return data

# Featured Articles
def mars_news(browser):
    
    # Scrape Mars news
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Set up the HTML parser. Convert the browser html to a soup object and then quit the browser.
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        # assign the title and summary text to variables to reference later. Begin scraping: 
        #slide_elem.find("div", class_='content_title')

        # Use the parent element to find the first 'a' tag and save it as `news_title`
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()
        
    except AttributeError:
        return None, None
    return news_title, news_p


# Featured Image JPL
def featured_image(browser):
# Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    except AttributeError:
        return None
    #img_url_rel

    # Use the base URL to create an absolute URL
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    return img_url

# Mars Facts
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]
        #df.head()
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Data']
    df.set_index('Description', inplace=True)
    #df
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

# Mars Weather
def mars_weather(browser):
    insight_url = 'https://mars.nasa.gov/insight/weather/'
    browser.visit(insight_url)
# Parse the data
    html = browser.html
    weather_soup = soup(html, 'html.parser')
# Scrape the Daily Weather Report table
    weather_table = weather_soup.find('table', class_='mb_table')
    print(weather_table.prettify())

    #<a class="inline_image_enlarge fancybox" href="https://mars.nasa.gov/rss/api/images/insight_marsweather_white.png">
#<img alt="Three Day Weather Report" src="https://mars.nasa.gov/rss/api/images/insight_marsweather_white.png">
# 
    # Find the relative image url
    #img_url_rel = weather_soup.select_one('a', class_='inline_image_enlarge fancybox').get('src')

    #weather_img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    return weather_table.prettify()

# Deliverable-1, Scrape High-Resolution Mars Hemisphere Images and Titles

# Initiate headless driver for deployment (initialize the browser)
browser = Browser("chrome", executable_path="chromedriver", headless=False)

# 1. Use browser to visit the URL 
long_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(long_url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=2)
# main_url 
short_url = 'https://astrogeology.usgs.gov'

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
browser.visit(long_url)
html = browser.html
hemi_soup = soup(html, 'html.parser')
main_url = hemi_soup.find_all('div', class_='item')
titles=[]

# Loop through the items previously stored
#def mars_hemispheres():
for i in main_url:
    hemispheres = {}
    title = i.find('h3').get_text()
    url = i.find('a')['href']
    hem_img_url= short_url+url
    #print(hem_img_url)
    browser.visit(hem_img_url)
    html = browser.html
    hemi_soup = soup(html, 'html.parser')
    hemisphere_img_original = hemi_soup.find('div', class_='downloads')
    hemisphere_img_url = hemisphere_img_original.find('a')['href']
    # use 'browser.back'  ***  
    #print(hemisphere_img_url)
    hemispheres = dict({'title': title, 'img_url': hemisphere_img_url})
    hemisphere_image_urls.append(hemispheres)
    browser.back()


#    hemispheres = {hemisphere_image_urls}
#mars_data['hemisphere_image_urls'] = hemisphere_image_urls

    #return mars_data

# 4. Print the list that holds the dictionary of each image url and title.
    hemisphere_image_urls

# 5. Quit the browser
browser.quit()

# Tell Flask the script is complete and ready. 
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

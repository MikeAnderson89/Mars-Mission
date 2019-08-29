def scrape():
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    import requests
    from splinter import Browser
    import time

    #Latest Headline / Paragraph
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    browser = Browser('chrome', headless=True)
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'lxml')

    first_link_title = soup.find(class_='content_title').text.strip()
    first_link_para = soup.find(class_='article_teaser_body').text.strip()
    browser.quit()




    #Image URL
    jpeg_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser = Browser('chrome', headless=True)
    browser.visit(jpeg_url)

    html = browser.html
    soup = bs(html, 'lxml')

    full_image_button = soup.find(class_="button fancybox")
    browser.click_link_by_id('full_image')
    time.sleep(2)

    browser.click_link_by_partial_text('more info')
    browser.click_link_by_partial_text('.jpg')

    featured_img_url = browser.url
    browser.quit()



    #Mars Weather
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser = Browser('chrome', headless=True)
    browser.visit(weather_url)

    html = browser.html
    soup = bs(html, 'lxml')

    mars_weather = soup.find(class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').get_text()
    browser.quit()


    #Mars Facts
    facts_url = 'https://space-facts.com/mars/'
    browser = Browser('chrome', headless=True)
    browser.visit(facts_url)

    mars_facts = pd.read_html(facts_url)
    mars_facts = mars_facts[1]
    mars_facts = mars_facts.rename(columns={0: 'Mars Planet Profile', 1: ''})
    mars_facts.set_index('Mars Planet Profile')

    mars_html = mars_facts.to_html(index=False, table_id='fact_table')



    #Mars Hemispheres
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser = Browser('chrome', headless=True)
    browser.visit(hemi_url)

    html = browser.html
    soup = bs(html, 'lxml')

    #Cerberus
    links = soup.find_all('h3')
    browser.click_link_by_partial_text('Cerberus')
    time.sleep(1)
    browser.click_link_by_partial_text('Sample')
    browser.windows.current = browser.windows[1]
    cerberus_url = browser.url
    cerberus_dict = {
        'title': 'Cerberus Hemisphere',
        'img_url': cerberus_url
    }

    browser.windows[1].close()
    browser.back()

    #Schiaparelli
    browser.click_link_by_partial_text('Schiaparelli')
    time.sleep(1)
    browser.click_link_by_partial_text('Sample')
    browser.windows.current = browser.windows[1]
    schiaparelli_url = browser.url
    schiaparelli_dict = {
        'title': 'Schiaparelli Hemisphere',
        'img_url': schiaparelli_url
    }

    browser.windows[1].close()
    browser.back()

    #Syrtis Major
    browser.click_link_by_partial_text('Syrtis')
    time.sleep(1)
    browser.click_link_by_partial_text('Sample')
    browser.windows.current = browser.windows[1]
    syrtis_url = browser.url
    syrtis_dict = {
        'title': 'Syrtis Major Hemisphere',
        'img_url': syrtis_url
    }

    browser.windows[1].close()
    browser.back()

    #Valles Marineris
    browser.click_link_by_partial_text('Valles')
    time.sleep(1)
    browser.click_link_by_partial_text('Sample')
    browser.windows.current = browser.windows[1]
    valles_url = browser.url
    valles_dict = {
        'title': 'Valles Marineris Hemisphere',
        'img_url': valles_url
    }
    browser.quit()

    #Hemisphere Dictionary
    hemisphere_urls = [cerberus_dict, schiaparelli_dict, syrtis_dict, valles_dict]

    #Summing Dictionary
    Mars_Info = {
    'headline': first_link_title,
    'paragraph': first_link_para,
    'featured_image': featured_img_url,
    'weather': mars_weather,
    'facts': mars_html,
    'hemispheres': hemisphere_urls
    }

    return Mars_Info

from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def get_article_text():
    web = 'https://www.newsweek.com/newsfeed'
    path = 'C:/Users/amitg/Downloads/chromedriver'

    # Creating the driver
    driver_service = Service(executable_path=path)
    driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
    driver.get(web)

    country_list_href = driver.find_elements(by='xpath',
                                            value='//*[@id="block-nw-nw-archive"]/div/div[2]/article/div[1]/a')

    article_list = []
    for l in country_list_href:
        link = l.get_attribute('href')
        driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
        driver.get(link)
        s = ''
        for t in driver.find_elements(by='xpath',value='//*[@id="v_article"]/div[5]/p'):
            s += t.text
        if len(s.split(' ')) > 100:
            article_list.append(s)
        driver.close()
    return article_list

article_list = get_article_text()
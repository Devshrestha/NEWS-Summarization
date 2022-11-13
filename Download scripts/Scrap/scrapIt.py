from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def get_article_text():
    web = 'https://www.bbc.com/news/the_reporters'
    path = 'C:/Users/amitg/Downloads/chromedriver'

    # Creating the driver
    driver_service = Service(executable_path=path)
    driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
    driver.get(web)

    country_list_href = driver.find_element(by='xpath',
                                            value='//*[@id="topos-component"]/div[3]/div/div/div[1]/div/div[2]/div[1]/a')

    link = country_list_href.get_attribute('href')
    driver.get(link)

    a = driver.find_elements(by='xpath', value='//*[@id="main-content"]/div[5]/div')

    text = []
    for k, i in enumerate(a):
        text.append(i.text)

    text = ' '.join(' '.join(text).split())
    return text

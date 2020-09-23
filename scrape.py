from selenium import webdriver
import Responses
from selenium.webdriver.chrome.options import Options
import time


def scrape(url, driver):
    # driver_path = 'chromedriver_win32/chromedriver.exe'
    # chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument("headless")

    # driver = webdriver.Chrome(driver_path, options=chromeOptions)

    driver.get(url)

    try:
        agree = driver.find_element_by_class_name("cIvzTE")
        agree.click()
        # print("Agreed to cookies")
    except:
        # print("There was no 'agree to cookies' box")
        pass

    iter = 0
    while True:
        try:
            button = driver.find_element_by_class_name("fwhQq")
            print("Clicked the button")
            button.click()
            iter +=10
            print("number added: {}".format(iter))
            time.sleep(.25)
        except:
            # print("Done clicking buttons")
            break



    className = []
    quality = []
    difficulty = []
    comments = []
    dates = []
    prof_name = None

    # for i in driver.find_elements_by_xpath("//*[text() = 'Quality']/following-sibling::text()"):
    #     # print("hello")
    #     quality.append('i')

    try:
        for i in driver.find_elements_by_xpath("//div[@class = 'RatingHeader__StyledHeader-sc-1dlkqw1-0 fLijLk']/div[@class = 'RatingHeader__ClassInfoWrapper-sc-1dlkqw1-1 jxOApy']/div[@class = 'RatingHeader__StyledClass-sc-1dlkqw1-2 cElrQc']"):
            className.append(i.text)
    except:
        print("Unable to find the class name for {}".format(url))

    try:
        for i in driver.find_elements_by_xpath("//div[@class = 'RatingValues__RatingValue-sc-6dc747-3 iZENup'] | //div[@class = 'RatingValues__RatingValue-sc-6dc747-3 fBPVTR'] | //div[@class = 'RatingValues__RatingValue-sc-6dc747-3 kMhQwk']"):
            quality.append(float(i.text))
    except:
        print("Unable to find the qualtiy rating for {}".format(url))

    try:
        for i in driver.find_elements_by_xpath("//div[@class = 'RatingValues__RatingValue-sc-6dc747-3 ieQwTJ']"):
            difficulty.append(float(i.text))
    except:
        print("Unable to find the difficulty rating for {}".format(url))

    try:
        for i in driver.find_elements_by_xpath("//div[@class = 'Rating__RatingInfo-sc-1rhvpxz-3 fFJUNb']/div[@class = 'Comments__StyledComments-dzzyvm-0 dvnRbr']"):
            comments.append(i.text)
    except:
        print("Unable to find the class name for {}".format(url))

    try:
        for i in driver.find_elements_by_xpath("//div[@id='root']/div[1]/div[1]/div[3]/div[4]/div[1]/div[1]/ul[1]/li/div[1]/div[1]/div[3]/div[1]/div[2]"):
            dates.append(i.text)
    except:
        print("Unable to find the date for {}".format(url))

    try:
        print("getting professor name")
        prof_first_name = driver.find_element_by_xpath("//div[@class = 'NameTitle__Name-dowf0z-0 jeLOXk']/span").text
        prof_last_name = driver.find_element_by_xpath("//span[@class = 'NameTitle__LastNameWrapper-dowf0z-2 glXOHH']").text
        prof_name = "{} {}".format(prof_first_name, prof_last_name)
        print(prof_name)

    except:
        prof_name = "Error Error"
        print("Unable to find the professor name for {}".format(url))

    # driver.quit()
    return className, quality, difficulty, comments, prof_name, dates

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
        print("There was no 'agree to cookies' box")

    while True:
        try:
            button = driver.find_element_by_class_name("fwhQq")
            button.click()
            # print("clicked the button")
            time.sleep(.25)
        except:
            # print("Done clicking buttons")
            break



    className = []
    quality = []
    difficulty = []
    comments = []

    # for i in driver.find_elements_by_xpath("//*[text() = 'Quality']/following-sibling::text()"):
    #     # print("hello")
    #     quality.append('i')

    for i in driver.find_elements_by_xpath("//div[@class = 'RatingHeader__StyledHeader-sc-1dlkqw1-0 gEcqZY']/div[@class = 'RatingHeader__ClassInfoWrapper-sc-1dlkqw1-1 cNKhAZ']/div[@class = 'RatingHeader__StyledClass-sc-1dlkqw1-2 hBbYdP']"):
        className.append(i.text)
    for i in driver.find_elements_by_xpath("//div[@class = 'RatingValues__RatingValue-sc-6dc747-3 huchqN'] | //div[@class = 'RatingValues__RatingValue-sc-6dc747-3 kANgLI'] | //div[@class = 'RatingValues__RatingValue-sc-6dc747-3 kUfTQq']"):
        quality.append(float(i.text))
    for i in driver.find_elements_by_xpath("//div[@class = 'RatingValues__RatingValue-sc-6dc747-3 cKZySD']"):
        difficulty.append(float(i.text))
    for i in driver.find_elements_by_xpath("//div[@class = 'Comments__StyledComments-dzzyvm-0 dEfjGB']"):
        comments.append(i.text)

    prof_name = driver.find_element_by_xpath("//div[@class = 'NameTitle__Name-dowf0z-0 cjgLEI']").text


    # driver.quit()
    return className, quality, difficulty, comments, prof_name
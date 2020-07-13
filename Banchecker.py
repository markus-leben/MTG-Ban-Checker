from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from playsound import playsound
import random
import string
import time


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def banCheck(url):
    chrome_driver = ChromeDriverManager().install()
    driver_ = webdriver.Chrome(chrome_driver)

    found = False

    count = 0
    while not found:
        randq = "?" + randomString(25)
        # garabgq = random.
        try:
            driver_.get(url + randq)
            soup = BeautifulSoup(driver_.page_source, "html.parser")
            this = soup.find(class_="content")
            that = soup.find(class_="no-result")

            if str(this.contents[1]) == "<p>You are not authorized to access this page.</p>"\
                    or str(that.contents[0]) == "\n        no result found      ":
                print("same old same old")
                time.sleep(5)
            else:
                print("you're allowed acccess now")
                found = True
            print(count)
            count += 1

        except:
            found = True # fails loud in order to alert you of if your internet cuts out or the code otherwise fails, to avoid giving a false sense of security
    playsound('Kill Bill Ironside Siren Sound.mp3')

    time.sleep(1200)

    driver_.quit()


if __name__ == "__main__":
    banCheck("https://magic.wizards.com/en/articles/archive/news/july-13-2020-banned-and-restricted-announcement")

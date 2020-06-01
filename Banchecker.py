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
        randq = "?" + randomString(25) # appending a garbage string in order to cold cache
        try:
            driver_.get(url + randq)
            soup = BeautifulSoup(driver_.page_source, "html.parser")
            this = soup.find(class_="content")

            if str(this.contents[1]) == "<p>You are not authorized to access this page.</p>":
                # Wizards pages you can't access will consistently have this string. 
                print("same old same old")
            else:
                print("you're allowed acccess now")
                found = True
            print(count)
            
            # if you want to limit your rate put a sleep somewhere in here 
            count += 1

        except:
            time.sleep(20) # prevents request spam in error case
    playsound('Kill Bill Ironside Siren Sound.mp3') # switch this with whatever

    driver_.quit()


if __name__ == "__main__":
    banCheck("https://magic.wizards.com/en/articles/archive/news/june-1-2020-banned-and-restricted-announcement")

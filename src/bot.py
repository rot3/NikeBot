from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from time import sleep
from datetime import datetime
import hashlib, os, pause

from product import Product,LaunchTime

CHROME_DRIVER_PATH = 'C:\Webdrive\chromedriver'

with open('mydata\\secrets.txt','r') as file:
    MY_EMAIL = file.readline().rstrip('\n')
    MY_PASSWORD = file.readline().rstrip('\n')
    HASHED_PASSWORD = file.readline().rstrip('\n')
    FIRST_NAME = file.readline().rstrip('\n')
    LAST_NAME = file.readline().rstrip('\n')
    NUMBER = file.readline().rstrip('\n')
    STREET = file.readline().rstrip('\n')
    CITY = file.readline().rstrip('\n')
    STATE = file.readline().rstrip('\n')
    ZIP_CODE = file.readline().rstrip('\n')

with open('mydata\\apa.txt','r') as file:
    APA_EMAIL = file.readline().rstrip('\n')
    APA_PASSWORD = file.readline().rstrip('\n')

class Bot:    
    def __init__(self,product,email=MY_EMAIL,password=MY_PASSWORD):
        self.product = product
        self.email = email
        self.password = password
        self.set_up()
        self.size = product.size
        options = Options()
        #options.headless = True
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH, options = options)
        self.driver.get(product.link)
        sleep(1)
        self.login()
        sleep(2)        
        self.countdown()
        self.select_size()
        sleep(1000)
        
    
    def set_up(self):
        release_time = self.product.launch_time.get_all()
        if release_time['min']  in range(0,5):
            release_time['min'] += 55
        pause.until(datetime(
            release_time['year'],
            release_time['mon'],
            release_time['day'],
            (release_time['hr']-1),
            (release_time['min'])-5))
    
    def countdown(self):
        pause.until(datetime(2020,8,17,9,59,58))
        self.driver.refresh()

    def login(self):
 
        sleep(1)
        LOG_IN = "//button[text() = 'Join / Log In']"
        try:
            self.driver.find_element_by_xpath("//button[@data-qa='top-nav-join-or-login-button']").click()
        except ElementNotInteractableException:
            self.driver.find_element_by_xpath("//i[@class = 'g72-menu va-sm-t']").click()
            sleep(1)
            self.driver.find_element_by_xpath("//button[@data-qa='join-login-button']").click()

        EMAIL_XPATH = "//input[@type = 'email']"
        while(True):
            try:
                email_input = self.driver.find_element_by_xpath(EMAIL_XPATH)
                break;
            except NoSuchElementException:
                sleep(.2)

        email_input.send_keys(self.email)
        PASSWORD_XPATH = "//input[@type = 'password']"
        password_input = self.driver.find_element_by_xpath(PASSWORD_XPATH)
        password_input.send_keys(self.password)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@value = 'SIGN IN']").click()
        sleep(1)
        while(True):
            try:
                self.driver.find_element_by_xpath("//input[@value = 'Dismiss this error']").click()
                self.driver.find_element_by_xpath(PASSWORD_XPATH).send_keys(self.password )
                self.driver.find_element_by_xpath("//input[@value = 'SIGN IN']").click()
            
            except NoSuchElementException:
                print('signed in')
                break
            except ElementNotInteractableException:
                print('signed in2')
                break


    def select_size(self):
        size_format = 'M '+ str(self.size) +' / W ' + str(self.size + 1.5)
        SIZE_XPATH = "//button[text() = '" + size_format +"']"
        self.driver.find_element_by_xpath(SIZE_XPATH).click()

        BUY_NOW = "//button[@data-qa = 'feed-buy-cta']"  
        self.driver.find_element_by_xpath(BUY_NOW).click()

        sleep(1)
        self.enter_cvv()

    def enter_cvv(self):
        while(True):
            try:
                x = self.driver.find_element_by_xpath("//input[@data-shortname='cvv']")
                x.click()
                x.send_keys('415')
                break
            except NoSuchElementException:
                print('looking')
                sleep(.5)

        save = self.driver.find_elements_by_xpath("//button[@data-qa = 'save-button']").click()
        for i in range (0,len(save)):
            try:
                save[i].click()
            except NoSuchElementException:
                continue
            except ElementNotInteractableException:
                continue

    def buy_(self):
        buy_now_x = ''
        self.driver.find_element_by_xpath(buy_now_x)
    def get_ship_path(self,path):
        shipping_paths = "//input[@id = '"+ path +"']"    
    


# size = input("Size: ")
# email = input('Account: ')
blk_jrdn = Product(size = 11,launch_time=LaunchTime(19,8),link = 'https://www.nike.com/launch/t/ajnt-23-black')
Bot(blk_jrdn)
Bot('https://www.nike.com/launch/t/ajnt-23-black',size = 10.5,email=APA_EMAIL,password=APA_PASSWORD)
#NikeBot(url,13)
#
# //button[text() = 'Go to Checkout']|
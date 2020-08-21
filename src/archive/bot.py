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
        self.enter_cvv()
        self.buy()
        
        
        sleep(1000)
        
    def find(self,xpath):
        self.driver.find_element_by_xpath(xpath)
    def find_click(self,xpath):
        self.driver.find_element_by_xpath(xpath).click()
    def find_send_key(self,xpath,key):
        self.driver.find_element_by_xpath(xpath).send_keys(key)

    def set_up(self):
        drop_time = self.product.launch_time.get_all()
        if drop_time['min']  in range(0,5):
            drop_time['min'] += 55

        pause.until(datetime(
            drop_time['year'],
            drop_time['mon'],
            drop_time['day'],
            (drop_time['hr']-1),
            (drop_time['min'])-5))
    
    def countdown(self):
        pause.until(datetime(2020,8,17,9,59,58))
        self.driver.refresh()

    def login(self):
        sleep(1)
        LOG_IN = "//button[text() = 'Join / Log In']"
        try:
            self.find_click("//button[@data-qa='top-nav-join-or-login-button']")
            # self.driver.find_element_by_xpath("//button[@data-qa='top-nav-join-or-login-button']").click()
        except ElementNotInteractableException:
            self.find_click("//i[@class = 'g72-menu va-sm-t']")
            sleep(1)
            self.find_click("//button[@data-qa='join-login-button']")
            # self.driver.find_element_by_xpath("//i[@class = 'g72-menu va-sm-t']").click()
            # sleep(1)
            # self.driver.find_element_by_xpath("//button[@data-qa='join-login-button']").click()

        EMAIL_XPATH = "//input[@type = 'email']"
        while(True):
            try:
                self.find_send_key(EMAIL_XPATH,self.email)
                #email_input = self.driver.find_element_by_xpath(EMAIL_XPATH)
                break;
            except NoSuchElementException:
                sleep(.2)
        #email_input.send_keys(self.email)

        PASSWORD_XPATH = "//input[@type = 'password']"
        self.find_send_key(PASSWORD_XPATH,self.password)
        # password_input = self.driver.find_element_by_xpath(PASSWORD_XPATH)
        # password_input.send_keys(self.password)
        
        sleep(1)
        self.find_click("//input[@value = 'SIGN IN']")
        #self.driver.find_element_by_xpath("//input[@value = 'SIGN IN']").click()
        sleep(1)
        #Handle login Error
        while(True):
            try:
                self.find_click("//input[@value = 'Dismiss this error']")
                self.find_send_key(PASSWORD_XPATH,self.password)
                self.find_click("//input[@value = 'SIGN IN']")

                # self.driver.find_element_by_xpath("//input[@value = 'Dismiss this error']").click()
                # self.driver.find_element_by_xpath(PASSWORD_XPATH).send_keys(self.password )
                # self.driver.find_element_by_xpath("//input[@value = 'SIGN IN']").click()
            
            except NoSuchElementException:
                print('signed in')
                break
            except ElementNotInteractableException:
                print('signed in2')
                break


    def select_size(self):
        size_format = 'M '+ str(self.size) +' / W ' + str(self.size + 1.5)
        if(self.product.is_shoe()):
            size_format = self.product.size

        self.find_click("//button[text() = '" + size_format +"']")
        # self.driver.find_element_by_xpath("//button[text() = '" + size_format +"']").click()

        # Buy Now Brings up payment screen
        self.find_click("//button[@data-qa = 'feed-but-cta']")
        # self.driver.find_element_by_xpath("//button[@data-qa = 'feed-buy-cta']" ).click() 



    def enter_cvv(self):
        sleep(1)
        iframe = self.driver.find_element_by_xpath("//iframe[@title='creditCardIframeForm']")
        self.driver.switch_to.frame(iframe)
        while(True):
            try:
                self.find_send_key("//input[@data-shortname='cvv']","415")
                # x = self.driver.find_element_by_xpath("//input[@data-shortname='cvv']")
                # x.click()
                # x.send_keys('415')
                break
            except NoSuchElementException:
                print('looking')
                sleep(.5)
        self.driver._switch_to.default_content()
        
        save = self.driver.find_elements_by_xpath("//button[@data-qa = 'save-button']")
        for i in range (0,len(save)):
            try:
                save[i].click()
            except NoSuchElementException:
                continue
            except ElementNotInteractableException:
                continue

    def buy(self):
        self.find_click("//button[text()='Submit Order']")
        # buy_now_x = "//button[text()='Submit Order']"
        # self.driver.find_element_by_xpath(buy_now_x).click()
   
    


# size = input("Size: ")
# email = input('Account: ')
blk_jrdn = Product(size = 4,launch_time=LaunchTime(20,8),link = 'https://www.nike.com/launch/t/space-hippie-01-wheat-white?size=11')
Bot(blk_jrdn)


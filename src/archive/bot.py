from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from time import sleep
from datetime import datetime
from pass_hash import hash_password
import hashlib, os
import pause

from flask import Flask, request, redirect,Response
from twilio.twiml.messaging_response import MessagingResponse

CHROME_DRIVER_PATH = 'C:\Webdrive\chromedriver'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



twilio_num = ""
with open('mydata\\secrets.txt','r') as file:
    EMAIL = file.readline().rstrip('\n')
    PASSWORD = file.readline().rstrip('\n')
    HASHED_PASSWORD = file.readline().rstrip('\n')
    FIRST_NAME = file.readline().rstrip('\n')
    LAST_NAME = file.readline().rstrip('\n')
    NUMBER = file.readline().rstrip('\n')
    STREET = file.readline().rstrip('\n')
    CITY = file.readline().rstrip('\n')
    STATE = file.readline().rstrip('\n')
    ZIP_CODE = file.readline().rstrip('\n')





verification_code = None

class NikeBot:
    CART_URL = 'https://www.nike.com/us/en/cart'
    def __init__(self,url,size):
        request_password_input = "Enter Password:"
        while True:
            self.PASSWORD = hash_password(input(request_password_input))
            if(HASHED_PASSWORD == PASSWORD):
                break
            else:
                print('Incorrect Password!')
        self.size = size

        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.driver.fullscreen_window()
        print(self.driver.get_window_size)
        self.driver.get(url)
        sleep(2)
        
        self.add_cart()
        sleep(500)
    
    def refresh(self):
        return
    def setup(self):
        
        return 
    def add_cart(self):
        #ex: M 13 / W 14.5
        size_format = 'M '+ str(self.size) +' / W ' + str(self.size + 1.5)
        SIZE_XPATH = "//label[text() = '" + size_format +"']"
        self.driver.find_element_by_xpath(SIZE_XPATH).click()
    
        ADD_CART_XPATH = "//button[text() = 'Add to Cart']"
        self.driver.find_element_by_xpath(ADD_CART_XPATH).click()

        CHECKOUT_CPATH = "//button[text()='Checkout']"
        while(True):
            try:
                self.driver.find_element_by_xpath(CHECKOUT_CPATH).click()
                break;
            except ElementNotInteractableException:
                print('Checkout Box not loaded')
        
        self.member_checkout()

    def open_cart(self):
        CART_XPATH = "//a[@href = 'https://www.nike.com/us/en/cart']" 
        self.driver.find_element_by_xpath(CART_XPATH).click()
        self.go_to_checkout()   
    #from cart
    def go_to_checkout(self):
        GO_TO_CHECKOUT_XPATH = "//button[text() = 'Go to Checkout']"
        CHECKOUT_XPATH =  "//button[text() = 'Checkout']"
        combined_path = GO_TO_CHECKOUT_XPATH +'|'+ CHECKOUT_XPATH
        while True:
            try:
                checkout = self.driver.find_elements_by_xpath(combined_path)
                break;
            except NoSuchElementException:
                print('Cart Loading')
        try:
            checkout[0].click()
        except ElementNotInteractableException:
            checkout[1].click()
        
        if self.driver.current_url == CART_URL:
            MEMBER_CHECKOUT_XPATH = "//button[text = 'Member Checkout']"
            GUEST_CHECKOUT_XPATH = "//button[text = 'Guest Checkout']"
        self.member_checkout()
        self.guest_checkout
         
    def member_checkout(self):
        EMAIL_XPATH = "//input[@type = 'email']"
        print(self.driver.current_url)
        if self.driver.current_url == CART_URL:
            self.go_to_checkout()
            return
        while(True):

            try:
                email_input = self.driver.find_element_by_xpath(EMAIL_XPATH)
                break;
            except NoSuchElementException:
                print('Waiting on Checkout page...' )
        email_input.send_keys(EMAIL)

        PASSWORD_XPATH = "//input[@type = 'password']"
        password_input = self.driver.find_element_by_xpath(PASSWORD_XPATH)
        password_input.send_keys(PASSWORD)

        keep_xpath = "//input[@type = 'checkbox']"
        keep_signed_in = self.driver.find_element_by_xpath(keep_xpath).click()
        
    def guest_checkout(self):
        if self.driver.current_url() == CART_URL:
            self.go_to_checkout()
            return
        GUEST_XPATH = "//button[@aria-label ='Guest Checkout']"
        while(True):
            try:
                self.driver.find_element_by_xpath(GUEST_XPATH).click()
                break;
            except NoSuchElementException:
                print('Waiting on checkkout page')

        #info enter
        FIRST_NAME_XPATH = "input[@id = 'firstName']"
        LAST_NAME_XPATH = "input[@id = 'lastName']"
        ADDRESS_XPATH = "input[@id = 'search-adress-input']"
        EMAIL_XPATH = "input[@id = 'email']"
        P_NUMBER_XPATH = "input[@id = 'phoneNumber']"

        driver.find_element_by_xpath(FIRST_NAME_XPATH).send_keys(FIRST_NAME)
        driver.find_element_by_xpath(LAST_NAME_XPATH).send_keys(LAST_NAME)
        driver.find_element_by_xpath(ADDRESS_XPATH).send_keys(STREET + ' ' +CITY)
        driver.find_element_by_xpath(EMAIL_XPATH).send_keys()
    def login(self):
        EMAIL_XPATH = "//input[@type = 'email']"

        while(True):
            try:
                email_input = self.driver.find_element_by_xpath(EMAIL_XPATH)
                break;
            except NoSuchElementException:
                print('Waiting on Checkout page...' )
        email_input.send_keys(EMAIL)

        PASSWORD_XPATH = "//input[@type = 'password']"
        password_input = self.driver.find_element_by_xpath(PASSWORD_XPATH)
        password_input.send_keys(PASSWORD)

        keep_xpath = "//input[@type = 'checkbox']"

class Sneaker:
    def __init__(self,name,style,price,month,day,time):
        self.name = name
        self.style = style
        self.price = price
        self.month = month
        self.day = day
        self.time = time


class Bot:    
    def __init__(self,link, size = 11,release_day = None):
        self.link = link
        self.size = size 
        self.release_day = release_day

        #self.set_up()
        options = Options()
        #options.headless = True
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH, options = options)
        #self.driver.maximize_window
        self.driver.get(link)
        sleep(1)
        self.login()
        sleep(3)        
        #self.countdown()
        self.select_size()
        sleep(100)
        

    
    def set_up(self):
        release_time = '10:00 AM'
        pause.until(datetime(2020,8,13,9,55))
    
    def countdown(self):
        pause.until(datetime(2020,8,13,9,59,58))
        self.driver.refresh()

    def login(self):
        #self.driver.get('https://www.nike.com/login')
        
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

        email_input.send_keys(EMAIL)
        PASSWORD_XPATH = "//input[@type = 'password']"
        password_input = self.driver.find_element_by_xpath(PASSWORD_XPATH)
        password_input.send_keys(PASSWORD)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@value = 'SIGN IN']").click()
        sleep(1)
        while(True):
            try:
                self.driver.find_element_by_xpath("//input[@value = 'Dismiss this error']").click()
                self.driver.find_element_by_xpath(PASSWORD_XPATH).send_keys(PASSWORD )
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
                x.send_keys('415')
                break
            except NoSuchElementException:
                print('looking')
                sleep(.5)
        self.driver.find_element_by_xpath("//button[@data-qa = 'save-button']").click()

    def get_ship_path(self,path):
        shipping_paths = "//input[@id = '"+ path +"']"    
    
    def fill_shipping_info(self):
        first_name_ = self.driver.find_element_by_xpath(self.get_ship_path('first-name-shipping'))
        last_name_ = self.driver.find_element_by_xpath(self.get_ship_path('first-name-shipping'))
        address_ = self.driver.find_element_by_xpath(self.get_ship_path('shipping-address-1'))
        city_ = self.driver.find_element_by_xpath(self.get_ship_path('city'))
        state_ = self.driver.find_element_by_xpath(self.get_ship_path('state'))
        zip_code_ = self.driver.find_element_by_xpath(self.get_ship_path('zipcode'))
        number_ = self.driver.find_element_by_xpath(self.get_ship_path('phone-number'))

        first_name_.send_keys(FIRST_NAME)
        last_name_.send_keys(LAST_NAME)
        address_.send_keys(STREET)
        city_.send_keys(CITY)
        state_.send_keys(STATE)
        zip_code_.send_keys(ZIP_CODE)
        number_.send_keys(NUMBER)

    def verify(self):
        self.driver.find_element_by_xpath("//input[@class = 'phoneNumber']").send_keys(twilio_num)
        while(not os.path.exists('verify.txt')):
            sleep(.5)
        with open('verify.txt','r') as file:
            verification_code = file.readline() 
                   
        verification_code = verification_code.split(' ')[-1]
        self.driver.find_element_by_xpath("//input[@class = 'code']").send_keys(verification_code)



Bot('https://www.nike.com/launch/t/adapt-bb-2-0-tie-dye',size = )
    
#NikeBot(url,13)
#
# //button[text() = 'Go to Checkout']|
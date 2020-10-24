from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from time import sleep
#from datetime import datetime

import hashlib, os, pause,datetime


CHROME_DRIVER_PATH = 'C:\Webdrive\chromedriver'

class Bot:    
    def __init__(self,product,email,password,cvv):
        self.product = product
        self.email = email
        self.password = password
        self.cvv = cvv

        self.set_up()
        options = Options()
        #options.headless = True
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH, options = options)
        self.driver.get('https://www.nike.com/launch?s=upcoming')
        sleep(1)
        self.login()
        sleep(2)        
        #self.countdown()
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
        pause.until((self.product.launch_time - datetime.timedelta(minutes = 5)))
    
    def countdown(self):
        print('counting down')

        pause.until((self.product.launch_time - datetime.timedelta(seconds = 6)))
        

    def login(self):
        sleep(1)
        
        try:
            self.find_click("//button[@data-qa='top-nav-join-or-login-button']")
        except ElementNotInteractableException:
            self.find_click("//i[@class = 'g72-menu va-sm-t']")
            sleep(1)
            self.find_click("//button[@data-qa='join-login-button']")
        while(True):
            try:
                self.find_send_key("//input[@type = 'email']",self.email)
                break;
            except NoSuchElementException:
                sleep(.2)
        self.find_send_key("//input[@type = 'password']",self.password)

        sleep(1)
        self.find_click("//input[@value = 'SIGN IN']")
        sleep(1)
        #Handle login Error
        while(True):
            try:
                self.find_click("//input[@value = 'Dismiss this error']")
                self.find_send_key("//input[@type = 'password']",self.password)
                self.find_click("//input[@value = 'SIGN IN']")
            except NoSuchElementException:
                break
            except ElementNotInteractableException:
                break
        print('logged in')        
                
    
    def select_size(self):
        size_format = self.product.size        
        if(self.product.is_shoe()):
            size_format = 'M '+ str(self.product.size) +' / W ' + str(float(self.product.size) + 1.5)
        while(True):
            try:
                self.find_click("//button[text() = '" + size_format +"']")
                break
            except NoSuchElementException:
                sleep(.5)
        # Buy Now Brings up payment screen
        self.find_click("//button[@data-qa = 'feed-but-cta']")

    def enter_cvv(self):
        sleep(1)
        iframe = self.find("//iframe[@title='creditCardIframeForm']")
        self.driver.switch_to.frame(iframe)
        while(True):
            try:
                self.find_send_key("//input[@data-shortname='cvv']",cvv)
                break
            except NoSuchElementException: #can'find cvv inputt
                sleep(.5)
        self.driver._switch_to.default_content()
        
        save = self.driver.find_elements_by_xpath("//button[@data-qa = 'save-button']")
        for i in range (len(save)):
            try:
                save[i].click()
            except NoSuchElementException:
                continue
            except ElementNotInteractableException:
                continue

    def buy(self):
        self.find_click("//button[text()='Submit Order']")
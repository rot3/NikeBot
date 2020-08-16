PRICE_CLASS = "//div[@class = 'ncss-brand pb6-sm fs14-sm fs16-md']"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector
from datetime import datetime
from getpass import getpass



def insert_snipe(name,color, price, time, sku):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password= getpass(),
        database = "nikebot"
    )
    my_cursor = mydb.cursor()
    query = "INSERT INTO active_snipes (name, color_way, price,realease_time,SKU)"
    val = (name, color, price, time , sku)
    my_cursor.execute(query,val)
    mydb.commit()
    print(mycursor.rowcount)

def get_snipe_data():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome('C:\Webdrive\chromedriver', options = options)
    driver.get(input('Enter Link: '))
    name = driver.find_element_by_xpath("//div[@class = 'product-info ncss-col-sm-12 full']/h1").text
    color = driver.find_element_by_xpath("//div[@class = 'product-info ncss-col-sm-12 full']/h5").text
    price = driver.find_element_by_xpath("//div[@class = 'product-info ncss-col-sm-12 full']/div").text
    time = driver.find_element_by_xpath("//div[@class = 'test-available-date']/div").text
    sku = driver.find_element_by_xpath("//div[@class = 'description-text text-color-grey']/p").text
    price = str(float(price[1:]))
    sku = sku[sku.index('SKU: ') + 5:]
    print(name)
    print(color)
    print(price)
    print(get_datetime(time))
    print(sku)
    insert_snipe(name,color, price, get_datetime(time), sku)
    

def get_datetime(x):
    y = x.split(' ')
    month,day = y[1].split('/')
    if(len(month) == 1):
        month = '0'+month
    if(len(day) == 1):
        day = '0'+day
    time = y[3]+':00'
    output = '2020-{}-{} {}'.format(month,day,time)
    return output

#print(mydb)
class Snipe:
    def __init__(self,price,day, month = datetime.now().strftime('%d')):
        self.price = price
        self.day = day
        self.month = month

def test():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password= 'bd79Bluesql!',
        database = "nikebot"
    )
    my_cursor = mydb.cursor()
    query = "INSERT INTO active_snipes (name, color_way, price,realease_time,SKU)"
    val = ('test', 'test', 'test', '2020-08-19 10:00:00' , 'testtest12')
    my_cursor.execute(query,val)
    mydb.commit()
    print(mycursor.rowcount)

#get_snipe_data()
test()
#print(get_datetime('AVAILABLE 8/19 AT 10:00 AM'))
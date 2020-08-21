from product import LaunchTime
from product import Product
import csv

valid_sizes =  list(map(str,[i*.5 for i in range(14,31)]))
valid_sizes.extend(['XS','S','M','L','XL','2XL'])
valid_link = 'nike.com'
valid_day = list(map(str,[i for i in range(1,32)]))
valid_month = list(map(str,[i for i in range(1,13)]))
valid_year = list(map(str,[i for i in range(2020,2022)]))

def get_inputs(item,valid_):
    while(True):
        x = input('{}: '.format(item)).upper()
        if(x in valid_):
            break
        print('Invalid')
    return x

def valid_time(x):
    if(len(x) != 5 or x.index(':') != 2):
        return False
    hour,minute = x.split(':')
    try:
        hour = int(hour)
        minute = int(minute)
    except ValueError:
        return False
    if((hour < 0 or hour >24) or (minute < 0 or minute > 59)):
        return False
    return True

def add_snipe():
    name = input('Name: ')
    while(True):
        link = input('Link: ')
        if(valid_link in link):
            break
        print('Invalid')
    size = get_inputs('Size',valid_sizes)
    day = get_inputs('Day',valid_day)
    month = get_inputs('Month', valid_month)
    year =  get_inputs('Year', valid_year)

    while(True):
        time = input('Time (XX:XX): ')
        print(time)
        if(time == '' or time == None):
            time = '10:00'
            break
        if(valid_time(time)):
            break
        print('Invalid 00-24:00-60')

    launch = LaunchTime(day,month,time,year)
    merch = Product(size,launch,link,name)
    with open('snipes.txt','a') as file:
        file.write(merch.__repr__())
        return
    
def add_from_file():
    with open('mydata\\snipes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            salt = row['salt']
            email = row['email']
            password = row['pass']
            cvv = row['cvv']

    launch = LaunchTime(day,month,time,year)
    merch = Product(size,launch,link)
    active_snipes = []
    with open('snipes.txt','r') as file:        
        merch_dets = ''
        for i in range(0,7):
            merch_dets = merch_dets + file.readline().rstrip('\n')
        snipe = eval(merch_dets)
        print(repr(snipe))

        
    with open('snipes.txt','w+') as file:
        file.write(merch.__repr__())

def purge_snipes():
    with open('snipes.txt','w+') as file:
        file.write("")

def load_products():
    products = {}
    with open('snipes.txt','r') as file:
        data = file.readlines()
        for line in data:
            name = line[(line.index('name')+6):-3]
            name = name +' '+ line[(line.index('size')+6):(line.index('size')+10)]
            products[name] = line.strip('\n')
    with open('snipe_data.txt','a') as file:
        file.write(str(products)+'\n')

def get_products():
    with open('snipe_data.txt','r') as file:
        products = eval(file.read())   
    #print(products)
    return products
actions = {
    '1':lambda:add_snipe(),
    '2':lambda:add_from_file(),
    '3':lambda:purge_snipes(),
    '4':lambda:load_products(),
    '5':lambda:get_products()
}
if(__name__ =="__main__"):
    while(True):
        action = input('Select Option Number\n1) Add Smipe\n2) Add From File\n3) Purge Snipes\n4) Load Products\n5) Get Products\n6) Exit\n')
        if(action == '6'):
            break
        x = actions[action]()    

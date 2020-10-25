
from product import Product
import csv
import datetime

valid_sizes =  list(map(str,[i*.5 for i in range(5,31)]))
valid_sizes.extend(['XS','S','M','L','XL','2XL'])
valid_link = 'nike.com'
valid_day = list(map(str,[i for i in range(1,32)]))
valid_month = list(map(str,[i for i in range(1,13)]))
valid_year = list(map(str,[i for i in range(2020,2022)]))
valid_hour = list(map(str,[i for i in range(0,25)]))
valid_minute = list(map(str,[i for i in range(0,61)]))

def get_inputs(item,valid_,default = None):
    while(True):
        x = input('{}: '.format(item)).upper()
        if(x == ''):
            return default
        if(x in valid_):
            break
        print('Invalid')
    return x


def add_snipe():
    name = input('Name: ')
    link = input('Link: ')
    size = get_inputs('Size',valid_sizes,)
    month = get_inputs('Month', valid_month)
    day = get_inputs('Day',valid_day) 
    year =  get_inputs('Year', valid_year,'2020')
    hour = get_inputs('Hour',valid_hour,'10')
    minute = get_inputs('Minute',valid_month,'0')
    launch = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute))
    merch = Product(size,launch,link,name)
    with open('snipe_data\\snipes.txt','a') as file:
        file.write(merch.__repr__())
        return
    
def add_from_file():
    with open('snipe_data\\snipes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            launch = eval("datetime.datetime({},{},{},{},{})".format(row['year'],row['month'],row['day'],row['hour'],row['min']))
            merch = Product(row['size'],launch,row['link'],row['name'])
            with open('snipe_data\\snipes.txt','a') as file:
                file.write(merch.__repr__())
                file.write('\n')
    return            

def purge_snipes():
    with open('snipe_data\\snipes.txt','w+') as file:
        file.write("")
    return

def load_products():
    products = {}
    with open('snipe_data\\snipes.txt','r') as file:
        data = file.readlines()
        for line in data:
            name = line[(line.index('name')+6):-2]
            name = name +' '+ line[(line.index('size')+6):(line.index('size')+10)]
            products[name] = line.strip('\n')
    with open('snipe_data\\snipe_data.txt','w+') as file:
        file.write(str(products)+'\n')

def get_products():
    with open('snipe_data\\snipe_data.txt','r') as file:
        products = eval(file.read())   
    if(__name__ =="__main__"):
        print(products)
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
        action = input('\nSelect Option Number\n1) Add Smipe\n2) Add From File\n3) Purge Snipes\n4) Load Products\n5) Get Products\n6) Exit\n')
        if(action == '6'):
            break
        try:
            x = actions[action]()
        except KeyError:
            continue    

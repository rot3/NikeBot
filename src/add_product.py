from product import LaunchTime
from product import Product
valid_sizes =  [i*.5 for i in range(14,31)]
valid_sizes.extend(['XS','S','M','L','XL','2XL'])
valid_link = 'nike.com'
valid_day = [i for i in range(1,32)]
valid_month = [i for i in range(1,13)]
valid_year = [i for i in range(2020,2022)]

def get_inputs(item,valid_):
    while(True):
        x = input('{}: '.format(item))
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
    while(True):
        link = input('Link: ')
        if(valid_link in link):
            break
        print('Invalid')
    while(True):
        size = input('Size: ').upper()
        if(size in valid_sizes):
            break
        print('Invalid') 
    day = get_inputs('Day',valid_day,)
    month = get_inputs('Month', valid_month)
    year = get_inputs('Year', valid_year)
    while(True):
        time = input('Time (XX:XX): ')
        if(valid_time(time)):
            break
        print('Invalid 00-24:00-60')

    launch = LaunchTime(day,month,time,year)
    merch = Product(link,size,launch)
    with open('snipes','w+') as file:
        file.write(launch.__repr__() + " "+ merch.__repr__())
    
def add_from_file(file_name):
    with open(file_name,'r') as file:
        day = file.readline()
        month = file.readline()
        year = file.readline()
        time = file.readline()
        size = file.readline()
        link= file.readline()

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
    
add_from_file('snipe_data.txt')
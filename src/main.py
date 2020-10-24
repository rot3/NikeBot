from mydata.pass_hash import hash_str
from product import Product
from add_product import get_products
from mydata.accounts import get_acc_dict
from getpass import getpass
from bot import Bot

if __name__ == "__main__":
    accounts = get_acc_dict()   
    products = get_products()
    while(True):
        email = input("Email: ")
        if(accounts.__contains__(email)):
            break
        print('Invalid')
    while(True):
        password = getpass()
        if(hash_str(password,accounts[email][0]) == accounts[email][1]):
            break
        print('Incorrect')
    while(True): 
        cvv = getpass('CVV: ')
        if(hash_str(cvv,accounts[email][0]) == accounts[email][2]):
            break
        print('Incorrect')

    snipe = input('Snipe: ')
    Bot(eval(products[snipe]),email,password,cvv)


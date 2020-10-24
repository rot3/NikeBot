from getpass import getpass
from mydata.pass_hash import get_random_salt, hash_str
import csv
from selenium import webdriver

def add_account():
    email = input("Email: ")
    password,confirm_pass = '','____'
    cvv,confirm_cvv = '','____'
    while(password != confirm_pass):
        if(password != '' and confirm_pass !='____'):
            print('Password do not match')
        password = getpass()
        confirm_pass = getpass("Confirm Passrowd: ")

    while(cvv != confirm_cvv):
        if(cvv != '' and confirm_cvv !='____'):
            print('CVV\'s do not match')
        cvv = getpass("CVV:")
        confirm_cvv = getpass("Confirm CVV: ")
    
    salt = get_random_salt(10)
    with open('mydata\\accounts.csv','a') as file:
        writer = csv.writer(file, delimiter = ',')
        writer.writerow([email,salt,hash_str(password,salt),hash_str(cvv,salt)])
        
def load_accounts():
    accs = {}
    with open('mydata\\accounts.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            accs[row['email']] = [row['salt'],row['pass'],row['cvv']]

    with open('mydata\\accounts.txt','w+') as file:
        file.write(str(accs))

    return accs

def get_acc_dict():
    with open('mydata\\accounts.txt','r') as file:
        acc_dict = eval(file.read())
    return acc_dict


def purge_accs():
    with open('mydata\\accounts.csv','w+') as file:
        file.write('email,salt,pass,cvv')
    load_accounts()
    get_acc_dict()

actions = {
    '1':lambda:add_account(),
    '2':lambda:load_accounts(),
    '3':lambda:get_acc_dict(),
    '4':lambda:purge_accs()
}
if(__name__ =="__main__"):
    while(True):
        action = input('Select Option Number\n1) Add Account\n2) Load Accounts(CSV)\n3) Get Accounts\n4) Purge Accounts\n5) Exit\n')
        if(action == '5'):
            break
        try:
            x = actions[action]()
        except KeyError:
            continue


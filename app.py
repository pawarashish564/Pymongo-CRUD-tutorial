import json
from pymongo import MongoClient
import argparse
from colorama import Fore,init,Style
import pprint
arg = argparse.ArgumentParser()
arg.add_argument('-p','--pass',help='passcode for mongo db atlas',required=True)
arg.add_argument('--count',help='count all the documents in collection ',action='store_true')
arg.add_argument('--add',help='Add new data ',action='store_true')
arg.add_argument('--find',help='get data ',action='store_true')
arg.add_argument('-v',help='verbose',action='store_true')

arg.add_argument('--find-one',help='get specific record',nargs='+')
arg.add_argument('--delete-one',help='delete specific record',nargs='+')
arg.add_argument('--update-one',help='delete specific record',nargs='+')

init(autoreset=True)
args = vars(arg.parse_args())

if args['v']:
    print(args)

client = MongoClient('mongodb+srv://test:'+args['pass']+'@cluster0.dcqm2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.get_database('student_db')
records = db.student_records

# print(records)

if args['count']:
    # count records
    count = records.count_documents({})
    print(Style.BRIGHT+Fore.GREEN + '-- Total Records '+ str(count) + ' -- ')
elif args['add']:
    user_name = input('Enter username >> ')
    password = input('Enter pass >> ')
    age = input('Enter age >> ')
    city = input('Enter city >> ')

    data = {
        'username':user_name,
        'password':password,
        'age':age,
        'city':city
    }

    records.insert_one(data)
    # insert_many for multiple  
    print(Style.BRIGHT + Fore.GREEN +' -- New Record Added -- ')
elif args['find']:
    # print(list(records.find()))
    pprint.pprint(list(records.find()))

elif  args['find_one'] != None:

    print(list(records.find({args['find_one'][0]:args['find_one'][1]})))
    print(Style.BRIGHT + Fore.YELLOW +' -- Record Retrieved -- ')

elif  args['delete_one'] != None:

    records.delete_one({args['delete_one'][0]:args['delete_one'][1]})
    print(Style.BRIGHT + Fore.RED+'-- Record Deleted --')

elif args['update_one'] != None:
    # --update-one age 20 name james city NYC
    updates = args['update_one']
    if len(updates) %2 != 0 :
        print(Style.BRIGHT + Fore.RED + ' -- Invalid format provided -- ')
        
    i = 2
    res = {}
    while i+1 <= len(updates) -1 :
        res[updates[i]] = updates[i+1]
        i += 2

    # print(res)
    records.update_one({args['update_one'][0]:args['update_one'][1]},{'$set':res})
    
    print(Style.BRIGHT + Fore.BLUE + ' -- Record Updated -- ')
    

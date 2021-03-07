# a module is basically a file containing a set of functions to include in your application.
# there are core python modules, modules you can install using the pip package manager (including django) as well as custom modules

#core modules
import datetime 
#to import date from datetime
from datetime import date

#today = datetime.date.today()

today = date.today()

print(today)

import time 
from time import time

timestamp = time()

print(timestamp)

#import custom module
import validate
from validate import validate_email

email = 'test@test.com'

if validate_email(email):
    print('email is valid')
else:
    print('email is bad')
#searches builtin then sys.path (PYTHONPATH)
#import sys, os, datetime, math, random, keyword... are built in #print(keyword.kwlist)
import test_module  as tm
#import test_module  as tm
#from test_module  import * 

tm.fn1()
# access first city
city = tm.cities_list[1]
print("Accessing 1st city:", city)

# Get all cities
cities = tm.cities_list
print("Accessing All cities :", cities)
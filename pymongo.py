# Import the python libraries
from pymongo import MongoClient
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(<<MONGODB URL>>)
#client = MongoClient(port=27017)

# Connect to the test db
db=client.test
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)



# Use the employee collection
employee = db.employee
employee_details = {
    'Name': 'Raj Kumar',
    'Address': 'Sears Streer, NZ',
    'Age': '42'
}

# Use the insert method
result = employee.insert_one(employee_details)

# Query for the inserted document.
Queryresult = employee.find_one({'Age': '42'})
pprint(Queryresult)

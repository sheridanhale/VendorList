# Read the file VendorList.csv into this program and create a dictionary of the customer's
# full name, email address and phone number where the key is the full name of the customer
# and the value is a dictionary where the keys are 'email' and 'phone' and the values
# are the corresponding email address and phone number of the customer. 

# Once the dictionary has been completed print it out. It shoud resemble what is shown
# below (first 2 and last 2 elements shown only):

#{'Tommie Goody': {'email': 'tgoody0@weather.com', 'phone': '809-992-7298'}, 
# 'Obadiah Godfery': {'email': 'ogodfery1@a8.net', 'phone': '560-745-9361'}......
# ..........'Kessiah Tynemouth': {'email': 'ktynemouthdu@ning.com', 'phone': '690-215-8097'}, 
# 'Carmela Kaubisch': {'email': 'ckaubischdv@wikia.com', 'phone': '307-726-6526'}}


# Using the dictionary, write the contents to a csv file. The output file shoud be exactly as
# what is shown in the file - marketinglist.csv.
# Name your file - marketinglistFINAL.csv


# Note: you can use the comments below to guide you through the logic of the code. You are not
# required to follow it. ALSO NOT ALL STEPS HAVE BEEN COMMENTED. You may have additional steps.


import csv

# open the vendorlist file; 
# file_object = open(filename, mode)
#import csv

infile = open('VendorList.csv','r')
outfile = open('marketinglistFINAL.csv' , 'w')

csvfile = csv.reader(infile, delimiter=',')
# create a csv object from the file object
next(csvfile)

outfile.write('Name, Email, Phone\n')
for record in csvfile:
    full_name = record[1] + " " + record[2]
    email_address = record[4]
    phone_number = record[5]

# create an output file
    outfile.write(full_name + ',' + email_address + ',' + phone_number + '\n')

outfile.close()



# create an empty dictionary
Customers = {}


# iterate through the csv object
for key in Customers:
    print(full_name)
    print(customers[full_name])

for value in customers.values():
    print(email_address)
    print(phone_number)


    # add the key-value pair to the dictionary #name and email



# print the dictionary after the loop is finished
#def main():

    #import csv

    #infile = open("EmployeePay.csv",'r')

    #csvfile = csv.reader(infile, delimiter=',')

    #next(csvfile)

    #for record in csvfile:
        #print("ID: ", record[0])
        #print("First name: ", record[1])
       # print("Last Name: ", record[2])
        #salary = (float(record[3])) * float(record[4]) + float(record[3])
        #print('Total Pay: ', '$' ,format(salary, ',.2f'),sep = '')
        #input('Press enter for next employee')
    
#main()

for email in Customers['email']:
    print(email)
    




# iternate through the dictionary and write to the output file



# close your output file

for x in Customers['info']:
  outfile.write(str(x['name'])+','+x['email']+','+str(x['phone'])+'\n')

outfile.close()
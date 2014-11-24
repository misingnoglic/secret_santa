__author__ = 'arya'
import sendgrid
from secrets import sendgrid_pass,sendgrid_user
from random import shuffle


sg = sendgrid.SendGridClient(sendgrid_user,sendgrid_pass)
people = {}
test_file = open('people.txt').read()
test_file = test_file.split("\n")
for item in test_file:
    item = item.split("\t")
    people[item[0]]=item[1]
print(people)


#people = {"Arya":'aboudaie@brandeis.edu',"Sofiya":"seaurchi@brandeis.edu"}
names1 = people.keys()[:]
names2 = names1[:]
shuffle(names2)
for i in range(len(names1)):
    if names1[i]==names2[i]:
        names2[(i+1)%len(names1)], names2[(i)] = names2[(i)],names2[(i+1)%len(names1)]

for i in range(len(names1)):
    message = sendgrid.Mail()
    message.add_to(names1[i]+" <"+people[names1[i]]+">")
    message.set_subject('Secret Santa Assignment!')
    message.set_html('Hello! Your secret santa is '+names2[i])
    message.set_text('Hello! Your secret santa is '+names2[i])
    message.set_from('Arya Boudaie <aboudaie@brandeis.edu>')
    status, msg = sg.send(message)

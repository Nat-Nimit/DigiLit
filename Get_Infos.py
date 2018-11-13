import re #import module
data_file = open("staff.txt", 'r+', encoding='utf-8') 
title = data_file.read()
regx = re.compile('title=\"([^\"]+)\"')
for match in regx.finditer(title):
	print(match.group(1))
	
import re #import module\n",
staff_file = open('ling_prof.txt', 'r+', encoding='utf-8') # open file and store data in variable data_file
info = staff_file.read() # read data in data_file\n",
regx_2 = re.compile('<a\shref=\".+\"\S+>([^\"]+\))(</a>|</strong>)<br')
regx_3 = re.compile('\S+@[a-zA-Z]+\.(com|\S+\.th)')
list_contact = []
profess_contact = []
for match2 in regx_2.finditer(info):
	profess_contact.append(match2.group(1))
for match3 in regx_3.finditer(info):
	list_contact.append(match3.group())
print("Name List=",profess_contact,"\nEmail:",set(list_contact))

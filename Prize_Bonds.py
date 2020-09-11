import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import re


url="http://savings.gov.pk/wp-content/uploads/15-07-2020-Rs-750-1.txt"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify()) # print the parsed data of html

text_only=soup.p.text
#print(text_only)

def getNumbers(str): 
    array = re.findall(r'[0-9]+', str) 
    return array 
  
# Driver code 
numbers_only = getNumbers(text_only) 
#print(numbers_only) 

#--------------    
new_list=[]
for index in range (0, len(numbers_only)):
	if (len(numbers_only[index])==6):
	    new_list.append(numbers_only[index])  

#convert to int
for i in range(0, len(new_list)): 
    new_list[i] = int(new_list[i]) 
#finally int list with codes only
#print(new_list) 


#----------------------------------------------------
#list of my bonds
my_bonds=[739880, 963683,456789, 542902, 793199]
random=[768575,84488,2874842,8328]

#-----------------------------------

# creating an empty list 
lst = [] 
  
# number of elemetns as input 
print("Enter total number of your prize bonds : ")
n = int(input())
  
# iterating till the range 
for i in range(0, n): 
    codes = int(input()) 
  
    lst.append(codes) # adding the element 
      
print("YOUR CODES LIST:",lst)
my_list=lst
#--------------------------------------------------
matched_result=set(my_list).intersection(new_list)
if (matched_result==set()):
    print("NO MATCHES FOUND :\"(")
else:
	print("MATCHES FOUND :)")
	print(matched_result)
sleep(10)
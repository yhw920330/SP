execfile('20131549.conf')  # YOUR STUDENT NUMBER HERE
from boto.s3.connection import S3Connection
from boto.dynamodb2.table import Table
from boto.dynamodb2.exceptions import ItemNotFound

myTable = Table('sp6_0619')  # TABLE NAME HERE

while True:
	searchitem=raw_input("Input :") #get the Object from user
	searchitem.strip()  #remover the enter
	if(len(searchitem) ==0): #terminate the program when there is no input
		break;
	try:
		find =myTable.get_item(words=searchitem) #find the search object in Table
	except ItemNotFound:
		print 0 #there is no data in DynamoDB  
		continue;
	print find['count'] #print the result 
		

execfile('20131549.conf')  # YOUR STUDENT NUMBER HERE
from boto.s3.connection import S3Connection
myBucket = S3Connection().get_bucket('sgcs15spproj6tokyo')

from boto.dynamodb2.table import Table

myTable = Table('sp6_0619')  # TABLE NAME HERE

# get item
for anyObject in myBucket.list():
	if 'output' in anyObject.key  and 'part-' in anyObject.key: #get the input file  
		content=anyObject.get_contents_as_string()
		for each_line in content.split('\n'):
			splitted = each_line.split('\t')
			if len(splitted) ==2: #if it is right input , length must be 2
				words, counts = each_line.split('\t') #split the item 
				myTable.put_item(data={'words': words, 'count':counts}) #store the item into DynamoDB 



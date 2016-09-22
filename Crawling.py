import requests
from bs4 import BeautifulSoup
#list to store the visited URL
visited=[]

def get(url,visited):
#make url as the direct path
	if(url.startswith("http://")):#direct path
			url=url
	elif(url == ""):#skip the NULL
			return ;
	elif(url.startswith("#")): #skip the # because this links to the same URL
			return
	elif(url.startswith("?")):# skip ?
			return
	else: #indirect path
			url="http://cspro.sogang.ac.kr/~gr120150253/"+url

#if this URL is alredy visited exit
	if url in visited:
			return
	else:
		try:
			r=requests.get(url);
			
		except requests.exceptions.ConnectionError:
				print "ConnectionError in URL: "+str(url)+"\n"
				return
		if(r.ok):
			b=BeautifulSoup(r.content)

#store textfile and add to visited 
			visited.append(url)
			new_txt="Output_{:04}.txt".format(len(visited))
			f=open(new_txt,'w')
			f.write(b.text)
			f.close()
			for i in b.find_all('a'):
				get(str(i['href']),visited)


#start the crawler with root page				
get("http://cspro.sogang.ac.kr/~gr120150253/index.html",visited)

#make URL file
f=open("URL.txt","w")
if len(visited) >0:
	f.write(visited[0])
	for i in visited[1:]:
		f.write("\n"+i)
f.close()



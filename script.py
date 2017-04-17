# -*- coding: utf-8 -*-
    
import urllib.request
import re
import MySQLdb


bdd= MySQLdb.connect("127.0.0.1","root","","browser_online")
fir= bdd.cursor()

fir.execute("SELECT link_indefine_link FROM  link_undefine ORDER BY link_indefine_id ASC LIMIT 1")

#for url in fir.fetchone():
   # url=url

#fir.execute("delete  from link_undefine  where link_indefine_link= '"+url+"'")

url="http://www.belcaire.fr/"
reg1 = "(http[s]?:\/\/[a-zA-Z0-9.]*)(\/[a-zA-Z0-9?\/_\-.=&]*)"
reg11=reg1.encode(encoding='UTF-8')
reg2= "href=\"(\/[a-zA-Z0-9._\/?&=-]*)"
reg22=reg2.encode(encoding='UTF-8')

reg3="(http[s]?://[a-zA-Z0-9._]*)"

off_htmlcode=urllib.request.urlopen(url)
off_htmlcode=off_htmlcode.read()

rec_htmllink=re.compile(reg11)
rec_htmllink=re.findall(rec_htmllink, off_htmlcode)

out_htmllink=re.compile(reg22)
out_htmllink=re.findall(out_htmllink, off_htmlcode)

bas_url= re.compile(reg3)
bas_url= re.search(bas_url,url).group()

#graph={}

for link in rec_htmllink:
    #graph.append(link[0] + link[1])
    print(link[0]+link[1])

    fir.execute("INSERT into link_undefine(link_indefine_link) values('" + (link[0]+link[1]).decode('utf-8') +"')")
    bdd.commit()
for link in out_htmllink:
   print (url + link.decode('utf-8'))
   #graph[url] = (url + link.decode('utf-8'))
   fir.execute("INSERT into link_undefine(link_indefine_link) values('" + url + link.decode('utf-8') + "')")
   bdd.commit()
#print(graph[url])

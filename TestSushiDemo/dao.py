import psycopg2

from TestSushiDemo.menu import MENU

def getMenu():

  conn = psycopg2.connect(database="TestPostgreDjango", user="postgres", password="liuchen198327", host="127.0.0.1", port="5432")
  print "Opened database successfully"

  cur = conn.cursor()
  directions={}
  list=[];
  
 
  cur.execute("select id,name,price,description,path from Menu where id =1")
  rows = cur.fetchall()
  for row in rows:

   """list.append(row[0])
      list.append(row[1].strip())
      list.append(row[2])
      list.append(row[3])"""
  
  menu=MENU(row[0],row[1].strip(),row[2],row[3],row[4]);
    
  #directions = {'id': row[0], 'name': row[1].strip(),'price':row[2],'description':row[3]}
  
  list.append(menu);
      
  """ print "ID = ", row[0]
   print "NAME = ", row[1]
   print "Price = ", row[2]
   print "Description = ", row[3], "\n"""

  print "Operation done successfully";
  conn.close()
  
  return list
  #return directions
  
  
  
  
  
  
  
  
def getProducts(id):

  conn = psycopg2.connect(database="TestPostgreDjango", user="postgres", password="liuchen198327", host="127.0.0.1", port="5432")
  print "Opened database successfully"

  cur = conn.cursor()
  list=[];
  
 
  cur.execute("select id,name,price,description,path from Menu where id =%s",id)
  rows = cur.fetchall()
  for row in rows:

   """list.append(row[0])
      list.append(row[1].strip())
      list.append(row[2])
      list.append(row[3])"""
  
  menu=MENU(row[0],row[1].strip(),row[2],row[3],row[4]);
  
  list.append(menu);
  
  """ print "ID = ", row[0]
   print "NAME = ", row[1]
   print "Price = ", row[2]
   print "Description = ", row[3], "\n"""

  print "Operation done successfully";
  conn.close()
  
  return list
  #return directions
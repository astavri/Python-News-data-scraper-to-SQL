# Python-News-data-scraper-to-SQL
In progress

The script has everything exmapled out.

The goal is to export large amounts of title data into mySQL where it can be further analyzed.
pygooglenews has a lot more than just title. I believe it feeds off the google rss

What you need to do:

1. create mySQL Database and Table.


    CREATE DATABASE database123 
    CREATE TABLE table123(
            title VARCHAR (255),
            published VARCHAR (255),
            search_keyword VARCHAR (255));


So it matches in the python script listed below:
    
 add_article =   ("INSERT IGNORE INTO table123" 
                    "(title, published, search_keyword)" 
                    "VALUES (%s, %s, %s)")               
  
2. mySQL login criteria from python
 replace the localhost, which if you are using local mySQL on your computer, it is likely localhost
 replace all the XXXXX with your information. this is where you enter credentials and choose a database, in this case, database123
    
mydb = mysql.connector.connect(                    
    host="localhost",    
    user="XXXXXXXXX",  
    password="XXXXXXXXX", 
    database="database123"   #Database Name in SQL   
    
3. Change the entries in YEAR, DD, MM

start_date = datetime(2021, 1, 23)  
min_date = start_date      
max_date = datetime(2021, 2, 23)

4. enter keywords

  a. you can run this with two different search keywords
  b. or you can keep adding more search criteria with quotes and commas seperating them.
  
searchlist = ["stocks", "bonds"]
    
5. Run Script


6. Im working on making an executable .exe that takes the input in a prompt, which seems to be successful so far, 
and then a GUI based one where it can save mySQL data where you dont have to retype user, pw, etc.

please let me know if you have other ideas i can strive for regarding the python portion of it.
Better yet, ill be happy to meet and work on something with you on yours, vice versa

    

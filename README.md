# Python-News-data-scraper-to-SQL
WIP

The goal is to export large amounts of data into mySQL where it can be further analyzed.
I figure webscraping is common and makes tons of data quickly.
The webscraping backend is from pygooglenews, thanks kotartemiy!
https://github.com/kotartemiy/pygooglenews

**INSTALLATION**
pip install "setuptools<58"

pip install -U --no-deps "dateparser>=1.0.0"

pip install -U --no-deps "feedparser>=6.0.8"

pip install pygooglenews==0.1.2

pip install mysql-connector-python

pip install pysimplegui

Install and setup mySQL

Create a database and create a table using the parameters listed below




![alt text](https://raw.githubusercontent.com/astavri/Python-News-data-scraper-to-SQL/main/Python_to_%20SQL.png)



**1-create mySQL Database and Table.**

    CREATE DATABASE database123;
    CREATE TABLE table123(
        title VARCHAR (255),
        published VARCHAR (255),
        keyword VARCHAR (255)
        link VARCHAR (255)
        );



**2-Match it to the mysql.connector script below:**

     add_article2 = " (title, published, keyword, link) VALUES (%s, %s, %s, %s)"
     
also check that you have the right # of entries and origin. In this case 4 entries. 

     data_article = (item['title'], item["published"], searchlist[i], item['link'])
     
     
  


**3-Type in your entries manually each time in the GUI. Or enter your values in the string below
    so the GUI entries are already populated for most things every time you run it**
    
    guivalues = ['', '2022-01-25', '2022-01-30', "localhost", "root", 'PASSWORD', 'database123', 'table123'];

    
    
    
**4- Run Script**

    You may search multiple keywords automatically by putting a comma after each entry
    Example:
    New York, California, Iowa, Florida

**5- Check mySQL. Use the data as you wish.**

    SELECT * FROM table123;






Im working on making an executable .exe that takes the input in a prompt, which seems to be successful so far, 
and then a GUI based one where it can save mySQL data where you dont have to retype user, pw, etc.

Please let me know if you have other ideas i can strive for regarding the python portion of it.


    

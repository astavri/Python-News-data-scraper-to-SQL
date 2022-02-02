# Python-News-data-scraper-to-SQL
WIP

The goal is to export large amounts of data into mySQL where it can be further analyzed.
I figure webscraping is common and makes tons of data quickly.
All the webscraping backend portion is from pygooglenews, thanks kotartemiy!
https://github.com/kotartemiy/pygooglenews

![](Python newscraper to SQL.png)
![alt text](https://raw.githubusercontent.com/astavri/Python-News-data-scraper-to-SQL/main/Python%20newscraper%20to%20SQL.png)





**1-create mySQL Database and Table.**

    CREATE DATABASE database123 
    CREATE TABLE table123(
        title VARCHAR (255),
        published VARCHAR (255),
        search_keyword VARCHAR (255));



**2-Match it to the mysql.connector script below:**

    add_article =   ("INSERT IGNORE INTO table123
        "(title, published, search_keyword)" 
        "VALUES (%s, %s, %s)")               
  


**3-Type in your entries manually each time in the GUI or enter your values in the string 
    so the GUI recognizes it everytime you run the script**
    
    guivalues = ['', '2022-01-25', '2022-01-30', "localhost", "root", 'PASSWORD', 'database123', 'table123'];

    
    
    
**4- Run Script**

    You may search multiple keywords automatically by putting a comma after each entry
    Example:
    New York, California, Iowa, Florida

**5- Check mySQL. Use the data as you wish.**

    SELECT * FROM table123






Im working on making an executable .exe that takes the input in a prompt, which seems to be successful so far, 
and then a GUI based one where it can save mySQL data where you dont have to retype user, pw, etc.

Please let me know if you have other ideas i can strive for regarding the python portion of it.


    

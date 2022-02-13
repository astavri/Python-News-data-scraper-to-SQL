import PySimpleGUI as pyGUI
import mysql.connector
from datetime import datetime, timedelta
from pygooglenews import GoogleNews
import warnings
warnings.filterwarnings(
    "ignore",
    message="The localize method is no longer necessary, as this time zone supports the fold attribute",)
gn = GoogleNews()
mySQL_flag = False


guivalues = [  #default gui entries
    '',
    '2022-01-28',
    '2022-01-30',
    "localhost",
    "root",
    'password',
    'pooptest1',
    'stocks'
]
pyGUI.theme('Dark2')
gui_layout = [
    [pyGUI.Text('Enter multiple Keywords, comma to separate')],
    [pyGUI.Text('Keywords', size=(20, 1)), pyGUI.InputText()],
    [pyGUI.Text('Start Date YYYY-MM-DD: ', size=(20, 1)), pyGUI.InputText(guivalues[1])],
    [pyGUI.Text('End Date YYYY-MM-DD: ', size=(20, 1)), pyGUI.InputText(guivalues[2])],
    [pyGUI.Text('Host (usually localhost): ', size=(20, 1)), pyGUI.InputText(guivalues[3])],
    [pyGUI.Text('User (usually root): ', size=(20, 1)), pyGUI.InputText(guivalues[4])],
    [pyGUI.Text('mySQL password: ', size=(20, 1)), pyGUI.InputText(guivalues[5])],
    [pyGUI.Text('Database: ', size=(20, 1)), pyGUI.InputText(guivalues[6])],
    [pyGUI.Text('Table: ', size=(20, 1)), pyGUI.InputText(guivalues[7])],
    [pyGUI.Checkbox('mySQL Enabled', key='mySQL.enabled', enable_events=True)],
    [pyGUI.Output(size=(70, 15))],
    [pyGUI.Button('Extract', bind_return_key=True), pyGUI.Button('Close')]
]
window = pyGUI.Window('Python to SQL', gui_layout)

def mysql_login():
    global mydb
    mydb = mysql.connector.connect(
        host=guivalues[3],
        user=guivalues[4],
        password=guivalues[5],
        database=guivalues[6])
def mysql_insert():
    global add_article
    global add_article1
    global add_article2
    add_article = "INSERT IGNORE INTO "
    add_article1 = guivalues[7]
    add_article2 = " (title, published, keyword, link) VALUES (%s, %s, %s, %s)"
    
def  mysql_flag_insert():
    cursor.execute(add_article + add_article1 + add_article2, data_article)
    mydb.commit()

def news_extract():
    key1 = guivalues[0]
    searchlist = key1.split(",")
    s_date = str(guivalues[1])
    start_date = datetime.strptime(s_date, "%Y-%m-%d")
    min_date = start_date
    e_date = str(guivalues[2])
    max_date = datetime.strptime(e_date, "%Y-%m-%d")
    sizeofList = len(searchlist)
    print("Number of keywords used: ", len(searchlist))
    i = 0
    while i < sizeofList:
        while min_date != max_date:
            min1_date = min_date + timedelta(days=1)
            print("Keyword: ", searchlist[i])
            print("From:" + min_date.strftime('%Y-%m-%d'))
            print("To:" + min1_date.strftime('%Y-%m-%d'))
            search = gn.search(searchlist[i], from_=min_date.strftime('%Y-%m-%d'), to_=min1_date.strftime('%Y-%m-%d'))
            for item in search['entries']:
                print(item['title'])
                global data_article
                data_article = (item['title'], item["published"], searchlist[i], item['link'])
                if mySQL_flag:
                    mysql_flag_insert()
            min_date = min_date + timedelta(days=1)
            print("Search Keyword: ", searchlist[i])
        else:
            min_date = start_date
        i += 1
    else:
        print("Print() Complete!")


while True:
    event, guivalues = window.read()
    if event in (None, 'Quit'):
        break
    if event == 'Close':
        break
    if event == 'mySQL.enabled':
        print("Extracting to mySQL Enabled")
        mySQL_flag = True
    if event == 'Extract':
        if mySQL_flag:
            mysql_login()
            cursor = mydb.cursor()
            mysql_insert()
            news_extract()
            mydb.close()
            print("Extract to mySQL Complete!")
        else:
            news_extract()

from csv import DictReader
import json
import mysql.connector

#get externally stored log in information
def pw(file):
    with open(file) as pwfile:
        logIn = json.load(pwfile)
        return logIn

#return list from a csv
def compare_list(filename, id_column, title):
    with open(filename,'r', encoding='utf8') as read_file:
        csv_dict= DictReader(read_file)
        id_list=[]
        for row in csv_dict:

            id_list.append({'id':row[id_column],'title':row[title]})
        return id_list

#establish database connection
def dataConnect(host,user, password,database):
    connection = mysql.connector.connect(
        host = host,
        user =  user,
        password = password,
        database = database)
    return connection


if __name__ == '__main__':

    logIn = pw("log ons.txt")
    al_db = dataConnect("server","user",logIn["pw"],"etd_available")
    cursor = al_db.cursor()
    cursor.execute(" SELECT * from etd_main")
    result = cursor.fetchall()

    digcom = compare_list("digitalcommons.csv", "identifier", "front_end_url")
    id_list = []
    for row in digcom:
        id_list.append(row["id"])

    for row in result:
        if row[0] not in id_list:
            print (row[0])
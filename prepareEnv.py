import sqlite3
import requests

def prepareEnviroment():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('CREATE TABLE Countries (Country, Population, Area)')
        countries = [('Ukraine', '41588354', '603628'),
                    ('France', '67399000', '640679'),
                    ('USA', '328239523', '9833520'),
                    ('China', '1400050000', '9596961')]
        cursor.executemany('INSERT INTO Countries VALUES (?,?,?)', countries)
        conn.commit()
    except:
        print('Database already exists')

    conn.close()

    url = 'http://apimeme.com/meme?meme=Alarm-Clock&top=Top+text&bottom=Bottom+text'

    p = requests.get(url)
    out = open("example.jpg", "wb")
    out.write(p.content)
    out.close()

__author__ = 'Vietworm'

import sqlite3


def insert():
    try:
        conn = sqlite3.connect('test.db')

        db = conn.cursor()
        db.execute('DROP TABLE IF EXISTS INFO')
        db.execute('CREATE TABLE INFO(name varchar(50), age char(3), description text)')
        db.execute('INSERT INTO INFO VALUES("Vietworm","34","Security researcher")')
        team = [
            ('Nguyen Tan Dung', '21', 'Web Pentest'),
            ('Truong Tan Sang', '25', 'Malware Analytics'),
            ('Nguyen Sinh Hung', '24', 'Script kiddie'),
            ('Nguyen Phu Trong', '15', 'Web Exploitation'),
            ('Phung Quang Thanh', '15', 'Member HackingTeam')
        ]

        db.executemany('INSERT INTO INFO VALUES(?,?,?)', team)

        conn.commit()
        conn.close()
        return True
    except:
        return False


def select():
    conn = sqlite3.connect('test.db')
    db = conn.cursor()
    for row in db.execute('SELECT * FROM INFO'):
        print row

    db.execute('SELECT * FROM INFO WHERE NAME =:x', {
        "x": 'Vietworm'
    })

    row = db.fetchone()
    print '-'*50
    print row
    conn.close()


if __name__ == "__main__":
    print ('[*] Free database memory')
    print('[*] Database insert successfully!' if insert() else 'Insert error')
    select()

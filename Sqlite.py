import sqlite3
import pandas as pd


class sqlite_engine(object):
    def __init__(self):
        self.conn = sqlite3.connect('Database.db')
        self.cursorObj = self.conn.cursor()
        print("connect successful")

        if self.conn is None:
            self.connect = False
        else:
            self.connect = True

    def getTxt(self, input_id, input_password):
        self.id = input_id
        self.password = input_password

    def insert(self):
        if self.connect:
            self.cursorObj.execute("INSERT INTO Member (ID,PASSWORD) \
            VALUES ('Mark', '')")

            self.conn.commit()
            print("data insert successful")
            self.conn.close()

    def query(self):
        if self.connect:
            tempStr = "select * from Member where id=\'" + \
                self.id + "\' and password=\'" + self.password + "\'"
            cursor = self.cursorObj.execute(tempStr)
            tmpData = cursor.fetchone()
            if tmpData is None:
                self.conn.close()
                return False
            else:
                self.conn.close()
                return True

    def update(self):
        if self.connect:
            self.cursorObj.execute(
                "UPDATE COMPANY set SALARY = 25000.00 where ID=1")
            self.conn.commit()

            print("Total number of rows updated :"), self.conn.total_changes

            cursor = self.cursorObj.execute(
                "SELECT id, name, address, salary  from COMPANY")
            for row in cursor:
                print("ID = ", row[0])
                print("PASSWORD = ", row[1], "\n")

            print("query successful")
            self.conn.close()

    def delete(self):
        if self.connect:
            self.cursorObj.execute("DELETE from COMPANY where ID=2;")
            self.conn.commit()

            print("Total number of rows deleted :"), self.conn.total_changes

            cursor = self.cursorObj.execute(
                "SELECT id, name, address, salary  from COMPANY")
            for row in cursor:
                print("ID = ", row[0])
                print("PASSWORD = ", row[1], "\n")

            print("query successful")
            self.conn.close()

    def test(self):
        tmp = "select * from Member where id='admin' and password='admin'"
        cursor = self.cursorObj.execute(tmp)
        for row in cursor:
            print("ID = ", row[0])
            print("PASSWORD = ", row[1], "\n")

            print("query successful")
            self.conn.close()

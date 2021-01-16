import sqlite3
from sqlite3 import Error
import pandas as pd


class RelationalDB:
    def __init__(self):
        self.database = r"src/database/pythonsqlite.db"

    def create_connection(self, db_file):
        """create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

    def createTable(self, conn, create_table_sql):
        """create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def insertData(self, conn, tableName, payload):
        try:
            sql = """ INSERT INTO {}(id,zipcode,name,email,phone)
                    VALUES(?,?,?,?,?) """.format(
                tableName
            )
            cur = conn.cursor()
            cur.execute(sql, payload)
            conn.commit()
        except Error as e:
            print(e)
        else:
            return cur.lastrowid

    def createTeamplate(self):
        try:
            sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            zipcode text,
                                            name text NOT NULL,
                                            email text,
                                            phone text
                                        ); """
            # create a database connection
            conn = self.create_connection(self.database)

            # create tables
            if conn is not None:
                # create projects table
                self.createTable(conn, sql_create_projects_table)
            else:
                print("Error! cannot create the database connection.")

            keys = pd.read_csv("dummy/sample.csv")
            for key in range(len(keys)):
                payload = (
                    key,
                    str(keys["zipcode"].iloc[key]),
                    keys["name"].iloc[key],
                    keys["email"].iloc[key],
                    keys["contact"].iloc[key],
                )
                self.insertData(conn, "projects", payload)
        except Error as e:
            print(e)

    def getData(self, zipcode, productName):
        result = None
        conn = None
        try:
            conn = self.create_connection(self.database)
            if conn is not None:
                cur = conn.cursor()
                query = """SELECT * FROM projects WHERE zipcode = "{}";""".format(
                    zipcode
                )
                cur.execute(query)
                result = cur.fetchall()
                return result
            else:
                print("Error! cannot create the database connection.")
        except Error as e:
            print(e)
        else:
            return result

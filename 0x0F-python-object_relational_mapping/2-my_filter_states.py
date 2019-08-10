#!/usr/bin/python3
""" takes in an argument and displays all values in the states """
import sys
import MySQLdb

if __name__ == "__main__":
    if(len(sys.argv) == 5):
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM states WHERE NAME='{}'\
        ORDER BY id ASC".format(sys.argv[4]))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()

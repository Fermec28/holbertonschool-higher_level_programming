#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    if(len(sys.argv) == 5):
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE NAME='{}'\
        ORDER BY id ASC".format(sys.argv[4].split(";")[0].split('\'')[0]))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()

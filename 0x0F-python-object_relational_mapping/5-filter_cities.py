#!/usr/bin/python3
""" the name of a state as an argument and lists all cities of that state """
import sys
import MySQLdb

if __name__ == "__main__":
    if(len(sys.argv) == 5):
        conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT cities.name FROM states INNER JOIN cities ON \
        cities.state_id  = states.id WHERE states.name = '{}' \
        ORDER BY \
        cities.id ASC".format(sys.argv[4].split(";")[0].split('\'')[0]))
        query_rows = cur.fetchall()
        result =""
        for row in query_rows:
            result = "{}{}, ".format(result,row[0])
        print(result[:-2])
        cur.close()
        conn.close()

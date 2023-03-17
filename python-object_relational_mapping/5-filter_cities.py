#!/usr/bin/python3
'''module'''
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <MySQL username> <MySQL password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id=states.id WHERE states.name=%s ORDER BY cities.id ASC", (state_name,))
        rows = cursor.fetchall()
        if not rows:
            print("No cities found in state {}".format(state_name))
        else:
            for row in rows:
                print(row)
        cursor.close()
        conn.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
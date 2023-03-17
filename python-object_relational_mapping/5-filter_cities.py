#!/usr/bin/python3
'''module'''
if __name__ == "__main__":
    from sys import argv
    import MySQLdb as DB

    db_connect = DB.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cmd = argv[4]

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT cities.name FROM cities \
                       INNER JOIN states ON states.id = cities.state_id \
            WHERE states.name = %(name)s ORDER BY cities.id", {'name': cmd})
    cities = db_cursor.fetchall()

    first = 0
    for city, in cities:
        if first != 0:
            print(", ", end="")
        print(city, end="")
        first += 1
    print()
    db_cursor.close()
    db_connect.close()
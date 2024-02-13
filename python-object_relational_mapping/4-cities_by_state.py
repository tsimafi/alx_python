#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieving MySQL credentials and database name from command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    # Connecting to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=mysql_db)

    # Creating a cursor object using cursor() method
    cursor = db.cursor()

    # SQL query to retrieve cities with their corresponding states
    sql_query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    try:
        # Executing the SQL command
        cursor.execute(sql_query)
        
        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()
        
        # Displaying the results
        for row in results:
            print(row)

    except Exception as e:
        print("Error: unable to fetch data")
        print(e)

    # Closing the database connection
    db.close()

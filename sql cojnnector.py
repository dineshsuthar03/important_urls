import pymysql

# Connect to the MySQL database
connection = pymysql.connect(host='127.0.0.1', user='root', password='11kajal', db='kajaldb')

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query
cursor.execute("SELECT * FROM vulmon_information")

# Fetch data from the cursor object
data = cursor.fetchall()

# Print the data
for row in data:
    print(row)

# Close the cursor object and the database connection
cursor.close()
connection.close()

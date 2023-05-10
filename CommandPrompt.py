import subprocess
import re
import mysql.connector

comm_name=(str(input("enter your command")))


# Run a command and capture its output
output = subprocess.check_output(comm_name, shell=True)   # it gives the outptut in the form of byte code
# Convert bytes to string
output_str = output.decode("utf-8")  # for converting the byte code into the String we use decode
print(output_str)

# Define a pattern to search for
pattern = r"\d\d\d\.\d\d\d\.\d\.\d"

# Search for the pattern in the output
matches = re.findall(pattern, output_str)
ip = matches[1]

print(" ip  >>>", ip)
# ip=matches
# print(ip[1])

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="commandpromptdb"
)

mycursor = mydb.cursor()

sql = f"INSERT INTO comm (Command_Name, Command_Result ,IP_Col )  VALUES (%s, %s,%s)"
val = (comm_name, output_str, ip)
mycursor.execute(sql,val)
mydb.commit()
print(" ip inserted successfully into the database")







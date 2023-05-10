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

with open('readme.txt', 'w') as f:
    f.write(output_str)

print(" ip  >>>",matches)
# ip=matches
# print(ip[1])

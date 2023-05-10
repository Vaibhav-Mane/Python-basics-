import re
import subprocess
import mysql.connector


class Project:
    # declaring global variable as ip.
    ip = ""

    # getter and setter method for initializing the global variable.
    def getIp(self):
        return self.ip

    def setIp(self, ip):
        self.ip = ip

    # Pattern matching logic method
    def getIpAddress(self, abc):
        # pattern class use from re package for given pattern matching eg.(ip address:192.168.1.111)
        pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        # use findall method of re module for pattern matching.
        matches = re.findall(pattern, abc)
        for match in matches:
            # if pattern is matched then store the matched value into the ip variable.
            self.ip = match
            print("ip found ...>> ", self.ip) # print the ip string value.

    def main(self):
        try:
            # take the input from user
            command = input("enter your command\n")
            # create a process and execute the command
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # waiting for given command execution
            p.wait()
            # read the line from console.
            output, error = p.communicate()
            abc = output.decode('utf-8') # store the data which is came from line into the abc variable

            # calling the getIpAddress method
            pj = Project() # creating a class object
            pj.getIpAddress(abc) # pass the abc as parameter to the getIpAddress method

            # JDBC Connection
            cnx = mysql.connector.connect(user='root', password='root',
                                          host='127.0.0.1', database='commandpromptdb')
            cursor = cnx.cursor()

            # insert the ip address into the database in IP_Col (column) by using prepared statement.
            add_command = ("INSERT INTO comm "
                           "(Command_Name, Command_Result, IP_Col) "
                           "VALUES (%s, %s, %s)")
            data_command = (command, abc, self.ip)
            cursor.execute(add_command, data_command)

            # Make sure data is committed to the database
            cnx.commit()

            print("saved successfully...") # print the success message.
            cursor.close()
            cnx.close()

        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))

        except Exception as e:
            print(e)


if __name__ == '__main__':
    p = Project()
    p.main()

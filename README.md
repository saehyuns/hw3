# Homework 3: Parallel SQL Processing Supporting Joins
* [Homework 3 Page](https://lipyeow.github.io/ics421s18/morea/queryproc/experience-hw3.html)
* [Installation](#installation)
  * [Install Docker Containers](#install-docker-containers)
  * [Setup a Docker Container](#setup-a-docker-container)
  * [Setup Python](#setup-python)
  * [How to Install Homework 3 Program](#how-to-install-homework-3-program)
  * [How to Run Homework 3 Program](#how-to-run-homework-3-program)
* [Overview](#overview)
  * [Directory Structure](#directory-structure)
  * [File and Program Descriptions](#file-and-program-descriptions)
    * [Server Files](#server-files)
    * [Configuration Files](#configuration-files)
    * [Client Program](#client-program)
  * [Expected Output and Error Conditions](#expected-output-and-error-conditions)
    * [Expected Output](#expected-output)
    * [Error Conditions](#error-conditions)
* [Cheat Sheets](#cheat-sheets)
  * [Docker Cheat Sheet](#docker-cheat-sheet)
  * [Linux Cheat Sheet](#linux-cheat-sheet)

# Installation

## Install Docker Containers
First, download the Docker Community Edition (CE) for the Desktop from their [download page](https://www.docker.com/community-edition#/download).

Secondly, follow their instructions at their [Getting Started Page](https://docs.docker.com/get-started/).

If you want [hands-on tutorials](https://docs.docker.com/get-started/) or would like to use their [training videos and online playground](http://training.play-with-docker.com/), please feel free to do so.

## Setup a Docker Container
First, open up a terminal or command prompt window and cd to the designated Docker directory:
```
cd Desktop/Docker
```
After you're in your designated Docker directory, start your own container. In this case, I named my container "myContainer" and started it up with Ubuntu:
```
docker run -it --name=[myContainer] ubuntu
```
Since the base Ubuntu image only has the bare minimal packages installed, we will need to install some more packages:
```
apt-get -y update
apt-get -y install iputils-ping
apt-get -y install iproute
apt-get -y install dnsutils
```
You can find the ip address of your current container by doing ip a. For example, my container's ip is 172.17.0.2.:
```
ip a
```

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: tunl0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1
    link/ipip 0.0.0.0 brd 0.0.0.0
3: ip6tnl0@NONE: <NOARP> mtu 1452 qdisc noop state DOWN group default qlen 1
    link/tunnel6 :: brd ::
6: eth0@if7: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```
You can also ping the address of your container or other containers that you have created by using the ping:
```
ping 172.18.0.3
```
Professor Lipyeow Lim provides us with a very good demonstration of setting up a docker container and pinging:
[![OH NO SOMETHING WENT WRONG](http://img.youtube.com/vi/YHL_TaSC_hk/0.jpg)](http://www.youtube.com/watch?feature=player_embedded&v=YHL_TaSC_hk)

## Setup Python
Now that we've installed the packages we need, let's also install Python3, package installer, vim, and sqlite3:
```
apt-get -y install python3
apt-get -y install python3-pip
apt-get -y install vim
apt-get -y install sqlite3
```
Since it is not a good practice to work in root, let's create a user account:
```
adduser [username]
```
Make sure to follow the onscreen instructions!
```
su [username]
cd
```
## How to Install Homework 3 Program
Leave the terminal or command prompt open and go to my [github page](https://github.com/saehyuns/hw3). Download the zip containing my homework 3 files and store / unzip it into the designated docker directory.

Now start up a new terminal or command prompt tab or window and go to your designated docker directory, and copy the files into your container. In my case:
```
cd Desktop/Docker
chmod -R 0777 hw2-master
docker cp /Users/SaeHyunSong/Desktop/Docker/hw3-master [Container Name]:/home/[user name]/
```
Now go back to your container and cd into the hw2-master directory and voila we're all done with the installation process!

## How to Run Homework 3 Program

Go the the main directory and type the following shell scripts in order:
```
init.sh
cur.sh
run.sh
post.sh
```
Each of the these shell scripts contains a way to run the program with more simplicity. The init.sh script basically drops all current tables on the database and runs the server node programs. Then, the cur.sh script runs the program that creates the tables and inserts the necessary data into the databases. The run.sh runs the program mySQL.py that performs the DDL command as specified in the homework. And finally the post.sh basically runs the test cases that show the database after performing queries.

Make sure to remove all the processes when wanting to reset the server nodes:
```
  PID TTY          TIME CMD
 4295 pts/1    00:00:02 bash
 7500 pts/1    00:00:00 python3
 7502 pts/1    00:00:00 python3
 7505 pts/1    00:00:00 python3
 7515 pts/1    00:00:00 ps
```

Kill all the processes that have the CMD of python3:
```
kill 7500
kill 7502
kill 7505
```

Now you can run eveything from the start again.
After running run.sh, You should then see the [expected output](#expected-output). 

Then run everything again from the [beginning](#how-to-run-homework-3-program).
If you get any errors, refer to the [Error Conditions Section](#error-conditions).

# Overview

## Directory Structure
The top-level directory structure contains:
```
catalog/                       # Holds the sqlite3 database mycatdb and the server program.
  mycatdb                      # The sqlite3 database called mycatdb.
  parDBd.py                    # The server program for the catalog node.
node1/                         # Holds the sqlite3 database mydb1 and the server program to simulate a different computer.
  mydb1                        # The sqlite3 database called mydb1.
  parDBd.py                    # The server program for the node1 node.
node2/                         # Holds the sqlite3 database mydb2 and the server program to simulate a different computer.
  mydb2                        # The sqlite3 database called mydb2.
  parDBd.py                    # The server program for the node2 node.
preTest/                       # Contains files for the init.sh script to run
  test1-saehyuns-1.1.sql       # Contains the SQL statement
  test1-saehyuns-1.pre         # Shell script that sets up the required tables for the test
  test1-saehyuns-1.pre.sql     # Contains the SQL statement
  test1-saehyuns-1.sql         # Contains the SQL statement
  test1-saehyuns-2.pre.sql     # Contains the SQL statement
  test1-saehyuns-2.sql         # Contains the SQL statement
postTest/
  test1-saehyuns-1.post        # Shell script that queries the databases after the test
  test1-saehyuns-1.post.1.sql  # Contains the SQL statement
  test1-saehyuns-1.post.2.sql  # Contains the SQL statement
  test1-saehyuns-1.post.exp    # Expected output of previous sql script
  test1-saehyuns-1.txt         # A description of what the test is testing.
books.sql                      # The sql file containing the commands
cur.sh                         # Shell script that runs program that creates / inserts content into db
init.sh                        # Shell script that runs program that resets the db
post.sh                        # Shell script that runs test cases for the db
run.sh                         # Shell script to run the runSQL.py with commandline arguments.
runSQL.py                      # The client program that executes SQL query via multithreading
test1-saehyuns-1.cfg           # Configuration for the cluster node for runSQL.py.
README.md                      # Contains information about installation and files.
```

## File and Program Descriptions

### Server Files
There are three server files one for each node called parDBd.py along with their own sqlite3 database:
```
catalog/                       # Holds the sqlite3 database mycatdb and the server program.
  mycatdb                      # The sqlite3 database called mycatdb.
  parDBd.py                    # The server program for the catalog node.
node1/                         # Holds the sqlite3 database mydb1 and the server program to simulate a different computer.
  mydb1                        # The sqlite3 database called mydb1.
  parDBd.py                    # The server program for the node1 node.
node2/                         # Holds the sqlite3 database mydb2 and the server program to simulate a different computer.
  mydb2                        # The sqlite3 database called mydb2.
  parDBd.py                    # The server program for the node2 node.
```
The node1 and node2 directory has the same server program but different database names:
```
node1/                         # Holds the sqlite3 database mydb1 and the server program to simulate a different computer.
  mydb1                        # The sqlite3 database called mydb1.
  parDBd.py                    # The server program for the node1 node.
node2/                         # Holds the sqlite3 database mydb2 and the server program to simulate a different computer.
  mydb2                        # The sqlite3 database called mydb2.
  parDBd.py                    # The server program for the node2 node.
```
The parDBd.py program for node1/ and node2/ contains:
```
import socket

import sqlite3
from sqlite3 import Error

# A Main function which listens for a message from the nodes to create catalog db and update the db.
def Main():
  # Host / port initialized with constant values.
  host = "127.0.0.2";
  port = 5000;

  # Messages received will be store in datas array.
  recvData = [];

  mySocket = socket.socket();
  mySocket.bind((host, port));
  mySocket.listen(100);

  while(1):
    conn, addr = mySocket.accept();
    receivedData = conn.recv(1024).decode();
    if not receivedData:
      return
    recvData.append(receivedData);
    receivedDatabase = receivedData.split("$")[0];
    receivedCommand = receivedData.split("$")[1];
    receivedCommand += ";";

    try:
      condb = sqlite3.connect("node1/" + receivedDatabase);
      cur = condb.cursor();
      cur.execute(receivedCommand);
      print(cur.fetchall());
      condb.commit();
      message = "[" + host + ":" + str(port) + "/" + receivedDatabase + "]: " + "test1-saehyuns-1.sql success.";
      conn.send(message.encode());
      condb.close();
    # If there is an error, send a message back to client that it was a failure.
    except Error as e:
      message = str(e);
      conn.send(message.encode());
    # After everything, finally close the db and the connection between client / server.
    finally:
      conn.close();
Main();
```
What this server program is basically doing is that it takes in two commandline arguments: IP address or hostname, and the port number. It uses those command line arguments to generate a socket with that ip address and port number. The socket will then listen for any data sent to it. Using the data it has received, it will connect to it's sqlite3 database with the data containing the database name. Execute the DDL statement that was sent along with the database name. Which then it will send a message back to the client program that it was successful or not. Then it finally closes all the connections after everything has been done. 

The catalog directory has a slightly different server program compared to the node1 and node2 servers:
```
catalog/                       # Holds the sqlite3 database mycatdb and the server program.
  mycatdb                      # The sqlite3 database called mycatdb.
  parDBd.py                    # The server program for the catalog node.
```
The parDBd.py program for catalog/ contains: 
```
import socket

import sqlite3
from sqlite3 import Error

# A Main function which listens for a message from the nodes to create catalog db and update the db.
def Main():
  # Host / port initialized with constant values.
  host = "127.0.0.10";
  port = 5000;

  # Messages received will be store in datas array.
  recvData = [];

  mySocket = socket.socket();
  mySocket.bind((host, port));
  mySocket.listen(100);

  while(1):
    conn, addr = mySocket.accept();
    print("Catalog Server: Connection from,", str(addr));
    receivedData = conn.recv(1024).decode();
    if not receivedData:
      return
    recvData.append(receivedData);
    print("Catalog Server: Received from client,", receivedData);
    # Connect to sqlite database in node1 directory and execute DDL command.
    try:
      con = sqlite3.connect("catalog/mycatdb");
      cur = con.cursor();
      cur.execute(receivedData);
      con.commit();
      message = "catalog updated.";
      conn.send(message.encode());
    # If there is an error, send a message back to client that it was a failure.
    except Error as e:
      message = str(e);
      conn.send(message.encode());
    # After everything, finally close the db and the connection between client / server.
    finally:
      con.close();
      conn.close();
Main(); 
```
What this server program does differently compared to the other server programs for node1 and node2 is that it receives from the client that the node1 or node2 was successful. Which then it creates the table called DTABLES it id does not already exist in the catalog database. After checking that, it will store the metadata about the DDL being executed in the catalog database. Then it sends the message back to the client that the catalog has been updated. The good thing about this is that the client will only send a message to the catalog server if node1 and node2 create tables were successful, saving time. It will be explained more when I am describing the client program runDDL.py.

### Configuration Files

There is one configuration file test1-saehyuns-1.cfg:
```
test1-saehyuns-1.cfg           # Configuration for the cluster node for runSQL.py.
```

The cluster.cfg file contains access information for each computer on the cluster such as the hostname, port, database name, and the number of nodes. This file will be parsed and the data will be used to send information to the cluster of node server programs. 
```
catalog.hostname=127.0.0.1:5000/mycatdb

numnodes=2

node1.hostname=127.0.0.2:5000/mydb1

node2.hostname=127.0.0.3:5000/mydb2
```

### Client Program

The client program called runSQL.py contains:
```

import re

import multiprocessing

# Importing socket library to do the socket connections between server and client.
import socket

# Importing sqlite3 library to do sqlite3 functions.
import sqlite3
from sqlite3 import Error

# Importing sys library to taking in commandline arguments.
import sys
from sys import argv

def openConfigFile(filename):
  configData = [];
  configFile = open(filename, "r");
  if (filename == "test1-saehyuns-1.cfg"):
    configData = configFile.read().strip().replace("\n", ";").split(";");
  configFile.close();
  return configData;

def openDDLFile(filename):
  ddlData = [];
  ddlFile = open(filename, "r");
  if (filename == "books.sql"):
    ddlData = ddlFile.read().strip().replace("\n", ";").split(";");
    ddlData = list(filter(('').__ne__, ddlData));
  ddlFile.close();
  return ddlData;

def parseConfigData(data):
  url = '';
  hostname = '';
  port = '';
  db = '';
  numnodes = 0;
  configNodes = [];

  for d in data:
    if d.strip():
      temp = d.strip().split("=");
      if temp[0].find("catalog") > -1:
        if temp[0].find("hostname") > -1:
          url = temp[1];
          hostname = temp[1].split("/")[0].split(":")[0];
          port = temp[1].split("/")[0].split(":")[1];
          db = temp[1].split("/")[1];
          configNodes.append(Node(url, hostname, port, db));
      if temp[0].find("node") > -1:
        if temp[0].find("hostname") > -1:
          url = temp[1];
          hostname = temp[1].split("/")[0].split(":")[0];
          port = temp[1].split("/")[0].split(":")[1];
          db = temp[1].split("/")[1];
          configNodes.append(Node(url, hostname, port, db));

  return configNodes;

def connectTo(catalogNode, serverNode, commands, tablename):
  url = serverNode.url;
  hostname = serverNode.hostname;
  port = serverNode.port;
  database = serverNode.db;
  
  for i in range(0, len(commands)):
    message = database + "$" + 'SELECT TITLE FROM BOOKS WHERE price>=10 and price <=20';

    mySocket = socket.socket();
    mySocket.connect((str(hostname), int(port)));
    mySocket.send(message.encode());
   
    recvData = mySocket.recv(1024).decode();
    print(recvData);

  mySocket.close();


def runDDL(argv):
  # Read from the cluster.cfg file and store it into an array called data.
  configData = [];
  configData = openConfigFile(argv[1]); 
  configData = list(filter(('').__ne__, configData));

  ddlData = [];
  ddlData = openDDLFile(argv[2]);
  
  configNodes = [];
  configNodes = parseConfigData(configData);

  numnodes = len(configNodes);
  tablename = "BOOKS";

  p1 = multiprocessing.Process(target=connectTo, args=(configNodes[0], configNodes[1], ddlData, tablename,));
  p2 = multiprocessing.Process(target=connectTo, args=(configNodes[0], configNodes[2], ddlData, tablename,));

  # Start the multi threading process
  p1.start();
  p2.start();

  # "Join" the two threads
  p1.join();
  p2.join();

  # Print done when both processes are done
  print("DONE");


# A class called node containing the url, hostname, port, and db name of the node.
class Node:
    def __init__(self, url, hostname, port, db):
        self.url = url;
        self.hostname = hostname;
        self.port = port;
        self.db = db;
    def displayNode(self):
        print("URL:", self.url, "HOSTNAME:", self.hostname, "PORT:", self.port, "DB:", self.db);

# Run the function runDDL with 2 commandline arguments.
runDDL(argv);
```
The runDDL program takes in two commandline arguments which are test1-saehyuns-1.cfg and books.sql. It will then parse the books.sql file and insert it into an array called ddlCommands. It also will parse the cluster.cfg file and store them into an array called data. Which then I create a loop for each data to split them and place each value in their respective variables and append that data into a Node class. Then I store each instance of the Node class that was created into the nodes array. Finally, I go through each each node and send the data that was parsed from the cluster.cfg and books.sql file to the node servers CONCURRENTLY USING THREADS and print out the message I receive from the server of whether or not it was successful. If it was successful, it will send that data to the catalog node to update the database there with the metadata. Otherwise, it will not send anything and just print out that the catalog was not updated. However, unlike the previous one, this supports select-from-where queries involving joins between exactly two tables.

## Expected Output and Error Conditions

### Expected Output
The expected output for runSQL.py should be:
```
[('Database Systems',), ('Operating Systems',)]
[127.0.0.2:5000/mydb1]: test1-saehyuns-1.sql success.
[]
[127.0.0.3:5000/mydb2]: test1-saehyuns-1.sql success.
DONE
```

### Error Conditions
An error condition would be if the ip address or hostname is inputted wrong / doesn't match the cluster.cfg file when using commandline arguments, it will give a connection refused error:
```
Traceback (most recent call last):
  File "runDDL.py", line 100, in <module>
    runDDL(argv);
  File "runDDL.py", line 64, in runDDL
    mySocket.connect((nodes[x].hostname, int(nodes[x].port)));
ConnectionRefusedError: [Errno 111] Connection refused
```

Another error condition would be if the server is not finished shutting down, it will say that the server ip address is already in use. I'd suggest waiting about a minute to restart the server:
```
  File "parDBd.py", line 53, in <module>
    Main(argv);
  File "parDBd.py", line 21, in Main
    mySocket.bind((str(host),int(port)))
OSError: [Errno 98] Address already in use
```

# Cheat Sheets

## Docker Cheat Sheet
Here is a simple [Docker Cheat Sheet](https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf) provided by Docker in case you're unfamiliar with the commands.

## Linux Cheat Sheet
Here is a [Linux/Unix Commands Reference](https://files.fosswire.com/2007/08/fwunixref.pdf) in case you're unfamiliar with the system as we will be using a Docker Linux Container with Ubuntu.

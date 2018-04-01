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
The parDBd.py program for hw2n0/ contains: 
```
# Import all necessary libraries.
import socket

import sqlite3
from sqlite3 import Error

import sys
from sys import argv

# A Main function which listens for a message from the nodes to create catalog db and update the db.
def Main(argv):
  host = argv[1];
  port = argv[2];

  # Messages received will be store in datas array.
  datas = [];

  mySocket = socket.socket()
  mySocket.bind((str(host),int(port)))
  mySocket.listen(100)

  while(1):
    conn, addr = mySocket.accept()
    # print ("Server: Connection from " + str(addr))
    data = conn.recv(1024).decode()
    if not data:
        return
    # print ("Server: recv " + str(data));
    datap = data.split("$");
    id = 0;
    if datap[2].find("mydb1") > -1:
      id = 1;
      # Connect to the mycatdb sqlite3 database and execute a create table / insert DDL command.
      try:
        con = sqlite3.connect("mycatdb");
        cur = con.cursor();
        cur.execute("CREATE TABLE IF NOT EXISTS DTABLES(tname char(32), nodedriver char(64), nodeurl char(128), nodeuser char(16), nodepasswd char(16), partmtd int, nodeid int, partcol char(32), partparam1 char(32), partparam2 char(32));");
        if(len(datap) >= 9):
cur.execute("INSERT INTO DTABLES(tname, nodedriver, nodeurl, nodeuser, nodepasswd, partmtd, nodeid, partcol, partparam1, partparam2) VALUES (" + "'" + datap[0] + "'" + ", " + "'" + datap[1] + "'" + ", " + "'" + datap[2] + "'" + ", " + "'" + datap[3] + "'" + ", " + "'" + datap[4] + "'" + ", " + "'" + datap[5] + "'" + ", " + "'" + str(id) + "'" + ", " + "'" + datap[6] + "'" + ", " + "'" + datap[7] + "'" + ", " + "'" + data[8] + "');");
        else:
          cur.execute("INSERT INTO DTABLES(tname, nodedriver, nodeurl, nodeuser, nodepasswd, partmtd, nodeid, partcol, partparam1, partparam2) VALUES (" + "'" + datap[1] + "'" + ", NULL, " + "'" + datap[2] + "'" + ", NULL, NULL, NULL, " + "'" + str(id) + "'" + ", NULL, NULL, NULL);");
        con.commit();
        message = "catalog updated.";
        conn.send(message.encode());
      # If there is an error send back an error message to client.
      except Error as e:
        print(e);
        message = e;
        conn.send(message.encode());
        con.close();
      # Finally, close all connections.
      finally:
        con.close();
    else:
      nodes = [];
      results = [];
      database = '';

      datap = data.split("$");
      database = datap[0];
      for i in range(1, len(datap)):
        nodes.append(datap[i]);
      try:
        con = sqlite3.connect(database);
        cur = con.cursor();
        for node in nodes:
          cur.execute("SELECT DISTINCT NODEURL FROM DTABLES WHERE NODEID=" + node);
          results.append(cur.fetchone());
          con.commit();
        message = "catalog updated.";
      # If there is an error send back an error message to client.
      except Error as e:
        print(e);
        message = e;
        conn.send(message.encode());
        con.close();
      # Finally, close all connections.
      finally:
        con.close();

      for result in results:
        message += "$" + str(result);
      conn.send(message.encode());

Main(argv);
```
What this server program does differently compared to the other server programs for node1 and node2 is that it receives from the client that the node1 or node2 was successful. Which then it creates the table called DTABLES it id does not already exist in the catalog database. After checking that, it will store the metadata about the DDL being executed in the catalog database. Then it sends the message back to the client that the catalog has been updated. The good thing about this is that the client will only send a message to the catalog server if node1 and node2 create tables were successful, saving time. It will be explained more when I am describing the client program runDDL.py.

### Configuration Files

There are five configuration files books.csv, books.sql, cluster.cfg, hash.cfg, range.cfg:
```
cluster.cfg       # A configuration file that contains information about the nodes.
hash.cfg          # A configuration file that contains information about the hash partition.
range.cfg         # A configuration file that contains information about the range partition.
books.csv         # A comma separated value file containing information to be added to the respective dbs.
books.sql         # Contains a DDL command which is used to run on the node's database.
```

The cluster.cfg file contains access information for each computer on the cluster such as the hostname, port, database name, and the number of nodes. This file will be parsed and the data will be used to send information to the cluster of node server programs. 
```
catalog.hostname=127.0.0.1:5000/mycatdb

numnodes=2

node1.hostname=127.0.0.2:5000/mydb1

node2.hostname=127.0.0.3:5000/mydb2
```

The hash.cfg file contains information for the hash partition. This file will be parsed
and the data/parameters will be used to determine which db the values in the csv file will go to.
```
catalog.driver=com.ibm.db2.jcc.DB2Driver
catalog.hostname=127.0.0.10:5000/mycatdb
catalog.username=db2inst1
catalog.passwd=mypasswd

tablename=books

partition.method=hash
partition.column=isbn
partition.param1=2
```

The range.cfg file contains information for the range partition. This file will be parsed
and the data/parameters will be used to determine which db the values in the csv file will go to.
```
catalog.driver=com.ibm.db2.jcc.DB2Driver
catalog.hostname=127.0.0.10:5000/mycatdb
catalog.username=db2inst1
catalog.passwd=mypasswd

tablename=books
partition.method=range
partition.column=isbn

numnodes=2
partition.node1.param1=100000000
partition.node1.param2=200000000

partition.node2.param1=200000000
partition.node2.param2=300000000
```

The file books.sql contains the DDL terminated by a semi-colon to be executed on the node server:
```
SELECT * FROM BOOKS;
```


The file books.csv contains the values to be added into the database.
```
123323232,"Database Systems","Ramakrishnan, Raghu"
234323423,"Operating Systems","Silberstein, Adam"
```

### Client Program

The client program called runSQL.py contains:
```
# Import necessary libraries / packages
import re

import socket

import sys
from sys import argv

import sqlite3
from sqlite3 import Error

import multiprocessing

# Function called runSQL takes in two commandline arguments
def runSQL(argv):
  # Initialize variables
  url = '';
  hostname = '';
  port = '';
  db = '';
  numnodes = 0;
  nodes = [];
  tablename = argv[2];
  tablename = tablename.replace(".sql", "").upper();
  message = "";

  data = [];
  ddlCommands = [];

  # Read int he cluster.cfg
  if argv[1] == "cluster.cfg":
    configFile = open(argv[1], "r");
    data = configFile.read().strip().replace("\n", ";").split(";");
    data = list(filter(('').__ne__, data));
    configFile.close();
  # Print error messag eif not cluster.cfg
  else:
    print("Please enter 'cluster.cfg' as the first commandline argument!");
  # Read in an .sql file
  if '.sql' in argv[2]:
    ddlFile = open(argv[2], "r");
    ddlCommands = ddlFile.read().strip().replace("\n", ";").split(";");
    ddlCommands = list(filter(('').__ne__, ddlCommands));
    ddlFile.close();
  # Print Error is not an .sql file.
  else:
    print("Please enter '[Insert Table Name].sql' as the first commandline argument!");

  # Parse the data and store into variabels
  for d in data:
    if d.strip():
      temp = d.strip().split("=");
      if temp[0].find("catalog") > -1:
        if temp[0].find("hostname") > -1:
          url = temp[1];
          hostname = temp[1].split("/")[0].split(":")[0];
          port = temp[1].split("/")[0].split(":")[1];
          db = temp[1].split("/")[1];
          nodes.append(Node(url, hostname, port, db));
      if temp[0].find("node") > -1:
        if temp[0].find("hostname") > -1:
          url = temp[1];
          hostname = temp[1].split("/")[0].split(":")[0];
          port = temp[1].split("/")[0].split(":")[1];
          db = temp[1].split("/")[1];
          nodes.append(Node(url, hostname, port, db));

  numnodes = len(nodes);

  # Multiprocessing / threading portion
  p1 = multiprocessing.Process(target=connect, args=(nodes[0], nodes[1], ddlCommands, tablename,));
  p2 = multiprocessing.Process(target=connect, args=(nodes[0], nodes[2], ddlCommands, tablename,));

  # Start the multi threading process
  p1.start();
  p2.start();

  # "Join" the two threads
  p1.join();
  p2.join();

  # Print done when both processes are done
  print("DONE");

# Function called connec that performs DDL on given servers via threading
def connect(catalogNode, serverNode, commands, tablename):
  url = serverNode.url;
  hostname = serverNode.hostname;
  port = serverNode.port;
  database = serverNode.db;

  for i in range(0, len(commands)):
    message = database + "$" + commands[i];

    mySocket = socket.socket();
    mySocket.connect((str(hostname),int(port)));
    mySocket.send(message.encode());

    received = mySocket.recv(1024).decode();
    receivedp = received.split("$");
    receivedp[3] = re.sub("'", '', receivedp[3]);
    mySocket.close();

    print(receivedp[3]);

    print("[" + url + "]: " + receivedp[0]);
    if(receivedp[0] == "./books.sql success."):
      message = receivedp[0] + "$" + tablename + "$" + url;
      mySocket2 = socket.socket();
      mySocket2.connect((catalogNode.hostname, int(catalogNode.port)));
      mySocket2.send(message.encode());
      received = mySocket2.recv(1024).decode();
      print("[" + catalogNode.url + "]: " + received);
      mySocket2.close();

# A class called node containing the url, hostname, port, and db name of the node.
class Node:
  def __init__(self, url, hostname, port, db):
    self.url = url;
    self.hostname = hostname;
    self.port = port;
    self.db = db;
  def displayNode(self):
    print("URL:", self.url, "HOSTNAME:", self.hostname, "PORT:", self.port, "DB:", self.db);

if __name__ == '__main__':
  runSQL(argv);
```
The runDDL program takes in two commandline arguments which are cluster.cfg and books.sql. It will then parse the books.sql file and insert it into an array called ddlCommands. It also will parse the cluster.cfg file and store them into an array called data. Which then I create a loop for each data to split them and place each value in their respective variables and append that data into a Node class. Then I store each instance of the Node class that was created into the nodes array. Finally, I go through each each node and send the data that was parsed from the cluster.cfg and books.sql file to the node servers CONCURRENTLY USING THREADS and print out the message I receive from the server of whether or not it was successful. If it was successful, it will send that data to the catalog node to update the database there with the metadata. Otherwise, it will not send anything and just print out that the catalog was not updated. 

The client program called loadCSV.py contains:
```
# Import needed packages
import socket

import re

import sys
from sys import argv

import sqlite3
from sqlite3 import Error

import multiprocessing

import csv

# Load function that takes commandline arguments
def load(argv):
  # Initialize variables
  tname = '';
  nodedriver = '';
  nodeurl = '';
  nodeuser = '';
  nodepasswd = '';
  partmtd = '';
  nodeid = '';
  partcol = '';
  partparam1 = '';
  partparam2 = '';

  configData = [];
  csvData = [];
  tables = [];

  parType = '';

  # If the config file is of type range partition run this part of the code
  if (argv[1] == "range.cfg"):
    parType = "range";

    # Open the config file for reading
    configFile = open(argv[1], "r");
    configData = configFile.read().strip().replace("\n", ";").split(";");
    configData = list(filter(('').__ne__, configData));
    configFile.close();

    # Parse through the config file and assign them into variables
    for d in configData:
      if d.strip():
        temp = d.strip().split("=");
        if temp[0].find("catalog") > -1:
          if temp[0].find("driver") > -1:
            nodedriver = temp[1];
          if temp[0].find("hostname") > -1:
            nodeurl = temp[1];
          if temp[0].find("username") > -1:
            nodeuser = temp[1];
          if temp[0].find("passwd") > - 1:
            nodepasswd = temp[1];
        if temp[0].find("tablename") > -1:
          tname = temp[1];
        if temp[0].find("partition") > -1:
          if temp[0].find("method") > -1:
            partmtd = 1;
          if temp[0].find("column") > -1:
            partcol = temp[1];
          if temp[0].find("node1") > -1:
            nodeid = 1;
            if temp[0].find("param1") > -1:
              partparam1 = temp[1];
            if temp[0].find("param2") > -1:
              partparam2 = temp[1];
              tables.append(Table(tname, nodedriver, nodeurl, nodeuser, nodepasswd, partmtd, nodeid, partcol, partparam1, partparam2));
          if temp[0].find("node2") > -1:
            nodeid = 2;
            if temp[0].find("param1") > -1:
              partparam1 = temp[1];
            if temp[0].find("param2") > -1:
              partparam2 = temp[1];
              tables.append(Table(tname, nodedriver, nodeurl, nodeuser, nodepasswd, partmtd, nodeid, partcol, partparam1, partparam2));

  # If the config file is of type hash partition run this part of the code
  elif argv[1] == "hash.cfg":
    parType = "hash";

    # Open the config file to reading
    configFile = open(argv[1], "r");
    configData = configFile.read().strip().replace("\n", ";").split(";");
    configData = list(filter(('').__ne__, configData));
    configFile.close();

    # Parse through the data and store them into variables
    for d in configData:
      if d.strip():
        temp = d.strip().split("=");
        if temp[0].find("catalog") > -1:
          if temp[0].find("driver") > -1:
            nodedriver = temp[1];
          if temp[0].find("hostname") > -1:
            nodeurl = temp[1];
          if temp[0].find("username") > -1:
            nodeuser = temp[1];
          if temp[0].find("passwd") > - 1:
            nodepasswd = temp[1];
        if temp[0].find("tablename") > -1:
          tname = temp[1];
        if temp[0].find("partition") > -1:
          if temp[0].find("method") > -1:
            partmtd = 2;
          if temp[0].find("column") > -1:
            partcol = temp[1];
          if temp[0].find("param1") > -1:
            partparam1 = temp[1];
    tables.append(Table(tname, nodedriver, nodeurl, nodeuser, nodepasswd, partmtd, nodeid, partcol, partparam1, partparam2));
  # If it is neither of the config file, print error message
  else:
    print("The config file has to be 'hash.cfg' or 'range.cfg'!");
    parType = "none";

  # Read from books.csv
  if (argv[2] == "books.csv"):
    csvFile = open(argv[2], "r");
    csvReader = csv.reader(csvFile, delimiter=",")
    for row in csvReader:
      csvData.append(row);
  # If it is not books.csv, print error message
  else:
    print("Please enter 'books.csv' as the second commandline argument!");

  temp = tables[0].nodeurl.split("/");
  database = temp[1];

  temp = temp[0].split(":");
  hostname = temp[0];
  port = temp[1];

  # If partition type is hash run this part of the code
  if parType == "hash":
    nodes =  [];
    for i in range (0, len(csvData)):
      tables[0].nodeid = (int(csvData[i][0]) % int(tables[0].partparam1)) + 1;
      nodes.append(tables[0].nodeid);

    message = database;
    for node in nodes:
      message += "$" + str(node);

    mySocket = socket.socket();
    mySocket.connect((str(hostname), int(port)));
    mySocket.send(message.encode());

    received = mySocket.recv(1024).decode();
    receivedp = received.split("$");
    result = receivedp[0];

    mySocket.close();

    dbNodes = [];
    for i in range(1, len(receivedp)):
      dbNodes.append(receivedp[i]);

    hostnames = [];
    ports = [];
    databases = [];

    # Remove unnecessary symbols
    for i in range(0, len(dbNodes)):
      count = nodes.count(i+1);
      dbNodes[i] = re.sub("[)',(]", '', dbNodes[i]);
      databases.append(dbNodes[i].split("/")[1]);
      hostnames.append(dbNodes[i].split("/")[0].split(":")[0]);
      ports.append(dbNodes[i].split("/")[0].split(":")[1]);

      mySocket2 = socket.socket();
      mySocket2.connect((str(hostnames[i]), int(ports[i])));
      message = databases[i];

      command = "insert into books (isbn, title, price) values (" + "'" + csvData[i][0] + "', " + "'" + csvData[i][1] + "', " + "'" + csvData[i][2] + "');";

      message += "$" + command;
      mySocket2.send(message.encode());
      received = mySocket2.recv(1024).decode();
      receivedp = received.split("$");
      mySocket2.close();

      print("[" + dbNodes[i] + "]: " + receivedp[0]);
      print("[" + dbNodes[i] + "]: " + str(count) + " rows inserted.");
      message = str(tables[0].tname) + "$" + str(tables[0].nodedriver) + "$" + dbNodes[i] + "$" + str(tables[0].nodeuser) + "$" + str(tables[0].nodepasswd) + "$" + str(tables[0].partmtd) + "$" + str(tables[0].partcol) + "$" + str(tables[0].partparam1) + "$" + str(tables[0].partparam2);
      mySocket3 = socket.socket();
      mySocket3.connect((str(hostname), int(port)));
      mySocket3.send(message.encode());
      received = mySocket3.recv(1024).decode();
      print("[" + tables[0].nodeurl + "]: " + received);
      mySocket3.close();

  # If the partition type is range, run this part of the code
  elif parType == "range":
    nodes =  [];
    for i in range (0, len(csvData)):
      if (int(csvData[i][0]) > int(tables[0].partparam1)) and (int(csvData[i][0]) <= int(tables[0].partparam2)):
        tables[0].nodeid = 1;
        nodes.append(tables[0].nodeid);
      elif (int(csvData[i][0]) > int(tables[1].partparam1)) and (int(csvData[i][0]) <= int(tables[1].partparam2)):
        tables[1].nodeid = 2;
        nodes.append(tables[1].nodeid);

    message = database;
    for node in nodes:
      message += "$" + str(node);

    mySocket = socket.socket();
    mySocket.connect((str(hostname), int(port)));
    mySocket.send(message.encode());

    received = mySocket.recv(1024).decode();
    receivedp = received.split("$");
    result = receivedp[0];
    mySocket.close();

    dbNodes = [];
    for i in range(1, len(receivedp)):
      dbNodes.append(receivedp[i]);

    hostnames = [];
    ports = [];
    databases = [];

    # Remove unnecessary symbols
    for i in range(0, len(dbNodes)):
      count = nodes.count(i+1);
      dbNodes[i] = re.sub("[)',(]", '', dbNodes[i]);
      databases.append(dbNodes[i].split("/")[1]);
      hostnames.append(dbNodes[i].split("/")[0].split(":")[0]);
      ports.append(dbNodes[i].split("/")[0].split(":")[1]);

      mySocket2 = socket.socket();
      mySocket2.connect((str(hostnames[i]), int(ports[i])));
      message = databases[i];

      command = "insert into books (isbn, title, price) values (" + "'" + csvData[i][0] + "', " + "'" + csvData[i][1] + "', " + "'" + csvData[i][2] + "');";

      message += "$" + command;
      mySocket2.send(message.encode());
      received = mySocket2.recv(1024).decode();
      receivedp = received.split("$");
      mySocket2.close();

      print("[" + dbNodes[i] + "]: " + receivedp[0]);
      print("[" + dbNodes[i] + "]: " + str(count) + " rows inserted.");
      message = str(tables[0].tname) + "$" + str(tables[0].nodedriver) + "$" + dbNodes[i] + "$" + str(tables[0].nodeuser) + "$" + str(tables[0].nodepasswd) + "$" + str(tables[0].partmtd) + "$" + str(tables[0].partcol) + "$" + str(tables[0].partparam1) + "$" + str(tables[0].partparam2);
      mySocket3 = socket.socket();
      mySocket3.connect((str(hostname), int(port)));
      mySocket3.send(message.encode());
      received = mySocket3.recv(1024).decode();
      print("[" + tables[0].nodeurl + "]: " + received);
      mySocket3.close();

  else:
    print("DOING NO PARTITION...\n");


class Table:
  def __init__(self, tname, nodedriver, nodeurl, nodeuser, nodepasswd, partmtd, nodeid, partcol, partparam1, partparam2):
    self.tname = tname;
    self.nodedriver = nodedriver;
    self.nodeurl = nodeurl;
    self.nodeuser = nodeuser;
    self.nodepasswd = nodepasswd;
    self.partmtd = partmtd;
    self.nodeid = nodeid;
    self.partcol = partcol;
    self.partparam1 = partparam1;
    self.partparam2 = partparam2;
  def displayTable(self):
    print("\nTable Name: ", self.tname, "\nNode Driver: ", self.nodedriver, "\nNode Url: ", self.nodeurl, "\nNode User: ", self.nodeuser, "\nNode Password: ", self.nodepasswd, "\nPartition Method: ", self.partmtd, "\nNode ID: ", self.nodeid, "\nPartition Column: ", self.partcol, "\nPartition Parameter 1: ", self.partparam1, "\nPartition Parameter 2: ", self.partparam2);

if __name__ == '__main__':
  load(argv);
```
The program loadCSV takes in two commandline arguments, hash.cfg or range.cfg and books.csv. The hash.cfg and range.cfg file contains access information for the name of the table to be loaded, and the partitioning information. The csv file contains the data to be loaded. Based off which configuration you want, either the hash or the range configuration. It calculates which node the data will belong to and consults the catalog db to get the nodeurl respective to the nodeid. 

The nodeid is determined by as provided in the homework page:
```
Note that you will need to convert the partition method specified as a string in the config file to the integer partition method stored in dtables. The values in the config file corresponding partmtd 0, 1, and 2 are notpartition, range, and hash respectively.

If the partition method is zero, ie, not partition, then the entire CSV file is inserted into the table at every node.

For range partitioning the rows that should be inserted into partition X should have a value in theipartcol between the minimum and maximum of the range for X:

partparam1 < partcol <= partparam2.
At the boundary ranges, partparam{1,2} may take the special values : -inf, +inf.

For hash partitioning the rows that should be inserted into partition X if

X = ( partcol mod partparam1 ) + 1.
The plus one is to handle the fact that our partition/node numbers start from 1 instead of 0. You may assume that only numeric columns will be partitioned for this assignment. The number of nodes in the dtables relation and the number of partitions in the config file should match. If not the program should return an error message and exit. You may assume the CSV file is error free (ie every row has the same number of columns of the right type).
```

Once it retrieves the nodeurl from the catalogdb, it sends the data from the books.csv file to their respective dbs. If it is successful, it will print out the message I receive from the server of whether or not it was successful. If it was successful, it will send that data to the catalog node to update the database there with the metadata. Otherwise, it will not send anything and just print out that the catalog was not updated. 

## Expected Output and Error Conditions

### Expected Output
The expected output for loadCSV.py should be:
```
[127.0.0.2:5000/mydb1]: ./books.sql success.
[127.0.0.2:5000/mydb1]: 1 rows inserted.
[127.0.0.10:5000/mycatdb]: catalog updated.
[127.0.0.3:5000/mydb2]: ./books.sql success.
[127.0.0.3:5000/mydb2]: 1 rows inserted.
[127.0.0.10:5000/mycatdb]: catalog updated.
```

The expected output for runSQL.py should be:
```
[(123323232, Database Systems, Ramakrishnan, Raghu)]
[127.0.0.2:5000/mydb1]: ./books.sql success.
[(234323423, Operating Systems, Silberstein, Adam)]
[127.0.0.3:5000/mydb2]: ./books.sql success.
[127.0.0.10:5000/mycatdb]: catalog updated.
[127.0.0.10:5000/mycatdb]: catalog updated.
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

Another error condition is if the ./books.sql in loadCSV.py program fails no rows will be inserted and the catalog will not be updated:
```
[127.0.0.2:5000/mydb1]: ./books.sql failure.
[127.0.0.2:5000/mydb1]: 0 rows inserted.
[127.0.0.3:5000/mydb2]: ./books.sql success.
[127.0.0.3:5000/mydb2]: 1 rows inserted.
[127.0.0.10:5000/mycatdb]: catalog updated.
```

Another error condition is that if the runSQL.py query fails, the catalog will not be updated and you will
not be able to see the result of the query:
```
[127.0.0.2:5000/mydb1]: ./books.sql failure.
[(234323423, Operating Systems, Silberstein, Adam)]
[127.0.0.3:5000/mydb2]: ./books.sql success.
[127.0.0.10:5000/mycatdb]: catalog updated.
DONE
```


# Cheat Sheets

## Docker Cheat Sheet
Here is a simple [Docker Cheat Sheet](https://www.docker.com/sites/default/files/Docker_CheatSheet_08.09.2016_0.pdf) provided by Docker in case you're unfamiliar with the commands.

## Linux Cheat Sheet
Here is a [Linux/Unix Commands Reference](https://files.fosswire.com/2007/08/fwunixref.pdf) in case you're unfamiliar with the system as we will be using a Docker Linux Container with Ubuntu.

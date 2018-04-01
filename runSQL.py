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

import socket

import sqlite3
from sqlite3 import Error

# A Main function which listens for a message from the nodes to create catalog db and update the db.
def Main():
  # Host / port initialized with constant values.
  host = "127.0.0.3";
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
      condb = sqlite3.connect("node2/" + receivedDatabase);
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

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

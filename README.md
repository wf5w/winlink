# winlink auxilliary programs

Pat winlink auxilliary programs

## patwinlinkmsgform -- bash (using yad)

Have you ever had the need to create a message for the pat winlink outbox, but don't want to do it in pat winlink? For instance, you are in a Emergency Comms situation where you want people to send message to their loved ones, that they are safe and sound, or messages requesting aid?

In this situation, you can have them create their own message and it will post to the output of pat winlink. Later on, you can send them all.

### prerequistes

* you need yad: $ sudo apt install yad
* you need pat winlink installed, using 73Linux by KM4ACK is a great way to do that.

### configuration

You must edit the file, and replace NOCALL with your own callsign. That's it.


## patwinlinkmail.py - with patwlclass.py (module)

This is written with cross platform capability in mind. It is written in python3 and with PySide6

This was writen to facilitate, during an emergency, obtaining multiple emails to send later on using the pat winlink command:
$ pat connect telnet # or some other protocol.

### prerequistes

* python3
* PySide6

After installing python3, install PySide6 by:
$ pip install pyside6

place the patwlclass.py file into the python site-packages directory




import socket

# Create a socket (like create a phone)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# (make the phone call)
# throws error if there were problems
mysock.connect(("data.pr4e.org", 80))

# Create and send command
# Headers can be put between the \r\n and \r\n
# encode => encodes to UTF-8, python is in unicode
cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

# Fetch data
while True:
    # Waits until 512 chars (or all the remaining chars)
    data = mysock.recv(512)

    # Stop when no more data
    # Connection on the other end has already closed
    if len(data) < 1:
        print()
        break

    # Decode from UTF-8 to unicode to be able to print in python
    print(data.decode(), end="")


# Close socket
mysock.close()

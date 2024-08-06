from socket import *


def createServer():
    # Create a socket (creating the phone)
    serversocket = socket(AF_INET, SOCK_STREAM)

    try:
        # Ready to receive phone calls on 9000
        # if the port is free
        serversocket.bind(("localhost", 9000))

        # 5 is the max requests that can be queued
        serversocket.listen(5)

        # Infinite loop to listen for requests
        while 1:
            print("loop start")
            # accept - ready to pick the phone up
            # that means it is blocking
            # sits there forever
            (clientsocket, address) = serversocket.accept()

            # runs when the phone call is received
            # http protocol says that the client has to speak first
            # whatever the browser sends, the server receives
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])

            # Construct response to return
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            # Encode to utf-8 and send the response and shut down the connection
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

            # Once the loop is done, it waits for the next connection/request

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as e:
        print("Error:\n")
        print(e)

    serversocket.close()


print("Access http://localhost:9000")
createServer()

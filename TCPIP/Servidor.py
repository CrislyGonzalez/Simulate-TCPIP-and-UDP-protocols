import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print(sys.stderr, 'empezando a levantar %s puerto %s' % server_address)

sock.bind(server_address)

sock.listen(1)


while True:

    print(sys.stderr, 'Esperando para conectarse')
    connection, client_address = sock.accept()

    try:
        print(sys.stderr, 'conexion desde', client_address)
        print("Dirección IP del Servidor: ",client_address[0],"\n"
              "Nombre del Servidor:", server_address[0],"\n"
              "")


        while True:
            data = connection.recv(19)
            print(sys.stderr, 'recibido "%s"' % data)
            if data:
                print(sys.stderr, 'enviando mensaje de vuelta al cliente')
                connection.sendall(data)
            else:
                print(sys.stderr, 'no hay mas datos', client_address)
                break

    finally:

        connection.close()
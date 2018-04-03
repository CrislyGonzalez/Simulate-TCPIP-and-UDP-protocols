import socket
import sys

# Creando el socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace de socket y puerto
server_address = ('localhost', 10000)
print (sys.stderr, 'empezando a levantar %s puerto %s' % server_address)
sock.bind(server_address)   #  Asocia el socket al servidor que se encuentra en localhost

# Escuchando conexiones entrantes
sock.listen(1)

while True:
    # Esperando conexion
    print(sys.stderr, 'Esperando para conectarse')
    connection, client_address = sock.accept()

    try:
        print(sys.stderr, 'concexion desde', client_address)

        # Recibe los datos en trozos y reetransmite
        while True:
            data = connection.recv(19)
            print(sys.stderr, 'recibido "%s"' % data)
            print("*** Mensaje del cliente recibido ***")
            break

    finally:
        # Cerrando conexion
        connection.close()
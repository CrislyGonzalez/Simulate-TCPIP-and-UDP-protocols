import socket
import sys

#Creando un socket TCP/IP
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 10000)
print(sys.stderr, 'conectando a %s puerto %s' % server_address)
sock.connect(server_address)

try:
    # Enviando datos
    message = 'Este es el mensaje.'
    print(sys.stderr, 'enviando "%s"' % message)
    print("  *** Este es mi mensaje ***  ")
    sock.sendall(message)

    print(" *** No me interesa la respuesta, soy UDP *** ")

finally:
    print(sys.stderr, 'cerrando socket')
    sock.close()

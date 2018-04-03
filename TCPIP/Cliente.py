import socket
import sys

sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 10000)
print(sys.stderr, 'conectando a %s puerto %s' % server_address)
sock.connect(server_address)

try:

    message = 'Este es el mensaje.  Se repitio.'
    print(sys.stderr, 'enviando "%s"' % message)
    sock.sendall(message)


    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(19)
        amount_received += len(data)
        print(sys.stderr, 'recibiendo "%s"' % data)

finally:
    print(sys.stderr, 'cerrando socket')
    sock.close()



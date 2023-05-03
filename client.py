import socket

# Crearea socket-ului pentru aplicatia client
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarea socket-ului creat la o adresa si un port anume, in cazul de fata la adresa si port-ul server-ului
clientSocket.connect(("localhost", 31469))

# Citirea de la tastatura a listei de numere, trimiterea acesteia la server si inchiderea socket-ului pentru client
mesajTrimis = input("Introduceti un set de numere cu cel putin 5 si cel mult 10 numere, separate printr-o virgula ").encode()
clientSocket.send(mesajTrimis)
mesajPrimit = clientSocket.recv(512)  # Mesajul primit de la server pentru rezultatul final

print("\n", mesajPrimit.decode())
clientSocket.close()

import socket

# Functie pentru a determina daca lista introdusa este o progresie aritmetica
def progresie_aritmetica(array):
    r = array[1] - array[0]
    for i in range(0, len(array)-1):
        if array[i + 1] - array[i] != r:
            return False
    return True


# Functie pentru a determina daca lista introdusa este o progresie geometrica
def progresie_geometrica(array):
    q = array[1] / array[0]
    for i in range(0, len(array)-1):
        if array[i + 1] / array[i] != q:
            return False
    return True


# Crearea socket-ului pentru aplicatia server, crearea conexiunii cu client-ul si acceptarea acestei conexiuni
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("localhost", 31469))
serverSocket.listen(1)
clientSocket, address = serverSocket.accept()

# Mesajul primit de catre client si transformarea acestuia intr-o lista de numere
mesajPrimit = clientSocket.recv(512)
lista = list(map(float, mesajPrimit.decode().split(",")))

# Verificarea listei trimise daca este progresie aritmetica sau geometrica
if progresie_aritmetica(lista):
    r = int(lista[1] - lista[0])
    stringProgresieAritmetica = f"A({r})"  # Raspunsul server-ului pentru rezultatul final
    clientSocket.send(stringProgresieAritmetica.encode())  # Trimitem raspunsul client-ului
elif progresie_geometrica(lista):
    q = int(lista[1] / lista[0])
    stringProgresieGeometrica = f"G({q})"
    clientSocket.send(stringProgresieGeometrica.encode())
else:
    clientSocket.send("N".encode())

# Inchiderea socket-urilor pentru client si server
serverSocket.close()
clientSocket.close()

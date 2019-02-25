import socket

portas = [21,23,80,8080,443]

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(2)
    cod = cliente.connect_ex(('site.com.br', porta))
    if cod == 0:
        print porta, "OPEN"

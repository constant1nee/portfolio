import socket
import time

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 0)
main_socket.bind(('localhost', 10000))
main_socket.setblocking(False)
main_socket.listen(2)

clients_sockets = []

running = True
while running:
    try:
        new_socket, addr = main_socket.accept()
        new_socket.setblocking(False)
        clients_sockets.append(new_socket)
        print(f'Подключился:{addr}')
    except:
        print('Никто не подключился')
        pass
    for cl_socket in clients_sockets:
        try:
            data = cl_socket.recv(1024)
            data = data.decode()
        except:
            pass
    for cl_socket in clients_sockets:
        try:
            cl_socket.send('Новое состояние'.encode())
        except:
            clients_sockets.remove(cl_socket)
            cl_socket.close()
            print('Клиент отключился')
        time.sleep(0.1)

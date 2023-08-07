import socket
import time

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))  # 서버의 IP 주소와 포트 설정
    server_socket.listen(1)

    print("서버 시작. 클라이언트 연결 대기 중...")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"클라이언트가 연결되었습니다: {client_addr}")

        try:
            while True:
                current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                client_socket.send(current_time.encode('utf-8'))
                time.sleep(1)
        except:
            print("클라이언트 연결이 종료되었습니다.")
            client_socket.close()

if __name__ == "__main__":
    start_server()
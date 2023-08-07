import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # 서버의 IP 주소와 포트 설정

    print("서버에 연결되었습니다.")

    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            print(f"서버 시간: {data}")
    except:
        print("서버 연결이 종료되었습니다.")
        client_socket.close()

if __name__ == "__main__":
    start_client()

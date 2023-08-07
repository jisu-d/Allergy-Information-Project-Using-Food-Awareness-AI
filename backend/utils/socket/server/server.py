import socket
import os
import json
import base64

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))  # 서버의 IP 주소와 포트 설정
    server_socket.listen(1)

    print("서버 시작. 클라이언트 연결 대기 중...")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"클라이언트가 연결되었습니다: {client_addr}")

        
        print("start")
        data = client_socket.recv(8388608)
        print(data)
        image_info = json.loads(data)

        # 이미지 디코딩 및 저장
        filename = image_info["filename"]
        image_data = base64.b64decode(image_info["img"])

        with open(f'downloads/{filename}', 'wb') as file:
            file.write(image_data)

        print(f"이미지 '{filename}'를 성공적으로 다운로드했습니다.")
    

if __name__ == "__main__":
    start_server()

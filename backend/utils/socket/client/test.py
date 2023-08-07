import socket
import json
import base64

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # 서버의 IP 주소와 포트 설정

    print("서버에 연결되었습니다.")

    try:
        image_path = './ai.jpg'  # 이미지 파일의 경로
        with open(image_path, 'rb') as file:
            image_data = file.read()

        # 이미지를 base64로 인코딩
        encoded_image = base64.b64encode(image_data).decode('utf-8')

        # JSON 형식으로 이미지 정보 전송
        image_info = {"filename": "ai.jpg", "img": encoded_image,"test":"tst"}
        # print(image_info)
        json_data = json.dumps(image_info).encode('utf-8')

        client_socket.send(json_data)

        print("이미지를 서버에 성공적으로 보냈습니다.")
    except:
        print("서버 연결이 종료되었습니다.")
        client_socket.close()

if __name__ == "__main__":
    start_client()

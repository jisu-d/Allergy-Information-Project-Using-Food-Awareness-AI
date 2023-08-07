import json
import socket
import cv2
import numpy
import base64

class MakeClientSocket():
    def __init__(self, IP:str, PORT:int, SIZE:int):
        self.IP = IP
        self.PORT = PORT
        self.SIZE = SIZE

    def _socketConnection(self):
        SERVER_ADDR = (self.IP, self.PORT)
        try:
            sock = socket.socket()
            return sock.connect(SERVER_ADDR)
        except:
            raise("SokcetConnectionError")

class ImageSendSocket(MakeClientSocket):
    def __init__(self, IP:str, PORT:int, SIZE:int):
        super().__init__(IP, PORT, SIZE)
    def sendImg(self,Img:str,FileName:str)->dict:
        try:
            sock = self._socketConnection()
            sock.send(json.dumps({"filename":FileName,"img":Img}))
            serverMsg = sock.recv(self.SIZE)

            return json.loads(serverMsg)
        except:
            raise("SendFailed")
        finally:
            sock.close()

if __name__ == "__main__":
    sockobj = ImageSendSocket("127.0.0.1",12345,1024)
    aiimg = None
    with open("ai.jpg", "rb") as img:
        aiimg = base64.b64encode(img.read())
    print(sockobj.sendImg(aiimg,"ai.jpg"))
        

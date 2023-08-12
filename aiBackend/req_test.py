import requests
import base64

# for i in range(1,4):
with open(f'./img/don2.jpg', 'rb') as img:
    base64_string:bytes = base64.b64encode(img.read())



res = requests.post("http://127.0.0.1:3456/ai",json={"b64string":base64_string.decode("utf-8")})
if (res.status_code != 200):
    print(res.status_code)
else:
    print(res.json())
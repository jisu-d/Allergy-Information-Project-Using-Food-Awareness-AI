import base64
import time

IMG_ROOT_PATH = "./public"

def b64img_write(imgstring):
    try:
        imgdata = base64.b64decode(imgstring)
        filename = f'{IMG_ROOT_PATH}/{time.time()}.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
        return True, filename
    except Exception as e:
        print(e)
        return False
    
if (__name__ == "__main__"):
    with open('./img/kimbob.jpg', 'rb') as img:
        base64_string = base64.b64encode(img.read())
    print(b64img_write(base64_string))
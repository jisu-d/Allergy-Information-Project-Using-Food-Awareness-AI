import traceback
import os
from flask import Flask, request, jsonify, Response
from utils.b64img import b64img_write
from ai import check_food_category

app = Flask(__name__)

@app.route("/ai", methods=["POST"])
def ai():
    payload:dict = request.get_json()
    b64string = payload.get("b64string")
    res, file_name = b64img_write(b64string)
    if (not res):
        return Response(status=500)
    try:
        res, name, p = check_food_category(file_name)
        print(res, name, p)
        if (not res):
            return Response(status=400)
        if (0.96 >= p):
            return jsonify({"status":False})
        http_res = {"status":True,"category":name, "accuracy":float(p)}
        return jsonify(http_res) 
    except Exception as e:
        print(e)
        return Response(status=500)
    finally:
        os.remove(file_name)

if __name__ == "__main__":
    app.run("127.0.0.1", 3456)
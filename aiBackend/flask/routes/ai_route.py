from flask import request, Response, jsonify
from flask.views import MethodView
from utils.ai.ai import check_food_category
from utils.insert_database_allergy.db import AllergyInfo

class AiView(MethodView):

    def post(self):
        payload:dict = request.get_json()
        b64string = payload.get("b64string")
        try:
            res, name, p = check_food_category(b64string)
            if (not res):
                return Response(status=400)
            if (0.94 >= p):
                return jsonify({"status":False})
            db = AllergyInfo()
            db_res:dict = db.Read(name)
            all_row_data:str = db_res.get("AllergyIngredient")
            all_list = all_row_data.split('|')
            if (all_list[0]=="NONE"):
                return jsonify({"status":True,"category":name,"allergy":None})
            http_res = {"status":True,"category":name,"allergy":all_list[0:len(all_list)-1]}
            return jsonify(http_res) 
        except Exception as e:
            print(e)
            return Response(status=500)

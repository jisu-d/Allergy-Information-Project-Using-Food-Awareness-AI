import os
import sys
import dotenv
import pymysql

dotenv_file_path = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file_path)

def table_exists():
    conn = make_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    mysql_db_exists_query = f"CREATE DATABASE IF NOT EXISTS FoodAllergyInfo;"
    cursor.execute(mysql_db_exists_query)
    mysql_table_exists_query = f"""
    CREATE TABLE IF NOT EXISTS INFO (
        id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
        FoodName VARCHAR(255) NOT NULL UNIQUE,
        AllergyIngredient VARCHAR(255)
    )
    """
    cursor.execute(mysql_table_exists_query)
    conn.close()

def make_connection() -> pymysql.Connection:
    return pymysql.connect(
        host=os.getenv("PYMYSQL_HOST"),
        port=int(os.getenv("PYMYSQL_PORT")),
        user=os.getenv("PYMYSQL_USER"),
        passwd=os.getenv("PYMYSQL_PASSWORD"),
        db=os.getenv("PYMYSQL_DB"),
        charset="utf8"
    )

def init_db():
    conn = make_connection()
    table_exists(conn,os.getenv("PYMYSQL_DB"),("INFO"))

class AllergyInfo():

    def _make_cursor(self):
        self._conn = make_connection()
        self._cursor = self._conn.cursor(pymysql.cursors.DictCursor)

    @staticmethod
    def _make_allergy_insert_data(AllergyInfo)->str:
        allergy_insert_data = ""
        for i in AllergyInfo:
            allergy_insert_data += f"{i}|"
        return allergy_insert_data

    def Create(self, FoodName:str, AllergyInfo)->dict|bool:
        try:
            self._make_cursor()
            insert_all_info = self._make_allergy_insert_data(AllergyInfo)
            create_query =f"""
                INSERT INTO INFO (FoodName,AllergyIngredient) VALUES ("{FoodName}","{insert_all_info}");
            """
            self._cursor.execute(create_query)
            self._conn.commit()
            return self._cursor.fetchall()
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"File:{fname} - Line:{exc_tb.tb_lineno} - {e}")
            return False
        finally:
            self._conn.close()


    def ReadAll(self)->dict|bool:
        try:
            self._make_cursor()
            read_query = f"""
                SELECT * FROM INFO;
            """
            self._cursor.execute(read_query)
            return self._cursor.fetchall()
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"File:{fname} - Line:{exc_tb.tb_lineno} - {e}")
            return False
        finally:
            self._conn.close()


    def Read(self, FoodName:str)->dict|bool:
        try:
            self._make_cursor()
            read_query = f"""
                SELECT * FROM FoodAllergyInfo.INFO WHERE FoodName="{FoodName}";
            """
            self._cursor.execute(read_query)
            return self._cursor.fetchone()
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"File:{fname} - Line:{exc_tb.tb_lineno} - {e}")
            return False
        finally:
            self._conn.close()

    def Update(self, FoodName:str, UpdateFoodName:str, UpdateAllergyIngredient:tuple[str])->dict|bool:
        try:
            self._make_cursor()
            update_query = f"""
                UPDATE INFO SET FoodName="{UpdateFoodName}", AllergyIngredient="{self._make_allergy_insert_data(UpdateAllergyIngredient)}"
                WHERE FoodName="{FoodName}"
            """
            self._cursor.execute(update_query)
            self._conn.commit()
            return self._cursor.fetchall()
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"File:{fname} - Line:{exc_tb.tb_lineno} - {e}")
            return False
        finally:
            self._conn.close()

    def Delete(self, FoodName:str)->dict|bool:
        try:
            self._make_cursor()
            delete_query = f"""
                DELETE FROM INFO
                WHERE FoodName="{FoodName}";
            """
            self._cursor.execute(delete_query)
            self._conn.commit()
            return self._cursor.fetchall()
        except Exception as e:
            _, _, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"File:{fname} - Line:{exc_tb.tb_lineno} - {e}")
            return False
        finally:
            self._conn.close()
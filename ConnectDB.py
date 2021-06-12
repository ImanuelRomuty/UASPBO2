import mysql.connector 

class connection:
    def __init__(self):
        try:
            self.__con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="apotek",
                    buffered = True
            )
            self.__cursor = self.__con.cursor()
        except mysql.connector.Error as e:
          print(e)

    def select_one(self, query, value):
        self.__cursor.execute(query,value)
        result = self.__cursor.fetchone()
        self.__con.commit()
        return result

    def select_all(self, query):
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        self.__con.commit()
        return result

    def execute(self, query, value):
        try:
            self.__cursor.execute(query, value)
            self.__con.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def execute_abis(self,query):
        try:
            self.__cursor.execute(query)
            self.__con.commit()
            return True
        except Exception as e:
            print(e)
            return False


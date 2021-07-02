import mysql.connector

class db:

    def __init__(self):

        self.con = mysql.connector.connect(host='localhost',database='chefxml',user='root',password='123456', port='3307')

        if self.con.is_connected():
            db_info = self.con.get_server_info()
            print("Conectado ao servidor MySQL versão ",db_info)

    def retorna_conexao(self):
        return self.con

    def fechar(self):
        self.con.close()
        print("Conexão Encerrada!")
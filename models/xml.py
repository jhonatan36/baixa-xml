class xml:

    def __init__(self, con):
        self.con = con
        self.sql_return = "SELECT * FROM xml"

    def retorna_xmls(self):
        cursor = self.con.cursor()
        cursor.execute(self.sql_return)
        linhas = cursor.fetchall()
        return linhas

    def salva_xml(linha):
        arquivo = open("arquivos/"+str(linha[0])+".xml", 'wb')
        arquivo.write(str(linha[1]).encode())
        arquivo.close()
        return
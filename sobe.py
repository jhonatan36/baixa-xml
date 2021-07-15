import os
import mysql.connector

pasta = './Autorizado'

con_chef = mysql.connector.connect(host='localhost',database='chef',user='root',password='123456', port='3307')
con_chefxml = mysql.connector.connect(host='localhost',database='chefxml',user='root',password='123456', port='3307')

query_return_tupla = ("SELECT * FROM chef.nota_saida WHERE chave_acesso = %s")
query_insert_chefxml = ("INSERT INTO chefxml.xml (id_xml, XML, id_nota_saida) values(%s, %s, %s)")

for diretorio, subpastas, arquivos in os.walk(pasta):

    cursor = con_chef.cursor()

    for arquivo in arquivos:
        chave = arquivo.split('.')[0]
        cursor.execute(query_return_tupla, ([chave]))
        linha = cursor.fetchone()
        id = linha[0]

        #id_nota_saida = linha[0]
        documento = os.path.realpath(diretorio + '\\' + arquivo)

        with open(documento, 'r', encoding='utf-8') as file:
            textoArquivo = file.read()
            cursor_xml = con_chefxml.cursor()
            cursor_xml.execute(query_insert_chefxml, ([id, str(textoArquivo), id]))
            con_chefxml.commit()

con_chefxml.close()
con_chef.close()
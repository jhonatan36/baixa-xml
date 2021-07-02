from models.db import db
from models.xml import xml

#conectando na base de dados
xml_conection = xml(db.retorna_conexao(db()))

xmls = xml.retorna_xmls(xml_conection)

for row in xmls:
    xml.salva_xml(row)
exit()

#fecha conexao com a base de dados
db.fechar(xml_conection)
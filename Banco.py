'''
Projeto Banco de Dados da DevMedia
https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
'''
from sqlite3 import *

bd = sqlite3.connect('banco.db')

class Banco():
    def __init__(self):
        self.conexao = bd
        self.createTable()
     
    def createTable(self):
        c = self.conexao.cursor()
     
        c.execute("""create table if not exists usuarios (
                     idusuario integer primary key autoincrement ,
                     nome text,
                     telefone text,
                     email text,
                     usuario text,
                     senha text)""")
        self.conexao.commit()
        c.close()

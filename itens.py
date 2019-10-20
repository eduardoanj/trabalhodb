import MySQLdb

class Itens:
    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__quantidade = 0

# GET and SETTER id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

# GET and SETTER nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

# GET and SETTER quantidade
    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

def salvar_item_db(nome, quantidade):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO ITENS (NOME, QUANTIDADE)" + 
    " VALUES ('{}', '{}')" .format(nome, quantidade))
    conexao.commit()
    conexao.close()

########## LISTAR ITENS DO DB ##########
def listar_itens_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ITENS")
    lista_itens = []
    for i in cursor.fetchall():
        item = Itens()
        item.id = i[0]
        item.nome = i[1]
        item.quantidade = i[2]        
        lista_itens.append(item)
    conexao.close()
    return lista_itens   

########## DELETAR ITEM DO DB ##########
def deletar_item(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM ITENS WHERE id={}".format(id))
    conexao.commit()
    conexao.close()        
    
import MySQLdb

class Planos:
    def __init__(self):
        self.__id = 0
        self.__tipo = ''
        self.__usuario_id = 0
        self.__plano_id = 0

# GET and SETTER id
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

# GET and SETTER tipo
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

# GET and SETTER usuario_id
    @property
    def usuario_id(self):
        return self.__usuario_id
    
    @usuario_id.setter
    def usuario_id(self, usuario_id):
        self.__usuario_id = usuario_id

# GET and SETTER plano_id
    @property
    def plano_id(self):
        return self.__plano_id
    
    @plano_id.setter
    def plano_id(self, plano_id):
        self.__plano_id = plano_id   



##### LISTAR PLANOS #####
def listar_planos_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM PLANOS")
    lista_planos = []
    for i in cursor.fetchall():
        plano = Planos()
        plano.id = i[0]
        plano.tipo = i[1]
        lista_planos.append(plano)
    conexao.close()
    return lista_planos  

##### SALVAR PLANO NA TABELA #####
def salvar_plano_db(plano:Planos):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO USUARIO_PLANO (ID_USUARIO, ID_PLANO)" + 
    " VALUES ('{}', '{}')"
    .format(plano.usuario_id, plano.plano_id))
    conexao.commit()
    conexao.close()  

##### BUSCAR PLANO POR ID #####
def buscar_plano_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM PLANOS WHERE id ={}'.format(id))
    p = Planos()
    for i in cursor.fetchall():
        p.id = i[0]
        p.tipo = i[1]
    conexao.close()
    return p    

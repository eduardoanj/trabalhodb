import MySQLdb 

class Usuario:
    def __init__(self):
        self.__id = 0
        self.__nome = ''
        self.__cpf = ''
        self.__endereco = ''
        self.__cep = ''        
        self.__cartao = ''
        self.__validade = ''
        self.__codigo = ''

#GET and SETTER id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id        

#GET and SETTER nome    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

#GET and SETTER cpf
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

#GET and SETTER endereco
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

#GET and SETTER cep
    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, cep):
        self.__cep = cep

#GET and SETTER cartao
    @property
    def cartao(self):
        return self.__cartao
    
    @cartao.setter
    def cartao(self, cartao):
        self.__cartao = cartao    
        
#GET and SETTER validade
    @property
    def validade(self):
        return self.__validade
    
    @validade.setter
    def validade(self, validade):
        self.__validade = validade            
        
#GET and SETTER codigo
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo                    
        

########## SALVAR USUARIO NO DB ##########
def salvar_usuario_db(usuario:Usuario):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO USUARIO (NOME, CEP, CPF, ENDERECO, CARTAO_DE_CREDITO, VALIDADE, COD_SEGURANCA)" + 
    " VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')"
    .format(usuario.nome, usuario.cep, usuario.cpf, usuario.endereco, usuario.cartao, usuario.validade, usuario.codigo))
    conexao.commit()
    conexao.close()        

########## ALTERAR USUARIO NO DB ##########
def alterar_usuario_db(usuario:Usuario):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("UPDATE USUARIO SET NOME='{}', CEP='{}', CPF='{}', ENDERECO='{}', CARTAO_DE_CREDITO='{}', VALIDADE='{}', COD_SEGURANCA='{}' WHERE ID = {}"
    .format(usuario.nome, usuario.cep, usuario.cpf, usuario.endereco, usuario.cartao, usuario.validade, usuario.codigo,  usuario.id))
    conexao.commit() 
    conexao.close()           

########## DELETAR USUARIO DO DB ##########
def deletar_usuario(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM USUARIO WHERE id={}".format(id))
    conexao.commit()
    conexao.close()    

########## FUNÇÃO AUXILIAR PARA BUSCAR USUÁRIO POR ID → USADA NAS FUNÇÕES DE ALTERAR E DELETAR ##########
def buscar_usuario_por_id(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM USUARIO WHERE id ={}'.format(id))
    c = Usuario()
    for i in cursor.fetchall():
        c.id = i[0]
        c.nome = i[1]
        c.cep = i[2]
        c.cpf = i[3]
        c.endereco = i[4]
        c.cartao = i[5]
        c.validade = i[6]
        c.codigo = i[7]
    conexao.close()
    return c

########## LISTAR USUARIOS DO DB ##########
def listar_usuarios_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae13", passwd="grupo08", database="zuplae13")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM USUARIO")
    lista_usuario = []
    for i in cursor.fetchall():
        usuario = Usuario()
        usuario.id = i[0]
        usuario.nome = i[1]
        usuario.cep = i[2]
        usuario.cpf = i[3]
        usuario.endereco = i[4]
        usuario.cartao = i[5]
        usuario.validade = i[6]
        usuario.codigo = i[7]
        lista_usuario.append(usuario)
    conexao.close()
    return lista_usuario  

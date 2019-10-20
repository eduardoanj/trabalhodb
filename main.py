from flask import Flask, render_template, request, redirect
from usuarios import Usuario, salvar_usuario_db, deletar_usuario, buscar_usuario_por_id, alterar_usuario_db, listar_usuarios_db
from itens import Itens, salvar_item_db, listar_itens_db, deletar_item
from planos import Planos, listar_planos_db, salvar_plano_db
import MySQLdb



app = Flask(__name__)

########## INDEX ##########
@app.route('/')
def inicio():
    return render_template('index.html')

########## TELA DE CADASTRO ##########
@app.route('/juntese')
def junte():
    return render_template('juntese.html') 

########## CADASTRAR USUARIO ##########
@app.route('/usuario/salvar', methods = ['POST'])
def salvar():
    nome = request.form['nome']
    cep = request.form['cep']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    cartao = request.form['cartao']
    validade = request.form['validade']
    codigo = request.form['codigo']

    usuario = Usuario()
    usuario.nome = nome 
    usuario.cep = cep
    usuario.cpf = cpf
    usuario.endereco = endereco
    usuario.cartao = cartao
    usuario.validade = validade
    usuario.codigo = codigo  

    salvar_usuario_db(usuario)

    return redirect('/lista_usuario')

########## ALTERAR USUARIO ##########

@app.route('/usuario/alterar')
def usuario_alterar():
    id = request.args['id']    
    usuario = buscar_usuario_por_id(id)
    return render_template('alterar_usuario.html', usuario=usuario)

@app.route('/usuario/alterar/salvar', methods=['POST'])
def usuario_alterar_salvar():
    id = request.form['id']
    nome = request.form['nome']
    cep = request.form['cep']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    cartao = request.form['cartao']
    validade = request.form['validade']
    codigo = request.form['codigo']

    usuario = Usuario()
    usuario.id = id
    usuario.nome = nome 
    usuario.cep = cep
    usuario.cpf = cpf
    usuario.endereco = endereco
    usuario.cartao = cartao
    usuario.validade = validade
    usuario.codigo = codigo 
    alterar_usuario_db(usuario)

    return redirect ('/lista_usuario')   

########## DELETAR USUARIO ##########
@app.route('/usuario/delete')
def usuario_deletar():
    id = request.args['id']
    deletar_usuario(id)
    return redirect ('/lista_usuario')



########## LISTAR USUARIOS ##########
@app.route('/lista_usuario')
def lista_usuario():
    lista = listar_usuarios_db()
    return render_template('lista_usuario.html', lista = lista)  




########## CADASTRAR ITEM ##########
@app.route('/itens_cadastro')
def itens_cadastro():
    return render_template('itens_cadastro.html') 

@app.route('/item/salvar', methods = ['POST'])
def salvar_item():
    nome = request.form['nome']
    quantidade = request.form['quantidade']

    item = Itens()
    item.nome = nome
    item.quantidade = quantidade

    salvar_item_db(item.nome, item.quantidade)

    return redirect('/lista_itens')



########## LISTAR ITENS ##########
@app.route('/lista_itens')
def lista_itens():
    lista = listar_itens_db()
    return render_template('lista_itens.html', lista = lista)    

########## DELETAR ITEM ##########
@app.route('/item/delete')
def item_deletar():
    id = request.args['id']
    deletar_item(id)
    return redirect ('/lista_itens')


########## PLANOS ##########
@app.route('/selec_plano')
def seleciona_plano():
    lista = listar_usuarios_db()
    lista_planos = listar_planos_db()
    return render_template('selec_plano.html', lista_planos = lista_planos, lista = lista, )

@app.route('/plano/salvar', methods = ['POST'])
def salvar_plano():
    nome = request.form['nome']
    plano = request.form['plano']

    plano = Planos()
    plano.usuario_id = nome
    plano.plano_id = plano

    salvar_plano_db(plano.usuario_id, plano.plano_id)

    return redirect('/lista_usuario')    

########## PROJETO ##########

@app.route('/projeto')
def projeto():
    return render_template('o_projeto.html') 



app.run()
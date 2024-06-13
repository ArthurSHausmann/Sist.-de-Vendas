from databasevendas import db, Pedido, Produto, BaseModel, Clientes, Fornecedor, MercadoriaComprada, Compra
import inquirer
from tkinter import *
import requests


#CONEXÃO COM O ARQUIVO DE BANCO DE DADOS
db.connect()
db.create_tables([Pedido, BaseModel, Clientes, Fornecedor, MercadoriaComprada, Compra, Produto])

#DECLARAÇÃO DE VARIAVEIS
cli = 0
forn = 0
questions = 0
questions1 = 0
answers = 0
amswers1 = 0
prod = 0
produtonome = 0
informacoescompra = 0
nomeadd = 0
cpfadd =   0
emailadd = 0
telefoneadd = 0
enderecoadd = 0

#MENU PRINCIAPAL  
def main():
    print ('============================================================================')
    questions = [
    inquirer.List("Opção selecionada:",message="Selecione o que deseja fazer",
                    choices=['Clientes', 
                             'Fornecedor',
                             'Produtos',
                             'Realizar uma compra de material(Temporariamente indisponivel)', 
                             'Realizar uma venda de material(Temporariamente indisponivel)'])]
                    
    answers = inquirer.prompt(questions)
    if answers == {'Opção selecionada:': 'Clientes'}:
        MenuCadastroCliente()
    elif answers == {'Opção selecionada:': 'Fornecedor'}:
        MenuCadastroFornecedor()
    elif answers == {'Opção selecionada:': 'Produtos'}:
        MenuCadastroProduto()
    elif answers == {'Opção selecionada:': 'Realizar uma compra de material(Temporariamente indisponivel)'}:
        CompraMaterial()
    elif answers == {'Opção selecionada:': 'Realizar uma venda de material(Temporariamente indisponivel)'}:
        VendaMaterial()


#MENU DE GERENCIAMENTO DE CLIENTES
def MenuCadastroCliente():
    print ('==================================================================')
    questions = [
    inquirer.List("Opção selecionada:",message="Selecione o que deseja fazer",
                    choices=['Cadastrar cliente', 'Consultar cliente', 'Voltar ao menu anterior'])]
    answers3 = inquirer.prompt(questions)
    if answers3 == {'Opção selecionada:': 'Cadastrar cliente'}:
        CadastroCliente()
    elif answers3 == {'Opção selecionada:': 'Consultar cliente'}:
        ConsultarCliente()
    elif answers3 == {'Opção selecionada:': 'Voltar ao menu anterior'}:
        main()

#FUNÇÃO PARA CONSULTAR OS CLIENTES
def ConsultarCliente():
    lista_cliente = Clientes.select()
    print("Listando clientes:")
    for c in lista_cliente:
        print ("-", c.id, c.nome)
    print("Para voltar ao menu anterior digite 0")
    Consulta = int(input("Ou digite o ID do cliente que deseja visualizar:\n"))
    if Consulta == 0:
        MenuCadastroCliente()
    else:
        pass
    cliente1 = Clientes.get(Clientes.id == Consulta)
    print ("==================================================================",
           "\nNOME DO USUARIO:",cliente1.nome,
           "\nCPF/CNPJ DO USUARIO:", cliente1.cpf, 
           "\nE-MAIL DO USUARIO:", cliente1.email,
           "\nTELEFONE DO CLIENTE:", cliente1.telefone,
           "\nENDEREÇO DO CLIENTE:", cliente1.Endereco,
           "\n==================================================================")
    MenuCadastroCliente()

#FUNÇÃO PARA CADASTRAR UM CLIENTE
def CadastroCliente():
    global cli
    cli = Clientes.create(nome=input('Digite o nome do cliente a ser adicionado:\n').upper(), 
                          email=input('Digite o e-mail do cliente:\n').upper(),
                          cpf = int(input('Digite o CPF:\n')),
                          telefone = int(input('digite o seu telefone: \n')),
                          Endereco=input('Digite o endereço:\n'))
    print('O Cliente', cli.nome, 'foi cadastrado!')
    main()

#FUNÇÃO DE GERENCIAMENTO DE FORNECEDORES
def MenuCadastroFornecedor():
    print ('============================================================================')
    questions = [
    inquirer.List("Opção selecionada:",message="Selecione o que deseja fazer",
                    choices=['Cadastrar fornecedor', 'Consultar fornecedor', 'Voltar ao menu anterior'])]
    answers3 = inquirer.prompt(questions)
    if answers3 == {'Opção selecionada:': 'Cadastrar fornecedor'}:
        CadastroFornecedor()
    elif answers3 == {'Opção selecionada:': 'Consultar fornecedor'}:
        ConsultarFornecedor()
    elif answers3 == {'Opção selecionada:': 'Voltar ao menu anterior'}:
        main()

#FUNÇÃO PARA CADASTRAR UM FORNECEDOR
def CadastroFornecedor():
    global forn
    forn = Fornecedor.create(nome=input('Digite o nome do fornecedor a ser adicionado:\n').upper(), 
                             email=input('Digite o e-mail do fornecedor:\n').upper(),
                             cnpj= int(input('Digite o CNPJ:\n')),
                             telefone = int(input('digite um contato da empresa: \n')),
                             endereco=input('Digite o endereço:\n'))
    print('O Fornecedor', forn.nome, 'foi cadastrado!')
    main()

#FUNÇÃO PARA CONSULTAR UM FORNECEDOR
def ConsultarFornecedor():
    lista_fornecedor = Fornecedor.select()
    print("Listando Fornecedores:")
    for f in lista_fornecedor:
        print ("-", f.id, f.nome)
    print("Para voltar ao menu anterior digite 0")
    Consulta1 = int(input("Ou digite o ID do fornecedor que deseja visualizar:\n"))
    if Consulta1 == 0:
        MenuCadastroFornecedor()
    else:
        pass
    fornecedor1 = Fornecedor.get(Fornecedor.id == Consulta1)
    print ("==================================================================",
           "\nNOME DO USUARIO:",fornecedor1.nome,
           "\nCPF/CNPJ DO USUARIO:", fornecedor1.cnpj, 
           "\nE-MAIL DO USUARIO:", fornecedor1.email,
           "\nTELEFONE DO CLIENTE:", fornecedor1.telefone,
           "\nENDEREÇO DO CLIENTE:", fornecedor1.endereco,
           "\n==================================================================")
    MenuCadastroFornecedor()



#FUNÇÃO PARA GERENCIAMENTO DE PRODUTOS
def MenuCadastroProduto():
    print ('==================================================================')
    questions = [
    inquirer.List("Opção selecionada:",message="Selecione o que deseja fazer",
                    choices=['Cadastrar Produto', 'Consultar Produto', 'Voltar ao menu anterior'])]
    answers3 = inquirer.prompt(questions)
    if answers3 == {'Opção selecionada:': 'Cadastrar Produto'}:
        CadastroDeProduto()
    elif answers3 == {'Opção selecionada:': 'Consultar Produto'}:
        ConsultarProduto()
    elif answers3 == {'Opção selecionada:': 'Voltar ao menu anterior'}:
        main()

#FUNÇÃO PARA CONSULTAR UM PRODUTO
def ConsultarProduto():
    lista_produtos = Produto.select()
    print("Listando Produtos:")
    for p in lista_produtos:
        print ("-", p.id, p.nome)
    print("Para voltar ao menu anterior digite 0")
    Consulta1 = int(input("Ou digite o ID do Produto que deseja visualizar:\n"))
    if Consulta1 == 0:
        MenuCadastroProduto()
    else:
        pass
    produto1 = Produto.get(Produto.id == Consulta1)
    print ("==================================================================",
           "\nNOME DO USUARIO:",produto1.nome,
           "\nVALOR DO PRODUTO:", produto1.valor_unitario, 
           "\nQUANTIDADE EM ESTOQUE:", produto1.quantidade_estoque,
           "\n==================================================================")
    MenuCadastroFornecedor()

#FUNÇÃO PARA CADASTRAR UM PRODUTO
def CadastroDeProduto():
    global prod
    prod = Produto.create(nome=input('Digite o nome do produto:\n').upper(), 
                          valor_unitario = bool(input('Digite o Valor do item:\n')),
                          quantidade_estoque = int(input('Digite a quantidade de items em estoque: \n')))
    print('O Produto', prod.nome, 'foi cadastrado!')
    main()         

#FUNÇÃO PARA COMPRA DE MATERIAL
def CompraMaterial():
    global produtonome
    produtosdisposniveis = Produto.select()
    fornecedoresdisponiveis = Fornecedor.select()
    print ("Listando fornecedores disponiveis:")
    for f in fornecedoresdisponiveis:
        print ('-',f.id, f.nome, "CNPJ:",f.cnpj)
    fornecedorescolhido = int(input ("Selecione o ID do fornecedor que deseja realizar a compra: \n"))
    x = Fornecedor.get(Fornecedor.id == fornecedorescolhido)
    print ("Agora selecione o produto que deseja comprar")
    for p in produtosdisposniveis:
        print ('-', p.id, p.nome, "Quantidades disponiveis:",p.quantidade_estoque, "Valor por unidade:", "R$",p.valor_unitario)
    informacoescompra = int(input("Digite o ID do produto que deseja comprar: \n"))
    z = Produto.get(Produto.id == informacoescompra)

    quantidadecomprada = int(input("Agora digite a quantidade de produtos que deseja comprar:\n"))
    if quantidadecomprada <= Produto.quantidade_estoque:
        print ("Você vai comprar",quantidadecomprada,"unidades do produto",z.nome,"da empresa",x.nome)
        print ("Seu total é de:",quantidadecomprada*z.valor_unitario)
        question = inquirer.List("Opção selecionada:", message='Deseja confirmar a compra?', choices= ["Sim", "Retornar"])
        answers3 = inquirer.prompt(questions)
        if answers3 == {'Opção selecionada:': "Sim"}:
            print ("Compra efetuada com sucesso!" )    
        else:
            print ("Retornando ao menu princiapl")
            main()


def VendaMaterial():
    print ("Voce selecionou Venda de material")

#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
#############################################################################################################################################
###################################### SESSÃO PARA MOSTRAR A INTERFACE GRAFICA ##############################################################

#INTERFACE GRAFICA
def mainJanela():
    janela =Tk()
    janela.title("SISTEMA DE VENDAS")
    janela.geometry("800x600")
    texto_orientacao = Label(janela, text="Selecione o que deseja fazer")
    texto_orientacao.grid(column=5, row=0, padx=30, pady=5)
    texto_inicial = Label(janela, text=" ")
    texto_inicial.grid(column=0, row=0)

    #BOTOES DA TELA INICIAL
    botao = Button(janela, text="Clientes", command= abrirjanelaCliente)
    botao1 = Button(janela, text="Fornecedores", command=abrirjanelaFornecedor)
    botao2 = Button(janela, text="Produtos", command=abrirjanelaPrdouto)
    botao3 = Button(janela, text="Realizar uma compra de material",command=abrirjanelaCompra)
    botao4 = Button(janela, text="Realizar uma venda de material",command=abrirjanelaVenda)

    botao.grid(column=5, row=1, padx=30, pady=5)
    botao1.grid(column=5, row=3, padx=30, pady=5)
    botao2.grid(column=5, row=5, padx=30, pady=5)
    botao3.grid(column=5, row=7, padx=30, pady=5)
    botao4.grid(column=5, row=9, padx=30, pady=5)




    texto_funcao = Label(janela, text=" ")
    texto_funcao.grid(column=3, row = 13, padx=30, pady=5)
    #texto_funcao["text"] = 
    janela.mainloop()

#BOTAO CLIENTE
def abrirjanelaCliente():

    janela = Tk()
    janela.title("MENU DE GERENCIAMENTO DE CLIENTES")
    janela.geometry("800x600")
    texto_top_page = Label(janela, text="Você selecionou a aba de gerenciamento de clientes, selecione o que deseja fazer")
    texto_top_page.grid (column=1, row=0, padx=30, pady=5)
    botaoCadCliente = Button(janela, text="Cadastrar um cliente", command=TelaCadCliente)
    botaoCadCliente.grid(column=1, row=2)

    BotaoconsultaCliente = Button(janela, text="Consultar cliente", command=ConsultaCliente)
    BotaoconsultaCliente.grid (column=1, row=4, pady=5)
                               
    janela.mainloop()
def ConsultaCliente():
    janela=Tk()
    janela.title("CONSULTA DE CLIENTES")
    janela.geometry("800x600")
    lista_clientescad = Clientes.select()
    cad = Clientes.nome
    cadcpf = Clientes.cpf
    textoescrito = Label(janela,text="Lista de clientes")
    textoescrito.grid(column=8, row=2)
    button = Button(janela, text="Atualizar")
    button.grid(column=8, row=5)
    lcd=Listbox(janela)
    lpf=Listbox(janela)
    lem=Listbox(janela)
    ltf=Listbox(janela)
    lend=Listbox(janela)
    for cad in lista_clientescad:
        lcd.insert(END,cad)
    for cadcpf in lista_clientescad:
        lpf.insert(END,cadcpf)
    for cademail in lista_clientescad:
        lem.insert(END,cademail)
    for cadtf in lista_clientescad:
        ltf.insert(END,cadtf)
    for cadend in lista_clientescad:
        lend.insert(END,cadend)

    lcd.pack()

    #INSERÇÃO DE INFORMAÇÕES DOS CLIENTES
def TelaCadCliente():
    global nomeadd
    global emailadd
    global telefoneadd
    global cpfadd
    global enderecoadd
    janela = Tk()
    janela.title("CADASTRO DE CLIENTE")
    janela.geometry("800x600")
    texto = Label(janela, text="INSERIR OS DADOS DO CLIENTE")
    texto.grid (column=2, row=1, pady=5)
    textoNome = Label(janela, text="DIGITE O NOME DO CLIENTE")
    textoNome.grid (column=1, row=2, pady=5)
    nomeadd = Entry(janela, width=70).grid(column=2, row=2, pady=5)
    textoCPF = Label(janela, text="DIGITE O CPF DO CLIENTE")
    textoCPF.grid(column=1, row=4, pady=5)
    cpfadd = Entry(janela, width=70).grid(column=2, row=4, pady=5)
    textoEMAIL = Label(janela, text="DIGITE O EMAIL DO CLIENTE")
    textoEMAIL.grid(column=1, row=6, pady=5)
    emailadd = Entry(janela, width=70).grid(column=2, row=6, pady=5)
    textoTELEFONE=Label(janela, text="DIGITE O TELEFONE DO CLIENTE")
    textoTELEFONE.grid(column=1, row=8, pady=5)
    telefoneadd=Entry(janela, width=70).grid(column=2, row=8, pady=5)
    texto_endereco = Label(janela, text="DIGITE O ENDERECO DO CLIENTE")
    texto_endereco.grid(column=1, row=10, pady=5)
    enderecoadd = Entry(janela, width=70).grid(column=2, row=10, pady=5)

    bottaoenviar = Button(janela,width=70, text="Confirmar cadastro do cliente", justify='center', command=AddCadCliente)
    bottaoenviar.grid(column=2, row=12, pady=5)

    janela.mainloop()

def AddCadCliente():
    global nomeadd
    global emailadd
    global telefoneadd
    global cpfadd
    global enderecoadd
    Clientes.create(nome = nomeadd, cpf=cpfadd, email=emailadd, telefone=telefoneadd, endereco=enderecoadd)
    janela = Tk()
    janela.title("CADASTRO DE CLIENTEO")
    texto = Label(text="CADASTRO DE CLIENTE EFETUADO COM SUCESSO")
    texto.grid(justify='center')
    
    janela.mainloop()
    #BOTAO FORNECEDOR
def abrirjanelaFornecedor():
    janela = Tk()
    janela.title("MENU DE GERENCIAMENTO DE FORNECEDORES")
    janela.geometry("800x600")
    texto_top_page = Label(janela, text="Você selecionou a aba de gerenciamento de fornecedores, selecione o que deseja fazer")
    texto_top_page.grid (column=1, row=0, padx=30, pady=5)
    
    janela.mainloop()
    
#BOTAO PRODUTO
def abrirjanelaPrdouto():
    janela = Tk()
    janela.title("MENU DE GERENCIAMENTO DE PRODUTOS")
    janela.geometry("800x600")
    texto_top_page = Label(janela, text="Você selecionou a aba de gerenciamento de produtos, selecione o que deseja fazer")
    texto_top_page.grid (column=1, row=0, padx=30, pady=5)


    janela.mainloop()

    #BOTAO COMPRA
def abrirjanelaCompra():
    janela = Tk()
    janela.title("MENU DE COMPRAS")
    janela.geometry("800x600")
    texto_top_page = Label(janela, text="Você selecionou a aba de compras")
    texto_top_page.grid (column=1, row=0, padx=30, pady=5)



    janela.mainloop()
    
     #BOTAO VENDAS
def abrirjanelaVenda():
    janela = Tk()
    janela.title("MENU DE VENDAS")
    janela.geometry("600x600")
    texto_top_page = Label(janela, text="Você selecionou a aba de vendas")
    texto_top_page.grid (column=1, row=0, padx=30, pady=5)
    botao = Button(janela, text="Realizar uma compra") #command=MenuCompra)


    janela.mainloop()
    


mainJanela() 

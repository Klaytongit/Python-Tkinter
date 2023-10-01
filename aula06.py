from tkinter import * #Chamando a biblioteca tkinter e tudo que contém
from tkinter import ttk #Chamando a biblioteca tkinter e importando ttk(Grid) 

root = Tk() #Criando uma variavel para receber Tkinter

class Aplicacao(): #Criando uma classe
    def __init__(self): #Criando funções automáticas
        self.root = root 
        self.tela()
        self.frames_de_tela()
        self.widgets_frame_1()
        self.lista_frame_2()
        root.mainloop() #Loop para manter a tela visível 
    def tela(self): #Criando funções de configuração de tela
        self.root.title("Cadastro de Clientes") #Título
        self.root.configure(background= '#008080') #Cor de fundo
        self.root.geometry('700x500') #Tamanho de inicialização de tela
        self.root.resizable(True, True) # Responsividade
        self.root.maxsize(width= 900, height=700) #Maximo tamanho da tela    
        self.root.minsize(width=400, height=300) #Minimo tamanho da tela
    def frames_de_tela(self): #Criando frames
        self.frame_1 = Frame(self.root, bd= 1, bg= '#F8F8FF', highlightbackground= '#008B8B', 
                             highlightthickness= 3) #Configuração frame_1
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd= 1, bg= '#F8F8FF', highlightbackground= '#008B8B', 
                             highlightthickness= 3) #Configuração frame_2
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)
    def widgets_frame_1(self): #Criando botões dentro do fram_1
        #Botão Limpar
        self.bt_limpar = Button(self.frame_1, text= "Limpar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Buscar
        self.bt_buscar = Button(self.frame_1, text= "Buscar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Novo
        self.bt_novo = Button(self.frame_1, text= "Novo", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_novo.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Alterar
        self.bt_alterar = Button(self.frame_1, text= "Alterar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_alterar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)
        #Botão Apagar
        self.bt_apagar = Button(self.frame_1, text= "Apagar", bg= '#008080', font = ('verdana', 8, 'bold'), bd= 2)
        self.bt_apagar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        #Criação da label "Código"
        self.lb_codigo = Label(self.frame_1, text= "Código", bg= '#F8F8FF', font = ('verdana', 8, 'bold'))
        self.lb_codigo.place(relx= 0.05, rely= 0.05)
        #Criação do input do label "Código"
        self.codigo_entry = Entry(self.frame_1, bg= '#008080', font=('verdana', 8, 'bold', 'italic'))
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.07)

        #Criação da label "Nome"
        self.lb_nome = Label(self.frame_1, text= "Nome", bg= '#F8F8FF', font = ('verdana', 8, 'bold'))
        self.lb_nome.place(relx= 0.05, rely= 0.35)
        #Criação do input do label "Nome"
        self.nome_entry = Entry(self.frame_1, bg= '#008080', font=('verdana', 8, 'bold', 'italic'))
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.7)

        #Criação da label "Telefone"
        self.lb_telefone = Label(self.frame_1, text= "Telefone", bg= '#F8F8FF', font = ('verdana', 8, 'bold'))
        self.lb_telefone.place(relx= 0.05, rely= 0.6)
        #Criação do input do label "Telefone"
        self.telefone_entry = Entry(self.frame_1, bg= '#008080', font=('verdana', 8, 'bold', 'italic'))
        self.telefone_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.4)

        #Criação da label "Cidade"
        self.lb_cidade = Label(self.frame_1, text= "Cidade", bg= '#F8F8FF', font = ('verdana', 8, 'bold'))
        self.lb_cidade.place(relx= 0.5, rely= 0.6)
        #Criação do input do label "Cidade"
        self.cidade_entry = Entry(self.frame_1, bg= '#008080', font=('verdana', 8, 'bold', 'italic'))
        self.cidade_entry.place(relx= 0.5, rely= 0.7, relwidth= 0.4)
    def lista_frame_2(self): #Cliando a função grid
        self.lista_clientes = ttk.Treeview(self.frame_2, height= 3, columns=('col1', 'col2', 'col3', 'col4')) #Especificando a quantidade de colunas da grid
        self.lista_clientes.heading('#0', text="") #Criando uma coluna vazia
        self.lista_clientes.heading('#1', text="Código") #Descrevendo a coluna
        self.lista_clientes.heading('#2', text="Nome") #Descrevendo a coluna
        self.lista_clientes.heading('#3', text="Telefone") #Descrevendo a coluna
        self.lista_clientes.heading('#4', text="Cidade") #Descrevendo a coluna

        #Configurando o tamanho de cada coluna dentro da grid
        self.lista_clientes.column('#0', width= 1) 
        self.lista_clientes.column('#1', width= 50)
        self.lista_clientes.column('#2', width= 200)
        self.lista_clientes.column('#3', width= 125)
        self.lista_clientes.column('#4', width= 125)

        #Configurando as posições das colunas
        self.lista_clientes.place(relx= 0.01, rely= 0.1, relwidth= 0.95, relheight= 0.85)

        #Criando um scrool na grid
        self.scroollista = Scrollbar(self.frame_2, orient= 'vertical') #Direcionando o scrool para o frame_2
        self.lista_clientes.configure(yscroll=self.scroollista.set) #Direcionando o scrool para a grid
        self.scroollista.place(relx= 0.96, rely= 0.1, relwidth= 0.04, relheight= 0.85) #Configurando o scrool na grid

Aplicacao() #Chamando a classe com suas funções


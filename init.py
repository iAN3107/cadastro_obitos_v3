from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import pymysql
from threading import Timer
from PIL import ImageTk, Image

conexao = pymysql.connect(
host = '192.168.0.19',
user = 'ian2',
passwd = 'password'
)    
c = conexao.cursor()

c.execute("USE cemiterio;")


class GUI:
    def __init__(self, master=None):
        self.botao = Frame(master)
        self.botao.pack()

        self.photo = Image.open("logo.jpg")
        self.photo = ImageTk.PhotoImage(self.photo)  

        self.lb_label = Label(self.botao, image = self.photo)
        self.lb_label.image = self.photo
        self.lb_label.pack()

        self.btn_inserir = Button(self.botao, text='INSERIR', command=self.insere)
        self.btn_inserir.pack(side=LEFT, ipadx=22, ipady=15)

        self.btn_buscar = Button(self.botao, text='BUSCAR', command=self.buscar)
        self.btn_buscar.pack(side=RIGHT,ipadx=22, ipady=15)

    def remove_banco(self):
        self.conexao = pymysql.connect(
        host = '192.168.0.19',
        user = 'ian2',
        passwd = 'password'
        )
        c = self.conexao.cursor()
        c.execute("USE cemiterio;")
        
        self.Resultado.delete(1.0,END)
        if (self.entBusca.get() != "" and self.entBusca2.get() != "" and self.entBusca3.get() != ""):
            c.execute("DELETE FROM cemiterio WHERE(Nome = '" + self.entBusca.get().lower() +"' and DataFalecimento = '"+ self.entBusca2.get().lower() +"' and NumSepultura = '"+ self.entBusca3.get().lower() +"');")
        
        elif (self.entBusca.get() != "" and self.entBusca2.get() != ""):
            c.execute("DELETE FROM cemiterio WHERE(Nome = '" + self.entBusca.get().lower() +"' and DataFalecimento = '"+ self.entBusca2.get().lower() +"');")
        
        elif (self.entBusca.get() != ""):
            c.execute("DELETE FROM cemiterio WHERE(Nome = '" + self.entBusca.get().lower() +"');")
        self.conexao.commit()

        c.close()

    def busca_avancada(self):
        self.jan2=Toplevel()

        self.jan2.geometry("400x625")

        self.buscaa = Frame(self.jan2)
        self.buscaa.pack()

        self.buscaa2 = Frame(self.jan2)
        self.buscaa2.pack()

        self.buscaa3 = Frame(self.jan2)
        self.buscaa3.pack()

        self.button = Frame(self.jan2)
        self.button.pack()

        self.caixaTextoo = Frame(self.jan2)
        self.caixaTextoo.pack()

        self.lblBuscaa = Label(self.buscaa, text="Buscar por: ")
        self.lblBuscaa.pack()

        
        self.cbBuscaa = Combobox(self.buscaa, values=[
            "",
            "NumObito",
            "NumSepultura",
            "NomeContribuinte",
            "Nome",
            "Idade",
            "Pai",
            "Mae",
            "Natural",
            "CausaMorte",
            "DataFalecimento",
            "InumadoSepultura",
            "Cemiterio",
            "Quadra",
            "Livro",
            "Folha"
        ], state="readonly")
        self.cbBuscaa.current()
        self.cbBuscaa.pack(side=LEFT)
        
        self.entBuscaa = Entry(self.buscaa)
        self.entBuscaa.pack(padx=10)
        
        self.cbBuscaa2 = Combobox(self.buscaa2, values=[
            "",
            "NumObito",
            "NumSepultura",
            "NomeContribuinte",
            "Nome",
            "Idade",
            "Pai",
            "Mae",
            "Natural",
            "CausaMorte",
            "DataFalecimento",
            "InumadoSepultura",
            "Cemiterio",
            "Quadra",
            "Livro",
            "Folha"
        ], state="readonly")
        self.cbBuscaa2.current()
        self.cbBuscaa2.pack(side=LEFT)

        self.entBuscaa2 = Entry(self.buscaa2)
        self.entBuscaa2.pack(padx=10)

        self.cbBuscaa3 = Combobox(self.buscaa3, values=[
            "",
            "NumObito",
            "NumSepultura",
            "NomeContribuinte",
            "Nome",
            "Idade",
            "Pai",
            "Mae",
            "Natural",
            "CausaMorte",
            "DataFalecimento",
            "InumadoSepultura",
            "Cemiterio",
            "Quadra",
            "Livro",
            "Folha"
        ], state="readonly")
        self.cbBuscaa3.current()
        self.cbBuscaa3.pack(side=LEFT)

        self.entBuscaa3 = Entry(self.buscaa3)
        self.entBuscaa3.pack(padx=10)

        self.btnBuscaa = Button(self.button, text="Buscar", command=self.busca_banco_avancado)
        self.btnBuscaa.pack(side=BOTTOM, pady=5)

        self.jan2.iconbitmap('images\icon.ico')
        self.jan2.title('Consulta de Obitos')

        self.Resultaado = scrolledtext.ScrolledText(self.caixaTextoo,width=45,height=35)
        self.Resultaado.pack()
    
        self.jan2.transient(pagina)#
    
        self.jan2.focus_force()#
            
        self.jan2.grab_set()#




    def buscar(self):
        self.jan=Toplevel()

        self.jan.geometry("400x625")

        self.busca = Frame(self.jan)
        self.busca.pack()

        self.busca2 = Frame(self.jan)
        self.busca2.pack()

        self.busca3 = Frame(self.jan)
        self.busca3.pack()

        self.button = Frame(self.jan)
        self.button.pack()

        self.caixaTexto = Frame(self.jan)
        self.caixaTexto.pack()
        
        self.cbBusca = Label(self.busca, text="Nome: ")
        self.cbBusca.pack()
        
        self.entBusca = Entry(self.busca)
        self.entBusca.pack()
        
        self.cbBusca2 = Label(self.busca2, text= "Data: ")
        self.cbBusca2.pack()

        self.entBusca2 = Entry(self.busca2)
        self.entBusca2.pack()

        self.cbBusca3 = Label(self.busca3, text="Nº Perpetua: ")
        self.cbBusca3.pack()

        self.entBusca3 = Entry(self.busca3)
        self.entBusca3.pack()

        self.btnBusca = Button(self.button, text="Buscar", command=self.buscar_banco)
        self.btnBusca.pack(side=LEFT, pady=5, padx=5)

        self.btnRemove = Button(self.button, text="Remover", command=self.remove_banco)
        self.btnRemove.pack(side=LEFT, pady=5,)

        self.btnBuscaAvnc = Button(self.button, text="Avançado", command=self.busca_avancada)
        self.btnBuscaAvnc.pack(side=RIGHT, padx=5, pady=5)

        self.jan.iconbitmap('images\icon.ico')
        self.jan.title('Consulta de Obitos')

        self.Resultado = scrolledtext.ScrolledText(self.caixaTexto,width=45,height=35)
        self.Resultado.pack()
    
        self.jan.transient(pagina)#
    
        self.jan.focus_force()#
            
        self.jan.grab_set()#
    def busca_banco_avancado(self):
        self.conexao = pymysql.connect(
        host = '192.168.0.19',
        user = 'ian2',
        passwd = 'password'
        )         
        c = self.conexao.cursor()  
        c.execute("USE cemiterio;")
        self.Resultaado.delete(1.0,END)
        if (self.cbBuscaa.get() != "" and self.entBuscaa.get() != "" and self.cbBuscaa2.get() != "" and self.entBuscaa2.get() != "" and self.cbBuscaa3.get() != "" and self.entBuscaa3.get() != ""):
            c.execute("SELECT * FROM cemiterio WHERE(" + self.cbBuscaa.get() +" LIKE '%" + self.entBuscaa.get().higher() +"%' and "+ self.cbBuscaa2.get() +" LIKE '%"+ self.entBuscaa2.get().lower() +"%' and "+ self.cbBuscaa3.get() +" LIKE '%"+ self.entBuscaa3.get().lower() +"%');")
            
            for linha in c:
                
                
                self.Resultaado.insert(INSERT, "Numero do Obito: ", INSERT, linha[0], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Numero da Sepultura: ", INSERT, linha[1], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Nome: ", INSERT, linha[2], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Nome Contribuinte: ", INSERT, linha[3], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Idade: ", INSERT, linha[4], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Pai: ", INSERT, linha[5], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Mae: ", INSERT, linha[6], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Natural de: ", INSERT, linha[7], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Causa da Morte: ", INSERT, linha[8], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Data de Falecimento: ", INSERT, linha[9], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Inumado em Sepultura: ", INSERT, linha[10], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Cemiterio: ", INSERT, linha[11], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Quadra: ", INSERT, linha[12], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Livro: ", INSERT, linha[13], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Folha: ", INSERT, linha[14], INSERT, "\n")
                self.Resultaado.insert(INSERT, "\n \n")  

                               

        elif (self.cbBuscaa.get() != "" and self.entBuscaa.get() != "" and self.cbBuscaa2.get() != "" and self.entBuscaa2.get() != ""):
            c.execute("SELECT * FROM cemiterio WHERE(" + self.cbBuscaa.get() +" LIKE '%" + self.entBuscaa.get().upper()+"%' and "+ self.cbBuscaa2.get() +" LIKE '%"+ self.entBuscaa2.get().lower() +"%');")
            for linha in c:    
                self.Resultaado.insert(INSERT, "Numero do Obito: ", INSERT, linha[0], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Numero da Sepultura: ", INSERT, linha[1], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Nome: ", INSERT, linha[2], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Nome Contribuinte: ", INSERT, linha[3], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Idade: ", INSERT, linha[4], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Pai: ", INSERT, linha[5], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Mae: ", INSERT, linha[6], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Natural de: ", INSERT, linha[7], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Causa da Morte: ", INSERT, linha[8], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Data de Falecimento: ", INSERT, linha[9], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Inumado em Sepultura: ", INSERT, linha[10], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Cemiterio: ", INSERT, linha[11], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Quadra: ", INSERT, linha[12], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Livro: ", INSERT, linha[13], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Folha: ", INSERT, linha[14], INSERT, "\n")
                self.Resultaado.insert(INSERT, "\n \n")  
            

        elif (self.cbBuscaa.get() != "" and self.entBuscaa.get() != ""):
            c.execute("SELECT * FROM cemiterio WHERE(" + self.cbBuscaa.get() +" LIKE '%" + self.entBuscaa.get().lower() +"%');")
            for linha in c:    
                self.Resultaado.insert(INSERT, "Numero do Obito: ", INSERT, linha[0], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Numero da Sepultura: ", INSERT, linha[1], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Nome: ", INSERT, linha[2], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Nome Contribuinte: ", INSERT, linha[3], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Idade: ", INSERT, linha[4], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Pai: ", INSERT, linha[5], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Mae: ", INSERT, linha[6], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Natural de: ", INSERT, linha[7], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Causa da Morte: ", INSERT, linha[8], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Data de Falecimento: ", INSERT, linha[9], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Inumado em Sepultura: ", INSERT, linha[10], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Cemiterio: ", INSERT, linha[11], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Quadra: ", INSERT, linha[12], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Livro: ", INSERT, linha[13], INSERT, "\n")
                self.Resultaado.insert(INSERT, "Folha: ", INSERT, linha[14], INSERT, "\n")
                self.Resultaado.insert(INSERT, "\n \n")  
             
        c.close()
    def buscar_banco(self):
        self.conexao = pymysql.connect(
        host = '192.168.0.19',
        user = 'ian2',
        passwd = 'password'
        )       
        c = self.conexao.cursor()  
        c.execute("USE cemiterio;")
        self.Resultado.delete(1.0,END)
        if (self.entBusca.get() != "" and self.entBusca2.get() != "" and self.entBusca3.get() != ""):
            c.execute("SELECT * FROM cemiterio WHERE(Nome LIKE '%" + self.entBusca.get() +"%' and DataFalecimento LIKE '%"+ self.entBusca2.get() +"%' and NumSepultura LIKE '%"+ self.entBusca3.get() +"%');")
            
            for linha in c:
                
                
                self.Resultado.insert(INSERT, "Numero do Obito: ", INSERT, linha[0], INSERT, "\n")
                self.Resultado.insert(INSERT, "Numero da Sepultura: ", INSERT, linha[1], INSERT, "\n")
                self.Resultado.insert(INSERT, "Nome: ", INSERT, linha[2], INSERT, "\n")
                self.Resultado.insert(INSERT, "Nome Contribuinte: ", INSERT, linha[3], INSERT, "\n")
                self.Resultado.insert(INSERT, "Idade: ", INSERT, linha[4], INSERT, "\n")
                self.Resultado.insert(INSERT, "Pai: ", INSERT, linha[5], INSERT, "\n")
                self.Resultado.insert(INSERT, "Mae: ", INSERT, linha[6], INSERT, "\n")
                self.Resultado.insert(INSERT, "Natural de: ", INSERT, linha[7], INSERT, "\n")
                self.Resultado.insert(INSERT, "Causa da Morte: ", INSERT, linha[8], INSERT, "\n")
                self.Resultado.insert(INSERT, "Data de Falecimento: ", INSERT, linha[9], INSERT, "\n")
                self.Resultado.insert(INSERT, "Inumado em Sepultura: ", INSERT, linha[10], INSERT, "\n")
                self.Resultado.insert(INSERT, "Cemiterio: ", INSERT, linha[11], INSERT, "\n")
                self.Resultado.insert(INSERT, "Quadra: ", INSERT, linha[12], INSERT, "\n")
                self.Resultado.insert(INSERT, "Livro: ", INSERT, linha[13], INSERT, "\n")
                self.Resultado.insert(INSERT, "Folha: ", INSERT, linha[14], INSERT, "\n")
                self.Resultado.insert(INSERT, "\n \n")   

                               

        elif (self.entBusca.get() != "" and self.entBusca2.get() != ""):
            c.execute("SELECT * FROM cemiterio WHERE( Nome LIKE '%" + self.entBusca.get() +"%' and DataFalecimento LIKE '%"+ self.entBusca2.get() +"%');")
            for linha in c:    
                self.Resultado.insert(INSERT, "Numero do Obito: ", INSERT, linha[0], INSERT, "\n")
                self.Resultado.insert(INSERT, "Numero da Sepultura: ", INSERT, linha[1], INSERT, "\n")
                self.Resultado.insert(INSERT, "Nome: ", INSERT, linha[2], INSERT, "\n")
                self.Resultado.insert(INSERT, "Nome Contribuinte: ", INSERT, linha[3], INSERT, "\n")
                self.Resultado.insert(INSERT, "Idade: ", INSERT, linha[4], INSERT, "\n")
                self.Resultado.insert(INSERT, "Pai: ", INSERT, linha[5], INSERT, "\n")
                self.Resultado.insert(INSERT, "Mae: ", INSERT, linha[6], INSERT, "\n")
                self.Resultado.insert(INSERT, "Natural de: ", INSERT, linha[7], INSERT, "\n")
                self.Resultado.insert(INSERT, "Causa da Morte: ", INSERT, linha[8], INSERT, "\n")
                self.Resultado.insert(INSERT, "Data de Falecimento: ", INSERT, linha[9], INSERT, "\n")
                self.Resultado.insert(INSERT, "Inumado em Sepultura: ", INSERT, linha[10], INSERT, "\n")
                self.Resultado.insert(INSERT, "Cemiterio: ", INSERT, linha[11], INSERT, "\n")
                self.Resultado.insert(INSERT, "Quadra: ", INSERT, linha[12], INSERT, "\n")
                self.Resultado.insert(INSERT, "Livro: ", INSERT, linha[13], INSERT, "\n")
                self.Resultado.insert(INSERT, "Folha: ", INSERT, linha[14], INSERT, "\n")
                self.Resultado.insert(INSERT, "\n \n")   
            

        elif (self.entBusca.get() != ""):
            c.execute("SELECT * FROM cemiterio WHERE(Nome LIKE '%" + self.entBusca.get() +"%');")
            for linha in c:    
                self.Resultado.insert(INSERT, "Numero do Obito: ", INSERT, linha[0], INSERT, "\n")
                self.Resultado.insert(INSERT, "Numero da Sepultura: ", INSERT, linha[1], INSERT, "\n")
                self.Resultado.insert(INSERT, "Nome: ", INSERT, linha[2], INSERT, "\n")
                self.Resultado.insert(INSERT, "Nome Contribuinte: ", INSERT, linha[3], INSERT, "\n")
                self.Resultado.insert(INSERT, "Idade: ", INSERT, linha[4], INSERT, "\n")
                self.Resultado.insert(INSERT, "Pai: ", INSERT, linha[5], INSERT, "\n")
                self.Resultado.insert(INSERT, "Mae: ", INSERT, linha[6], INSERT, "\n")
                self.Resultado.insert(INSERT, "Natural de: ", INSERT, linha[7], INSERT, "\n")
                self.Resultado.insert(INSERT, "Causa da Morte: ", INSERT, linha[8], INSERT, "\n")
                self.Resultado.insert(INSERT, "Data de Falecimento: ", INSERT, linha[9], INSERT, "\n")
                self.Resultado.insert(INSERT, "Inumado em Sepultura: ", INSERT, linha[10], INSERT, "\n")
                self.Resultado.insert(INSERT, "Cemiterio: ", INSERT, linha[11], INSERT, "\n")
                self.Resultado.insert(INSERT, "Quadra: ", INSERT, linha[12], INSERT, "\n")
                self.Resultado.insert(INSERT, "Livro: ", INSERT, linha[13], INSERT, "\n")
                self.Resultado.insert(INSERT, "Folha: ", INSERT, linha[14], INSERT, "\n")
                self.Resultado.insert(INSERT, "\n \n")                
        c.close()

    def insere(self):

        self.insere=Toplevel()

        self.insere.geometry("275x530")
        
        self.NumObito = Frame(self.insere)
        self.NumObito["padding"] = 5
        self.NumObito.pack()

        self.NumRequerimento = Frame(self.insere)
        self.NumRequerimento["padding"] = 5
        self.NumRequerimento.pack()
        
        self.NumSepultura = Frame(self.insere)
        self.NumSepultura["padding"] = 5
        self.NumSepultura.pack()
        
        self.Nome = Frame(self.insere)
        self.Nome["padding"] = 5
        self.Nome.pack()

        self.NomeContribuinte = Frame(self.insere)
        self.NomeContribuinte["padding"] = 5
        self.NomeContribuinte.pack()

        self.Idade = Frame(self.insere)
        self.Idade["padding"] = 5
        self.Idade.pack()

        self.Pai = Frame(self.insere)
        self.Pai["padding"] = 5
        self.Pai.pack()

        self.Mae = Frame(self.insere)
        self.Mae["padding"] = 5
        self.Mae.pack()

        self.Natural = Frame(self.insere)
        self.Natural["padding"] = 5
        self.Natural.pack()
        
        self.CausaMorte = Frame(self.insere)
        self.CausaMorte["padding"] = 5
        self.CausaMorte.pack()

        self.DataFalecimento = Frame(self.insere)
        self.DataFalecimento["padding"] = 5
        self.DataFalecimento.pack()
        
        self.InumadoSepultura = Frame(self.insere)
        self.InumadoSepultura["padding"] = 5
        self.InumadoSepultura.pack()

        self.Cemiterio = Frame(self.insere)
        self.Cemiterio["padding"] = 5
        self.Cemiterio.pack()

        self.Quadra = Frame(self.insere)
        self.Quadra["padding"] = 5
        self.Quadra.pack()

        self.Livro = Frame(self.insere)
        self.Livro["padding"] = 0
        self.Livro.pack()
        
        self.Folha = Frame(self.insere)
        self.Folha["padding"] = 5
        self.Folha.pack()

        self.botao = Frame(self.insere)
        self.botao.pack()

        self.Msg = Frame(self.insere)
        self.Msg.pack()

        self.lblNumObito = Label(self.NumObito, text="Nº Obito: ", width=20).pack(side=LEFT)
        self.lblNumRequerimento = Label(self.NumRequerimento, text="Nº Requerimento: ", width=20).pack(side=LEFT)
        self.lblNumSepultura = Label(self.NumSepultura, text="Nº Sepultura: ", width=20).pack(side=LEFT)
        self.lblNome = Label(self.Nome, text="Nome: ", width=20).pack(side=LEFT)
        self.lblNomeContribuinte = Label(self.NomeContribuinte, text="Nome Contribuinte:", width=20).pack(side=LEFT)
        self.lblIdade = Label(self.Idade, text="Idade: ", width=20).pack(side=LEFT)
        self.lblPai = Label(self.Pai, text="Pai: ", width=20).pack(side=LEFT)
        self.lblMae = Label(self.Mae, text="Mãe: ", width=20).pack(side=LEFT)
        self.lblNatural = Label(self.Natural, text="Natural de: ", width=20).pack(side=LEFT)
        self.lblCausaMorte = Label(self.CausaMorte, text="Causa da Morte: ", width=20).pack(side=LEFT)
        self.lblDataFalecimento = Label(self.DataFalecimento, text="Data do Falecimento: ", width=20).pack(side=LEFT)
        self.lblInumadoSepultura = Label(self.InumadoSepultura, text="Inumado em Sepultura: ", width=22).pack(side=LEFT)
        self.lblCemiterio = Label(self.Cemiterio, text="Cemiterio: ", width=20).pack(side=LEFT)
        self.lblQuadra = Label(self.Quadra, text="Quadra: ", width=20).pack(side=LEFT)
        self.lblLivro = Label(self.Livro, text="Livro: ", width=20).pack(side=LEFT)
        self.lblFolha = Label(self.Folha, text="Folha: ", width=20).pack(side=LEFT)
 
        self.entNumObito = Entry(self.NumObito)
        self.entNumRequerimento = Entry(self.NumRequerimento)
        self.entNumSepultura = Entry(self.NumSepultura)
        self.entNome = Entry(self.Nome)
        self.entIdade = Entry(self.Idade)
        self.entPai = Entry(self.Pai)
        self.entMae = Entry(self.Mae)
        self.entNatural = Entry(self.Natural)
        self.entCausaMorte = Entry(self.CausaMorte)
        self.entDataFalecimento = Entry(self.DataFalecimento)
        self.entNomeContribuinte = Entry(self.NomeContribuinte)
        self.entInumadoSepultura = Entry(self.InumadoSepultura, width='18')
        self.entCemiterio = Entry(self.Cemiterio)
        self.entQuadra = Entry(self.Quadra)
        self.entLivro = Entry(self.Livro)
        self.entFolha = Entry(self.Folha)

        self.entNumObito.pack(side=LEFT)
        self.entNumRequerimento.pack(side=LEFT)
        self.entNumSepultura.pack(side=LEFT)
        self.entNome.pack(side=LEFT)
        self.entNomeContribuinte.pack(side=LEFT)
        self.entIdade.pack(side=LEFT)
        self.entPai.pack(side=LEFT)
        self.entMae.pack(side=LEFT)
        self.entNatural.pack(side=LEFT)
        self.entCausaMorte.pack(side=LEFT)
        self.entDataFalecimento.pack(side=LEFT)
        self.entInumadoSepultura.pack(side=LEFT)
        self.entCemiterio.pack(side=LEFT)
        self.entQuadra.pack(side=LEFT)
        self.entLivro.pack(side=LEFT)
        self.entFolha.pack(side=LEFT)

        self.btnInsere = Button(self.botao, text="Inserir", command=self.insere_banco)
        self.btnInsere.pack()

        self.lblMsg = Label(self.Msg, text="")
        self.lblMsg.pack()

        self.insere.transient(pagina)
    
        self.insere.focus_force()
            
        self.insere.grab_set()

        self.insere.iconbitmap('images\icon.ico')
        self.insere.title('Consulta de Obitos')

    def reset(self):
        self.lblMsg['text'] = ""
    
    def insere_banco(self):
        if (self.entNome.get().lower() == "" or self.entDataFalecimento.get().lower() == ""):
            self.lblMsg['text'] = 'O nome e a data não podem ser nulos!'
            self.lblMsg['foreground'] = "red"
            t = Timer(4, self.reset)
            t.start()

        else:
            try:
                self.conexao = pymysql.connect(
                host = '192.168.0.19',
                user = 'ian2',
                passwd = 'password'
                )    
                c = self.conexao.cursor()  
                c.execute("USE cemiterio;")
                c.execute("INSERT INTO cemiterio VALUES(\
                    '" + self.entNumObito.get().lower() + "',\
                    '" + self.entNumSepultura.get().lower() + "',\
                    '" + self.entNome.get().lower() + "',\
                    '" + self.entNomeContribuinte.get().lower() + "',\
                    '" + self.entIdade.get().lower() + "',\
                    '" + self.entPai.get().lower() + "',\
                    '" + self.entMae.get().lower() + "',\
                    '" + self.entNatural.get().lower() + "',\
                    '" + self.entCausaMorte.get().lower() + "',\
                    '" + self.entDataFalecimento.get().lower() + "',\
                    '" + self.entInumadoSepultura.get().lower() + "',\
                    '" + self.entCemiterio.get().lower() + "',\
                    '" + self.entQuadra.get().lower() + "',\
                    '" + self.entLivro.get().lower() + "',\
                    '" + self.entFolha.get().lower() + "');")

                self.conexao.commit()
                c.close()
                
                self.entNumObito.delete(0, END)
                self.entNumSepultura.delete(0, END)
                self.entNome.delete(0, END)
                self.entIdade.delete(0, END)
                self.entPai.delete(0, END)
                self.entMae.delete(0, END)
                self.entNatural.delete(0, END)
                self.entCausaMorte.delete(0, END)
                self.entDataFalecimento.delete(0, END)
                self.entNomeContribuinte.delete(0, END)
                self.entInumadoSepultura.delete(0, END)
                self.entCemiterio.delete(0, END)
                self.entQuadra.delete(0, END)
                self.entLivro.delete(0, END)
                self.entFolha.delete(0, END)
                self.lblMsg['text'] = 'Cadastrou'
                self.lblMsg['foreground'] = "green"
                t = Timer(4, self.reset)
                t.start()
            except:
                self.lblMsg['text'] = 'Ocorreu um erro no cadastro de Obito'
                self.lblMsg['foreground'] = "red"
                t = Timer(4, self.reset)
                t.start()


pagina = Tk()
pagina.iconbitmap('images\icon.ico')
pagina.title('Consulta de Obitos')

GUI(pagina)
pagina.mainloop()

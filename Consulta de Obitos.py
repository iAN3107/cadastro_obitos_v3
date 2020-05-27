from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import sqlite3
from threading import Timer
from PIL import ImageTk, Image

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
        self.btn_buscar.pack(side=LEFT,ipadx=22, ipady=15)

        self.btn_remover = Button(self.botao, text='REMOVER')
        self.btn_remover.pack(side=LEFT,ipadx=22,ipady=15)


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

        self.lblBusca = Label(self.busca, text="Buscar por: ")
        self.lblBusca.pack()

        
        self.cbBusca = Combobox(self.busca, values=[
            "",
            "NumObito",
            "NumSepultura",
            "Nome",
            "Idade",
            "Pai",
            "Mae",
            "Natural",
            "CausaMorte",
            "DataFalecimento",
            "DeclaradoPor",
            "InumadoSepultura",
            "Atestado",
            "Funcao",
            "Cemiterio",
            "Quadra",
            "Livro",
            "Folha"
        ], state="readonly")
        self.cbBusca.current()
        self.cbBusca.pack(side=LEFT)
        
        self.entBusca = Entry(self.busca)
        self.entBusca.pack(padx=10)
        
        self.cbBusca2 = Combobox(self.busca2, values=[
            "",
            "NumObito",
            "NumSepultura",
            "Nome",
            "Idade",
            "Pai",
            "Mae",
            "Natural",
            "CausaMorte",
            "DataFalecimento",
            "DeclaradoPor",
            "InumadoSepultura",
            "Atestado",
            "Funcao",
            "Cemiterio",
            "Quadra",
            "Livro",
            "Folha"
        ], state="readonly")
        self.cbBusca2.current()
        self.cbBusca2.pack(side=LEFT)

        self.entBusca2 = Entry(self.busca2)
        self.entBusca2.pack(padx=10)

        self.cbBusca3 = Combobox(self.busca3, values=[
            "",
            "NumObito",
            "NumSepultura",
            "Nome",
            "Idade",
            "Pai",
            "Mae",
            "Natural",
            "CausaMorte",
            "DataFalecimento",
            "DeclaradoPor",
            "InumadoSepultura",
            "Atestado",
            "Funcao",
            "Cemiterio",
            "Quadra",
            "Livro",
            "Folha"
        ], state="readonly")
        self.cbBusca3.current()
        self.cbBusca3.pack(side=LEFT)

        self.entBusca3 = Entry(self.busca3)
        self.entBusca3.pack(padx=10)

        self.btnBusca = Button(self.button, text="Buscar", command=self.buscar_banco)
        self.btnBusca.pack(side=BOTTOM, pady=5)

        self.jan.iconbitmap('images\icon.ico')
        self.jan.title('Consulta de Obitos')

        self.Resultado = scrolledtext.ScrolledText(self.caixaTexto,width=45,height=35)
        self.Resultado.pack()
    
        self.jan.transient(pagina)#
    
        self.jan.focus_force()#
            
        self.jan.grab_set()#
    def buscar_banco(self):
        self.conexao = sqlite3.connect('promemoria.db')
        
        c = self.conexao.cursor()  
        self.Resultado.delete(1.0,END)
        if (self.cbBusca.get() != "" and self.entBusca.get() != "" and self.cbBusca2.get() != "" and self.entBusca2.get() != "" and self.cbBusca3.get() != "" and self.entBusca3.get() != ""):
            c.execute("SELECT * FROM cemiterio WHERE(" + self.cbBusca.get() +" = '" + self.entBusca.get().lower() +"' and "+ self.cbBusca2.get() +" = '"+ self.entBusca2.get().lower() +"' and "+ self.cbBusca3.get() +" = '"+ self.entBusca3.get().lower() +"') COLLATE NOCASE;")
            
            for linha in c:
                
                
                self.Resultado.insert(INSERT, "Numero do Obito: ", INSERT, linha[0], INSERT, "\n")
                self.Resultado.insert(INSERT, "Numero da Sepultura: ", INSERT, linha[1], INSERT, "\n")
                self.Resultado.insert(INSERT, "Nome: ", INSERT, linha[2], INSERT, "\n")
                self.Resultado.insert(INSERT, "Idade: ", INSERT, linha[3], INSERT, "\n")
                self.Resultado.insert(INSERT, "Pai: ", INSERT, linha[4], INSERT, "\n")
                self.Resultado.insert(INSERT, "Mae: ", INSERT, linha[5], INSERT, "\n")
                self.Resultado.insert(INSERT, "Natural de: ", INSERT, linha[6], INSERT, "\n")
                self.Resultado.insert(INSERT, "Causa da Morte: ", INSERT, linha[7], INSERT, "\n")
                self.Resultado.insert(INSERT, "Data de Falecimento: ", INSERT, linha[8], INSERT, "\n")
                self.Resultado.insert(INSERT, "Declarado por: ", INSERT, linha[9], INSERT, "\n")
                self.Resultado.insert(INSERT, "Inumado em Sepultura: ", INSERT, linha[10], INSERT, "\n")
                self.Resultado.insert(INSERT, "Atestado: ", INSERT, linha[11], INSERT, "\n")
                self.Resultado.insert(INSERT, "Função: ", INSERT, linha[12], INSERT, "\n")
                self.Resultado.insert(INSERT, "Cemiterio: ", INSERT, linha[13], INSERT, "\n")
                self.Resultado.insert(INSERT, "Quadra: ", INSERT, linha[14], INSERT, "\n")
                self.Resultado.insert(INSERT, "Livro: ", INSERT, linha[15], INSERT, "\n")
                self.Resultado.insert(INSERT, "Folha: ", INSERT, linha[16], INSERT, "\n")
                self.Resultado.insert(INSERT, "\n \n")   

                               

        elif (self.cbBusca.get() != "" and self.entBusca.get() != "" and self.cbBusca2.get() != "" and self.entBusca2.get() != ""):
            c.execute("SELECT * FROM cemiterio WHERE(" + self.cbBusca.get() +" = '" + self.entBusca.get().lower() +"' and "+ self.cbBusca2.get() +" = '"+ self.entBusca2.get().lower() +"') COLLATE NOCASE;")
            for linha in c:    
                self.Resultado.insert(INSERT, "Numero do Obito: ", INSERT, linha[0], INSERT, "\n")
                self.Resultado.insert(INSERT, "Numero da Sepultura: ", INSERT, linha[1], INSERT, "\n")
                self.Resultado.insert(INSERT, "Nome: ", INSERT, linha[2], INSERT, "\n")
                self.Resultado.insert(INSERT, "Idade: ", INSERT, linha[3], INSERT, "\n")
                self.Resultado.insert(INSERT, "Pai: ", INSERT, linha[4], INSERT, "\n")
                self.Resultado.insert(INSERT, "Mae: ", INSERT, linha[5], INSERT, "\n")
                self.Resultado.insert(INSERT, "Natural de: ", INSERT, linha[6], INSERT, "\n")
                self.Resultado.insert(INSERT, "Causa da Morte: ", INSERT, linha[7], INSERT, "\n")
                self.Resultado.insert(INSERT, "Data de Falecimento: ", INSERT, linha[8], INSERT, "\n")
                self.Resultado.insert(INSERT, "Declarado por: ", INSERT, linha[9], INSERT, "\n")
                self.Resultado.insert(INSERT, "Inumado em Sepultura: ", INSERT, linha[10], INSERT, "\n")
                self.Resultado.insert(INSERT, "Atestado: ", INSERT, linha[11], INSERT, "\n")
                self.Resultado.insert(INSERT, "Função: ", INSERT, linha[12], INSERT, "\n")
                self.Resultado.insert(INSERT, "Cemiterio: ", INSERT, linha[13], INSERT, "\n")
                self.Resultado.insert(INSERT, "Quadra: ", INSERT, linha[14], INSERT, "\n")
                self.Resultado.insert(INSERT, "Livro: ", INSERT, linha[15], INSERT, "\n")
                self.Resultado.insert(INSERT, "Folha: ", INSERT, linha[16], INSERT, "\n")
                self.Resultado.insert(INSERT, "\n \n")  

            

        elif (self.cbBusca.get() != "" and self.entBusca.get() != ""):
            c.execute("SELECT * FROM cemiterio WHERE(" + self.cbBusca.get() +" = '" + self.entBusca.get().lower() +"') COLLATE NOCASE;")
            for linha in c:    
                self.Resultado.insert(INSERT, "Numero do Obito: ", INSERT, linha[0], INSERT, "\n")
                self.Resultado.insert(INSERT, "Numero da Sepultura: ", INSERT, linha[1], INSERT, "\n")
                self.Resultado.insert(INSERT, "Nome: ", INSERT, linha[2], INSERT, "\n")
                self.Resultado.insert(INSERT, "Idade: ", INSERT, linha[3], INSERT, "\n")
                self.Resultado.insert(INSERT, "Pai: ", INSERT, linha[4], INSERT, "\n")
                self.Resultado.insert(INSERT, "Mae: ", INSERT, linha[5], INSERT, "\n")
                self.Resultado.insert(INSERT, "Natural de: ", INSERT, linha[6], INSERT, "\n")
                self.Resultado.insert(INSERT, "Causa da Morte: ", INSERT, linha[7], INSERT, "\n")
                self.Resultado.insert(INSERT, "Data de Falecimento: ", INSERT, linha[8], INSERT, "\n")
                self.Resultado.insert(INSERT, "Declarado por: ", INSERT, linha[9], INSERT, "\n")
                self.Resultado.insert(INSERT, "Inumado em Sepultura: ", INSERT, linha[10], INSERT, "\n")
                self.Resultado.insert(INSERT, "Atestado: ", INSERT, linha[11], INSERT, "\n")
                self.Resultado.insert(INSERT, "Função: ", INSERT, linha[12], INSERT, "\n")
                self.Resultado.insert(INSERT, "Cemiterio: ", INSERT, linha[13], INSERT, "\n")
                self.Resultado.insert(INSERT, "Quadra: ", INSERT, linha[14], INSERT, "\n")
                self.Resultado.insert(INSERT, "Livro: ", INSERT, linha[15], INSERT, "\n")
                self.Resultado.insert(INSERT, "Folha: ", INSERT, linha[16], INSERT, "\n")
                self.Resultado.insert(INSERT, "\n \n") 
             
        c.close()

    def insere(self):

        self.insere=Toplevel()

        self.insere.geometry("275x590")
        
        self.NumObito = Frame(self.insere)
        self.NumObito["padding"] = 5
        self.NumObito.pack()
        
        self.NumSepultura = Frame(self.insere)
        self.NumSepultura["padding"] = 5
        self.NumSepultura.pack()
        
        self.Nome = Frame(self.insere)
        self.Nome["padding"] = 5
        self.Nome.pack()

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
        
        self.DeclaradoPor = Frame(self.insere)
        self.DeclaradoPor["padding"] = 5
        self.DeclaradoPor.pack()

        self.InumadoSepultura = Frame(self.insere)
        self.InumadoSepultura["padding"] = 5
        self.InumadoSepultura.pack()

        self.Atestado = Frame(self.insere)
        self.Atestado["padding"] = 5
        self.Atestado.pack()

        self.Func = Frame(self.insere)
        self.Func["padding"] = 5
        self.Func.pack()

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
        self.lblNumSepultura = Label(self.NumSepultura, text="Nº Sepultura: ", width=20).pack(side=LEFT)
        self.lblNome = Label(self.Nome, text="Nome: ", width=20).pack(side=LEFT)
        self.lblIdade = Label(self.Idade, text="Idade: ", width=20).pack(side=LEFT)
        self.lblPai = Label(self.Pai, text="Pai: ", width=20).pack(side=LEFT)
        self.lblMae = Label(self.Mae, text="Mãe: ", width=20).pack(side=LEFT)
        self.lblNatural = Label(self.Natural, text="Natural de: ", width=20).pack(side=LEFT)
        self.lblCausaMorte = Label(self.CausaMorte, text="Causa da Morte: ", width=20).pack(side=LEFT)
        self.lblDataFalecimento = Label(self.DataFalecimento, text="Data do Falecimento: ", width=20).pack(side=LEFT)
        self.lblDeclaradoPor = Label(self.DeclaradoPor, text="Declarado por: ", width=20).pack(side=LEFT)
        self.lblInumadoSepultura = Label(self.InumadoSepultura, text="Inumado em Sepultura: ", width=22).pack(side=LEFT)
        self.lblAtestado = Label(self.Atestado, text="Atestado por: ", width=20).pack(side=LEFT)
        self.lblFunc = Label(self.Func, text="Função: ", width=20).pack(side=LEFT)
        self.lblCemiterio = Label(self.Cemiterio, text="Cemiterio: ", width=20).pack(side=LEFT)
        self.lblQuadra = Label(self.Quadra, text="Quadra: ", width=20).pack(side=LEFT)
        self.lblLivro = Label(self.Livro, text="Livro: ", width=20).pack(side=LEFT)
        self.lblFolha = Label(self.Folha, text="Folha: ", width=20).pack(side=LEFT)
 
        self.entNumObito = Entry(self.NumObito)
        self.entNumSepultura = Entry(self.NumSepultura)
        self.entNome = Entry(self.Nome)
        self.entIdade = Entry(self.Idade)
        self.entPai = Entry(self.Pai)
        self.entMae = Entry(self.Mae)
        self.entNatural = Entry(self.Natural)
        self.entCausaMorte = Entry(self.CausaMorte)
        self.entDataFalecimento = Entry(self.DataFalecimento)
        self.entDeclaradoPor = Entry(self.DeclaradoPor)
        self.entInumadoSepultura = Entry(self.InumadoSepultura, width='18')
        self.entAtestado = Entry(self.Atestado)
        self.entFunc = Entry(self.Func)
        self.entCemiterio = Entry(self.Cemiterio)
        self.entQuadra = Entry(self.Quadra)
        self.entLivro = Entry(self.Livro)
        self.entFolha = Entry(self.Folha)

        self.entNumObito.pack(side=LEFT)
        self.entNumSepultura.pack(side=LEFT)
        self.entNome.pack(side=LEFT)
        self.entIdade.pack(side=LEFT)
        self.entPai.pack(side=LEFT)
        self.entMae.pack(side=LEFT)
        self.entNatural.pack(side=LEFT)
        self.entCausaMorte.pack(side=LEFT)
        self.entDataFalecimento.pack(side=LEFT)
        self.entDeclaradoPor.pack(side=LEFT)
        self.entInumadoSepultura.pack(side=LEFT)
        self.entAtestado.pack(side=LEFT)
        self.entFunc.pack(side=LEFT)
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

    def cria_banco(self):
        self.conexao = sqlite3.connect('promemoria.db')
        c = self.conexao.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS cemiterio(\
            NumObito int(20),\
            NumSepultura int(20),\
            Nome varchar(100),\
            Idade int(3),\
            Pai varchar(100),\
            Mae varchar(100),\
            Natural varchar(100),\
            CausaMorte varchar(100),\
            DataFalecimento varchar(30),\
            DeclaradoPor varchar(100),\
            InumadoSepultura varchar(100),\
            Atestado varchar(100),\
            Funcao varchar(100),\
            Cemiterio varchar(100),\
            Quadra varchar(100),\
            Livro varchar(100),\
            Folha varchar(100));")

    def reset(self):
        self.lblMsg['text'] = ""
    
    def insere_banco(self):
        if (self.entNumObito.get().lower() == ""):
            self.lblMsg['text'] = 'O numero do Obito não pode ser nulo!'
            self.lblMsg['foreground'] = "red"
            t = Timer(4, self.reset)
            t.start()

        else:
            try:
                self.conexao = sqlite3.connect('promemoria.db')
                c = self.conexao.cursor()  
                c.execute("INSERT INTO cemiterio VALUES(\
                    '" + self.entNumObito.get().lower() + "',\
                    '" + self.entNumSepultura.get().lower() + "',\
                    '" + self.entNome.get().lower() + "',\
                    '" + self.entIdade.get().lower() + "',\
                    '" + self.entPai.get().lower() + "',\
                    '" + self.entMae.get().lower() + "',\
                    '" + self.entNatural.get().lower() + "',\
                    '" + self.entCausaMorte.get().lower() + "',\
                    '" + self.entDataFalecimento.get().lower() + "',\
                    '" + self.entDeclaradoPor.get().lower() + "',\
                    '" + self.entInumadoSepultura.get().lower() + "',\
                    '" + self.entAtestado.get().lower() + "',\
                    '" + self.entFunc.get().lower() + "',\
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
                self.entDeclaradoPor.delete(0, END)
                self.entInumadoSepultura.delete(0, END)
                self.entAtestado.delete(0, END)
                self.entFunc.delete(0, END)
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



GUI.cria_banco(GUI) #cria o banco se n existir
pagina = Tk()
pagina.iconbitmap('images\icon.ico')
pagina.title('Consulta de Obitos')

GUI(pagina)
pagina.mainloop()

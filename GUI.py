# -*- coding: utf-8 -*-

import io
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class GUI():
    def __init__(self, dictCB):
        self.callbacks = dictCB
        self.root = tk.Tk()

        self.bgLightYellow = "#E6E8D7"
        self.dataSociosPunto3 = []
        self.dataSociosPunto4 = []
        self.dataSociosPunto5 = []

        #Configuración Inicial
        self.initialConfig()
        self.welcomeFrame()
        self.loadFrame()
        self.punto1Frame()
        self.punto2Frame()
        self.punto3Frame()
        self.punto4Frame()
        self.punto5Frame()
    
        self.root.mainloop()
        pass

    def initialConfig(self):
        self.root.title("Challenge Recursiva - Carrasco Gastón")

        self.minH = int(self.root.winfo_screenheight() * 0.3)
        self.minW = int(self.root.winfo_screenwidth() * 0.3)
        
        self.minH = max(310,self.minH)
        self.minW = max(575,self.minW)

        self.root.resizable(0,0)
        self.root.geometry("%ix%i+0+0"%(self.minW,self.minH))
        self.root.config(
            height=self.minH,width=self.minW
        )
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.config(
            background= self.bgLightYellow
        )
        self.mainFrame.pack(side='top',fill='both',expand=True)

        self.tkPath = tk.StringVar()

    def welcomeFrame(self):
        self.welcomeBaseFrame = tk.Frame(self.mainFrame)
        self.welcomeBaseFrame.config(background=self.bgLightYellow)
        self.welcomeBaseFrame.pack(side='top',fill='x',ipadx=2)

        self.lblWelcome = tk.Label(self.welcomeBaseFrame)
        self.lblWelcome.config(
            text="Bienvenido! Este programa esta desarrollado para el Challenge - Superliga. \nSimplemente seleccione el archivo de socios correspondiente y obtenga los resultados pedidos.",
            background=self.bgLightYellow,
            anchor='w'
        )
        self.lblWelcome.pack(side='top',ipadx=2,pady=(5,1))

    def loadFrame(self):
        self.loadBaseFrame = tk.Frame(self.mainFrame)
        self.loadBaseFrame.config(background=self.bgLightYellow)
        self.loadBaseFrame.pack(side='top',fill='x',ipady=10,ipadx=2)

        self.loadLabel = tk.Label(self.loadBaseFrame)
        self.loadLabel.config(
            text="Seleccione el archivo:",
            anchor="e", background=self.bgLightYellow
        )
        self.loadLabel.pack(side='left',padx=(8,3))

        self.loadButton = tk.Button(self.loadBaseFrame)
        self.loadButton.config(
            text="Buscar", command=self.selectFile
        )
        self.loadButton.pack(side='right',padx=(5,8),ipadx=1,ipady=1)
        
        self.loadEntryFile = tk.Entry(self.loadBaseFrame)
        self.loadEntryFile.config(
            textvariable=self.tkPath,
            state='disabled',
            background='white'
        )
        self.loadEntryFile.pack(side='left',fill='x',expand=True)


    def punto1Frame(self):
        self.punto1FrameBase = tk.Frame(self.mainFrame)
        self.punto1FrameBase.config(background=self.bgLightYellow)
        self.punto1FrameBase.pack(side='top',fill='x',ipady=10,ipadx=2)

        self.punto1Title = tk.Label(self.punto1FrameBase)
        self.punto1Title.config(
            text="Punto 1: ",
            anchor="e", background=self.bgLightYellow
        )
        self.punto1Title.pack(side='left',padx=(8,3))

        self.lblResponsePunto1 = tk.Label(self.punto1FrameBase)
        self.lblResponsePunto1.config(
            text="Sin respuesta. No se ha cargado ningún archivo aún.",
            anchor='e',background=self.bgLightYellow
        )
        self.lblResponsePunto1.pack(side='left',padx=(4,3),fill='x')

    def punto2Frame(self):
        self.punto2FrameBase = tk.Frame(self.mainFrame)
        self.punto2FrameBase.config(background=self.bgLightYellow)
        self.punto2FrameBase.pack(side='top',fill='x',ipady=10,ipadx=2)

        self.punto2Title = tk.Label(self.punto2FrameBase)
        self.punto2Title.config(
            text="Punto 2: ",
            anchor="e", background=self.bgLightYellow
        )
        self.punto2Title.pack(side='left',padx=(8,3))

        self.lblResponsePunto2 = tk.Label(self.punto2FrameBase)
        self.lblResponsePunto2.config(
            text="Sin respuesta. No se ha cargado ningún archivo aún.",
            anchor='e',background=self.bgLightYellow
        )
        self.lblResponsePunto2.pack(side='left',padx=(4,3),fill='x')

    def punto3Frame(self):
        self.punto3FrameBase = tk.Frame(self.mainFrame)
        self.punto3FrameBase.config(background=self.bgLightYellow)
        self.punto3FrameBase.pack(side='top',fill='x',ipady=10,ipadx=2)

        self.punto3Title = tk.Label(self.punto3FrameBase)
        self.punto3Title.config(
            text="Punto 3: ",
            anchor="e", background=self.bgLightYellow
        )
        self.punto3Title.pack(side='left',padx=(8,3))

        self.lblResponsePunto3 = tk.Label(self.punto3FrameBase)
        self.lblResponsePunto3.config(
            text="Sin respuesta. No se ha cargado ningún archivo aún.",
            anchor='e',background=self.bgLightYellow
        )
        self.lblResponsePunto3.pack(side='left',padx=(4,3),fill='x')

    def punto4Frame(self):
        self.punto4FrameBase = tk.Frame(self.mainFrame)
        self.punto4FrameBase.config(background=self.bgLightYellow)
        self.punto4FrameBase.pack(side='top',fill='x',ipady=10,ipadx=2)

        self.punto4Title = tk.Label(self.punto4FrameBase)
        self.punto4Title.config(
            text="Punto 4: ",
            anchor="e", background=self.bgLightYellow
        )
        self.punto4Title.pack(side='left',padx=(8,3))

        self.lblResponsePunto4 = tk.Label(self.punto4FrameBase)
        self.lblResponsePunto4.config(
            text="Sin respuesta. No se ha cargado ningún archivo aún.",
            anchor='e',background=self.bgLightYellow
        )
        self.lblResponsePunto4.pack(side='left',padx=(4,3),fill='x')

    def punto5Frame(self):
        self.punto5FrameBase = tk.Frame(self.mainFrame)
        self.punto5FrameBase.config(background=self.bgLightYellow)
        self.punto5FrameBase.pack(side='top',fill='x',ipady=10,ipadx=2)

        self.punto5Title = tk.Label(self.punto5FrameBase)
        self.punto5Title.config(
            text="Punto 5: ",
            anchor="e", background=self.bgLightYellow
        )
        self.punto5Title.pack(side='left',padx=(8,3))

        self.lblResponsePunto5 = tk.Label(self.punto5FrameBase)
        self.lblResponsePunto5.config(
            text="Sin respuesta. No se ha cargado ningún archivo aún.",
            anchor='e',background=self.bgLightYellow
        )
        self.lblResponsePunto5.pack(side='left',padx=(4,3),fill='x')

    def selectFile(self):
        path = filedialog.askopenfilename(
            title="Seleccionar archivo de socios",
            filetypes=(("csv","*.csv"),("Todos los archivos","*.*"))
        )
        if path != "":
            print("Path: " + path)
            if not path.endswith(".csv"):
                ext = path.split('.')[-1]
                messagebox.showerror(
                    message="Error, la extensión del archivo no puede ser %s"%(ext),
                    title="Error de lectura"
                )
            else:
                self.callbacks["resetSocios"]()
                fileSocio = io.open(path,'r',encoding='cp1252')
                readingError = False
                
                line = fileSocio.readline()
                line = line.replace('\r','').replace('\n','')
                if line == "":
                    readingError = True
                    messagebox.showerror(
                        message="Error, el archivo esta vacio.",
                        title="Error de lectura"
                    )

                try:
                    while (line!=""):
                        nombre,edad,equipo,estCivil,estudios = line.split(';')

                        #generar nuevo Socio
                        self.callbacks["addSocio"](nombre,int(edad),equipo,estCivil,estudios)
                    
                        line = fileSocio.readline()
                        line = line.replace('\r','').replace('\n','')
                except Exception as e:
                    print(e)
                    messagebox.showerror(
                        message="Error, el formato del archivo no es el esperado.",
                        title="Error de lectura"
                    )
                    readingError = True
                if not readingError:
                    self.tkPath.set(path)
                    self.callbacks["genIndexList"]()
                    self.executePunto1()
                    self.executePunto2()
                    self.executePunto3()
                    self.executePunto4()
                    self.executePunto5()
        else:
            pass

    #Ejecucion Pto1
    def executePunto1(self):
        response = self.callbacks["punto1"]()
        self.lblResponsePunto1.config(text=response)
        self.lblResponsePunto1.update()
    #Ejecucion Pto2
    def executePunto2(self):
        response = self.callbacks["punto2"]()
        self.lblResponsePunto2.config(text=response)
        self.lblResponsePunto2.update()
    #Ejecucion Pto3
    def executePunto3(self):
        response = self.callbacks["punto3"]()
        self.dataSociosPunto3 = response
        if response == []:
            self.punto3EmptyResponse()
        else:
            self.punto3LoadResponse()
    
    def punto3EmptyResponse(self):
        if hasattr(self,"btnResponsePunto3"):
            self.btnResponsePunto3.pack_forget()
            self.btnResponsePunto3.destroy()
            del self.btnResponsePunto3
        if not hasattr(self,"lblResponsePunto3"):
            self.lblResponsePunto3 = tk.Label(self.punto3FrameBase)
            self.lblResponsePunto3.config(
                text="No hay socios registrados que cumplan los requisitos.",
                anchor='e',background=self.bgLightYellow
            )
            self.lblResponsePunto3.pack(side='left',padx=(4,3),fill='x')
        else:
            self.lblResponsePunto3.config(text="No hay socios registrados que cumplan los requisitos.")
            self.lblResponsePunto3.update()

    def punto3LoadResponse(self):
        if hasattr(self,"lblResponsePunto3"):
            self.lblResponsePunto3.pack_forget()
            self.lblResponsePunto3.destroy()
            del self.lblResponsePunto3
        if not hasattr(self,"btnResponsePunto3"):
            self.btnResponsePunto3 = tk.Button(self.punto3FrameBase)
            self.btnResponsePunto3.config(
                text="Ver respuesta", command=self.showResponsePunto3
            )
            self.btnResponsePunto3.pack(side='left',padx=(4,3))
    
    def showResponsePunto3(self):
        if hasattr(self,"topFramePto3"):
            self.topFramePto3.focus()
        else:
            xInit = int(self.root.winfo_rootx()) + int(self.root.winfo_width()*0.25)
            yInit = int(self.root.winfo_rooty()) + int(self.root.winfo_height()*0.25)

            self.topFramePto3 = tk.Toplevel(self.root)
            self.topFramePto3.title("Socios casados, universitarios y ordenados por edad.")
            self.topFramePto3.geometry("450x270+%i+%i"%(xInit,yInit))
            btnFrame = ttk.Frame(self.topFramePto3)
            btnFrame.pack(side='bottom',fill='x')
            btnOK = ttk.Button(btnFrame)
            btnOK.config(text="Aceptar",command=self.destroyTopPto3)
            btnOK.pack(side='right',padx=(0,10), pady=(0,3))

            tableFrame = ttk.Frame(self.topFramePto3)
            tableFrame.pack(side='top',fill='both',expand='True')
            
            dataColumns = ["#","Nombre","Edad","Equipo"]
            tableResponse = ttk.Treeview(tableFrame,columns=dataColumns,show='headings')
            
            for c in dataColumns:
                tableResponse.heading(c,text=c,anchor='w')
                tableResponse.column(c,width=len(c),stretch=True,anchor='w')
            for i in range(len(self.dataSociosPunto3)):
                nombre,edad,equipo = self.dataSociosPunto3[i]
                tableResponse.insert('','end',values=(i+1,nombre,edad,equipo))
        
            scroll = ttk.Scrollbar(tableFrame,orient='vertical',command=tableResponse.yview)
            tableResponse.config(yscrollcommand=scroll.set)
            tableResponse.pack(side='left',fill='both',expand=True,padx=(15,0),pady=5)
            scroll.pack(side='left',fill='y',padx=(0,10),pady=5)

    def destroyTopPto3(self):
        self.topFramePto3.destroy()
        del self.topFramePto3
    #Ejecucion Pto4
    def executePunto4(self):
        response = self.callbacks["punto4"]()
        self.dataSociosPunto4 = response
        if response == []:
            self.punto4EmptyResponse()
        else:
            self.punto4LoadResponse()
    
    def punto4EmptyResponse(self):
        if hasattr(self,"btnResponsePunto4"):
            self.btnResponsePunto4.pack_forget()
            self.btnResponsePunto4.destroy()
            del self.btnResponsePunto4
        if not hasattr(self,"lblResponsePunto4"):
            self.lblResponsePunto4 = tk.Label(self.punto4FrameBase)
            self.lblResponsePunto4.config(
                text="No hay socios registrados hinchas de River.",
                anchor='e',background=self.bgLightYellow
            )
            self.lblResponsePunto4.pack(side='left',padx=(4,3),fill='x')
        else:
            self.lblResponsePunto4.config(text="No hay socios registrados hinchas de River.")
            self.lblResponsePunto4.update()

    def punto4LoadResponse(self):
        if hasattr(self,"lblResponsePunto4"):
            self.lblResponsePunto4.pack_forget()
            self.lblResponsePunto4.destroy()
            del self.lblResponsePunto4
        if not hasattr(self,"btnResponsePunto4"):
            self.btnResponsePunto4 = tk.Button(self.punto4FrameBase)
            self.btnResponsePunto4.config(
            text="Ver respuesta", command=self.showResponsePunto4
            )
            self.btnResponsePunto4.pack(side='left',padx=(4,3))
    
    def showResponsePunto4(self):
        if hasattr(self,"topFramePto4"):
            self.topFramePto4.focus()
        else:
            xInit = int(self.root.winfo_rootx()) + int(self.root.winfo_width()*0.25)
            yInit = int(self.root.winfo_rooty()) + int(self.root.winfo_height()*0.25)

            self.topFramePto4 = tk.Toplevel(self.root)
            self.topFramePto4.title("Ranking Top-5 Nombres de socios de River.")
            self.topFramePto4.geometry("400x220+%i+%i"%(xInit,yInit))
            btnFrame = ttk.Frame(self.topFramePto4)
            btnFrame.pack(side='bottom',fill='x')
            btnOK = ttk.Button(btnFrame)
            btnOK.config(text="Aceptar",command=self.destroyTopPto4)
            btnOK.pack(side='right',padx=(0,10), pady=(0,3))

            tableFrame = ttk.Frame(self.topFramePto4)
            tableFrame.pack(side='top',fill='both',expand='True')
            
            dataColumns = ["#","Nombre","Socios"]
            tableResponse = ttk.Treeview(tableFrame,columns=dataColumns,show='headings')
            
            for c in dataColumns:
                tableResponse.heading(c,text=c,anchor='w')
                tableResponse.column(c,width=len(c),stretch=True,anchor='w')
            for i in range(len(self.dataSociosPunto4)):
                nombre,cantSocios = self.dataSociosPunto4[i]
                tableResponse.insert('','end',values=(i+1,nombre,cantSocios))
        
            scroll = ttk.Scrollbar(tableFrame,orient='vertical',command=tableResponse.yview)
            tableResponse.config(yscrollcommand=scroll.set)
            tableResponse.pack(side='left',fill='both',expand=True,padx=(15,0),pady=5)
            scroll.pack(side='left',fill='y',padx=(0,10),pady=5)
    
    def destroyTopPto4(self):
        self.topFramePto4.destroy()
        del self.topFramePto4
    #Ejecucion Pto5
    def executePunto5(self):
        response = self.callbacks["punto5"]()
        self.dataSociosPunto5 = response
        if response == []:
            self.punto5EmptyResponse()
        else:
            self.punto5LoadResponse()
    
    def punto5EmptyResponse(self):
        if hasattr(self,"btnResponsePunto5"):
            self.btnResponsePunto5.pack_forget()
            self.btnResponsePunto5.destroy()
            del self.btnResponsePunto5
        if not hasattr(self,"lblResponsePunto5"):
            self.lblResponsePunto5 = tk.Label(self.punto5FrameBase)
            self.lblResponsePunto5.config(
                text="No hay socios de equipos registrados necesarios para formar una respuesta.",
                anchor='e',background=self.bgLightYellow
            )
            self.lblResponsePunto5.pack(side='left',padx=(4,3),fill='x')
        else:
            self.lblResponsePunto5.config(text="No hay socios de equipos registrados necesarios para formar una respuesta.")
            self.lblResponsePunto5.update()

    def punto5LoadResponse(self):
        if hasattr(self,"lblResponsePunto5"):
            self.lblResponsePunto5.pack_forget()
            self.lblResponsePunto5.destroy()

        if not hasattr(self,"btnResponsePunto5"):
            self.btnResponsePunto5 = tk.Button(self.punto5FrameBase)
            self.btnResponsePunto5.config(
            text="Ver respuesta", command=self.showResponsePunto5
            )
            self.btnResponsePunto5.pack(side='left',padx=(4,3))
    
    def showResponsePunto5(self):
        if hasattr(self,"topFramePto5"):
            self.topFramePto5.focus()
        else:
            xInit = int(self.root.winfo_rootx()) + int(self.root.winfo_width()*0.25)
            yInit = int(self.root.winfo_rooty()) + int(self.root.winfo_height()*0.25)

            self.topFramePto5 = tk.Toplevel(self.root)
            self.topFramePto5.title("Ranking de equipos según su cantidad de socios.")
            self.topFramePto5.geometry("485x270+%i+%i"%(xInit,yInit))
            btnFrame = ttk.Frame(self.topFramePto5)
            btnFrame.pack(side='bottom',fill='x')
            btnOK = ttk.Button(btnFrame)
            btnOK.config(text="Aceptar",command=self.destroyTopPto5)
            btnOK.pack(side='right',padx=(0,10), pady=(0,3))

            tableFrame = ttk.Frame(self.topFramePto5)
            tableFrame.pack(side='top',fill='both',expand='True')
            
            dataColumns = ["#","Equipo","Socios","Max. Edad","Min. Edad"]
            tableResponse = ttk.Treeview(tableFrame,columns=dataColumns,show='headings')
            
            for c in dataColumns:
                tableResponse.heading(c,text=c,anchor='w')
                tableResponse.column(c,width=len(c),stretch=True,anchor='w')
            for i in range(len(self.dataSociosPunto5)):
                equipo,cantSocios,maxEdad,minEdad = self.dataSociosPunto5[i]
                tableResponse.insert('','end',values=(i+1,equipo,cantSocios,maxEdad,minEdad))
        
            scroll = ttk.Scrollbar(tableFrame,orient='vertical',command=tableResponse.yview)
            tableResponse.config(yscrollcommand=scroll.set)
            tableResponse.pack(side='left',fill='both',expand=True,padx=(15,0),pady=5)
            scroll.pack(side='left',fill='y',padx=(0,10),pady=5)
    
    def destroyTopPto5(self):
        self.topFramePto5.destroy()
        del self.topFramePto5

    
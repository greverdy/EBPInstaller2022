#!/usr/bin/python3
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#

#                                                            ╔══════════════════════════╗
#                                                            ║  EBP INSTALLER GUI 2022  ║
#                                                            ╠══════════════════════════╣
#                                                            ║                          ║
#                                                            ║       Made By Gugus      ║
#                                                            ║        For Ecoris        ║
#                                                            ║          With ♥️          ║
#                                                            ║                          ║
#                                                            ╚══════════════════════════╝

#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#


#                                                            ╔══════════════╗
#                                                            ║    IMPORT    ║
#                                                            ╚══════════════╝

import customtkinter

from PIL import Image

import tkinter as tk
from tkinter import filedialog

from tkinter import messagebox

from functools import partial

import requests

import os

import shutil

from mega import Mega

from threading import *


#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#


#                                                            ╔═══════════════════╗
#                                                            ║    DEFINITIONS    ║
#                                                            ╚═══════════════════╝

class EBP(customtkinter.CTk):

    def __init__(self):
        global ebpinstall_button

        super().__init__()
        
        messagebox.showinfo('Information', 'Bonjour,\ncet exemplaire est une première version de l\'utilitaire d\'installation des logiciels EBP via une interface graphique. Quelques bugs peuvent survenir, et tous les détails d\'installation ne sont pas \'cachés\' (Ex: Une fenêtre noir peut s\'ouvrir durant l\'installation, merci de ne pas la fermer).\n\nMerci de votre compréhension.\n\nLe service informatique\ninformatique@ecoris.fr')
        
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
        
        self.geometry("1000x500")
        self.title("EBP 2022 | V "+version_package+'                                                                                                 informatique@ecoris.fr | ECORIS')
        self.configure(fg_color="lightgrey")
        self.resizable(False,False)

        try:
            icone = tk.PhotoImage(file=os.environ['LOCALAPPDATA']+'/ebp-logo.png')
            self.iconphoto(True, icone)
        except:
            os.system("curl \"https://raw.githubusercontent.com/greverdy/EBPInstaller2022/main/ebp-logo.png\" --output %LOCALAPPDATA%/ebp-logo.png")
            icone = tk.PhotoImage(file=os.environ['LOCALAPPDATA']+'/ebp-logo.png')
            self.iconphoto(True, icone)
        else:
            pass

        self.create_menu_bar()

        title_ebp = customtkinter.CTkLabel(master=self, text="EBP 2022", width=200, height=50, font=('Arial',40))
        title_ebp.place(relx=0.5, rely=0.17, anchor=customtkinter.CENTER)

        self.create_checkbox()
        self.create_switchcase()

        ebpinstall_button = customtkinter.CTkButton(master=self, state='disabled', text="Démarrer l'installation", corner_radius=10, command=EBP.ebp_valid_install, width=250, height=40, hover=True, font=('Arial',20))
        ebpinstall_button.place(relx=0.5, rely=0.4, anchor="w")


    def create_menu_bar(self):
        global combobox1
        global combobox2

        frame = customtkinter.CTkFrame(master=self,width=800,height=100,corner_radius=0,fg_color="grey")
        frame.grid(row=0, column=0, padx=0, pady=0)

        combobox_var = customtkinter.StringVar(value="Menu")  # set initial value
        combobox1 = customtkinter.CTkOptionMenu(master=frame, values=["M.A.J. EBP", "----------------------------------------", "Signaler Comme Fiable", "----------------------------------------", "M.A.J. Windows"], command=EBP.optionmenu_1, variable=combobox_var, hover=True)
        combobox1.grid(row=0, column=0, padx=10, pady=10)

        combobox_var = customtkinter.StringVar(value="Info")  # set initial value
        combobox2 = customtkinter.CTkOptionMenu(master=frame, values=["Version","Aide", "----------", "?"], command=EBP.optionmenu_2, variable=combobox_var, hover=True)
        combobox2.grid(row=0, column=1, padx=10, pady=10)

        text_var = customtkinter.StringVar(value="                                                                                                                                                                                                                      ")

        label = customtkinter.CTkLabel(master=frame, textvariable=text_var, width=120, height=25, corner_radius=8)
        label.grid(row=0, column=2, padx=10, pady=10)


    def optionmenu_1(choice):
        combobox1.set("Menu") 
        if choice == "M.A.J. EBP":
            EBP.CheckVersion()
        elif choice == "Signaler Comme Fiable":
            EBP.ApprovePackage()
        elif choice == "M.A.J. Windows":
            EBP.CheckUpdate()


    def optionmenu_2(choice):
        combobox2.set("Info") 
        if choice == "Version":
            EBP.display_version()
        elif choice == "Aide":
            EBP.display_help()
        elif choice == "?":
            EBP.display_information()
        else:
            pass

    def create_checkbox(self):
        global separator,label_choice

        label_choice = customtkinter.CTkLabel(master=self, text="Choix :", width=200, height=50, font=('Arial',20))
        label_choice.place(relx=0.06, rely=0.25, anchor=customtkinter.CENTER)
        
        globals()["checkbox_{}".format(0)] = customtkinter.CTkCheckBox(master=self, text="Tout installer", command=partial(EBP.checkbox_event, EBP_List_Logiciel, "checkbox_0"), variable=customtkinter.StringVar(value="off"), onvalue="all", offvalue="off")
        globals()["checkbox_{}".format(0)].place(relx=0.025, rely=0.35, anchor="w")

        y=0.42
        for elem in EBP_List_Logiciel:
            globals()["checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)] = customtkinter.CTkCheckBox(master=self, text=elem[0], command=partial(EBP.checkbox_event, elem, "checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)), variable=customtkinter.StringVar(value="off"), onvalue=elem[1], offvalue="off")
            globals()["checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)].place(relx=0.025, rely=y, anchor="w")
            y+=0.07


        separator = customtkinter.CTkFrame(master=self,width=5,height=275,corner_radius=0,fg_color="black")
        separator.place(relx=0.425, rely=0.58, anchor="w")


    def create_switchcase(self):
        global foldername
        foldername="%LOCALAPPDATA%"

        y=0.56
        for elem in Event_Swtichcase:
            globals()["switch_{}".format(Event_Swtichcase.index(elem)+1)] = customtkinter.CTkSwitch(master=self, text=elem[0], command=partial(EBP.switch_event, elem[0], elem[1], "switch_{}".format(Event_Swtichcase.index(elem)+1)), variable=customtkinter.StringVar(value=elem[2]), onvalue="Oui", offvalue="Non", state=elem[3])
            if elem[2] =="Oui":
                 globals()["switch_{}".format(Event_Swtichcase.index(elem)+1)].select()
            globals()["switch_{}".format(Event_Swtichcase.index(elem)+1)].place(relx=0.5, rely=y, anchor="w")
            y+=0.07


    def checkbox_event(definition, param):
        global EBP_List_Select

        if param == 'checkbox_0' :
            if globals()[param].get() == "all" :
                EBP_List_Select.clear()
                for i in range(1,8):
                    globals()["checkbox_{}".format(i)].configure(state="disable", variable=customtkinter.StringVar(value="off"))
                EBP_List_Select = EBP_List_Logiciel
            else:
                for i in range(1,8):
                    globals()["checkbox_{}".format(i)].configure(state="normal")
                EBP_List_Select.clear()
                
        elif globals()[param].get() != 'off' :
            EBP_List_Select.append(definition)
        else:
            if EBP_List_Select:
                EBP_List_Select.remove(definition)
        
        if EBP_List_Select:
            ebpinstall_button.configure(state='normal')
        else:
            ebpinstall_button.configure(state='disabled')


    def switch_event(EventText, definition,param):
        func = getattr(EBP, definition)
        Installation=False
        func(definition, Installation, EventText, param,globals()[param].get())
        

    def restart(self, Installation, EventText, param, value):
        if not Installation:
            if value == "Non":
                globals()[param].configure(variable=customtkinter.StringVar(value="Non"), text=EventText[:-3]+"Non")
            else:
                globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text=EventText[:-3]+"Oui")

            textlist=EventText[:-3]+("Non" if value == "Oui" else "Oui")
            for elem in Event_Swtichcase:
                if textlist in elem:
                    elem[0]=EventText[:-3]+globals()[param].get()
        else:
            if param == "Oui" and not no_ebp:
                EBP.wait(value)
                value.configure(state="normal")
                value.insert(tk.END, f"          • Le poste va redémarrer.\n")
                value.configure(state="disabled")
                EBP.wait(value)
                EBP.wait(value)
                EBP.wait(value)
                EBP.wait(value)
                EBP.wait(value)
                os.system("shutdown -r -t 2")
            elif param == "Oui" and no_ebp:
                EBP.wait(value)
                value.configure(state="normal")
                value.insert(tk.END, f"\n          • Aucune nouvelle application n'a été installée. Le poste ne va pas redémarrer.\n")
                value.configure(state="disabled")
                EBP.wait(value)
                EBP.wait(value)

    def Change_path(self, Installation, EventText, param, value):
        global foldername
        if not Installation:
            if value == "Non":
                foldername = tk.filedialog.askdirectory(initialdir = os.environ['USERPROFILE'],
                                                title = "Select a Folder")
                if foldername:
                    if foldername[-7:]=="EBP2022":
                        foldername=foldername[:len(foldername)-len(foldername[-7:])-1]
                    globals()[param].configure(variable=customtkinter.StringVar(value="Chemin : "+foldername), text="Chemin : "+foldername)
                else:
                    foldername="%LOCALAPPDATA%"
                    globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text="Chemin par défault : %LOCALAPPDATA%")
            else:
                foldername="%LOCALAPPDATA%"
                globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text="Chemin par défault : %LOCALAPPDATA%")

            for elem in Event_Swtichcase:
                for celem in elem:
                    if "Chemin" in celem:
                        elem[0]=("Chemin : " if foldername != "%LOCALAPPDATA%" else "Chemin par défaut : ")+foldername
        else:
            pass


    def log(self, Installation, EventText, param, value):
        if not Installation:
            if value == "Non":
                globals()[param].configure(variable=customtkinter.StringVar(value="Non"), text=EventText[:-3]+"Non")
            else:
                globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text=EventText[:-3]+"Oui")

            textlist=EventText[:-3]+("Non" if value == "Oui" else "Oui")
            for elem in Event_Swtichcase:
                if textlist in elem:
                    elem[0]=EventText[:-3]+globals()[param].get()
        else:
            pass


    def delete_EBP_packages(self, Installation, EventText, param, value):
        if not Installation:
            if value == "Non":
                globals()[param].configure(variable=customtkinter.StringVar(value="Non"), text=EventText[:-3]+"Non")
            else:
                globals()[param].configure(variable=customtkinter.StringVar(value="Oui"), text=EventText[:-3]+"Oui")

            textlist=EventText[:-3]+("Non" if value == "Oui" else "Oui")
            for elem in Event_Swtichcase:
                if textlist in elem:
                    elem[0]=EventText[:-3]+globals()[param].get()
        else:
            if param == "Oui" and not no_ebp:
                EBP.nettoyage(foldername, value)
            elif param == "Oui" and no_ebp:
                value.configure(state="normal")
                value.insert(tk.END, f"\n          • Aucune nouvelle application n'a été installée. Le dossier EBP2022 ne sera pas supprimé.\n")
                value.configure(state="disabled")


    def ebp_valid_install():

        for elem in Event_Swtichcase:
            globals()["switch_{}".format(Event_Swtichcase.index(elem)+1)].destroy()

        globals()["checkbox_{}".format(0)].destroy()

        for elem in EBP_List_Logiciel:
            globals()["checkbox_{}".format(EBP_List_Logiciel.index(elem)+1)].destroy()

        separator.destroy()
        label_choice.destroy()
        ebpinstall_button.destroy()

        EBP.install(EBP_List_Select,)


    def wait(resultbox):
        var = customtkinter.IntVar()
        app.after(400, var.set, 1)
        app.wait_variable(var)
        resultbox.yview(tk.END)


    def waitprogressbar(resultbox):
        var = customtkinter.IntVar()
        app.after(10000, var.set, 1)
        app.wait_variable(var)
        try:
            resultbox.yview(tk.END)
        except:
            pass


    def install(choice):

        #mega = Mega()

        resultbox = customtkinter.CTkTextbox(app, width=800, height=200)
        resultbox.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        resultbox.insert("0.0", f"\n")

        for elem in Event_Swtichcase:
            EBP.wait(resultbox)
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"• {elem[0]} \n")
            resultbox.configure(state="disabled")

        resultbox.configure(state="normal")
        resultbox.insert(tk.END, f"\n")
        resultbox.configure(state="disabled")
        EBP.wait(resultbox)

        if foldername == "%LOCALAPPDATA%":
            try:
                os.mkdir(os.environ['LOCALAPPDATA']+'\\EBP2022')
                resultbox.configure(state="normal")
                resultbox.insert(tk.END, f'• Dossier EBP2022 créé dans le répertoire : {foldername}.\n')
                resultbox.configure(state="disabled")
            except PermissionError:
                resultbox.configure(state="normal")
                resultbox.insert(tk.END, '• Impossible de créer un dossier.\n     Merci de relancer le script en Administrateur, ou de sélectionner un dossier auquel vous avez accès!\n')
                resultbox.configure(state="disabled")
            except Exception as e:
                resultbox.configure(state="normal")
                resultbox.insert(tk.END, f'• Dossier EBP2022 existant dans le répertoire : {foldername}.\n')
                resultbox.configure(state="disabled")
        else:
            try:
                os.mkdir(foldername+'/EBP2022')
                resultbox.configure(state="normal")
                resultbox.insert(tk.END, f'• Dossier EBP2022 créé dans le répertoire : {foldername}.\n')
                resultbox.configure(state="disabled")
            except PermissionError:
                resultbox.configure(state="normal")
                resultbox.insert(tk.END, '• Impossible de créer un dossier.\n     Merci de relancer le script en Administrateur, ou de sélectionner un dossier auquel vous avez accès!\n')
                resultbox.configure(state="disabled")
            except Exception as e:
                resultbox.configure(state="normal")
                resultbox.insert(tk.END, f'• Dossier EBP2022 existant dans le répertoire : {foldername}.\n')
                resultbox.configure(state="disabled")
    
        EBP.wait(resultbox)

        try:
            os.mkdir(os.environ['PROGRAMDATA']+'/EBP')
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, '• Dossier PROGRAMDATA\EBP créé.\n')
            resultbox.configure(state="disabled")
        except PermissionError:
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, '• Impossible de créer le dossier PROGRAMDATA\EBP !\n     Merci de relancer le script en Administrateur.\n')
            resultbox.configure(state="disabled")
        except Exception as e:
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f'• Dossier \"%PROGRAMDATA%\EBP\" existant.\n')
            resultbox.configure(state="disabled")



        for elem in choice :

            EBP.wait(resultbox)

            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"\n\n")
            resultbox.insert(tk.END, f" • {elem[0]} | [{choice.index(elem)+1}/{len(choice)}]")
            resultbox.insert(tk.END,f"\n   • Téléchargement de {elem[1]}.exe : en cours\n")
            resultbox.configure(state="disabled") 

            EBP.wait(resultbox)
            if not os.path.isdir(elem[3]):
                if not os.path.isfile(foldername+f"/EBP2022/{elem[1]}.exe"):
                    progressbar1 = customtkinter.CTkProgressBar(master=app, mode="indeterminate", indeterminate_speed=0.675, variable=customtkinter.IntVar(value=1))
                    progressbar1.place(relx=0.3, rely=0.8, anchor=customtkinter.CENTER)
                    progressbar1.set(0.0)
                    progressbar1.start()
                    try:
                        EBP.wait(resultbox)

                        #"DOWNLOAD"
                        t2=Thread(target=EBP.MegaDownload,kwargs={"elem" : elem[2]})
                        t2.start()

                        while t2.is_alive():
                            EBP.waitprogressbar(resultbox)

                        #mega = Mega()
                        #mega.download_url(elem,foldername+'/EBP2022/')

                        resultbox.configure(state="normal")
                        resultbox.insert(tk.END, f"        • Téléchargement de {elem[1]} : OK\n")
                        resultbox.configure(state="disabled")

                        progressbar1.destroy()

                        EBP.wait(resultbox)

                        resultbox.configure(state="normal")
                        resultbox.insert(tk.END, f"          • Installation de {elem[1]} : en cours\n")
                        resultbox.configure(state="disabled")

                        EBP.wait(resultbox)

                        progressbar2 = customtkinter.CTkProgressBar(master=app, mode="indeterminate", indeterminate_speed=0.675, variable=customtkinter.IntVar(value=1))
                        progressbar2.place(relx=0.7, rely=0.8, anchor=customtkinter.CENTER)
                        progressbar2.set(0.0)
                        progressbar2.start()

                        t2=Thread(target=EBP.InstallProduct_dl,kwargs={"elem" : elem[1],"resultbox" : resultbox, "progressbar2" : progressbar2})
                        t2.start()
                        #InstallProduct_dl(elem,resultbox,progressbar2)

                        while t2.is_alive():
                            EBP.waitprogressbar(resultbox)

                    except WindowsError as a:
                        if os.path.isfile(foldername+'/EBP2022/'+elem[1]+'.exe'):

                            resultbox.configure(state="normal")
                            resultbox.insert(tk.END, f"        • Téléchargement de {elem[1]} : OK\n")
                            resultbox.configure(state="disabled")

                            progressbar1.destroy()

                            EBP.wait(resultbox)

                            resultbox.configure(state="normal")
                            resultbox.insert(tk.END, f"          • Installation de {elem[1]} : en cours\n")
                            resultbox.configure(state="disabled")

                            EBP.wait(resultbox)

                            t2=Thread(target=EBP.InstallProduct_dl,kwargs={"elem" : elem[1],"resultbox" : resultbox, "progressbar2" : progressbar2})
                            t2.start()
                            #InstallProduct_dl(elem,resultbox,progressbar2)

                            while t2.is_alive():
                                EBP.waitprogressbar(resultbox)
                        else:
                            resultbox.configure(state="normal")
                            resultbox.insert(tk.END, f"            • [WindowsError] - Fichier introuvable ! Merci de contacter informatique@ecoris.fr, avec l\'aide du fichier \'EBPInstaller_Rapport_Erreurs.txt\' généré sur votre Bureau (ou sur la session administrateur), pour signaler cette erreur !\n")
                            resultbox.configure(state="disabled")
                            Failed_List.append(elem)
                            try:
                                os.system(f"echo Erreur Telechargement {elem[1]} - WindowsError - {a} >> %userprofile%/Desktop/EBPInstaller_Rapport_Erreurs.txt")
                            except:
                                pass
                    except Exception as e:
                        resultbox.configure(state="normal")
                        resultbox.insert(tk.END, f"            • Fichier introuvable ! Merci de contacter informatique@ecoris.fr, avec l\'aide du fichier \'EBPInstaller_Rapport_Erreurs.txt\' généré sur votre Bureau (ou sur la session administrateur), pour signaler cette erreur !\n")
                        resultbox.configure(state="disabled")
                        Failed_List.append(elem)
                        try:
                            os.system(f"echo Erreur Telechargement {elem[1]} - WindowsError - {e} >> %userprofile%/Desktop/EBPInstaller_Rapport_Erreurs.txt")
                        except:
                            pass
                else:

                    EBP.wait(resultbox)
                    resultbox.configure(state="normal")
                    resultbox.insert(tk.END, f"        • {elem[1]}.exe est déjà téléchargé dans le dossier {foldername}/EBP2022\n")
                    resultbox.configure(state="disabled")

                    EBP.wait(resultbox)

                    resultbox.configure(state="normal")
                    resultbox.insert(tk.END, f"          • Installation de {elem[1]} : en cours\n")
                    resultbox.configure(state="disabled")

                    EBP.wait(resultbox)

                    progressbar2 = customtkinter.CTkProgressBar(master=app, mode="indeterminate", indeterminate_speed=0.675, variable=customtkinter.IntVar(value=1))
                    progressbar2.place(relx=0.7, rely=0.8, anchor=customtkinter.CENTER)
                    progressbar2.set(0.0)
                    progressbar2.start()

                    EBP.wait(resultbox)

                    
                    t2=Thread(target=EBP.InstallProduct_dl,kwargs={"elem" : elem[1],"resultbox" : resultbox, "progressbar2" : progressbar2})
                    t2.start()
                    #InstallProduct_dl(elem,resultbox,progressbar2)

                    while t2.is_alive():
                        EBP.waitprogressbar(resultbox)

            else:
                resultbox.configure(state="normal")
                resultbox.insert(tk.END, f"     • {elem[1]} est déjà installé [Dossier d'installation présent]\n")
                resultbox.configure(state="disabled")
                Failed_List.append(elem)

            EBP.wait(resultbox)

        EBP.wait(resultbox)
        EBP.licenseXML(choice,Failed_List,resultbox)

    
    def MegaDownload(elem):
        mega = Mega()
        mega.download_url(elem,foldername+'/EBP2022/')
    
    def InstallProduct(elem,resultbox,progressbar2):
        if os.system(foldername+"/EBP2022/"+elem+".exe /s NETWORK=FALSE PERSONALIZED=TRUE WEBCHECKED=FALSE > nul") == 0: #
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"            • Installation de {elem} : OK\n")
            resultbox.configure(state="disabled")
            progressbar2.destroy()
        else:
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"            • Erreur ! L'installation de {elem} a échoué !\n")
            resultbox.configure(state="disabled")
            Failed_List.append(elem)
            progressbar2.destroy()
            try:
                os.system(f"echo Erreur installation {foldername}\EBP2022\{elem}.exe >> %userprofile%/Desktop/EBPInstaller_Rapport_Erreurs.txt")
            except:
                pass

    def InstallProduct_WindowsError(elem,resultbox,progressbar2):
        if os.system(foldername+"/EBP2022/"+elem+".exe /s NETWORK=FALSE PERSONALIZED=TRUE WEBCHECKED=FALSE > nul") == 0: #
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"            • Installation de {elem} : OK\n")
            resultbox.configure(state="disabled")
            progressbar2.destroy()
        else:
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"            • Erreur ! L'installation de {elem} a échoué !\n")
            resultbox.configure(state="disabled")
            Failed_List.append(elem)
            progressbar2.destroy()
            try:
                os.system(f"echo WindowsError - Erreur installation {foldername}\EBP2022\{elem}.exe >> %userprofile%/Desktop/EBPInstaller_Rapport_Erreurs.txt")
            except:
                pass

    def InstallProduct_dl(elem,resultbox,progressbar2):
        if os.system(foldername+"/EBP2022/"+elem+".exe /s NETWORK=FALSE PERSONALIZED=TRUE WEBCHECKED=FALSE > nul") == 0: #
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"            • Installation de {elem} : OK\n")
            resultbox.configure(state="disabled")
            progressbar2.destroy()
        else:
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"            • Erreur ! L'installation de {elem} a échoué !\n")
            resultbox.configure(state="disabled")
            Failed_List.append(elem)
            progressbar2.destroy()
            try:
                os.system(f"echo [Already_DL] - Erreur installation - {foldername}\EBP2022\{elem}.exe >> %userprofile%/Desktop/EBPInstaller_Rapport_Erreurs.txt")
            except:
                pass


    def licenseXML(list,error,resultbox):
        global no_ebp

        no_ebp=False

        EBP.wait(resultbox)

        for elem in error:
            try:
                list.remove(elem)
            except:
                pass
        
        resultbox.configure(state="normal")
        resultbox.insert(tk.END, f"\n\n")
        resultbox.insert(tk.END, f"   • Configuration des licences.\n")
        resultbox.configure(state="disabled")
        EBP.wait(resultbox)

        if list:
            if os.path.isfile(os.environ['PROGRAMDATA']+'/EBP/license.xml'):

                resultbox.configure(state="normal")
                resultbox.insert(tk.END, f"     • Un fichier de licence existe.\n")
                resultbox.configure(state="disabled")

                EBP.wait(resultbox)
                try:
                    with open(os.environ['PROGRAMDATA']+'/EBP/license.xml', 'r') as fr:
                        lines = fr.readlines()
                        with open(os.environ['PROGRAMDATA']+'/EBP/license-new.xml', 'w') as fw:
                            for line in lines:
                                if line.strip('\n') != '</ApplicationsLicenses>':
                                    fw.write(line)
                            for elem in list:
                                fw.write(elem[4][1:] if list.index(elem)==0 else elem[4])

                            fw.write('\n</ApplicationsLicenses>')
                        fw.close()
                    fr.close()
                    with open(os.environ['PROGRAMDATA']+'/EBP/license-new.xml', 'r+') as fd:
                        lines = fd.readlines()
                        fd.seek(0)
                        fd.writelines(line for line in lines if line.strip())
                        fd.truncate()
                    fd.close()

                    path = os.replace(os.environ['PROGRAMDATA']+'/EBP/license-new.xml', os.environ['PROGRAMDATA']+'/EBP/license.xml')

                    resultbox.configure(state="normal")
                    resultbox.insert(tk.END, f"        • Fichier de licence modifié !\n")
                    resultbox.configure(state="disabled")

                    EBP.wait(resultbox)
                except:
                    resultbox.configure(state="normal")
                    resultbox.insert(tk.END, f"        • Une erreur est survenue lors de la modification du fichier de licence !\n          Merci de contacter informatique@ecoris.fr pour signaler cette erreur !\n")
                    resultbox.configure(state="disabled")

                    EBP.wait(resultbox)
                    
            else:

                resultbox.configure(state="normal")
                resultbox.insert(tk.END, f"        • Aucun fichier de licence existant.\n")
                resultbox.configure(state="disabled")

                EBP.wait(resultbox)
                try:
                    with open(os.environ['PROGRAMDATA']+'/EBP/license.xml', 'w') as fw:
                        fw.write('<ApplicationsLicenses>\n')
                        for elem in list:
                                fw.write(elem[4][1:] if list.index(elem)==0 else elem[4])
                        fw.write('\n</ApplicationsLicenses>')
                    fw.close()

                    with open(os.environ['PROGRAMDATA']+'/EBP/license.xml', 'r+') as fd:
                        lines = fd.readlines()
                        fd.seek(0)
                        fd.writelines(line for line in lines if line.strip())
                        fd.truncate()
                    fd.close()

                    resultbox.configure(state="normal")
                    resultbox.insert(tk.END, f"          • Fichier de licence créé !\n")
                    resultbox.configure(state="disabled")

                    EBP.wait(resultbox)
                    
                except:

                    resultbox.configure(state="normal")
                    resultbox.insert(tk.END, f"          • Une erreur est survenue lors de la création du fichier de licence !\n            Merci de contacter informatique@ecoris.fr pour signaler cette erreur !\n")
                    resultbox.configure(state="disabled")

                    EBP.wait(resultbox)
        else:

            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"          • Aucune nouvelle application n'a été installée. Le fichier de licence ne sera pas modifié.\n")
            resultbox.configure(state="disabled")
            no_ebp=True

            EBP.wait(resultbox)
        
        for elem in Event_Swtichcase:
            try:
                func = getattr(EBP, elem[1])
                Installation=True
                func(elem[1], Installation, None, elem[0][-3:], resultbox)
            except:
                pass

        
        EBP.wait(resultbox)
        resultbox.configure(state="normal")
        resultbox.insert(tk.END, f"\n\n")
        resultbox.insert(tk.END, f"   • Instance terminée. Fermeture de l'application.\n")
        resultbox.configure(state="disabled")
        EBP.wait(resultbox)
        EBP.wait(resultbox)
        EBP.wait(resultbox)
        EBP.wait(resultbox)
        EBP.wait(resultbox)
        EBP.wait(resultbox)
        EBP.wait(resultbox)
        EBP.wait(resultbox)
        EBP.wait(resultbox)
        EBP.wait(resultbox)

        try:
            os.system(f"exit")
        except:
            exit()
        else:
            os._exit(0)


    def nettoyage(folder, resultbox):
        
        resultbox.configure(state="normal")
        resultbox.insert(tk.END, f"\n\n")
        resultbox.insert(tk.END, f"   • Phase de nettoyage.\n")
        resultbox.configure(state="disabled")
        EBP.wait(resultbox)
        progressbar3 = customtkinter.CTkProgressBar(master=app, mode="indeterminate", indeterminate_speed=0.675, variable=customtkinter.IntVar(value=1))
        progressbar3.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
        progressbar3.set(0.0)
        progressbar3.start()

        if os.path.isdir(folder+'/EBP2022'):
            try:
                shutil.rmtree(folder+'/EBP2022')

                resultbox.configure(state="normal")
                resultbox.insert(tk.END, f"     • Dossier EBP2022 supprimé.\n")
                resultbox.configure(state="disabled")

                EBP.wait(resultbox)

                progressbar3.destroy()
            except:

                resultbox.configure(state="normal")
                resultbox.insert(tk.END, f"     • Impossible de supprimer le dossier EBP2022 !\n   Merci de vous rendre dans {foldername} et de supprimer le dossier EBP2022\n")
                resultbox.configure(state="disabled")

                EBP.wait(resultbox)

                progressbar3.destroy()
        else:
            EBP.wait(resultbox)
            resultbox.configure(state="normal")
            resultbox.insert(tk.END, f"     • Aucun dossier EBP2022.\n")
            resultbox.configure(state="disabled")
            EBP.wait(resultbox)


    def CheckVersion():
        request = requests.get('https://github.com/greverdy/EBPInstaller2022/blob/main/v.'+version_package+'.md')
        if request.status_code == 200:
            messagebox.showinfo('CheckVersion', 'Utilitaire à jour !')
        else:
            check_y_n = messagebox.askyesno('CheckVersion', 'Utilitaire obsolète !\nUne nouvelle version semble disponible sur https://soft.ecoris.fr\nVoulez vous ouvrir le site internet ?')
            if check_y_n :
                try:
                    os.system('start msedge soft.ecoris.fr')
                except:
                    os.system('start firefox soft.ecoris.fr')
                else:
                    pass



    def CheckUpdateCommand():
        global resultmaj
        resultmaj = os.popen('powershell -command "$session = New-Object -com "Microsoft.Update.Session"; "$searcher = $session.CreateUpdateSearcher()"; "$results = $searcher.search(\'IsInstalled=0\')"; " $results.updates.count"').read()


    def CheckUpdate():
        checkmaj=Thread(target=EBP.CheckUpdateCommand)
        checkmaj.start()
        messagebox.showinfo('CheckUpdate', 'Merci d\'attendre le temps que le programme calcul la présence de mise à jour !')
        while checkmaj.is_alive():
            EBP.waitprogressbar("check")
        if resultmaj.strip() == "0" :
            messagebox.showinfo('CheckUpdate', 'Aucune mise à jour en attentes !')
        else:
            check_y_n = messagebox.askyesno('CheckUpdate', 'Des mises à jour sont en attentes ! Ouvrir Windows update ?')
            if check_y_n :
                try:
                    os.system('start ms-settings:windowsupdate')
                except:
                    pass


    def ApprovePackage():
        check_y_n = messagebox.askyesno('ApprovePackage', 'Souhaitez-vous approuver ce package ?')
        if check_y_n :
            try:
                os.system('start msedge "https://feedback.smartscreen.microsoft.com/feedback.aspx?v=6&t=16&result=block&type=download&dr=1&osVer=10.0.19045.2006.vb_release&prodGuid=381ddd1e-e600-42de-94ed-8c34bf73f16d&locale=fr-FR&fv=1.2.2211.6&url=aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2dyZXZlcmR5L0VCUEluc3RhbGxlcjIwMjIvbWFpbi9FQlAyMDIyLmV4ZQ%3D%3D&refUrl=aHR0cHM6Ly9zb2Z0LmVjb3Jpcy5mci8%3D&fn=RUJQMjAyMiAoMSkuZXhl&fh=e36e2673cc7b47fa52fa9d440359eb0bf2f7eea190d688f36e7772685d3e68d1&vs=0&sn=RUNPUklT&sh=d2684002447fdf0b45ab03081be69c45319c3830&in=RUNPUklT&ih=0000000000000000000000000000000000000000&corrId=B29A3CC7-7B57-4EEC-9769-78BB799C02A6"')
            except:
                os.system('start firefox "https://feedback.smartscreen.microsoft.com/feedback.aspx?v=6&t=16&result=block&type=download&dr=1&osVer=10.0.19045.2006.vb_release&prodGuid=381ddd1e-e600-42de-94ed-8c34bf73f16d&locale=fr-FR&fv=1.2.2211.6&url=aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2dyZXZlcmR5L0VCUEluc3RhbGxlcjIwMjIvbWFpbi9FQlAyMDIyLmV4ZQ%3D%3D&refUrl=aHR0cHM6Ly9zb2Z0LmVjb3Jpcy5mci8%3D&fn=RUJQMjAyMiAoMSkuZXhl&fh=e36e2673cc7b47fa52fa9d440359eb0bf2f7eea190d688f36e7772685d3e68d1&vs=0&sn=RUNPUklT&sh=d2684002447fdf0b45ab03081be69c45319c3830&in=RUNPUklT&ih=0000000000000000000000000000000000000000&corrId=B29A3CC7-7B57-4EEC-9769-78BB799C02A6"')
            else:
                pass
    #


    def display_version():
        messagebox.showinfo('display_version', '-----------------------------------\n          Version : '+version_package+'\n        Version GUI 1.0\n-----------------------------------')


    def display_help():
        messagebox.showinfo('display_help', '--------------------------------------------------\n       Pour une demande d\'aide \n        ou pour signaler un bug \n      merci d\'envoyer un mail à :\n\n         informatique@ecoris.fr.\n\n--------------------------------------------------')


    def display_information():
        messagebox.showinfo('display_information', '--------------------------------------------------\n L\'exécutable \"EBP2022.exe\" vous\n  permettra d\'installer la suite de\nlogiciel EBP en fonction de vos choix.\n\n  Pour plus d\'informations, merci\n  de vous rendre sur soft.ecoris.fr\n     et de cliquer sur \"dépôt\"\n--------------------------------------------------')
            


#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#


#                                                            ╔═══════════════════════╗
#                                                            ║    VARIABLES FIXES    ║
#                                                            ╚═══════════════════════╝


EBP_List_Logiciel =[
["EBPOL 2022 Autonome Paie","EBPOL_2022_Autonome_Paie_13_14_0_13423","https://mega.nz/file/AONFyC4L#R6WNqniUKo53vq0zbDUMA6cBE6tKah7z2-S20Pge4bQ","C:\\Program Files\\EBP\\Payroll13.14FRFR50"],
["EBPOL 2022 Classic BusinessPlan","EBPOL_2022_Classic_BusinessPlan_14_0_0_2005","https://mega.nz/file/Na0Q3QDR#7rO8M_acqY9-AwaP3cgxjh6r3LrBvliu8t-myvCYlyQ","C:\\Program Files\\EBP\\BusinessPlan14.0FRFR20"],
["EBPOL 2022 LigneOL CRM","EBPOL_2022_LigneOL_CRM_14_0_0_1201","https://mega.nz/file/0D8wxLzY#f1lgrzkx0lvfQuLL_WMXHzT87UmfYOoCo60hFD1LlRw","C:\\Program Files\\EBP\\CRM14.0FRFR40"],
["EBPOL 2022 LigneOL Immos","EBPOL_2022_LigneOL_Immos_14_0_0_3619","https://mega.nz/file/VfNDjDQT#Dv4pkwA2ffQ96sr1Wgw7DxupkNYgh29q3Qj7bJhXKBI","C:\\Program Files\\EBP\\CapitalAsset14.0FRFR40"],
["EBP 2022 Comptabilite ELITE","EBP_2022_Comptabilite_ELITE_21_0_0_9593","https://mega.nz/file/Ne1DkYqD#SLvfwS87Q-9hPxfPi9cTAuX4LXVM8Z6GYJQzNT68f7s","C:\\Program Files\\EBP\\Accounting21.0FRFR40"],
["EBP 2022 Etats Financiers PRO","EBP_2022_Etats_Financiers_PRO_21_3_1_3765","https://mega.nz/file/pLt0gKjK#83t7ckEzf_iVNGnFYbyE56ru-_-3l9jeSsKE4gRJo74","C:\\Program Files\\EBP\\FinState21.3FRFR30"],
["EBP 2022 Gestion ELITE","EBP_2022_Gestion_ELITE_21_1_0_6632","https://mega.nz/file/4DdgHBBK#R6jsDhpc7Ad5638_GFAmikD28SWuwK7R4THAjoncmXw","C:\\Program Files\\EBP\\Invoicing21.1FRFR40"]
]

EBP_List_Select = []

Failed_List=[]

Event_Swtichcase=[
["Supprimer les packages après l'installation : Non","delete_EBP_packages","Non","normal"],
["Redémarrer après l'installation : Non","restart","Non","normal"],
["Chemin par défault : %LOCALAPPDATA%", "Change_path","Oui","normal"]
]
#["Générer le rapport d'erreur : Oui", "log","Oui","disabled"]

version_package="1.4.1"

#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#


#                                                            ╔════════════╗
#                                                            ║    CODE    ║
#                                                            ╚════════════╝

if __name__ == "__main__":
    try:
        with open("C:/Windows/AdminTry_EBP2022.log", 'w') as testAdmin:
            print("")
        testAdmin.close()
        os.system("del C:/Windows/AdminTry_EBP2022.log")
    except:
        messagebox.showerror('NOT ADMIN', '---------------------------------------------\n  Merci de relancer EBP2022.exe\n           en Administrateur !\n---------------------------------------------')
        try:
            os.system(f"exit")
        except:
            exit()
        else:
            os._exit(0)
    app = EBP()
    app.mainloop()
    try:
        os.system(f"exit")
    except:
        exit()
    else:
        os._exit(0)
    

#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#
#╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬#



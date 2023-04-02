from tkinter import *
from tkinter import messagebox
from customtkinter import CTkCheckBox
import DataUser
import customtkinter as ctk

tela = ctk.CTk()

frame_home = ctk.CTkFrame(master=tela, width=350, height=380, corner_radius=20)
frame_home.pack(side=RIGHT)

into_label = ctk.CTkLabel(master=frame_home, text="este projeto é uma GUI (interface gráfica do usuário)            \n"
                                                     "com a finalidade de logar/cadastrar o usuário para              \n"
                                                     "que haja uma interação entre o usuário e o código               \n"
                                                     "por trás dessa interface gráfica e também para de-              \n"
                                                     "monstrar algumas das minhas skills de back-end na            \n"
                                                     "linguagem de programação python.                                      \n", font=("Roboto", 12, 'bold'))

into_label.place(x=10, y=130)

about_label = ctk.CTkLabel(master=frame_home, text="By: Haba")
about_label.place(x=160, y=350)

about_tema = ctk.CTkLabel(master=frame_home, text="About the Project", font=('Roboto', 30, 'bold'))
about_tema.place(x=50, y=40)

pyt = PhotoImage(file="fotos/py.png")
pyt_label = ctk.CTkLabel(master=frame_home, image=pyt, text="")
pyt_label.place(x=220, y=350)

pyt = PhotoImage(file="fotos/pyt1.png")
pyt_label = ctk.CTkLabel(master=tela, image=pyt, text="")
pyt_label.place(x=40, y=110)


class Application():
    def __init__(self):
        self.tela = tela
        self.tema()
        self.layout()
        self.tela_login()
        tela.mainloop()

    @staticmethod
    def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def layout(self):
        self.tela.geometry("700x400")
        self.tela.title("Access Panel")
        self.tela.iconbitmap("fotos/pro.ico")
        self.tela.resizable(width=False, height=False)

    @staticmethod
    def tela_login():
        img = PhotoImage(file="fotos/login.png")
        img_Label = ctk.CTkLabel(master=tela, image=img, text="")
        img_Label.place(x=5000, y=90)

        frame = ctk.CTkFrame(master=tela, width=350, height=380, corner_radius=20)
        frame.pack_forget()

        def Home():
            img_Label.place(x=50, y=90)
            frame.pack(side=RIGHT)
            frame_home.pack_forget()

        next_button = ctk.CTkButton(master=frame_home, text="NEXT", width=200, hover_color="#000000", corner_radius=80, command=Home)
        next_button.place(x=90, y=270)

        copy = PhotoImage(file="fotos/C.png")
        copy = ctk.CTkLabel(master=frame, text="", image=copy)
        copy.place(x=220, y=355)

        copy_Label = ctk.CTkLabel(master=frame, text="Haba 2023", font=('Roboto', 10, 'bold'))
        copy_Label.place(x=160, y=355)

        git = PhotoImage(file="fotos/git.png")
        git_Label = ctk.CTkLabel(master=frame, image=git, text="")
        git_Label.place(x=315, y=350)

        link = PhotoImage(file="fotos/link.png")
        link_Label = ctk.CTkLabel(master=frame, image=link, text="")
        link_Label.place(x=280, y=350)

        sis = ctk.CTkLabel(master=frame, text="Login", font=('Roboto', 30, 'bold'))
        sis.place(x=150, y=40)

        EntryName = ctk.CTkEntry(master=frame, placeholder_text="Username", width=290, height=0,
                                     font=("Roboto", 20, 'bold'))
        EntryName.place(x=30, y=105)

        EntryPassword = ctk.CTkEntry(master=frame, placeholder_text="Password", width=290, height=0,
                                         font=("Roboto", 20, 'bold'), show="*")
        EntryPassword.place(x=30, y=170)

        chekbox = ctk.CTkCheckBox(master=frame, text="remember me")
        chekbox.place(x=30, y=235)

        def Login():
            User = EntryName.get()
            Pass = EntryPassword.get()
            DataUser.cursor.execute("""
            SELECT * FROM Users
            WHERE User = ? and Password = ?
            """, (User, Pass))
            print('Carregando...')
            VerifyLogin = DataUser.cursor.fetchone()
            try:
                if User in VerifyLogin and Pass in VerifyLogin:
                    messagebox.showinfo(title="Login Info", message="Login sucefull")

            except:
                messagebox.showinfo(title="Login Info",
                                    message="access denied, check if you are registered in the system")

        LoginButton = ctk.CTkButton(master=frame, text="Login", width=200, hover_color="#000000", corner_radius=80, command=Login)
        LoginButton.place(x=90, y=270)

        def Register():
            LoginButton.place(x=5000)
            RegisterButton.place(x=5000)
            frame.pack_forget()
            img_Label.place(x=5000)
            cadastro = ctk.CTkFrame(master=tela, width=350, height=380, corner_radius=20)
            cadastro.pack(side=RIGHT)

            cadastre_tema = ctk.CTkLabel(master=cadastro, text="Register", font=('Roboto', 30, 'bold'))
            cadastre_tema.place(x=130, y=40)

            reg = PhotoImage(file="fotos/register.png")
            reg_label = ctk.CTkLabel(master=tela, image=reg, text="")
            reg_label.place(x=40, y=100)

            NameUser = ctk.CTkEntry(master=cadastro, placeholder_text="Full Name", width=290, height=0,
                                        font=("Roboto", 20, 'bold'))
            NameUser.place(x=30, y=105)

            EntryEmail = ctk.CTkEntry(master=cadastro, placeholder_text="Email", width=290, height=0,
                                          font=("Roboto", 20, 'bold'))
            EntryEmail.place(x=30, y=145)

            Password = ctk.CTkEntry(master=cadastro, placeholder_text="Password", width=290, height=0,
                                        font=("Roboto", 20, 'bold'), show="*")
            Password.place(x=30, y=185)

            Confirma_Password = ctk.CTkEntry(master=cadastro, placeholder_text="Confirm Password", width=290, height=0,
                                                 font=("Roboto", 20, 'bold'), show="*")
            Confirma_Password.place(x=30, y=225)

            chekbox: CTkCheckBox = ctk.CTkCheckBox(master=cadastro, text="I accept all terms and privacy policies")
            chekbox.place(x=30, y=265)

            def RegisterDataUser():
                Name = NameUser.get()
                Email = EntryEmail.get()
                User = EntryName.get()
                Pass = Password.get()

                if Name == "" and Email == "" and User == "" and Pass == "":
                    messagebox.showerror(title="register error", message="fill in all fields")
                else:
                    DataUser.cursor.execute("""
                        INSERT INTO Users(Name, Email, User, Password) VALUES(?,?,?,?)
                    """, (Name, Email, User, Pass))
                    DataUser.conn.commit()
                    messagebox.showinfo(title="Registe Info", message="account created successfully")

            Register = ctk.CTkButton(cadastro, text="Register", width=150, hover_color="#000000", corner_radius=80, command=RegisterDataUser)
            Register.place(x=110, y=330)

            def back():
                cadastro.pack_forget()
                frame.pack(side=RIGHT)
                reg_label.place(x=5000)
                img_Label.place(x=50)
                Register.place(x=5000)
                LoginButton.place(x=90)
                RegisterButton.place(x=140)

            back = ctk.CTkButton(master=cadastro, text="Back", width=10, fg_color="gray", hover_color="#000000", corner_radius=80,command=back)
            back.place(x=30, y=330)

        RegisterButton = ctk.CTkButton(frame, text="Register", width=100, hover_color="#000000", corner_radius=80, command=Register)
        RegisterButton.place(x=140, y=320)

        RegisterLabel = ctk.CTkLabel(master=frame, text="not registered?", font=("Roboto", 11, 'bold'))
        RegisterLabel.place(x=40, y=320)


Application()

import tkinter as Tk
from tkinter import *
from tkinter.tix import *
from tkinter import messagebox, ttk
import numpy as np
import pymysql
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

class Register:

    def temp_text(self):
        self.txt_email.delete(0,"end")

    def __init__(self,root):
        self.root= root
        self.root.title("Cálculo de reservas")
        self.root.geometry("1350x700+0+0") 
    
        
        #Background image
        self.bg=ImageTk.PhotoImage(file="imagenes/azul1.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)
        
        #Welcome frame
        frame1=Frame(self.root, bg="white")
        frame1.place(x=800, y=100, width=400, height=500)

        title=Label(frame1, text="YAGLE",font=("times new roman", 50, "bold"),bg = "white",fg="black").place(x=75, y=20)
        title2=Label(frame1, text="Cálculo de reservas - Versión 2.0",font=("times new roman", 20, "bold"),bg = "white" , fg="black").place(x=5, y=100) 
        
        btn_login=Button(frame1, text="Comenzar", command=self.iniciar, font=("times new roman",30, "bold"),bg="blue", fg="white", cursor="hand2").place(x=25, y=240, width=350, height=60)
        
        
        #Left image
        self.left=ImageTk.PhotoImage(file="imagenes/left3.jpg")
        #left=Label(self.root, image=self.left).place(x=80, y=100, width=400,height=500)
        
        #self.photo_=ImageTk.PhotoImage(file="imagenes/logoudo.jpg")
        #photo_=Label(frame1, image=self.photo_).place(x=10, y=10, width=100, height= 100)

    def conociendome(self):
        self.root=root
        self.root.title("Conociendome")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #Background image
        self.bg=ImageTk.PhotoImage(file="imagenes/azul1.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        #Register frame
        frame1=Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title=Label(frame1, text="Software YAGLE 2.0",font=("times new roman", 50, "bold"),bg="white",fg="black").place(x=50, y=20)

        self.middle=ImageTk.PhotoImage(file="imagenes/Conociendome.png")
        middle=Label(frame1, image=self.middle).place(x=75, y=100, width=400,height=400)

        btn_login=Button(frame1,text="Entrar", font=("times new roman", 20), bg="Orange", cursor="hand2", command=self.iniciar).place(x=530, y=400, width=150, height=60)
        btn_formulario=Button(frame1,text="Formulario", font=("times new roman", 20), bg="Blue",fg="white", cursor="hand2", command=self.formulario).place(x=530, y=330, width=150, height=60)
       
    def formulario(self):
        self.root=root
        self.root.title("formulario")
        self.root.geometry("1350x700+0+0")
        self.bg=ImageTk.PhotoImage(file="imagenes/azul2.jpg")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        self.center=ImageTk.PhotoImage(file="imagenes/formulario.png")
        center=Label(self.root, image=self.center).place(x=40, y=80, width=1262,height=500)
        
    
        btn_vol=Button(self.root, text="Volver", command=self.conociendome, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=600, y=600, width=200, height=40)

    def registro(self):
        self.root=root
        self.root.title("Ventana de registro")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #Background image
        self.bg=ImageTk.PhotoImage(file="imagenes/azul1.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        #Register frame
        frame1=Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title=Label(frame1, text="Regístrate aquí",font=("times new roman", 20, "bold"),bg="white",fg="blue").place(x=50, y=30)

        #Nombre y apellido
        f_name=Label(frame1, text="Nombre",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=50, y=100)
        self.txt_fname=Entry(frame1, font=("times new roman",15), bg="lightgray")
        self.txt_fname.place(x=50,y=130, width=250)

        l_name=Label(frame1, text="Apellido",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=370, y=100)
        self.txt_lname=Entry(frame1, font=("times new roman",15), bg="lightgray")
        self.txt_lname.place(x=370,y=130, width=250)

        #Ocupacion e email
        ocup=Label(frame1, text="Ocupacion",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=50, y=170)
        self.txt_ocup=Entry(frame1, font=("times new roman",15), bg="lightgray")
        self.txt_ocup.place(x=50,y=200, width=250)

        email=Label(frame1, text="Email",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=370, y=170)
        self.txt_email=Entry(frame1, font=("times new roman",15), bg="lightgray")
        self.txt_email.place(x=370,y=200, width=250)
        
        #Preguntas
        question=Label(frame1, text="Pregunta de seguridad",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=50, y=240)
        self.cmb_question=ttk.Combobox(frame1, font=("times new roman",13),state="readonly", justify=CENTER)
        self.cmb_question["values"]=("Selecciona","Nombre de tu primera mascota","Lugar de nacimiento","Nombre de tu mejor amigo")
        self.cmb_question.place(x=50,y=270, width=250)
        self.cmb_question.current(0)

        answer=Label(frame1, text="Respuesta",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=370, y=240)
        self.txt_answer=Entry(frame1, font=("times new roman",15), bg="lightgray")
        self.txt_answer.place(x=370,y=270, width=250)

        #Contrasena
        password=Label(frame1, text="Contraseña",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=50, y=310)
        self.txt_password=Entry(frame1, show="*", bg="lightgray")
        self.txt_password.place(x=50,y=340, width=250, height=25)

        cpassword=Label(frame1, text="Confirmar contraseña",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=370, y=310)
        self.txt_cpassword=Entry(frame1, show="*", bg="lightgray")
        self.txt_cpassword.place(x=370,y=340, width=250, height=25)


        #Terminos y condiciones
        self.var_chk=IntVar()
        chk=Checkbutton(frame1, text="Acepto los terminos y condiciones", variable=self.var_chk,onvalue=1,offvalue=0, bg="white", font=("times new roman", 12)).place(x=50,y=380)
       
        '''
        self.btn_img=ImageTk.PhotoImage(file="imagenes/")
        btn=Button(frame1,image=self.btn_imag,bd=0,cursor=hand2).plave(x=50,y=420)
        '''
        btn_register=Button(frame1,text="Registrarte", font=("times new roman", 20), bg="Blue",fg ="White", bd=0, cursor="hand2", command=self.register_data).place(x=50, y=420)
        btn_login=Button(frame1,text="Entrar", font=("times new roman", 20), bg="Orange",fg ="black", cursor="hand2", command=self.iniciar).place(x=525, y=420)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_ocup.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_question.current(0)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_ocup.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Selecciona" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error", "Todos los campos deben llenarse", parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error", "Las contraseñas deben coincidir", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Por favor acepta los terminos y condiciones", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="",database="usuarios")
                cur=con.cursor()
                cur.execute("select * from usuarios where email=%s", self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error", "El usuario ya existe, por favor intenta con otro email", parent=self.root)
                    self.clear()
                else:   
                    cur.execute("insert into usuarios (f_name, l_name, ocup, email, question, answer, password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_ocup.get(),
                                    self.txt_email.get(),
                                    self.cmb_question.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Exitoso", "Registro exitoso", parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error", f"Error debido a: {str(es)}", parent=self.root)

    def iniciar(self):
        self.root=root
        self.root.title("Iniciar Sesion")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #Background image
        self.bg=ImageTk.PhotoImage(file="imagenes/azul1.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)
        
        #Welcome frame
        frame1=Frame(self.root, bg="white")
        frame1.place(x=800, y=100, width=400, height=500)

        title=Label(frame1, text="YAGLE",font=("times new roman", 50, "bold"),bg = "white",fg="black").place(x=75, y=20)
        title2=Label(frame1, text="Cálculo de reservas",font=("times new roman", 20, "bold"),bg = "white" , fg="black").place(x=85, y=100) 
        self.txt_email=Entry(frame1,font=("times new roman", 15, "bold"),bg="lightgray")
        self.txt_email.place(x=25, y=150, width=350, height=35)
        self.txt_email.insert(0, "Email") 

        self.txt_password=Entry(frame1,show="*",bg="lightgray")
        self.txt_password.place(x=25, y=195, width=350, height=35)
        self.txt_password.insert(0, "Contraseña")
        btn_reg=Button(frame1,cursor="hand2",text="Crear cuenta nueva", command=self.registro, font=("times new roman",14),bg="green", bd=0, fg="white").place(x=120, y=350)
        btn_forget=Button(frame1,cursor="hand2",text="¿Olvidaste tu contraseña?", command=self.forget_password, font=("times new roman",14),bg="white", bd=0, fg="orange").place(x=100, y=310)

        btn_login=Button(frame1, text="Iniciar sesión", command=self.login, font=("times new roman",30, "bold"),bg="blue", fg="white", cursor="hand2").place(x=25, y=240, width=350, height=60)
        btn_conociendo=Button(frame1,text="Conociendome", font=("times new roman", 20), bg="Orange", cursor="hand2", command=self.conociendome).place(x=100, y=400)
        
        #Left image
        self.left=ImageTk.PhotoImage(file="imagenes/left3.jpg")
        #left=Label(self.root, image=self.left).place(x=80, y=100, width=400,height=500)
        
        #self.photo_=ImageTk.PhotoImage(file="imagenes/logoudo.jpg")
        #photo_=Label(frame1, image=self.photo_).place(x=10, y=10, width=100, height= 100)
        

    def reset(self):
        self.cmb_question.current(0)
        self.txt_npassword.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password1(self):
        if self.cmb_question.get()=="Selecciona" or self.txt_answer.get()=="" or self.txt_npassword.get()=="":
            messagebox.showerror("Error", "Todos los campos deben llenarse", parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root", password="", database="usuarios")
                cur=con.cursor()
                cur.execute("select * from usuarios where email=%s and question=%s and answer=%s",(self.txt_email.get(), self.cmb_question.get(), self.txt_answer.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error", "Por favor seleccione la pregunta de seguridad / Respuesta correcta", parent=self.root2)
                else:
                    cur.execute("update usuarios set password=%s where email=%s",(self.txt_npassword.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Cambio exitoso", "Su contraseña fue cambiada, por favor inicie sesión con su nueva contraseña", parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)


    def forget_password(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error", "Por favor introduce un email para cambiar la contraseña", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root", password="", database="usuarios")
                cur=con.cursor()
                cur.execute("select * from usuarios where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error", "Por favor introduce un email valido para cambiar la contraseña", parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Olvidó contraseña")
                    self.root2.geometry("400x400+450+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t=Label(self.root2,text="Olvidó contraseña", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=10,relwidth=1)

                    #Preguntas
                    question=Label(self.root2, text="Pregunta de seguridad",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=100, y=100)

                    self.cmb_question=ttk.Combobox(self.root2, font=("times new roman",13),state="readonly", justify=CENTER)
                    self.cmb_question["values"]=("Selecciona","Nombre de tu primera mascota","Lugar de nacimiento","Nombre de tu mejor amigo")
                    self.cmb_question.place(x=70,y=130, width=250)
                    self.cmb_question.current(0)

                    answer=Label(self.root2, text="Respuesta",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=150, y=180)
                    self.txt_answer=Entry(self.root2, font=("times new roman",15), bg="lightgray")
                    self.txt_answer.place(x=70,y=210, width=250)

                    npassword=Label(self.root2, text="Nueva contraseña",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=120, y=260)
                    self.txt_npassword=Entry(self.root2,show="*", bg="lightgray")
                    self.txt_npassword.place(x=70,y=290, width=250, height=25)

                    btn_change_password=Button(self.root2, text="Cambiar contraseña", command=self.forget_password1, bg="red", fg="black",font=("times new roman", 15, "bold")).place(x=100,y=340)


            except Exception as es:
                messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)



    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "Llene todos los campos",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root", password="", database="usuarios")
                cur=con.cursor()
                cur.execute("select * from usuarios where email=%s and password=%s",(self.txt_email.get(), self.txt_password.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error", "Datos incorrectos",parent=self.root)
                else:
                    messagebox.showinfo("Inicio exitoso", "Bienvenido",parent=self.root)
                    self.ventana1()
                con.close()
            except Exception as es:
                 messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)
    
    def ventana1(self):
        self.root=root
        self.root.title("Ventana de yacimiento")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="orange")


        self.bg=ImageTk.PhotoImage(file="imagenes/azul2.jpg")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        
        frame2=Frame(self.root, bg="white")
        frame2.place(x=100, y=100, width=1100, height=500)

        title=Label(frame2, text="Escoja el tipo de yacimiento",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=250, y=80)
        btn_pet=Button(frame2,cursor="hand2",text="Yacimiento de petróleo", command=self.yaci_pet, font=("times new roman",30),bg="orange", fg="black").place(x=100, y=250, width=400, height=60)
        btn_gas=Button(frame2, text="Yacimiento de gas", command=self.yaci_gas, font=("times new roman",30),bg="orange", fg="black", cursor="hand2").place(x=590, y=250, width=400, height=60)
        btn_vol=Button(frame2, text="Cerrar sesión", command= self.iniciar, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=435, y=420, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_YAC)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_YAC)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)

    def register_calculoMV(self):
             
                con=pymysql.connect(host="localhost", user="root", password="",database="usuarios")
                cur=con.cursor()
                
                cur.execute("insert into `resultado petroleo` (Swi, ESPESOR, AREA, VOLUMEN, POROSIDAD, Boi, POES, FR, Reserva, METODO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_satagua.get(),
                                self.txt_espesor.get(),
                                self.txt_area.get(),
                                self.txt_volumen.get(),
                                self.txt_porosidad.get(),
                                self.txt_boi.get(),
                                self.txt_poes,
                                self.txt_FR,
                                self.txt_RESERVA,
                                "Metodo Volumetrico"
                                ))
                con.commit()
                con.close()
                messagebox.showinfo("Exitoso", "Registro exitoso", parent=self.root)
                self.clear()

    def register_calculoEBMCC(self):

                con=pymysql.connect(host="localhost", user="root", password="",database="usuarios")
                cur=con.cursor()
                
                cur.execute("insert into `resultado petroleo` (FR, Reserva, P, Pi, Bo, Boi, Bg, RP, Rs, Rsi, Swi, Cw, Cf, We, Wp, Bw, NP, Winy, m, Giny, Bginy, Bgi, POES, METODO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_FR,
                                self.txt_RESERVA,
                                self.txt_Pr,
                                self.txt_Pi,
                                self.txt_Bo,
                                self.txt_Boi,
                                self.txt_Bg,
                                self.txt_Rp,
                                self.txt_Rs,
                                self.txt_Rsi,
                                self.txt_Swi,
                                self.txt_Cw,
                                self.txt_Cf,
                                self.txt_We,
                                self.txt_Wp,
                                self.txt_Bw,
                                self.txt_Np,
                                self.txt_Winj,
                                self.txt_m,
                                self.txt_Ginj,
                                self.txt_Bginj,
                                self.txt_Bgi,
                                self.txt_poes,
                                "EBM con capa de gas"
                                ))
                                
                con.commit()
                con.close()
                messagebox.showinfo("Exitoso", "Registro exitoso", parent=self.root)
                self.clear()
                

    def register_calculoEBMSC(self):
             
                con=pymysql.connect(host="localhost", user="root", password="",database="usuarios")
                cur=con.cursor()
                
                cur.execute("insert into `resultado petroleo` (FR, Reserva, P, Pi, Bo, Boi, Bg, RP, Rs, Rsi, Swi, Cw, Cf, We, Wp, Bw, NP, Winy, POES, METODO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_FR,
                                self.txt_RESERVA,
                                self.txt_Pr,
                                self.txt_Pi,
                                self.txt_Bo,
                                self.txt_Boi,
                                self.txt_Bg,
                                self.txt_Rp,
                                self.txt_Rs,
                                self.txt_Rsi,
                                self.txt_Swi,
                                self.txt_Cw,
                                self.txt_Cf,
                                self.txt_We,
                                self.txt_Wp,
                                self.txt_Bw,
                                self.txt_Np,
                                self.txt_Winj,
                                self.txt_poes,
                                "EBM sin capa de gas"
                                ))
                                
                con.commit()
                con.close()
                messagebox.showinfo("Exitoso", "Registro exitoso", parent=self.root)
                self.clear()

    def register_calculoMVGC(self):
             
                con=pymysql.connect(host="localhost", user="root", password="",database="usuarios")
                cur=con.cursor()
                
                cur.execute("insert into `resultado petroleo` (FR, Reserva, POROSIDAD, API, Bgi, Swi, RGC, ESPESOR, P, AREA, T, VOLUMEN, Zgc, COES, GCOES, GOES, METODO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_FR,
                                self.txt_RESERVA,
                                self.txt_porosidad.get(),
                                self.txt_Api,
                                self.txt_Bgi,
                                self.txt_satagua.get(),
                                self.txt_rgc.get(),
                                self.txt_espesor.get(),
                                self.txt_presion.get(),
                                self.txt_area.get(),
                                self.txt_T,
                                self.txt_volumen.get(),
                                self.txt_Zgc,
                                self.txt_coes,
                                self.txt_Gcoes,
                                self.txt_Goes,
                                "Metodo Volumetrico"
                                ))
                con.commit()
                con.close()
                messagebox.showinfo("Exitoso", "Registro exitoso", parent=self.root)
                self.clear()

    def register_calculoMVGS(self):
             
                con=pymysql.connect(host="localhost", user="root", password="",database="usuarios")
                cur=con.cursor()
                
                cur.execute("insert into `resultado petroleo` (POROSIDAD, Bgi, Swi, ESPESOR, Pi, AREA, T, VOLUMEN, Z, dc, GOES, METODO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_porosidad.get(),
                                self.txt_Bgi,
                                self.txt_satagua.get(),
                                self.txt_espesor.get(),
                                self.txt_presion.get(),
                                self.txt_area.get(),
                                self.txt_T,
                                self.txt_volumen.get(),
                                self.txt_Z,
                                self.txt_dc,
                                self.txt_Goes,
                                "Metodo Volumetrico"
                                ))
                con.commit()
                con.close()
                messagebox.showinfo("Exitoso", "Registro exitoso", parent=self.root)
                self.clear()

    def register_calculoEBMGS(self):
             
                con=pymysql.connect(host="localhost", user="root", password="",database="usuarios")
                cur=con.cursor()
                
                cur.execute("insert into `resultado petroleo` (FR, Reserva, P, Pi, Bg, Bgi, Swi, Cw, Cf, We, Wp, Bw, GP, GOES, METODO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_FR,
                                self.txt_RESERVA,
                                self.txt_Pr,
                                self.txt_Pi,
                                self.txt_Bg,
                                self.txt_Bgi,
                                self.txt_Swi,
                                self.txt_Cw,
                                self.txt_Cf,
                                self.txt_We,
                                self.txt_Wp,
                                self.txt_Bw,
                                self.txt_Gp,
                                self.txt_Goes,
                                "EBM gas seco"
                                ))
                                
                con.commit()
                con.close()
                messagebox.showinfo("Exitoso", "Registro exitoso", parent=self.root)
                self.clear()


    def register_calculoEYJ(self):
             
                con=pymysql.connect(host="localhost", user="root", password="",database="usuarios")
                cur=con.cursor()
                
                cur.execute("insert into `resultado petroleo` (POROSIDAD, Swi, ESPESOR, AREA, VOLUMEN, T, Pi, RGC, API, GOES, COES, METODO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_porosidad,
                                self.txt_Swi,
                                self.txt_espesor,
                                self.txt_area,
                                self.txt_volumen,
                                self.txt_temperatura,
                                self.txt_Pi,
                                self.txt_rgc,
                                self.txt_api,
                                self.txt_Goes,
                                self.txt_coes,
                                "Correlaciones de Eaton y Jacoby"
                                ))
                                
                con.commit()
                con.close()
                messagebox.showinfo("Exitoso", "Registro exitoso", parent=self.root)
                self.clear()

    def register_calculoDP1(self):

                con=pymysql.connect(host="localhost", user="root", password="",database="usuarios")
                cur=con.cursor()

                cur.execute("insert into `declinacion` (P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, Cpa1, Cpa2, Cpa3, Cpa4, Cpa5, Cpa6, Cpa7, Cpa8, Cpa9, Cpa10, Cpa11, Z2f1, Z2f2, Z2f3, Z2f4, Z2f5, Z2f6, Z2f7, Z2f8, Z2f9, Z2f10, Z2f11, Gpt1, Gpt2, Gpt3, Gpt4, Gpt5, Gpt6, Gpt7, Gpt8, Gpt9, Gpt10, Gpt11, API, RGC, GOES, COES, GCOES, METODO) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_presion,
                                self.txt_presion1,
                                self.txt_presion2,
                                self.txt_presion3,
                                self.txt_presion4,
                                self.txt_presion5,
                                self.txt_presion6,
                                self.txt_presion7,
                                self.txt_presion8,
                                self.txt_presion9,
                                self.txt_presion10,
                                self.txt_cpa,
                                self.txt_cpa1,
                                self.txt_cpa2,
                                self.txt_cpa3,
                                self.txt_cpa4,
                                self.txt_cpa5,
                                self.txt_cpa6,
                                self.txt_cpa7,
                                self.txt_cpa8,
                                self.txt_cpa9,
                                self.txt_cpa10,
                                self.txt_z2f,
                                self.txt_z2f1,
                                self.txt_z2f2,
                                self.txt_z2f3,
                                self.txt_z2f4,
                                self.txt_z2f5,
                                self.txt_z2f6,
                                self.txt_z2f7,
                                self.txt_z2f8,
                                self.txt_z2f9,
                                self.txt_z2f10,
                                self.txt_gpt,
                                self.txt_gpt1,
                                self.txt_gpt2,
                                self.txt_gpt3,
                                self.txt_gpt4,
                                self.txt_gpt5,
                                self.txt_gpt6,
                                self.txt_gpt7,
                                self.txt_gpt8,
                                self.txt_gpt9,
                                self.txt_gpt10,
                                self.txt_api,
                                self.txt_rgc,
                                self.txt_goes,
                                self.txt_coes,
                                self.txt_gcoes,
                                "Declinacion de presion"
                                ))
                                
                con.commit()
                con.close()
                messagebox.showinfo("Exitoso", "Registro exitoso", parent=self.root)
                self.clear()

    def barraAcercade_YAC(self):
        messagebox.showinfo("Yacimiento", "Es una unidad geológica de volumen limitado, porosa y permeable, capaz de contener hidrocarburos líquidos y/o gaseosos. Este concepto implica la correlación de dos aspectos fundamentales para la industria petrolera, como lo son las consideraciones geológicas y las propiedades de los fluidos contenidos en el yacimiento.-CIED")

    def barraAyuda_YAC(self):
        messagebox.showinfo("Clasificación", "los yacimientos se puede clasificar en grupos: Yacimientos de gas y yacimientos de líquido o petróleo. ")

    def yaci_pet(self):
        self.root=root
        self.root.title("Yacimiento de petróleo")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.bg=ImageTk.PhotoImage(file="imagenes/Petroleo.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)
        
        frame3=Frame(self.root, bg="white")
        frame3.place(x=120, y=100, width=1100, height=500)    
        title=Label(frame3, text="Escoja un método de cálculo",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=250, y=80)
        btn_vol=Button(frame3, text="Volver", command=self.ventana1, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=435, y=420, width=200, height=40)
        btn_pet=Button(frame3,cursor="hand2",text="Método volumétrico", command=self.volum_pet, font=("times new roman",30),bg="orange", fg="black").place(x=70, y=250, width=350, height=60)
        btn_gas=Button(frame3, text="Ecuación de Balance de Materiales", command=self.EBM_pet1, font=("times new roman",30),bg="orange", fg="black", cursor="hand2").place(x=480, y=250, width=570, height=60)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_YACP)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_YACP)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_YACP(self):
        messagebox.showinfo("Yacimiento de Petróleo", "Las mezclas de hidrocarburos que existen en estado líquido a condiciones de yacimiento son clasificados como yacimientos de petróleo. Estos líquidos están divididos en yacimientos de petróleo de alto encogimiento y bajo encogimiento , en base a la cantidad de líquido que se produce en superficie. Además de esa clasificación existe los yacimientos saturados y subsaturados, dependiendo de las condiciones iniciales del yacimiento.-Halliburton")

    def barraAyuda_YACP(self):
        messagebox.showinfo("¿Qué método escoger?", "Esto va a depender de los datos que se tienen; los métodos de EBM permiten determinar solamente los volúmenes de petróleo que se encuentran en comunicación con los pozos de producción; por esta razón a estos métodos se le llama DINAMICO. En cambio los métodos volumétricos se tiene en cuenta el volumen total de petróleo en sitio de zonas comunicadas y no comunicadas se les llama ESTATICOS y regularmente arrojan reservas mayores a los dinámicos.")


    #Calculo Metodo volumetrico petroleo
    
    def calculos2(self):
        
        
        try:
            if self.txt_porosidad.get()=="" or self.txt_satagua.get()=="" or self.txt_boi.get()=="":
                messagebox.showerror("Error", "Por favor, llene todos los campos",parent=self.root)

            else:

                if self.txt_espesor.get()=="" and self.txt_area.get()=="":
                    boi=float(self.txt_boi.get())
                    poes=(7758*float(self.txt_porosidad.get())*float(self.txt_volumen.get())*(1-float(self.txt_satagua.get())))/boi/1000000
                    RESERVA = poes*float(self.txt_FR.get())
                    
                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    FR = float(self.txt_FR.get())
                    self.txt_FR = FR

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    t=Label(frame1,text="El POES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)
                    
                    goes1=Label(frame1, text=f'{str(poes)} MMBN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)

                    t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                    RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMBN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                
                    self.txt_RESERVA = RESERVA
                    self.txt_poes = poes
                    self.register_calculoMV()
                    
            
                if self.txt_volumen.get()=="":
                    boi=float(self.txt_boi.get())
                    poes=(7758*float(self.txt_porosidad.get())*float(self.txt_area.get())*float(self.txt_espesor.get())*(1-float(self.txt_satagua.get())))/boi/1000000

                    RESERVA = poes*float(self.txt_FR.get())    

                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    FR = float(self.txt_FR.get())
                    self.txt_FR = FR

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    t=Label(frame1,text="El POES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)
                    
                    goes1=Label(frame1, text=f'{str(poes)} MMBN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)

                    t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                    RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMBN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                    
                    self.txt_RESERVA = RESERVA
                    self.txt_poes = poes
                    self.register_calculoMV()

                if self.txt_espesor.get()!= 0 and self.txt_area.get()!= 0 and self.txt_volumen.get()!= 0:
                    messagebox.showerror("Error", "Por favor, coloque solo los valores de espesor y área o volumen",parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)

    #Informacion de inputs
    def info_porosidad(self):
        messagebox.showinfo( "Porosidad","Este valor corresponde al porcentaje de volumen de poros o espacio poroso, o el volumen de roca que puede contener fluidos.")

    def info_swi(self):
        messagebox.showinfo("Saturacion del agua","La fracción de agua de un espacio poral dado. Se expresa en volumen/volumen, porcentaje o unidades de saturación.")
    
    def info_espesor(self):
        messagebox.showinfo("Espesor","el espesor de la litología con calidad de yacimiento (generalmente arena) en la unidad.")
    
    def info_area(self):
        messagebox.showinfo("Area","Superficie acotada, que se distingue de lo que la rodea.")
    
    def info_volumen(self):
        messagebox.showinfo("Volumen","magnitud escalar definida como el espacio ocupado por un cuerpo.")
    
    def info_boi(self):
        messagebox.showinfo("Factor volumentrico inicial del petroleo","Volumen de petróleo y gas disuelto en condiciones del yacimiento dividido por el volumen del petróleo en condiciones normales.")

    def info_p(self):
        messagebox.showinfo("P(Lpca)","Presión del Yacimiento a un Tiempo dado.")
    
    def info_pi(self):
        messagebox.showinfo("Pi(Lpca)"," Presión Inicial del Yacimiento.")

    def info_bo(self):
        messagebox.showinfo("Bo(BY/BN)","Factor Volumétrico del Petróleo, BY/BN.")
    
    def info_bg(self):
        messagebox.showinfo("Bg(BY/BN)","Factor Volumétrico del Gas, BY/BN.")

    def info_bgi(self):
        messagebox.showinfo("Bgi(BY/BN)"," Factor Volumétrico del Gas a (Pi, Tf), BY/PCN.")

    def info_rp(self):
        messagebox.showinfo("Rp(PCN/BN)"," Relación Gas-Petróleo Acumulado, PCN/BN .")
    
    def info_rs(self):
        messagebox.showinfo("Rs(PCN/BN)","Relación Gas-Petróleo en Solución, PCN/BN.")

    def info_rsi(self):
        messagebox.showinfo("Rsi(PCN/BN)","Relación Gas-Petróleo en Solución inicial, PCN/BN.")

    def info_cw(self):
        messagebox.showinfo("Cw","Compresibilidad del Agua, lpc-1.")

    def info_cf(self):
        messagebox.showinfo("Cf","Compresibilidad de la Formación, lpc-1.")
    
    def info_we(self):
        messagebox.showinfo("We(BY)","Intrusión de Agua, BY.")

    def info_wp(self):
        messagebox.showinfo("Wp(BN)","Agua Producida, BN.")

    def info_bw(self):
        messagebox.showinfo("Bw(BY/BN)"," Factor Volumétrico del Agua, BY/BN.")

    def info_np(self):
        messagebox.showinfo("Np(BN)","Petróleo Producido, BN.")
    
    def info_winy(self):
        messagebox.showinfo("Winy","Agua inyectada acumulada.")
    
    def info_giny(self):
        messagebox.showinfo("Giny","Gas inyectado acumulada.")
    
    def info_bginy(self):
        messagebox.showinfo("Bginy","Factor volumétrico del gas inyectado")
    
    def info_m(self):
        messagebox.showinfo("m","Razón de Volumen de Gas Inicial y Volumen de Petróleo Inicial, adimensional.")
    
    def info_api(self):
        messagebox.showinfo("API","Gravedad API del Líquido de Tanque.")
    
    def info_rgc(self):
        messagebox.showinfo("RGC(PCN/BN)","Relación Gas-Condensado, PCN/BN.")

    def info_temperatura(self):
        messagebox.showinfo("Temperatura","magnitud física que indica la energía interna de un cuerpo, de un objeto o del medio ambiente en general.")

    def info_factor_zgc(self):
        messagebox.showinfo("Zgc","Factor de compresibilidad del gas condensado.")

    def info_factor_z(self):
        messagebox.showinfo("Factor Z","Factor de compresibilidad del gas")
    
    def info_gravedad(self):
        messagebox.showinfo("Gravedad específica","Gravedad específica del gas.")
    
    def info_gp(self):
        messagebox.showinfo("GP","Gas producido acumulado.")

    def info_FR(self):
        messagebox.showinfo("Factor de Recobro","Cantidad recuperable de hidrocarburos existente en el lugar, normalmente expresada como un porcentaje. El factor de recuperación es una función del mecanismo de desplazamiento. Un objetivo importante de la recuperación de petróleo mejorada es incrementar el factor de recuperación.")
    
    
    def volum_pet(self):
        self.root=root
        self.root.title("Yacimiento de petróleo")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        self.bg=ImageTk.PhotoImage(file="imagenes/Petroleo.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        #frame
        frame3=Frame(self.root, bg="white")
        frame3.place(x=120, y=100, width=1100, height=500)  
        title=Label(frame3, text="Introduzca la siguiente información",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=180, y=80)
        
        porosidad=Label(frame3, text="Porosidad (fraccion)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=40, y=190)
        Boton_porosidad = Button(frame3, text ="?", command= self.info_porosidad, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=220, y=190)
        self.txt_porosidad=Entry(frame3, font=("times new roman",15), bg="lightgray")
        self.txt_porosidad.place(x=60,y=220, width=150)

        satagua=Label(frame3, text="Swi (fraccion)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=265, y=190)
        Boton_satagua = Button(frame3, text ="?", command= self.info_swi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=390, y=190)
        self.txt_satagua=Entry(frame3, font=("times new roman",15), bg="lightgray")
        self.txt_satagua.place(x=260,y=220, width=150)

        espesor=Label(frame3, text="Espesor (pies)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=460, y=190)
        Boton_espesor = Button(frame3, text ="?", command= self.info_espesor, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=590, y=190)
        self.txt_espesor=Entry(frame3, font=("times new roman",15), bg="lightgray")
        self.txt_espesor.place(x=460,y=220, width=150)
        

        area=Label(frame3, text="Área (Acres) ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=670, y=190)
        Boton_area = Button(frame3, text ="?", command= self.info_area, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=790, y=190)
        self.txt_area=Entry(frame3, font=("times new roman",15), bg="lightgray")
        self.txt_area.place(x=660,y=220, width=150)
        

        volumen=Label(frame3, text="Volumen (Acres-pies)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=840, y=190)
        Boton_volumen = Button(frame3, text ="?", command= self.info_volumen, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1035, y=190)
        self.txt_volumen=Entry(frame3, font=("times new roman",15), bg="lightgray")
        self.txt_volumen.place(x=860,y=220, width=150)

        #segunda fila

        boi=Label(frame3, text="Boi (BY/BN)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=460, y=280)
        Boton_boi = Button(frame3, text ="?", command= self.info_boi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=585, y=280)
        self.txt_boi=Entry(frame3, font=("times new roman",15), bg="lightgray")
        self.txt_boi.place(x=460,y=310, width=150)

        FR=Label(frame3, text="FR (fracción)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=670, y=280)
        Boton_FR = Button(frame3, text ="?", command= self.info_FR, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=800, y=280)
        self.txt_FR=Entry(frame3, font=("times new roman",15), bg="lightgray")
        self.txt_FR.place(x=670,y=310, width=150)


        btn_cal=Button(frame3, text="Calcular", command= self.calculos2, font=("times new roman",15),bg="orange", fg="black", cursor="hand2").place(x=435, y=370, width=200, height=40)

        btn_vol=Button(frame3, text="Volver", command=self.yaci_pet, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=435, y=420, width=200, height=40)
        
        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_VOL)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_VOL)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)

         #botones de ayuda

        
    def barraAcercade_VOL(self):
        messagebox.showinfo("Método Volumétrico", "El método volumétrico es probablemente el método más fácil utilizado por los ingenieros para estimar las reservas. Requiere una cantidad limitada de datos para la estimación, ésto implica que inmediatamente después del descubrimiento de las acumulaciones de hidrocarburos, durante la delimitación inicial y el desarrollo de un campo, el método volumétrico es la clave para la estimación del volumen de hidrocarburos.-Okotie y Ikporo")

    def barraAyuda_VOL(self):
        messagebox.showinfo("Identificar si va a trabajar con Volumen o Area", "Si en los datos proporcionados, estan espesor y area, deje vacia la casilla de volumen no coloque ningún valor tampoco cero; en caso de que que se le proporcione volumen deje vacias las casillas de espesor y area, no coloque ningún numero tampoco cero. Para decimales utilice el punto.")

    def EBM_pet1(self):

        self.root=root
        self.root.title("Yacimiento de petróleo")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="imagenes/Petroleo.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        #Register frame
        frame3=Frame(self.root, bg="white")
        frame3.place(x=120, y=100, width=1100, height=500)    
        title=Label(frame3, text="Escoja si el yacimiento tiene o no capa de gas",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=50, y=80)
        btn_vol=Button(frame3, text="Volver", command=self.yaci_pet, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=435, y=420, width=200, height=40)
        btn_pet=Button(frame3,cursor="hand2",text="Sin capa de gas", command=self.EBM_pet2, font=("times new roman",30),bg="orange", fg="black").place(x=180, y=250, width=350, height=60)
        btn_gas=Button(frame3, text="Con capa de gas", command=self.EBM_pet, font=("times new roman",30),bg="orange", fg="black", cursor="hand2").place(x=600, y=250, width=350, height=60)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_EBM)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_EBM)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_EBM(self):
        messagebox.showinfo("Ecuación de Balance de Materiales (EBM)", "La Ecuación de Balance de Materiales hace uso del concepto básico de conservación de masa que establece que la producción acumulada observada, expresada como una extracción subterránea, debe ser igual a la expansión de los fluidos en el yacimiento resultante de una caída de presión finita o expresada como la masa de fluidos originalmente en el lugar igual a la masa de fluido restante más la masa de fluido producido.—Ahmed T.")

    def barraAyuda_EBM(self):
        messagebox.showinfo("Identificar si tiene capa de gas", "La capa de gas esta representada por la variable m. Si el valor de m es cero no hay capa de gas, pero si el valor de m es distinto de cero si hay capa de gas.")
    #Sin capa de gas

    def calculos6(self):

        try:
            if self.presion_.get()=="" or self.presion_inicial_.get()=="" or self.N_petroleo.get()=="" or self.B_petroleo.get()=="" or self.Bi_petroleo.get()=="" or self.Bg_gas_.get()=="" or self.produc_acum_.get()=="" or self.Rgas_petroleo_.get()=="" or self.Rigas_petroleo_.get()=="" or self.saturacion_agua_.get()=="" or self.comp_agua_.get()=="" or self.comp_roca_.get()=="" or self.intrusion_agua_.get()=="" or self.agua_producida_.get()=="" or self.B_agua_.get()=="" or self.Winy_.get()=="":
                messagebox.showerror("Error", "Por favor, llene todos los campos si no tiene algun dato coloque cero",parent=self.root)
            
            else:
                    
                Np=float(self.N_petroleo.get())
                Pr=float(self.presion_.get())
                Pi=float(self.presion_inicial_.get())
                Bo=float(self.B_petroleo.get())
                Boi=float(self.Bi_petroleo.get())
                Bg=float(self.Bg_gas_.get())
                Rp=float(self.produc_acum_.get())
                Rs=float(self.Rgas_petroleo_.get())
                Rsi=float(self.Rigas_petroleo_.get())
                Swi=float(self.saturacion_agua_.get())
                Cw=float(self.comp_agua_.get())
                Cf=float(self.comp_roca_.get())
                We=float(self.intrusion_agua_.get())
                Wp=float(self.agua_producida_.get())
                Bw=float(self.B_agua_.get())
                Winj=float(self.Winy_.get())
                FR = float(self.txt_FR.get())

                A=Np*(Bo+(Rp-Rs)*Bg)-(We-Wp*Bw)-Winj*Bw
                B=(Bo-Boi)
                C=(Rsi-Rs)*Bg
                E=Boi*(((Swi*Cw)+Cf)/(1-Swi))*(Pi-Pr)
                Poes=A/(B+C+E)/1000000
                RESERVA = Poes*float(self.txt_FR.get())

                self.txt_Pr = Pr
                self.txt_Pi = Pi
                self.txt_Bo = Bo
                self.txt_Boi = Boi
                self.txt_Bg = Bg
                self.txt_Rp = Rp
                self.txt_Rs = Rs
                self.txt_Rsi = Rsi
                self.txt_Swi = Swi
                self.txt_Cw = Cw
                self.txt_Cf = Cf
                self.txt_We = We
                self.txt_Wp = Wp
                self.txt_Bw = Bw
                self.txt_Np = Np
                self.txt_Winj = Winj
                self.txt_poes = Poes
                self.txt_RESERVA = RESERVA
                self.txt_FR = FR
                        
                self.root2=Toplevel()
                self.root2.title("Resultado")
                self.root2.geometry("400x250+400+300")
                self.root2.config(bg="white")
                self.root2.focus_force()
                self.root2.grab_set()

                frame1=Frame(self.root2, bg="white")
                frame1.place(x=1, y=1, width=500, height=500)

                t=Label(frame1,text="El POES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)               
                goes2=Label(frame1, text=f'{str(Poes)} MMBN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)
                
                t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMBN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)

                self.register_calculoEBMSC()
                            
        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)   

    def EBM_pet2(self):

        self.root=root
        self.root.title("Yacimiento de petróleo")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="imagenes/Petroleo.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)
        
        miframe=Frame(root, bg="white").place(x=100, y=100, width=1100, height=550)
        titleframe=Label(miframe, text="Introduzca los datos",font=("times new roman", 30, "bold"),bg="white",fg="black").place(x=470, y=100)

        #----------------------------------------------fila 1--------------------------------------------------
        presion=Label(miframe, text="P(Lpca):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=140, y=180)
        Boton_presion = Button(miframe, text ="?", command= self.info_p, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=265, y=180)
        self.presion_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.presion_.place(x=140,y=210, width=150)

        presion_inicial=Label(miframe, text="Pi(Lpca): ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=140, y=260)
        Boton_presion_inicial = Button(miframe, text ="?", command= self.info_pi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=265, y=260)
        self.presion_inicial_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.presion_inicial_.place(x=140,y=290, width=150)

        Bpetroleo=Label(miframe, text="Bo(BY/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=140, y=340)
        Boton_Bpetroleo = Button(miframe, text ="?", command= self.info_bo, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=265, y=340)
        self.B_petroleo=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.B_petroleo.place(x=140,y=370, width=150)

        Bipetroleo=Label(miframe, text="Boi(BY/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=140, y=420)
        Boton_Bipetroleo = Button(miframe, text ="?", command= self.info_boi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=265, y=420)
        self.Bi_petroleo=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Bi_petroleo.place(x=140,y=450, width=150)

        #---------------------------------------------fila 2-----------------------------------------
        Bg_gas=Label(miframe, text="Bg(BY/PCN):  ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=180)
        Boton_bg_gas = Button(miframe, text ="?", command= self.info_bg, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=180)
        self.Bg_gas_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Bg_gas_.place(x=420,y=210, width=150)

        produc_acum=Label(miframe, text="RP(PCN/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=260)
        Boton_produc_acum = Button(miframe, text ="?", command= self.info_rp, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=260)
        self.produc_acum_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.produc_acum_.place(x=420,y=290, width=150)

        Rgas_petroleo=Label(miframe, text="Rs(PCN/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=340)
        Boton_Rgas_petroleo = Button(miframe, text ="?", command= self.info_rs, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=340)
        self.Rgas_petroleo_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Rgas_petroleo_.place(x=420,y=370, width=150)

        Rigas_petroleo=Label(miframe, text="Rsi(PCN/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=420)
        Boton_Rigas_petroleo = Button(miframe, text ="?", command= self.info_rsi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=420)
        self.Rigas_petroleo_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Rigas_petroleo_.place(x=420,y=450, width=150)

        #---------------------------------------------fila 3-----------------------------------------------
        saturacion_agua=Label(miframe, text="Swi(fraccion):  ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=700, y=180)
        Boton_saturacion_agua = Button(miframe, text ="?", command= self.info_swi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=180)
        self.saturacion_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.saturacion_agua_.place(x=700,y=210, width=150)

        comp_agua=Label(miframe, text="Cw(lpc^-1): ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=700, y=260)
        Boton_comp_agua = Button(miframe, text ="?", command= self.info_cw, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=260)
        self.comp_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.comp_agua_.place(x=700,y=290, width=150)

        comp_roca=Label(miframe, text="Cf(lpc^-1):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=700, y=340)
        Boton_comp_roca = Button(miframe, text ="?", command= self.info_cf, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=340)
        self.comp_roca_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.comp_roca_.place(x=700,y=370, width=150)

        intrusion_agua=Label(miframe, text="We(BY):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=700, y=420)
        Boton_intrusion_agua = Button(miframe, text ="?", command= self.info_we, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=420)
        self.intrusion_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.intrusion_agua_.place(x=700,y=450, width=150)

        #-----------------------------------------------fila 4--------------------------------------------------
        agua_producida=Label(miframe, text="Wp(BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=990, y=180)
        Boton_agua_producida = Button(miframe, text ="?", command= self.info_wp, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1110, y=180)
        self.agua_producida_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.agua_producida_.place(x=980,y=210, width=150)

        B_agua=Label(miframe, text="Bw(BY/BN):  ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=990, y=260)
        Boton_B_agua = Button(miframe, text ="?", command= self.info_bw, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1110, y=260)
        self.B_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.B_agua_.place(x=980,y=290, width=150)

        Npetroleo=Label(miframe, text="NP(BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=990, y=340)
        Boton_Npetroleo= Button(miframe, text ="?", command= self.info_np, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1110, y=340)
        self.N_petroleo=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.N_petroleo.place(x=980,y=370, width=150)

        Winy=Label(miframe, text="Winy(BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=990, y=420)
        Boton_Winy = Button(miframe, text ="?", command= self.info_winy, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1110, y=420)
        self.Winy_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Winy_.place(x=980,y=450, width=150)

        #------------------------------------------5ta fila--------------------------------------------------------------------------

        FR=Label(miframe, text="FR (fracción)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=560, y=500)
        Boton_FR = Button(miframe, text ="?", command= self.info_FR, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=690, y=500)
        self.txt_FR=Entry(miframe, font=("times new roman",15), bg="lightgray")
        self.txt_FR.place(x=560,y=530, width=150)

        #-----------------------------------------final de filas-----------------------------------------------------

        #-----------------------------------------Botones--------------------------------------------------------
        btn_calular=Button(miframe, text="Calcular", font=("times new roman",15),bg="orange", fg="black", cursor="hand2", command=self.calculos6).place(x=700, y=580, width=200, height=40)

        btn_volver=Button(miframe, text="Volver", font=("times new roman",15),bg="gray", fg="black", cursor="hand2", command=self.EBM_pet1).place(x=360, y=580, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_EBMP)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_EBMP)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_EBMP(self):
        messagebox.showinfo("Ecuación de Balance de Materiales (EBM)", "La Ecuación de Balance de Materiales hace uso del concepto básico de conservación de masa que establece que la producción acumulada observada, expresada como una extracción subterránea, debe ser igual a la expansión de los fluidos en el yacimiento resultante de una caída de presión finita o expresada como la masa de fluidos originalmente en el lugar igual a la masa de fluido restante más la masa de fluido producido.—Ahmed T.")

    def barraAyuda_EBMP(self):
        messagebox.showinfo("¿Cómo sustituir los datos?", "Se debe rellenar todas las casillas, si no tiene algún dato coloque cero; para decimales utilice el punto.")

    #Calculo EBM con capa de gas

    def calculos5(self):
            
        try:
            if self.presion_.get()=="" or self.presion_inicial_.get()=="" or self.N_petroleo.get()=="" or self.B_petroleo.get()=="" or self.Bi_petroleo.get()=="" or self.Bg_gas_.get()=="" or self.Bgi_gas_.get()=="" or self.produc_acum_.get()=="" or self.Rgas_petroleo_.get()=="" or self.Rigas_petroleo_.get()=="" or self.saturacion_agua_.get()=="" or self.comp_agua_.get()=="" or self.comp_roca_.get()=="" or self.intrusion_agua_.get()=="" or self.agua_producida_.get()=="" or self.B_agua_.get()=="" or self.Giny_.get()=="" or self.Bginy_.get()=="" or self.Winy_.get()=="" or self.capa_gas_.get()=="":
                messagebox.showerror("Error", "Por favor, llene todos los campos si no tiene algun dato coloque cero",parent=self.root)
            
            else:
                    
                Np=float(self.N_petroleo.get())
                Pr=float(self.presion_.get())
                Pi=float(self.presion_inicial_.get())
                Bo=float(self.B_petroleo.get())
                Boi=float(self.Bi_petroleo.get())
                Bg=float(self.Bg_gas_.get())
                Bgi=float(self.Bgi_gas_.get())
                Rp=float(self.produc_acum_.get())
                Rs=float(self.Rgas_petroleo_.get())
                Rsi=float(self.Rigas_petroleo_.get())
                Swi=float(self.saturacion_agua_.get())
                Cw=float(self.comp_agua_.get())
                Cf=float(self.comp_roca_.get())
                m=float(self.capa_gas_.get())
                Ginj=float(self.Giny_.get())
                Bginj=float(self.Bginy_.get())
                We=float(self.intrusion_agua_.get())
                Wp=float(self.agua_producida_.get())
                Bw=float(self.B_agua_.get())
                Winj=float(self.Winy_.get())
                FR = float(self.txt_FR.get())

                A=Np*(Bo+(Rp-Rs)*Bg)-(We-Wp*Bw)-Ginj*Bginj-Winj*Bw
                B=(Bo-Boi)
                C=(Rsi-Rs)*Bg
                D=m*Boi*((Bg/Bgi-1))
                E=Boi*(1+m)*(((Swi*Cw)+Cf)/(1-Swi))*(Pi-Pr)
                Poes=A/(B+C+D+E)/1000000
                RESERVA = Poes*float(self.txt_FR.get())

                self.txt_Pr = Pr
                self.txt_Pi = Pi
                self.txt_Bo = Bo
                self.txt_Boi = Boi
                self.txt_Bg = Bg
                self.txt_Rp = Rp
                self.txt_Rs = Rs
                self.txt_Rsi = Rsi
                self.txt_Swi = Swi
                self.txt_Cw = Cw
                self.txt_Cf = Cf
                self.txt_We = We
                self.txt_Wp = Wp
                self.txt_Bw = Bw
                self.txt_Np = Np
                self.txt_Winj = Winj
                self.txt_m = m
                self.txt_Ginj = Ginj
                self.txt_Bginj = Bginj
                self.txt_Bgi = Bgi
                self.txt_poes = Poes
                self.txt_FR = FR
                self.txt_RESERVA = RESERVA
                        
                self.root2=Toplevel()
                self.root2.title("Resultado")
                self.root2.geometry("400x250+400+300")
                self.root2.config(bg="white")
                self.root2.focus_force()
                self.root2.grab_set()

                frame1=Frame(self.root2, bg="white")
                frame1.place(x=1, y=1, width=500, height=500)

                t=Label(frame1,text="El POES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)               
                poes2=Label(frame1, text=f'{str(Poes)} MMBN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)

                t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMBN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)

                self.register_calculoEBMCC()

        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)

    #Con capa de gas

    def EBM_pet(self):
        self.root=root
        self.root.title("Yacimiento de petróleo")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="imagenes/Petroleo.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)
        
        miframe=Frame(root, bg="white").place(x=100, y=100, width=1100, height=550)
        titleframe=Label(miframe, text="Introduzca los datos",font=("times new roman", 30, "bold"),bg="white",fg="black").place(x=470, y=100)

        #----------------------------------------------columna 1--------------------------------------------------
        presion=Label(miframe, text="P(Lpca):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=155, y=180)
        Boton_presion = Button(miframe, text ="?", command= self.info_p, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=270, y=180)
        self.presion_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.presion_.place(x=140,y=210, width=150)

        presion_inicial=Label(miframe, text="Pi(Lpca): ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=155, y=260)
        Boton_presion_inicial = Button(miframe, text ="?", command= self.info_pi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=270, y=260)
        self.presion_inicial_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.presion_inicial_.place(x=140,y=290, width=150)

        Npetroleo=Label(miframe, text="NP(BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=155, y=340)
        Boton_Npetroleo = Button(miframe, text ="?", command= self.info_np, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=270, y=340)
        self.N_petroleo=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.N_petroleo.place(x=140,y=370, width=150)

        Bpetroleo=Label(miframe, text="Bo(BY/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=155, y=420)
        Boton_Bpetroleo = Button(miframe, text ="?", command= self.info_bo, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=270, y=420)
        self.B_petroleo=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.B_petroleo.place(x=140,y=450, width=150)

        Bipetroleo=Label(miframe, text="Boi(BY/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=155, y=500)
        Boton_Bipetroleo = Button(miframe, text ="?", command= self.info_boi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=270, y=500)
        self.Bi_petroleo=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Bi_petroleo.place(x=140,y=530, width=150)

        #---------------------------------------------columna 2-----------------------------------------
        Bg_gas=Label(miframe, text="Bg(BY/PCN):  ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=180)
        Boton_Bg_gas = Button(miframe, text ="?", command= self.info_bg, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=180)
        self.Bg_gas_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Bg_gas_.place(x=420,y=210, width=150)

        Bgi_gas=Label(miframe, text="Bgi(BY/PCN): ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=260)
        Boton_Bgi_gas= Button(miframe, text ="?", command= self.info_bgi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=260)
        self.Bgi_gas_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Bgi_gas_.place(x=420,y=290, width=150)

        produc_acum=Label(miframe, text="RP(PCN/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=340)
        Boton_produc_acum = Button(miframe, text ="?", command= self.info_rp, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=340)
        self.produc_acum_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.produc_acum_.place(x=420,y=370, width=150)

        Rgas_petroleo=Label(miframe, text="Rs(PCN/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=420)
        Boton_Rgas_petroleo = Button(miframe, text ="?", command= self.info_rs, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=420)
        self.Rgas_petroleo_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Rgas_petroleo_.place(x=420,y=450, width=150)

        Rigas_petroleo=Label(miframe, text="Rsi(PCN/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=500)
        Boton_Rigas_petroleo= Button(miframe, text ="?", command= self.info_rsi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=500)
        self.Rigas_petroleo_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Rigas_petroleo_.place(x=420,y=530, width=150)

        #---------------------------------------------columna 3-----------------------------------------------
        saturacion_agua=Label(miframe, text="Swi(fraccion):  ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=705, y=180)
        Boton_saturacion_agua = Button(miframe, text ="?", command= self.info_swi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=180)
        self.saturacion_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.saturacion_agua_.place(x=700,y=210, width=150)

        comp_agua=Label(miframe, text="Cw(lpc^-1): ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=705, y=260)
        Boton_comp_agua = Button(miframe, text ="?", command= self.info_cw, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=260)
        self.comp_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.comp_agua_.place(x=700,y=290, width=150)

        comp_roca=Label(miframe, text="Cf(lpc^-1):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=705, y=340)
        Boton_comp_roca = Button(miframe, text ="?", command= self.info_cf, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=340)
        self.comp_roca_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.comp_roca_.place(x=700,y=370, width=150)

        intrusion_agua=Label(miframe, text="We(BY):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=705, y=420)
        Boton_intrusion_agua = Button(miframe, text ="?", command= self.info_we, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=420)
        self.intrusion_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.intrusion_agua_.place(x=700,y=450, width=150)

        agua_producida=Label(miframe, text="Wp(BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=705, y=500)
        Boton_agua_producida = Button(miframe, text ="?", command= self.info_wp, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=500)
        self.agua_producida_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.agua_producida_.place(x=700,y=530, width=150)

        #-----------------------------------------------columna 4--------------------------------------------------
        B_agua=Label(miframe, text="Bw(BY/BN):  ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=975, y=180)
        Boton_B_agua = Button(miframe, text ="?", command= self.info_bw, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1110, y=180)
        self.B_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.B_agua_.place(x=980,y=210, width=150)

        Giny=Label(miframe, text="Giny(PCN): ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=975, y=260)
        Boton_Giny = Button(miframe, text ="?", command= self.info_giny, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1110, y=260)
        self.Giny_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Giny_.place(x=980,y=290, width=150)

        Bginy=Label(miframe, text="Bginy(BY/BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=975, y=340)
        Boton_Bginy = Button(miframe, text ="?", command= self.info_bginy, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1110, y=340)
        self.Bginy_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Bginy_.place(x=980,y=370, width=150)

        Winy=Label(miframe, text="Winy(BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=975, y=420)
        Boton_winy = Button(miframe, text ="?", command= self.info_winy, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1110, y=420)
        self.Winy_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Winy_.place(x=980,y=450, width=150)

        capa_gas=Label(miframe, text="m(ADIM):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=975, y=500)
        Boton_B_agua = Button(miframe, text ="?", command= self.info_m, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1110, y=500)
        self.capa_gas_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.capa_gas_.place(x=980,y=530, width=150)

        FR=Label(miframe, text="FR (fracción)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=975, y=580)
        Boton_FR = Button(miframe, text ="?", command= self.info_FR, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1105, y=580)
        self.txt_FR=Entry(miframe, font=("times new roman",15), bg="lightgray")
        self.txt_FR.place(x=975,y=610, width=150)
        #-----------------------------------------final de filas-----------------------------------------------------

        #-----------------------------------------Botones--------------------------------------------------------
        btn_calular=Button(miframe, text="Calcular", font=("times new roman",15),bg="orange", fg="black", cursor="hand2", command=self.calculos5).place(x=700, y=580, width=200, height=40)

        btn_volver=Button(miframe, text="Volver", font=("times new roman",15),bg="gray", fg="black", cursor="hand2", command=self.EBM_pet1).place(x=360, y=580, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_EBMPC)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_EBMPC)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_EBMPC(self):
        messagebox.showinfo("Ecuación de Balance de Materiales (EBM)", "La Ecuación de Balance de Materiales hace uso del concepto básico de conservación de masa que establece que la producción acumulada observada, expresada como una extracción subterránea, debe ser igual a la expansión de los fluidos en el yacimiento resultante de una caída de presión finita o expresada como la masa de fluidos originalmente en el lugar igual a la masa de fluido restante más la masa de fluido producido.—Ahmed T.")

    def barraAyuda_EBMPC(self):
        messagebox.showinfo("¿Cómo sustituir los datos?", "Se debe rellenar todas las casillas, si no tiene algún dato coloque cero; para decimales utilice el punto.")

    def yaci_gas(self):
        self.root=root
        self.root.title("Yacimiento de gas")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="imagenes/gas.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        #Frame
        frame4=Frame(self.root, bg="white")
        frame4.place(x=100, y=100, width=1100, height=500)    
        title=Label(frame4, text="Escoja un tipo de yacimiento",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=250, y=80)
        btn_pet=Button(frame4,cursor="hand2",text="Gas condensado", command=self.gas_cond, font=("times new roman",30),bg="orange", fg="black").place(x=100, y=250, width=400, height=60)
        btn_gas=Button(frame4, text="Gas seco", command=self.gas_sec, font=("times new roman",30),bg="orange", fg="black", cursor="hand2").place(x=580, y=250, width=400, height=60)
        btn_vol=Button(frame4, text="Volver", command=self.ventana1, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=435, y=420, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_EBMG)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_EBMG)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_EBMG(self):
        messagebox.showinfo("Yacimiento de Gas", "Los gases naturales consisten generalmente de 60% a 80% de metano, y el resto principalmente compuesto de hidrocarburos gaseosos como el etano, propano, butano, y pentano. Los hidrocarburos que estan en condición de vapor en el yacimiento están clasificados como gas, y se subdividen en tres clasificaciones: gas condensado, gas mojado, o gas seco.-Halliburton")

    def barraAyuda_EBMG(self):
        messagebox.showinfo("Diferencias", "1-Los API son más relevantes si se considera su comportamiento respecto al tiempo. 2-El color dependerá de la riqueza del hidrocarburo en fracciones pesadas. Mientras estas sean mayores la mezcla se tornara más oscura. 3-En un gas seco no hay líquido o es muy escaso. 4-El gas condensado presenta condensación retrograda.")

    def gas_cond(self):
        self.root=root
        self.root.title("Yacimiento de gas condensado")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="imagenes/gas.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        frame5=Frame(self.root, bg="white")
        frame5.place(x=100, y=100, width=1100, height=500)    
        title=Label(frame5, text="Escoja un método de cálculo",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=250, y=70)
        btn_mv=Button(frame5,cursor="hand2",text="Método volumétrico", command=self.volum_gasc, font=("times new roman",30),bg="orange", fg="black").place(x=170, y=190, width=350, height=60)
        btn_dp=Button(frame5, text="Declinacion de presion", command=self.GasDP, font=("times new roman",30),bg="orange", fg="black", cursor="hand2").place(x=570, y=190, width=380, height=60)
        btn_eyj=Button(frame5,cursor="hand2",text="Correlaciones de Eaton & Jacoby", command=self.EJ_gas, font=("times new roman",30),bg="orange", fg="black").place(x=270, y=300, width=570, height=60)

        btn_vol=Button(frame5, text="Volver", command=self.yaci_gas, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=435, y=420, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_GasC)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_GasC)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_GasC(self):
        messagebox.showinfo("Yacimiento de Gas Condensado", "La composición de la mezcla de hidrocarburos de un yacimiento de gas condensado es todavía predominantemente metano (>60%) como en el caso de los yacimientos de gas seco y gas húmedo, aunque la cantidad relativa de hidrocarburos de pesados es considerablemente mayor. Un gas condensado es un gas con líquido disuelto.Cuenta con un Relación de Gas-condensado (RGC) mayor que 3.200 PCN/BN,  el condensado tiene una gravedad API entre 40- 60% y posee un contenido de C7+ < 12,5%.-Rojas")

    def barraAyuda_GasC(self):
        messagebox.showinfo("¿Qué método escoger?", "Esto va a depender de los datos que se tienen; El metodo de Declinación de presión es necesario tener un historia de producción, API y RGC; en cambio el Método Volumétricos y Correlaciones de Eaton y Jacoby se necesita propiedades petrofisicas y de los fluidos para aplicarse, esto se debe a que se obtiene el volumen total de gas en sitio de zonas comunicadas y no comunicadas.")

    #Calculo Declinacion de presion

    def GasDP(self):
        self.root= root
        self.root.title("Cálculo de reservas")
        self.root.geometry("1350x700+0+0") 

        self.bg=ImageTk.PhotoImage(file="imagenes/gas.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        frame1=Frame(self.root, bg="white")
        frame1.place(x=25, y=20, width=1300, height=650)
        title=Label(frame1, text="Por favor, introduzca estos valores antes de continuar",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=50, y=80)

        RGC=Label(frame1, text="RGC (PCN/BN)",font=("times new roman", 30, "bold"),bg="white",fg="black").place(x=690, y=300)
        Boton_RGC = Button(frame1, text ="?", command= self.info_rgc, font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=975, y=308)
        self.txt_rgc=Entry(frame1, font=("times new roman",30), bg="lightgray")
        self.txt_rgc.place(x=715,y=350, width=250, height=50)

        API=Label(frame1, text="API condensado",font=("times new roman", 30, "bold"),bg="white",fg="black").place(x=310, y=300)
        Boton_API = Button(frame1, text ="?", command= self.info_api, font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=600, y=308)
        self.txt_api=Entry(frame1, font=("times new roman",30), bg="lightgray")
        self.txt_api.place(x=340,y=350, width=250, height=50)

        FR=Label(frame1, text="FR (fracción)",font=("times new roman", 30, "bold"),bg="white",fg="black").place(x=550, y=430)
        Boton_FR = Button(frame1, text ="?", command= self.info_FR, font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=800, y=430)
        self.txt_FR=Entry(frame1, font=("times new roman",30), bg="lightgray")
        self.txt_FR.place(x=550,y=480, width=250)

        btn_Int=Button(frame1, text="Introducir datos", font=("times new roman",15),bg="orange", fg="black", cursor="hand2", command=self.Calculos).place(x=680, y=580, width=160, height=40) 
        btn_vol=Button(frame1, text="Volver", command=self.gas_cond, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=470, y=580, width=160, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_GasCDP)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_GasCDP)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_GasCDP(self):
        messagebox.showinfo("Declinación de Presión", "Es uno de los métodos más ampliamente usado para predecir la producción futura de campo de gas y petróleo desde que Aps lo presento en 1945. Es un método alternativo cuando no se puede aplicar EBM ni simulación numérica por falta de información de presiones y/o propiedades del yacimiento y fluidos.-Rojas Gonzalo")

    def barraAyuda_GasCDP(self):
        messagebox.showinfo("¿Cómo sustituir los datos?", "Se debe rellenar ambas casillas; para decimales utilice el punto.")


    def calculo1(self):
        try:
            x=np.array(self.calculo1_1())
            y=np.array(self.calculo2_1())

            plt.plot(x, y, 'o')
            plt.xlabel("Gpt")
            plt.ylabel("Cpa*(P/Z2f)")
            plt.title("Gráfico del Metodo Declinación de presión")
            m,b=np.polyfit(x, y, 1)
            plt.plot(x, m*x+b)
            plt.show()
            gcoes=-b/m/1000000
            coes=gcoes/float(self.txt_rgc.get())
            mc=6084/(float(self.txt_api.get())-5.9)
            dc=141.5/(float(self.txt_api.get())+131.5)
            fg=float(self.txt_rgc.get())/(float(self.txt_rgc.get())+132800*(dc/mc))
            goes=gcoes*fg

            self.root2=Toplevel()
            self.root2.title("Resultado")
            self.root2.geometry("400x250+400+300")
            self.root2.config(bg="white")
            self.root2.focus_force()
            self.root2.grab_set()

            frame1=Frame(self.root2, bg="white")
            frame1.place(x=1, y=1, width=500, height=500)

            t=Label(frame1,text="El GCOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=10)
            gcoes2=Label(frame1, text=f'{str(gcoes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=40)

            t1=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=70)
            coes2=Label(frame1, text=f'{str(goes)} MMPCN' ,font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=100)

            t2=Label(frame1,text="El COES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=130)
            coes2=Label(frame1, text=f'{str(coes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=160)

            self.txt_presion = float(self.txt_presion.get())
            self.txt_presion1 = float(self.txt_presion1.get())
            self.txt_presion2 = float(self.txt_presion2.get())
            self.txt_presion3 = float(self.txt_presion3.get())
            self.txt_presion4 = float(self.txt_presion4.get())
            self.txt_presion5 = float(self.txt_presion5.get())
            self.txt_presion6 = float(self.txt_presion6.get())
            self.txt_presion7 = float(self.txt_presion7.get())
            self.txt_presion8 = float(self.txt_presion8.get())
            self.txt_presion9 = float(self.txt_presion9.get())
            self.txt_presion10 = float(self.txt_presion10.get())
            self.txt_cpa = float(self.txt_cpa.get())
            self.txt_cpa1 = float(self.txt_cpa1.get())
            self.txt_cpa2 = float(self.txt_cpa2.get())
            self.txt_cpa3 = float(self.txt_cpa3.get())
            self.txt_cpa4 = float(self.txt_cpa4.get())
            self.txt_cpa5 = float(self.txt_cpa5.get())
            self.txt_cpa6 = float(self.txt_cpa6.get())
            self.txt_cpa7 = float(self.txt_cpa7.get())
            self.txt_cpa8 = float(self.txt_cpa8.get())
            self.txt_cpa9 = float(self.txt_cpa9.get())
            self.txt_cpa10 = float(self.txt_cpa10.get())  
            self.txt_z2f = float(self.txt_z2f.get())
            self.txt_z2f1 = float(self.txt_z2f1.get())
            self.txt_z2f2 = float(self.txt_z2f2.get())
            self.txt_z2f3 = float(self.txt_z2f3.get())
            self.txt_z2f4 = float(self.txt_z2f4.get())
            self.txt_z2f5 = float(self.txt_z2f5.get())
            self.txt_z2f6 = float(self.txt_z2f6.get())
            self.txt_z2f7 = float(self.txt_z2f7.get())
            self.txt_z2f8 = float(self.txt_z2f8.get())
            self.txt_z2f9 = float(self.txt_z2f9.get())
            self.txt_z2f10 = float(self.txt_z2f10.get())
            self.txt_gpt = float(self.txt_gpt.get())
            self.txt_gpt1 = float(self.txt_gpt1.get())
            self.txt_gpt2 = float(self.txt_gpt2.get())
            self.txt_gpt3 = float(self.txt_gpt3.get())
            self.txt_gpt4 = float(self.txt_gpt4.get())
            self.txt_gpt5 = float(self.txt_gpt5.get())
            self.txt_gpt6 = float(self.txt_gpt6.get())
            self.txt_gpt7 = float(self.txt_gpt7.get())
            self.txt_gpt8 = float(self.txt_gpt8.get())
            self.txt_gpt9 = float(self.txt_gpt9.get())
            self.txt_gpt10 = float(self.txt_gpt10.get())
            self.txt_api = float(self.txt_api.get())
            self.txt_rgc = float(self.txt_rgc.get())
            self.txt_gcoes = gcoes
            self.txt_coes = coes
            self.txt_goes = goes

            self.register_calculoDP1()
           
        except Exception as es:
            pass
            #messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)

        

    def calculo1_1(self):
        x=[]
        if self.txt_presion.get()=="" or self.txt_cpa.get()=="" or self.txt_z2f.get()=="" or self.txt_gpt.get()=="":
            messagebox.showerror("Error", "Llene al menos una fila de valores",parent=self.root)
        else:
            x.append(self.txt_gpt.get())
        if self.txt_gpt1.get()=="":
            pass
        else:
            x.append(self.txt_gpt1.get())
        if self.txt_gpt2.get()=="":
            pass
        else:
            x.append(self.txt_gpt2.get())
        if self.txt_gpt3.get()=="":
            pass
        else:
            x.append(self.txt_gpt3.get())
        if self.txt_gpt4.get()=="":
            pass
        else:
            x.append(self.txt_gpt4.get())
        if self.txt_gpt5.get()=="":
            pass
        else:
            x.append(self.txt_gpt5.get())
        if self.txt_gpt6.get()=="":
            pass
        else:
            x.append(self.txt_gpt6.get())
        if self.txt_gpt7.get()=="":
            pass
        else:
            x.append(self.txt_gpt7.get())
        if self.txt_gpt8.get()=="":
            pass
        else:
            x.append(self.txt_gpt8.get())
        if self.txt_gpt9.get()=="":
            pass
        else:
            x.append(self.txt_gpt9.get())
        if self.txt_gpt10.get()=="":
            pass
        else:
            x.append(self.txt_gpt10.get())
        try:
            for i in range(len(x)):
                x[i]=float(x[i])

            return x
        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)
            
    def calculo2_1(self):
    #Presion
        p=[]
        if self.txt_presion.get()=="":
            pass
        else:
            p.append(self.txt_presion.get())

        if self.txt_presion1.get()=="":
            pass
        else:
            p.append(self.txt_presion1.get())

        if self.txt_presion2.get()=="":
            pass
        else:
            p.append(self.txt_presion2.get())

        if self.txt_presion3.get()=="":
            pass
        else:
            p.append(self.txt_presion3.get())

        if self.txt_presion4.get()=="":
            pass
        else:
            p.append(self.txt_presion4.get())

        if self.txt_presion5.get()=="":
            pass
        else:
            p.append(self.txt_presion5.get())

        if self.txt_presion6.get()=="":
            pass
        else:
            p.append(self.txt_presion6.get())

        if self.txt_presion7.get()=="":
            pass
        else:
            p.append(self.txt_presion7.get())

        if self.txt_presion8.get()=="":
            pass
        else:
            p.append(self.txt_presion8.get())

        if self.txt_presion9.get()=="":
            pass
        else:
            p.append(self.txt_presion9.get())

        if self.txt_presion10.get()=="":
            pass
        else:
            p.append(self.txt_presion10.get())
        try:
            for i in range(len(p)):
                p[i]=float(p[i])
        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)

    #CPA

        c=[]
        if self.txt_cpa.get()=="":
            pass
        else:
            c.append(self.txt_cpa.get())

        if self.txt_cpa1.get()=="":
            pass
        else:
            c.append(self.txt_cpa1.get())

        if self.txt_cpa2.get()=="":
            pass
        else:
            c.append(self.txt_cpa2.get())

        if self.txt_cpa3.get()=="":
            pass
        else:
            c.append(self.txt_cpa3.get())

        if self.txt_cpa4.get()=="":
            pass
        else:
            c.append(self.txt_cpa4.get())

        if self.txt_cpa5.get()=="":
            pass
        else:
            c.append(self.txt_cpa5.get())

        if self.txt_cpa6.get()=="":
            pass
        else:
            c.append(self.txt_cpa6.get())

        if self.txt_cpa7.get()=="":
            pass
        else:
            c.append(self.txt_cpa7.get())

        if self.txt_cpa8.get()=="":
            pass
        else:
            c.append(self.txt_cpa8.get())

        if self.txt_cpa9.get()=="":
            pass
        else:
            c.append(self.txt_cpa9.get())

        if self.txt_cpa10.get()=="":
            pass
        else:
            c.append(self.txt_cpa10.get())
        try:
            for i in range(len(c)):
                c[i]=float(c[i])
        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)
        
    #Z2f

        z=[]
        if self.txt_z2f.get()=="":
            pass
        else:
            z.append(self.txt_z2f.get())

        if self.txt_z2f1.get()=="":
            pass
        else:
            z.append(self.txt_z2f1.get())

        if self.txt_z2f2.get()=="":
            pass
        else:
            z.append(self.txt_z2f2.get())

        if self.txt_z2f3.get()=="":
            pass
        else:
            z.append(self.txt_z2f3.get())

        if self.txt_z2f4.get()=="":
            pass
        else:
            z.append(self.txt_z2f4.get())

        if self.txt_z2f5.get()=="":
            pass
        else:
            z.append(self.txt_z2f5.get())

        if self.txt_z2f6.get()=="":
            pass
        else:
            z.append(self.txt_z2f6.get())

        if self.txt_z2f7.get()=="":
            pass
        else:
            z.append(self.txt_z2f7.get())

        if self.txt_z2f8.get()=="":
            pass
        else:
            z.append(self.txt_z2f8.get())

        if self.txt_z2f9.get()=="":
            pass
        else:
            z.append(self.txt_z2f9.get())

        if self.txt_z2f10.get()=="":
            pass
        else:
            z.append(self.txt_z2f10.get())

        try:
            for i in range(len(z)):
                z[i]=float(z[i])

            product=[i/j for i, j in zip(p,z)]

            y=np.multiply(c, product)

            return y
        except Exception as es:
                 messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)


    def Calculos(self):
        if self.txt_rgc.get()=="" or self.txt_api.get()=="":
            messagebox.showerror("Error", "Introduzca un valor de API y RGC", parent=self.root)
        else:
            self.root=root
            self.root.title("Declinación de presión")
            self.root.geometry("1350x700+0+0")
            self.root.config(bg="white")
            bg1=Label(self.root, bg="white", bd=0)
            bg1.place(x=0, y=0, relwidth=1,relheight=1)

            #Register frame
            frame1=Frame(self.root, bg="white")
            frame1.place(x=25, y=20, width=1300, height=650)    
            title=Label(frame1, text="Método de declinación de presión",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=280, y=80)


            #Presion

            presion=Label(frame1, text="Presion (lpca)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=125, y=170)
            self.txt_presion=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion.place(x=50,y=200, width=250)

            self.txt_presion1=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion1.place(x=50,y=230, width=250)        

            self.txt_presion2=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion2.place(x=50,y=260, width=250)

            self.txt_presion3=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion3.place(x=50,y=290, width=250)

            self.txt_presion4=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion4.place(x=50,y=320, width=250)


            self.txt_presion5=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion5.place(x=50,y=350, width=250)

            self.txt_presion6=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion6.place(x=50,y=380, width=250)
        
        
            self.txt_presion7=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion7.place(x=50,y=410, width=250)

            self.txt_presion8=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion8.place(x=50,y=440, width=250)

            self.txt_presion9=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion9.place(x=50,y=470, width=250)
        
            self.txt_presion10=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_presion10.place(x=50,y=500, width=250)
    
            #CPA

            cpa=Label(frame1, text="Cpa",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=470, y=170)
            self.txt_cpa=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa.place(x=370,y=200, width=250)

            self.txt_cpa1=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa1.place(x=370,y=230, width=250)        

            self.txt_cpa2=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa2.place(x=370,y=260, width=250)

            self.txt_cpa3=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa3.place(x=370,y=290, width=250)

            self.txt_cpa4=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa4.place(x=370,y=320, width=250)


            self.txt_cpa5=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa5.place(x=370,y=350, width=250)

            self.txt_cpa6=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa6.place(x=370,y=380, width=250)
        
        
            self.txt_cpa7=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa7.place(x=370,y=410, width=250)

            self.txt_cpa8=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa8.place(x=370,y=440, width=250)

            self.txt_cpa9=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa9.place(x=370,y=470, width=250)
        
            self.txt_cpa10=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_cpa10.place(x=370,y=500, width=250)


            
            #Z2F

            z2f=Label(frame1, text="Z2f (ADIM)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=770, y=170)
            self.txt_z2f=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f.place(x=690,y=200, width=250)

            self.txt_z2f1=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f1.place(x=690,y=230, width=250)        

            self.txt_z2f2=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f2.place(x=690,y=260, width=250)

            self.txt_z2f3=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f3.place(x=690,y=290, width=250)

            self.txt_z2f4=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f4.place(x=690,y=320, width=250)


            self.txt_z2f5=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f5.place(x=690,y=350, width=250)

            self.txt_z2f6=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f6.place(x=690,y=380, width=250)
        
        
            self.txt_z2f7=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f7.place(x=690,y=410, width=250)

            self.txt_z2f8=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f8.place(x=690,y=440, width=250)

            self.txt_z2f9=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f9.place(x=690,y=470, width=250)
        
            self.txt_z2f10=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_z2f10.place(x=690,y=500, width=250)


            #GPT

            gpt=Label(frame1, text="Gpt (PCN)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=1090, y=170)
            self.txt_gpt=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt.place(x=1010,y=200, width=250)


            self.txt_gpt1=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt1.place(x=1010,y=230, width=250)        


            self.txt_gpt2=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt2.place(x=1010,y=260, width=250)

            self.txt_gpt3=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt3.place(x=1010,y=290, width=250)

            self.txt_gpt4=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt4.place(x=1010,y=320, width=250)


            self.txt_gpt5=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt5.place(x=1010,y=350, width=250)

            self.txt_gpt6=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt6.place(x=1010,y=380, width=250)
        
        
            self.txt_gpt7=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt7.place(x=1010,y=410, width=250)

            self.txt_gpt8=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt8.place(x=1010,y=440, width=250)

            self.txt_gpt9=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt9.place(x=1010,y=470, width=250)
        
            self.txt_gpt10=Entry(frame1, font=("times new roman",15), bg="lightgray")
            self.txt_gpt10.place(x=1010,y=500, width=250)

            btn_cal=Button(frame1, text="Calcular", font=("times new roman",15),bg="orange", fg="black", cursor="hand2", command=self.calculo1).place(x=680, y=570, width=160, height=40)
            btn_volver=Button(frame1, text="Volver", font=("times new roman",15),bg="gray", fg="black", cursor="hand2", command=self.GasDP).place(x=500, y=570, width=160, height=40)

            barraMenu=Menu(self.root)
            Filemenu=Menu(barraMenu)
            archivoMenu=Menu(barraMenu, tearoff=0)
            archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_GasCDDP)
            archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_GasCDDP)
            barraMenu.add_cascade(label="Menu", menu=archivoMenu)
            self.root.config(menu=barraMenu)
    
    def barraAcercade_GasCDDP(self):
        messagebox.showinfo("Declinación de Presión", "Es uno de los métodos más ampliamente usado para predecir la producción futura de campo de gas y petróleo desde que Aps lo presento en 1945. Es un método alternativo cuando no se puede aplicar EBM ni simulación numérica por falta de información de presiones y/o propiedades del yacimiento y fluidos.-Rojas Gonzalo")

    def barraAyuda_GasCDDP(self):
        messagebox.showinfo("¿Cómo sustituir los datos?", "Se debe rellenar por lo menos dos filas de casillas para realizar la grafica; para decimales utilice el punto.")


    #Calculo Eaton y Jacoby

    def calculos3(self):
        try:
            if self.txt_porosidad.get()=="" and self.txt_satagua.get()=="" and self.txt_espesor.get()=="" and self.txt_area.get()=="" and self.txt_volumen.get()=="" and self.txt_temperatura.get()=="" and self.txt_presion.get()=="" and self.txt_rgc.get()=="" and self.txt_api.get()=="":
                messagebox.showerror("Error", "Por favor, llene todos los campos",parent=self.root)
            else:

                if self.txt_volumen.get()=="":
                    vp=7758*float(self.txt_area.get())*float(self.txt_espesor.get())*float(self.txt_porosidad.get())*(1-float(self.txt_satagua.get()))
                    calculo1=0.0831*np.log(float(self.txt_rgc.get()))
                    calculo2=0.4265*np.log(float(self.txt_presion.get()))
                    calculo3=0.3185*np.log(float(self.txt_temperatura.get()))
                    goes=np.e**(4.5484+calculo1+calculo2-calculo3)/1000000
                    goes1=goes*vp
                    calculo4=0.90398*np.log(float(self.txt_rgc.get()))
                    calculo5=0.48940*np.log(float(self.txt_presion.get()))
                    calculo6=0.300084*np.log(float(self.txt_temperatura.get()))
                    calculo7=0.29243*np.log(float(self.txt_api.get()))
                    coes=np.e**(2.60977-calculo4+calculo5-calculo6+calculo7)/1000000
                    coes1=coes*vp

                    self.txt_api = float(self.txt_api.get())
                    self.txt_porosidad = float(self.txt_porosidad.get())
                    self.txt_Swi = float(self.txt_satagua.get())
                    self.txt_espesor = float(self.txt_espesor.get())
                    self.txt_area = float(self.txt_area.get())
                    self.txt_volumen = "N/A"
                    self.txt_temperatura = float(self.txt_temperatura.get())
                    self.txt_Pi = float(self.txt_presion.get())
                    self.txt_rgc = float(self.txt_rgc.get())
                    self.txt_Goes = goes1
                    self.txt_coes = coes1

                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    t=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)               
                    goes2=Label(frame1, text=f'{str(goes1)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)

                    t1=Label(frame1,text="El COES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)
                    gces2=Label(frame1, text=f'{str(coes1)} MMBN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                    
                    self.register_calculoEYJ()

                if self.txt_area.get()=="" and self.txt_espesor.get()=="":
                    vp=7758*float(self.txt_volumen.get())*(1-float(self.txt_satagua.get()))
                    goes=np.e**(4.5484+(0.0831*np.log(float(self.txt_rgc.get())))+(0.4265*np.log(float(self.txt_presion.get())))+(0.3185*np.log(float(self.txt_temperatura.get()))))
                    goes1=goes*vp/1000000
                    coes=np.e**(2.60977-(0.90398*np.log(float(self.txt_rgc.get())))+(0.48940*np.log(float(self.txt_presion.get())))-(0.300084*np.log(float(self.txt_temperatura.get())))+(0.29243*np.log(float(self.txt_api.get()))))
                    coes1=coes*vp/1000000

                    self.txt_api = float(self.txt_api.get())
                    self.txt_porosidad = float(self.txt_porosidad.get())
                    self.txt_Swi = float(self.txt_satagua.get())
                    self.txt_espesor = "N/A"
                    self.txt_area = "N/A"
                    self.txt_volumen = float(self.txt_volumen.get())
                    self.txt_temperatura = float(self.txt_temperatura.get())
                    self.txt_Pi = float(self.txt_presion.get())
                    self.txt_rgc = float(self.txt_rgc.get())
                    self.txt_Goes = goes1
                    self.txt_coes = coes1
    
                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    t=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)         
                    goes2=Label(frame1, text=f'{str(goes1)} MMPCN',font=("times new roman", 20, "bold"),bg="orange",fg="black").place(x=20, y=40)

                    t1=Label(frame1,text="El COES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)         
                    coes2=Label(frame1, text=f'{str(coes1)} MMPCN',font=("times new roman", 20, "bold"),bg="orange",fg="black").place(x=20, y=100)
                    
                    self.register_calculoEYJ()

        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)

    def EJ_gas(self):
        self.root=root
        self.root.title("Yacimiento de gas condensado")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="imagenes/gas.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        frame5=Frame(self.root, bg="white")
        frame5.place(x=100, y=100, width=1200, height=500)    
        title=Label(frame5, text="Introduzca la siguiente información",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=200, y=80)    
        
        porosidad=Label(frame5, text="Porosidad (fraccion)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=90, y=190)
        Boton_porosidad = Button(frame5, text ="?", command= self.info_porosidad, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=265, y=190)        
        self.txt_porosidad=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_porosidad.place(x=120,y=220, width=150)

        satagua=Label(frame5, text="Swi (fraccion)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=325, y=190)
        Boton_satagua = Button(frame5, text ="?", command= self.info_swi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=450, y=190)
        self.txt_satagua=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_satagua.place(x=320,y=220, width=150)

        espesor=Label(frame5, text="Espesor (pies)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=530, y=190)
        Boton_espesor = Button(frame5, text ="?", command= self.info_espesor, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=650, y=190)
        self.txt_espesor=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_espesor.place(x=520,y=220, width=150)

        area=Label(frame5, text="Área (Acres)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=720, y=190)
        Boton_area = Button(frame5, text ="?", command= self.info_area, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=850, y=190)
        self.txt_area=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_area.place(x=720,y=220, width=150)

        volumen=Label(frame5, text="Volumen (Acres-pies)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=890, y=190)
        Boton_volumen = Button(frame5, text ="?", command= self.info_volumen, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1080, y=190)
        self.txt_volumen=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_volumen.place(x=920,y=220, width=150)

        #segunda fila

        temperatura=Label(frame5, text="Temperatura (°F)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=100, y=280)
        Boton_temperatura = Button(frame5, text ="?", command= self.info_temperatura, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=255, y=280)
        self.txt_temperatura=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_temperatura.place(x=120,y=310, width=150)

        presion=Label(frame5, text="Presión inicial (lpca)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=295, y=280)
        Boton_presion = Button(frame5, text ="?", command= self.info_pi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=470, y=280)
        self.txt_presion=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_presion.place(x=320,y=310, width=150)

 
        rgc=Label(frame5, text="RGC (PCN/BN)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=520, y=280)
        Boton_rgc = Button(frame5, text ="?", command= self.info_rgc, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=660, y=280)
        self.txt_rgc=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_rgc.place(x=520,y=310, width=150)

        api=Label(frame5, text="°API",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=770, y=280)
        Boton_api = Button(frame5, text ="?", command= self.info_api, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=850, y=280)
        self.txt_api=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_api.place(x=720,y=310, width=150)

        FR=Label(frame5, text="FR (fracción)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=890, y=280)
        Boton_FR = Button(frame5, text ="?", command= self.info_FR, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1020, y=280)
        self.txt_FR=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_FR.place(x=920,y=310, width=150)

        btn_cal=Button(frame5, text="Calcular", command=self.calculos3, font=("times new roman",15),bg="orange", fg="black", cursor="hand2").place(x=500, y=370, width=200, height=40)
           
        btn_vol=Button(frame5, text="Volver", command=self.gas_cond, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=500, y=420, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_GasCEJ)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_GasEJ)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_GasCEJ(self):
        messagebox.showinfo("Correlaciones de Eaton y Jacoby", "Eaton y Jacoby mejoraron las correlaciones de Jacoby y cols., usando datos de análisis PVT y de pruebas de pozos de 27 sistemas de gas condensado y crudos volátiles. El comportamiento de PVT de cada mezcla fue determinado en el laboratorio y luego por balance de materiales, obtuvieron el comportamiento de producción por depleción. Con los datos obtenidos previamente elaboraron las correlaciones usando el método estadístico de regresión múltiple.-Rojas Gonzalo")

    def barraAyuda_GasEJ(self):
        messagebox.showinfo("Identificar si va a trabajar con Volumen o Area", "Si en los datos proporcionados, estan espesor y area, deje vacia la casilla de volumen no coloque ningún valor tampoco cero; en caso de que se le proporcione volumen deje vacias las casillas de espesor y area, no coloque ningún numero tampoco cero. Para decimales utilice el punto.")

    #Calculo Metodo Volumetrico Gas Condensado 

    def calculos4(self):
        try:
            if self.txt_porosidad.get()=="" or self.txt_satagua.get()=="":
                messagebox.showerror("Error", "Llene todos los campos",parent=self.root)
            if self.txt_espesor.get()=="" and self.txt_area.get()=="" and self.txt_bgi.get()=="":
                api=float(self.txt_api.get())
                Mc=6084/(api-5.9)
                dc=141.5/(api+131.5)
                temperatura=float(self.txt_temperatura.get())+460
                presion=float(self.txt_presion.get())
                zgc=float(self.txt_factorz.get())
                bgi=0.00504*zgc*(temperatura/presion)
                Gcoes=(7758*float(self.txt_volumen.get())*float(self.txt_porosidad.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                fg=float(self.txt_rgc.get())/(float(self.txt_rgc.get())+350*370.4*(dc/Mc))
                Goes=Gcoes*fg
                Coes=Gcoes/float(self.txt_rgc.get())

                self.root2=Toplevel()
                self.root2.title("Resultado")
                self.root2.geometry("400x250+400+300")
                self.root2.config(bg="white")
                self.root2.focus_force()
                self.root2.grab_set()

                self.txt_Api = api
                self.txt_Bgi = bgi
                self.txt_T = temperatura
                self.txt_Zgc = zgc
                self.txt_coes = Coes
                self.txt_Gcoes = Gcoes
                self.txt_Goes = Goes
                
                frame1=Frame(self.root2, bg="white")
                frame1.place(x=1, y=1, width=500, height=500)

                t=Label(frame1,text="El GCOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=10)
                gcoes2=Label(frame1, text=str(Gcoes),font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=40)

                t1=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=70)
                coes2=Label(frame1, text=str(Goes),font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=100)

                t2=Label(frame1,text="El COES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=130)
                coes2=Label(frame1, text=str(Coes),font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=160)
                
                self.register_calculoMVGC()

            if self.txt_volumen.get()=="" and self.txt_bgi.get()=="":
                api=float(self.txt_api.get())
                Mc=6084/(api-5.9)
                dc=141.5/(api+131.5)
                temperatura=float(self.txt_temperatura.get())+460
                presion=float(self.txt_presion.get())
                zgc=float(self.txt_factorz.get())
                bgi=0.00504*zgc*(temperatura/presion)
                Gcoes=(7758*float(self.txt_espesor.get())*float(self.txt_area.get())*float(self.txt_porosidad.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                fg=float(self.txt_rgc.get())/(float(self.txt_rgc.get())+350*370.4*(dc/Mc))
                Goes=Gcoes*fg
                Coes=Gcoes/float(self.txt_rgc.get())

                self.txt_Api = api
                self.txt_Bgi = bgi
                self.txt_T = temperatura
                self.txt_Zgc = zgc
                self.txt_coes = Coes
                self.txt_Gcoes = Gcoes
                self.txt_Goes = Goes

                self.root2=Toplevel()
                self.root2.title("Resultado")
                self.root2.geometry("400x250+400+300")
                self.root2.config(bg="white")
                self.root2.focus_force()
                self.root2.grab_set()

                frame1=Frame(self.root2, bg="white")
                frame1.place(x=1, y=1, width=500, height=500)

                t=Label(frame1,text="El GCOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=10)
                gcoes2=Label(frame1, text=f'{str(Gcoes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=40)

                t1=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=70)
                coes2=Label(frame1, text=f'{str(Goes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=100)

                t2=Label(frame1,text="El COES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=130)
                coes2=Label(frame1, text=f'{str(Coes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=160)
                
                self.register_calculoMVGC()

            if self.txt_espesor.get()=="" and self.txt_area.get()=="" and self.txt_factorz.get()=="" and self.txt_presion.get()=="" and self.txt_temperatura.get()=="":
                api=float(self.txt_api.get())
                Mc=6084/(api-5.9)
                dc=141.5/(api+131.5)
                bgi=float(self.txt_bgi.get())
                Gcoes=(7758*float(self.txt_volumen.get())*float(self.txt_porosidad.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                fg=float(self.txt_rgc.get())/(float(self.txt_rgc.get())+350*370.4*(dc/Mc))
                Goes=Gcoes*fg
                Coes=Gcoes/float(self.txt_rgc.get())     

                self.txt_Zgc = "N/A"
                self.txt_Api = api
                self.txt_Bgi = bgi
                self.txt_T = "N/A"
                self.txt_coes = Coes
                self.txt_Gcoes = Gcoes         
                self.txt_Goes = Goes

                self.root2=Toplevel()
                self.root2.title("Resultado")
                self.root2.geometry("400x250+400+300")
                self.root2.config(bg="white")
                self.root2.focus_force()
                self.root2.grab_set()

                frame1=Frame(self.root2, bg="white")
                frame1.place(x=1, y=1, width=500, height=500)

                t=Label(frame1,text="El GCOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=10)
                gcoes2=Label(frame1, text=f'{str(Gcoes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=40)

                t1=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=70)
                coes2=Label(frame1, text=f'{str(Goes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=100)

                t2=Label(frame1,text="El COES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=130)
                coes2=Label(frame1, text=f'{str(Coes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=160)

                self.register_calculoMVGC()

            if self.txt_volumen.get()=="" and self.txt_factorz.get()=="" and self.txt_presion.get()=="" and self.txt_temperatura.get()=="":
                api=float(self.txt_api.get())
                Mc=6084/(api-5.9)
                dc=141.5/(api+131.5)
                bgi=float(self.txt_bgi.get())
                Gcoes=(7758*float(self.txt_espesor.get())*float(self.txt_area.get())*float(self.txt_porosidad.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                fg=float(self.txt_rgc.get())/(float(self.txt_rgc.get())+350*370.4*(dc/Mc))
                Goes=Gcoes*fg
                Coes=Gcoes/float(self.txt_rgc.get())

                self.txt_Api = api
                self.txt_Bgi = bgi
                self.txt_T = "N/A"
                self.txt_Zgc = "N/A"
                self.txt_coes = Coes
                self.txt_Gcoes = Gcoes
                self.txt_Goes = Goes

                self.root2=Toplevel()
                self.root2.title("Resultado")
                self.root2.geometry("400x250+400+300")
                self.root2.config(bg="white")
                self.root2.focus_force()
                self.root2.grab_set()

                frame1=Frame(self.root2, bg="white")
                frame1.place(x=1, y=1, width=500, height=500)

                t=Label(frame1,text="El GCOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=10)
                gcoes2=Label(frame1, text=f'{str(Gcoes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=40)

                t1=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=70)
                coes2=Label(frame1, text=f'{str(Goes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=100)

                t2=Label(frame1,text="El COES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=0, y=130)
                coes2=Label(frame1, text=f'{str(Coes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=10, y=160)
                
                self.register_calculoMVGC()

            if self.txt_espesor.get()!= 0 and self.txt_area.get()!= 0 and self.txt_volumen.get()!= 0:
                messagebox.showerror("Error", "Por favor, coloque solo los valores de espesor y área o volumen",parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)


    def volum_gasc(self):
        self.root=root
        self.root.title("Yacimiento de gas condensado")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="imagenes/gas.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        frame5=Frame(self.root, bg="white")
        frame5.place(x=100, y=100, width=1200, height=500)    
        title=Label(frame5, text="Introduzca la siguiente información",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=200, y=60)


        porosidad=Label(frame5, text="Porosidad (fraccion)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=90, y=170)
        Boton_porosidad = Button(frame5, text ="?", command= self.info_porosidad, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=265, y=170)
        self.txt_porosidad=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_porosidad.place(x=120,y=200, width=150)

        satagua=Label(frame5, text="Swi (fraccion)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=325, y=170)
        Boton_satagua = Button(frame5, text ="?", command= self.info_swi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=450, y=170)
        self.txt_satagua=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_satagua.place(x=320,y=200, width=150)

        espesor=Label(frame5, text="Espesor (pies)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=520, y=170)
        Boton_espesor = Button(frame5, text ="?", command= self.info_espesor, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=650, y=170)
        self.txt_espesor=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_espesor.place(x=520,y=200, width=150)

        area=Label(frame5, text="Área (Acres)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=725, y=170)
        Boton_area = Button(frame5, text ="?", command= self.info_area, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=850, y=170)
        self.txt_area=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_area.place(x=720,y=200, width=150)

        volumen=Label(frame5, text="Volumen (Acres-pies)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=900, y=170)
        Boton_volumen = Button(frame5, text ="?", command= self.info_volumen, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1085, y=170)
        self.txt_volumen=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_volumen.place(x=920,y=200, width=150)

        #segunda fila

        api=Label(frame5, text="°API",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=170, y=260)
        Boton_api= Button(frame5, text ="?", command= self.info_api, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=250, y=260)
        self.txt_api=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_api.place(x=120,y=290, width=150)

        rgc=Label(frame5, text="RGC (PCN/BN)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=310, y=260)
        Boton_rgc = Button(frame5, text ="?", command= self.info_rgc, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=460, y=260)
        self.txt_rgc=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_rgc.place(x=320,y=290, width=150)

 
        presion=Label(frame5, text="Presion (lpca)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=525, y=260)
        Boton_presion = Button(frame5, text ="?", command= self.info_p, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=650, y=260)
        self.txt_presion=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_presion.place(x=520,y=290, width=150)

        temperatura=Label(frame5, text="Temperatura (°F)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=705, y=260)
        Boton_temperatura = Button(frame5, text ="?", command= self.info_temperatura, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=860, y=260) 
        self.txt_temperatura=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_temperatura.place(x=720,y=290, width=150)

        factorz=Label(frame5, text="Factor Zgc (adim)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=905, y=260)
        Boton_factorz = Button(frame5, text ="?", command= self.info_factor_zgc, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1060, y=260)
        self.txt_factorz=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_factorz.place(x=920,y=290, width=150)

        #3ra fila
        bgi=Label(frame5, text="Bgi (BY/PCN)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=115, y=350)
        Boton_bgi= Button(frame5, text ="?", command= self.info_bgi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=250, y=350)
        self.txt_bgi=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_bgi.place(x=120,y=380, width=150)

        FR=Label(frame5, text="FR (fracción)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=310, y=350)
        Boton_FR = Button(frame5, text ="?", command= self.info_FR, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=440, y=350)
        self.txt_FR=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_FR.place(x=310,y=380, width=150)

        btn_cal=Button(frame5, text="Calcular", command=self.calculos4, font=("times new roman",15),bg="orange", fg="black", cursor="hand2").place(x=500, y=370, width=200, height=40)
        btn_vol=Button(frame5, text="Volver", command=self.gas_cond, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=500, y=420, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_GasCV)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_GasCV)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_GasCV(self):
        messagebox.showinfo("Método Volumétrico", "El método volumétrico es probablemente el método más fácil utilizado por los ingenieros para estimar las reservas. Requiere una cantidad limitada de datos para la estimación, ésto implica que inmediatamente después del descubrimiento de las acumulaciones de hidrocarburos, durante la delimitación inicial y el desarrollo de un campo, el método volumétrico es la clave para la estimación del volumen de hidrocarburos.-Okotie y Ikporo")

    def barraAyuda_GasCV(self):
        messagebox.showinfo("Identificar si va a trabajar con Volumen o Area, Bgci o Zgc", "Si en los datos proporcionados, estan espesor y area, deje vacia la casilla de volumen no coloque ningún valor tampoco cero; en caso de que se le proporcione volumen deje vacias las casillas de espesor y area, no coloque ningún numero tampoco cero. Si se tiene Zgc deje vacia la casilla de Bgi, no coloque ningun valor tampoco cero. En caso de que se le proporcione el valor de Bgi deje vacia las casillas de Presion, Temperatura y Zgc, no coloque ningun valor tampoco cero. Para decimales utilice el punto.")

    def gas_sec(self):
        self.root=root
        self.root.title("Yacimiento de gas seco")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="imagenes/gas.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        frame5=Frame(self.root, bg="white")
        frame5.place(x=100, y=100, width=1100, height=500)    
        title=Label(frame5, text="Escoja un método de cálculo",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=250, y=80)
        btn_pet=Button(frame5,cursor="hand2",text="Método volumétrico", command=self.volum_gas, font=("times new roman",30),bg="orange", fg="black").place(x=70, y=250, width=350, height=60)
        btn_gas=Button(frame5, text="Ecuación de Balance de Materiales", command=self.EBM_gas, font=("times new roman",30),bg="orange", fg="black", cursor="hand2").place(x=480, y=250, width=570, height=60)
        btn_vol=Button(frame5, text="Volver", command=self.yaci_gas, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=435, y=420, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_GasS)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_GasS)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_GasS(self):
        messagebox.showinfo("Yacimiento de Gas Seco", "Son aquellos yacimientos que contienen principalmente metano (%C1>90) con pequeñas cantidades de pentano y componentes más pesados (%C5+<1).Generalmente un sistema de hidrocarburos que produzca con una relación de gas-liquido (RGL) mayor de 100000 PCN/BN se considera seco.-Paris de Ferrer")

    def barraAyuda_GasS(self):
        messagebox.showinfo("¿Qué método escoger?", "Esto va a depender de los datos que se tienen; el método de EBM permiten determinar solamente los volúmenes de gas que se encuentran en comunicación con los pozos de producción; por esta razón a este método se le llama DINAMICO. En cambio los métodos volumétricos se tiene en cuenta el volumen total de gas en sitio de zonas comunicadas y no comunicadas se les llama ESTATICOS y regularmente arrojan reservas mayores a los dinámicos.")

    #Calculo Metodo Volumetrico Gas seco

    def calculos1(self):

        try:
            if self.txt_porosidad.get()=="" or self.txt_satagua.get()=="":
                messagebox.showerror("Error", "Por favor, llene todos los campos",parent=self.root)

            else:

                #Calcular bgi y se tiene volumen

                if self.txt_espesor.get()=="" and self.txt_factorz.get()=="" and self.txt_area.get()=="" and self.txt_bgi.get()=="":
                    graved=float(self.txt_gravedad.get())
                    psc=677+(15*graved)-(37.5*graved**2)
                    tsc=168+(325*graved)-(12.5*graved**2)
                    psr=float(self.txt_presion.get())/psc
                    temp=float(self.txt_temperatura.get())+460
                    tsr=temp/tsc
                    z_1=((3.52*psr)/(10**(0.9813*tsr)))
                    z_2=((0.274*(psr**2))/(10**(0.8157*tsr)))
                    z=1-(z_1+z_2)
                    bgi=0.00504*((z*temp)/float(self.txt_presion.get()))
                    goes=(7758*float(self.txt_porosidad.get())*float(self.txt_volumen.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                    RESERVA = goes*float(self.txt_FR.get())
                    FR = float(self.txt_FR.get())
                    
                    self.txt_Bgi = "N/A"
                    self.txt_T = temp
                    self.txt_Z = "N/A"
                    self.txt_dc = graved
                    self.txt_Goes = goes
                    self.txt_FR = FR
                    self.txt_RESERVA = RESERVA

                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    t=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)
                    
                    goes1=Label(frame1, text=f'{str(goes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)
                    
                    t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                    RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                    
                    self.register_calculoMVGS()

                #calcular bgi y se tiene espesor y area
                if self.txt_volumen.get()=="" and self.txt_factorz.get()=="" and self.txt_bgi.get()=="":
                    graved=float(self.txt_gravedad.get())
                    psc=677+(15*graved)-(37.5*graved**2)
                    tsc=168+(325*graved)-(12.5*graved**2)
                    psr=float(self.txt_presion.get())/psc
                    temp=float(self.txt_temperatura.get())+460
                    tsr=temp/tsc
                    z_1=((3.52*psr)/(10**(0.9813*tsr)))
                    z_2=((0.274*(psr**2))/(10**(0.8157*tsr)))
                    z=1-(z_1+z_2)
                    bgi=0.00504*((z*temp)/float(self.txt_presion.get()))
                    goes=(7758*float(self.txt_porosidad.get())*float(self.txt_espesor.get())*float(self.txt_area.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                    RESERVA = goes*float(self.txt_FR.get())
                    FR = float(self.txt_FR.get())

                    self.txt_FR = FR
                    self.txt_RESERVA = RESERVA

                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    t=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)
                    
                    goes1=Label(frame1, text=f'{str(goes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)
                    
                    t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                    RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                    
                    self.register_calculoMVGS()

                #calcular bgi y se tiene factor z, area y espesor
                if self.txt_volumen.get()=="" and self.txt_gravedad.get()=="" and self.txt_bgi.get()=="":
                    temp=float(self.txt_temperatura.get())+460
                    z=float(self.txt_factorz.get())
                    bgi=0.00504*((z*temp)/float(self.txt_presion.get()))
                    goes=(7758*float(self.txt_porosidad.get())*float(self.txt_espesor.get())*float(self.txt_area.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                    RESERVA = goes*float(self.txt_FR.get())
                    FR = float(self.txt_FR.get())

                    self.txt_FR = FR
                    self.txt_RESERVA = RESERVA

                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    t=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)
                    
                    goes1=Label(frame1, text=f'{str(goes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)
                    
                    t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                    RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                    
                    self.register_calculoMVGS()

                #calcular bgi y se tiene factor z y volumen
                if self.txt_espesor.get()=="" and self.txt_gravedad.get()=="" and self.txt_area.get()=="" and self.txt_bgi.get()=="":
                    temp=float(self.txt_temperatura.get())+460
                    z=float(self.txt_factorz.get())
                    bgi=0.00504*((z*temp)/float(self.txt_presion.get()))
                    print(bgi)
                    goes=(7758*float(self.txt_porosidad.get())*float(self.txt_volumen.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                    RESERVA = goes*float(self.txt_FR.get())
                    FR = float(self.txt_FR.get())

                    self.txt_FR = FR
                    self.txt_RESERVA = RESERVA

                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    t=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)
                    
                    goes1=Label(frame1, text=f'{str(goes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)
                    
                    t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                    RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                    
                    self.register_calculoMVGS()

                if self.txt_espesor.get()=="" and self.txt_gravedad.get()=="" and self.txt_area.get()=="" and self.txt_factorz.get()=="" and self.txt_temperatura.get()=="" and self.txt_presion.get()=="":
                    bgi=float(self.txt_bgi.get())
                    goes=(7758*float(self.txt_porosidad.get())*float(self.txt_volumen.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                    RESERVA = goes*float(self.txt_FR.get())
                    FR = float(self.txt_FR.get())

                    self.txt_FR = FR
                    self.txt_RESERVA = RESERVA

                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    t=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)
                    
                    goes1=Label(frame1, text=f'{str(goes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)
                    
                    t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                    RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                    
                    self.register_calculoMVGS()

                if self.txt_volumen.get()=="" and self.txt_gravedad.get()=="" and self.txt_factorz.get()=="" and self.txt_temperatura.get()=="" and self.txt_presion.get()=="":
                    bgi=float(self.txt_bgi.get())
                    goes=(7758*float(self.txt_porosidad.get())*float(self.txt_area.get())*float(self.txt_espesor.get())*(1-float(self.txt_satagua.get())))/bgi/1000000
                    RESERVA = goes*float(self.txt_FR.get())
                    FR = float(self.txt_FR.get())

                    self.txt_FR = FR
                    self.txt_RESERVA = RESERVA

                    self.root2=Toplevel()
                    self.root2.title("Resultado")
                    self.root2.geometry("400x250+400+300")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    frame1=Frame(self.root2, bg="white")
                    frame1.place(x=1, y=1, width=500, height=500)

                    self.txt_Bgi = self.txt_bgi.get()
                    self.txt_T = "N/A"
                    self.txt_Z = "N/A"
                    self.txt_dc = "N/A"
                    self.txt_Goes = goes

                    t=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)
                    
                    goes1=Label(frame1, text=f'{str(goes)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)
                    
                    t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                    RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                    
                    self.register_calculoMVGS()

                if self.txt_espesor.get()!= 0 and self.txt_area.get()!= 0 and self.txt_volumen.get()!= 0:
                    messagebox.showerror("Error", "Por favor, coloque solo los valores de espesor y área o volumen",parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)


    def volum_gas(self):
        self.root=root
        self.root.title("Yacimiento de gas seco")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="imagenes/gas.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

        frame5=Frame(self.root, bg="white")
        frame5.place(x=100, y=100, width=1200, height=500)    
        title=Label(frame5, text="Introduzca la siguiente información",font=("times new roman", 40, "bold"),bg="white",fg="black").place(x=200, y=60)
        
        porosidad=Label(frame5, text="Porosidad (fraccion)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=85, y=190)
        Boton_porosidad = Button(frame5, text ="?", command= self.info_porosidad, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=260, y=190)
        self.txt_porosidad=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_porosidad.place(x=120,y=220, width=150)

        satagua=Label(frame5, text="Swi (fraccion)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=330, y=190)
        Boton_satagua = Button(frame5, text ="?", command= self.info_swi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=450, y=190)
        self.txt_satagua=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_satagua.place(x=320,y=220, width=150)

        espesor=Label(frame5, text="Espesor (pies)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=520, y=190)
        Boton_espesor = Button(frame5, text ="?", command= self.info_espesor, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=650, y=190)
        self.txt_espesor=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_espesor.place(x=520,y=220, width=150)

        area=Label(frame5, text="Área (Acres)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=730, y=190)
        Boton_area = Button(frame5, text ="?", command= self.info_area, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=850, y=190)
        self.txt_area=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_area.place(x=720,y=220, width=150)

        volumen=Label(frame5, text="Volumen (Acres-pies)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=895, y=190)
        Boton_volumen = Button(frame5, text ="?", command= self.info_volumen, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1085, y=190)
        self.txt_volumen=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_volumen.place(x=920,y=220, width=150)

        #segunda fila

        temperatura=Label(frame5, text="Temperatura (°F)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=95, y=280)
        Boton_temperatura = Button(frame5, text ="?", command= self.info_temperatura, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=250, y=280)
        self.txt_temperatura=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_temperatura.place(x=120,y=310, width=150)

        presion=Label(frame5, text="Presión inicial (lpca)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=300, y=280)
        Boton_presion = Button(frame5, text ="?", command= self.info_pi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=475, y=280)
        self.txt_presion=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_presion.place(x=320,y=310, width=150)

 
        gravedad=Label(frame5, text="γg (adim)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=550, y=280)
        Boton_gravedad = Button(frame5, text ="?", command= self.info_gravedad, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=645, y=280)
        self.txt_gravedad=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_gravedad.place(x=520,y=310, width=150)

        factorz=Label(frame5, text="Factor Z (adim)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=710, y=280)
        Boton_factorz = Button(frame5, text ="?", command= self.info_factor_z, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=855, y=280)
        self.txt_factorz=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_factorz.place(x=720,y=310, width=150)

        bgi=Label(frame5, text="Bgi (BY/PCN)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=920, y=280)
        Boton_bgi = Button(frame5, text ="?", command= self.info_bgi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1050, y=280)
        self.txt_bgi=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_bgi.place(x=920,y=310, width=150)

        #tercera fila

        FR=Label(frame5, text="FR (fracción)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=920, y=370)
        Boton_FR = Button(frame5, text ="?", command= self.info_FR, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1050, y=370)
        self.txt_FR=Entry(frame5, font=("times new roman",15), bg="lightgray")
        self.txt_FR.place(x=920,y=410, width=150)

        btn_cal=Button(frame5, text="Calcular", command=self.calculos1, font=("times new roman",15),bg="orange", fg="black", cursor="hand2").place(x=500, y=370, width=200, height=40)

        btn_vol=Button(frame5, text="Volver", command=self.gas_sec, font=("times new roman",15),bg="gray", fg="black", cursor="hand2").place(x=500, y=420, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_GasSV)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_GasSV)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    

    def barraAcercade_GasSV(self):
        messagebox.showinfo("Método Volumétrico", "El método volumétrico es probablemente el método más fácil utilizado por los ingenieros para estimar las reservas. Requiere una cantidad limitada de datos para la estimación, ésto implica que inmediatamente después del descubrimiento de las acumulaciones de hidrocarburos, durante la delimitación inicial y el desarrollo de un campo, el método volumétrico es la clave para la estimación del volumen de hidrocarburos.-Okotie y Ikporo")

    def barraAyuda_GasSV(self):
        messagebox.showinfo("Identificar si va a trabajar con Volumen o Area, Bgi o Z", "Si en los datos proporcionados, estan espesor y area, deje vacia la casilla de volumen no coloque ningún valor tampoco cero; en caso de que se le proporcione volumen deje vacias las casillas de espesor y area, no coloque ningún numero tampoco cero. Si se tiene Z deje vacia la casilla de Bgi, no coloque ningun valor tampoco cero. En caso de que se le proporcione el valor de Bgi deje vacia las casillas de Presion, Temperatura, γg y Z, no coloque ningun valor tampoco cero. Para decimales utilice el punto.")

   #Gas seco EBM 
    def calculos7(self):
        try:
            if self.presion_.get()=="" or self.presion_inicial_.get()=="" or self.G_producido_.get()=="" or self.B_gas.get()=="" or self.Bi_gas.get()=="" or self.saturacion_agua_.get()=="" or self.comp_agua_.get()=="" or self.comp_roca_.get()=="" or self.intrusion_agua_.get()=="" or self.agua_producida_.get()=="" or self.B_agua_.get()=="":
                messagebox.showerror("Error", "Por favor, llene todos los campos si no tiene algun dato coloque cero", parent=root)
        
            else:
                Pr=float(self.presion_.get())
                Pin=float(self.presion_inicial_.get())
                Gp=float(self.G_producido_.get())
                Bg=float(self.B_gas.get())
                Bgi=float(self.Bi_gas.get())
                Swi=float(self.saturacion_agua_.get())
                Cw=float(self.comp_agua_.get())
                Cf=float(self.comp_roca_.get())
                We=float(self.intrusion_agua_.get())
                Wp=float(self.agua_producida_.get())
                Bw=float(self.B_agua_.get())
                FR = float(self.txt_FR.get())

                A=Bg*Gp
                B=-We+Wp*Bw
                C=(Bg-Bgi)
                D=Bgi*((Cw*Swi+Cf)/(1-Swi))*(Pin-Pr)

                GoesM=(A+B)/(C+D)/1000000
                RESERVA = GoesM*float(self.txt_FR.get())
                
                self.txt_Pr = Pr
                self.txt_Pi = Pin
                self.txt_Bg = Bg
                self.txt_Bgi = Bgi
                self.txt_Swi = Swi
                self.txt_Cw = Cw
                self.txt_Cf = Cf
                self.txt_We = We
                self.txt_Wp = Wp
                self.txt_Bw = Bw
                self.txt_Gp = Gp
                self.txt_Goes = GoesM
                self.txt_FR = FR
                self.txt_RESERVA = RESERVA

                self.root2=Toplevel()
                self.root2.title("Resultado")
                self.root2.geometry("400x250+400+300")
                self.root2.config(bg="white")
                self.root2.focus_force()
                self.root2.grab_set()

                frame1=Frame(self.root2, bg="white")
                frame1.place(x=1, y=1, width=500, height=500)

                t=Label(frame1,text="El GOES es", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=10)
                    
                goes1=Label(frame1, text=f'{str(GoesM)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=40)
                
                t1=Label(frame1,text="Las Reservas son", font=("times new roman",20, "bold"), bg="white", fg="black").place(x=20, y=70)

                RESERVA1=Label(frame1, text=f'{str(RESERVA)} MMPCN',font=("times new roman", 20, "bold"),bg="white",fg="black").place(x=20, y=100)
                
                self.register_calculoEBMGS()

        except Exception as es:
            messagebox.showerror("Error", f"Error debido a {str(es)}",parent=self.root)
    
    def EBM_gas(self):
        self.root=root
        self.root.title("Yacimiento de petróleo")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="orange")
        self.bg=ImageTk.PhotoImage(file="imagenes/gas.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)
    
        miframe=Frame(root, bg="white").place(x=100, y=100, width=1100, height=550)
        titleframe=Label(miframe, text="Introduzca los datos",font=("times new roman", 30, "bold"),bg="white",fg="black").place(x=490, y=100)

        #----------------------------------------------columna 1--------------------------------------------------
        presion=Label(miframe, text="P(Lpca):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=170, y=180)
        Boton_presion = Button(miframe, text ="?", command= self.info_p, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=270, y=180)
        self.presion_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.presion_.place(x=140,y=210, width=150)

        presion_inicial=Label(miframe, text="Pi(Lpca): ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=170, y=300)
        Boton_presion_inicial = Button(miframe, text ="?", command= self.info_pi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=270, y=300)
        self.presion_inicial_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.presion_inicial_.place(x=140,y=330, width=150)

        G_producido=Label(miframe, text="GP(PCN):  ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=170, y=420)
        Boton_G_producido = Button(miframe, text ="?", command= self.info_gp, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=270, y=420)
        self.G_producido_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.G_producido_.place(x=140,y=450, width=150)

        #-------------------------------------------columna 2----------------------------------------------------

        Bgas=Label(miframe, text="Bg(BY/PCN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=180)
        Boton_Bgas = Button(miframe, text ="?", command= self.info_bg, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=180)
        self.B_gas=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.B_gas.place(x=420,y=210, width=150)

        Bigas=Label(miframe, text="Bgi(BY/PCN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=300)
        Boton_G_producido = Button(miframe, text ="?", command= self.info_bgi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=300)
        self.Bi_gas=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.Bi_gas.place(x=420,y=330, width=150)

        B_agua=Label(miframe, text="Bw(BY/BN):  ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=420, y=420)
        Boton_B_agua = Button(miframe, text ="?", command= self.info_bw, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=550, y=420)
        self.B_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.B_agua_.place(x=420,y=450, width=150)

        #---------------------------------------------columna 3-----------------------------------------------
        saturacion_agua=Label(miframe, text="Swi(fraccion):  ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=700, y=180)
        Boton_saturacion = Button(miframe, text ="?", command= self.info_swi, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=180)
        self.saturacion_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.saturacion_agua_.place(x=700,y=210, width=150)

        comp_agua=Label(miframe, text="Cw(lpc^-1): ",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=700, y=300)
        Boton_comp_agua = Button(miframe, text ="?", command= self.info_cw, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=300)
        self.comp_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.comp_agua_.place(x=700,y=330, width=150)

        comp_roca=Label(miframe, text="Cf(lpc^-1):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=700, y=420)
        Boton_comp_roca = Button(miframe, text ="?", command= self.info_cf, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=830, y=420)
        self.comp_roca_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.comp_roca_.place(x=700,y=450, width=150)

        #------------------------------------------columna 4----------------------------------------------------------

        intrusion_agua=Label(miframe, text="We(BY):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=990, y=180)
        Boton_intrusion_agua = Button(miframe, text ="?", command= self.info_we, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1090, y=180)
        self.intrusion_agua_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.intrusion_agua_.place(x=960,y=210, width=150)

        agua_producida=Label(miframe, text="Wp(BN):",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=990, y=300)
        Boton_producida = Button(miframe, text ="?", command= self.info_wp, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1090, y=300)
        self.agua_producida_=Entry(miframe, font=("times new roman",15), bg="lightgray", justify="right")
        self.agua_producida_.place(x=960,y=330, width=150)

        FR=Label(miframe, text="FR (fracción)",font=("times new roman", 15, "bold"),bg="white",fg="black").place(x=960, y=420)
        Boton_FR = Button(miframe, text ="?", command= self.info_FR, font=("times new roman", 10, "bold"),bg="white",fg="black").place(x=1090, y=420)
        self.txt_FR=Entry(miframe, font=("times new roman",15), bg="lightgray")
        self.txt_FR.place(x=960,y=450, width=150)



        #-----------------------------------------final de filas-----------------------------------------------------

        #-----------------------------------------Botones--------------------------------------------------------
        btn_calular=Button(miframe, text="Calcular", font=("times new roman",15),bg="orange", fg="black", cursor="hand2", command=self.calculos7).place(x=700, y=580, width=200, height=40)

        btn_volver=Button(miframe, text="Volver", font=("times new roman",15),bg="gray", fg="black", cursor="hand2", command=self.gas_sec).place(x=360, y=580, width=200, height=40)

        barraMenu=Menu(self.root)
        Filemenu=Menu(barraMenu)
        archivoMenu=Menu(barraMenu, tearoff=0)
        archivoMenu.add_command(label="Acerca de", command=self.barraAcercade_GasSEM)
        archivoMenu.add_command(label="Ayuda", command=self.barraAyuda_GasSEM)
        barraMenu.add_cascade(label="Menu", menu=archivoMenu)
        self.root.config(menu=barraMenu)
    
    def barraAcercade_GasSEM(self):
        messagebox.showinfo("Ecuación de Balance de Materiales (EBM)", "La Ecuación de Balance de Materiales hace uso del concepto básico de conservación de masa que establece que la producción acumulada observada, expresada como una extracción subterránea, debe ser igual a la expansión de los fluidos en el yacimiento resultante de una caída de presión finita o expresada como la masa de fluidos originalmente en el lugar igual a la masa de fluido restante más la masa de fluido producido.—Ahmed T.")

    def barraAyuda_GasSEM(self):
        messagebox.showinfo("¿Cómo sustituir los datos?", "Se debe rellenar todas las casillas, si no tiene algún dato coloque cero; para decimales utilice el punto.")


root=Tk()

obj=Register(root)
root.mainloop()

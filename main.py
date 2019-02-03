#!/usr/bin/env python
# coding: utf-8
from tkinter import *
from ttk import *
import tkMessageBox
from PIL import Image, ImageTk  
import tkinter.font as tkFont




#Le chiffrement de Vigenere utilisé est constitué du chiffrement des caract`eres accentu´es, des caract`eres majuscules, 
#des signes de ponctuation, des chifres... grace au codage ASCII qui comprend 255 caracteres au total ;) 
#car souvent les mot de passe sont constitué de caract`eres majuscules, des signes de ponctuation, des chifres.
fenetre = Tk()
y = 0
re1, re2, re3 = 0, 0, 0

fenetre.geometry("400x350+500+200")
fenetre.title("Mot de passe")
fenetre.resizable(width=False, height=False)
canvas = Canvas(fenetre, width=400, height=400)
canvas.pack()
image = Image.open("img.png")  
photo = ImageTk.PhotoImage(image)  
canvas.create_image(0,0, image=photo) 

fenetre.style = Style()
fenetre.style.theme_use("clam")


carre_couleur = "grey"
test0 = canvas.create_rectangle(80,80,100,100,fill=carre_couleur,outline='black')
test1 = canvas.create_rectangle(190,80,210,100,fill=carre_couleur,outline='black')
test2 = canvas.create_rectangle(290,80,310,100,fill=carre_couleur,outline='black')

test3 = canvas.create_rectangle(80,160,100,180,fill=carre_couleur,outline='black')
test4 = canvas.create_rectangle(190,160,210,180,fill=carre_couleur,outline='black')
test5 = canvas.create_rectangle(290,160,310,180,fill=carre_couleur,outline='black')

test6 = canvas.create_rectangle(80,240,100,260,fill=carre_couleur,outline='black')
test7 = canvas.create_rectangle(190,240,210,260,fill=carre_couleur,outline='black')
test8 = canvas.create_rectangle(290,240,310,260,fill=carre_couleur,outline='black')


case1, case2, case3, case4, case5, case6, case7, case8, case9, re1, re2, re3, tet  = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , ""
po, caisse = 0, 0
recommencer1 = 0






def anim():
    global recommencer1, caisse, po, test0
    if po == 0 :
        po = 1
        if caisse == 1:
            canvas.itemconfig(test0,fill='#76EEC6')
        if caisse == 2:
            canvas.itemconfig(test1,fill='#76EEC6')
        if caisse == 3:
            canvas.itemconfig(test2,fill='#76EEC6')
        if caisse == 4:
            canvas.itemconfig(test3,fill='#76EEC6')
        if caisse == 5:
            canvas.itemconfig(test4,fill='#76EEC6')
        if caisse == 6:
            canvas.itemconfig(test5,fill='#76EEC6')
        if caisse == 7:
            canvas.itemconfig(test6,fill='#76EEC6')
        if caisse == 8:
            canvas.itemconfig(test7,fill='#76EEC6')
        if caisse == 9:
            canvas.itemconfig(test8,fill='#76EEC6')
        fenetre.after(300, anim)
    elif recommencer1 == 1:
        canvas.itemconfig(test0,fill='#76EEC6')
        canvas.itemconfig(test1,fill='#76EEC6')
        canvas.itemconfig(test2,fill='#76EEC6')
        canvas.itemconfig(test3,fill='#76EEC6')
        canvas.itemconfig(test4,fill='#76EEC6')
        canvas.itemconfig(test5,fill='#76EEC6')
        canvas.itemconfig(test6,fill='#76EEC6')
        canvas.itemconfig(test7,fill='#76EEC6')
        canvas.itemconfig(test8,fill='#76EEC6')
        po = 1
        recommencer1 = 0
        fenetre.after(300, anim)



    elif po == 1 :
        po, caisse = 0, 0
        canvas.itemconfig(test0,fill='grey')
        canvas.itemconfig(test1,fill='grey')
        canvas.itemconfig(test2,fill='grey')
        canvas.itemconfig(test3,fill='grey')
        canvas.itemconfig(test4,fill='grey')
        canvas.itemconfig(test5,fill='grey')
        canvas.itemconfig(test6,fill='grey')
        canvas.itemconfig(test7,fill='grey')
        canvas.itemconfig(test8,fill='grey')

    


def quitter():
    fenetre1.quit()
        

     
def code(event):
    global caisse, fenetre1, y, tet, texte1, texte2, texte3, texte4, texte5, texte6, texte7, texte8, texte9, case1, case2, case3, case4, case5, case6, case7, case8, case9, fenetre, button, entry1, entry9, entry2, entry3, entry4, entry5, entry6, entry7, entry8
    if event.x >= 80 and event.x <= 100 and event.y >= 80 and event.y <= 100:
        case1 = case1 + 1
        caisse = 1
        anim()
    if event.x >= 190 and event.x <= 210 and event.y >= 80 and event.y <= 100:
        case2 = case2 + 1
        caisse = 2
        anim()
    if event.x >= 290 and event.x <= 310 and event.y >= 80 and event.y <= 100:
        case3 = case3 + 1
        caisse = 3
        anim()
    if event.x >= 80 and event.x <= 100 and event.y >= 160 and event.y <= 180:
        case4 = case4 + 1
        caisse = 4
        anim()
    if event.x >= 190 and event.x <= 210 and event.y >= 160 and event.y <= 180:
        case5 = case5 + 1
        caisse = 5
        anim()
    if event.x >= 290 and event.x <= 310 and event.y >= 160 and event.y <= 180:
        case6 = case6 + 1
        caisse = 6
        anim()
    if event.x >= 80 and event.x <= 100 and event.y >= 240 and event.y <= 260:
        case7 = case7 + 1
        caisse = 7
        anim()
    if event.x >= 190 and event.x <= 210 and event.y >= 240 and event.y <= 260:
        case8 = case8 + 1
        caisse = 8
        anim()
    if event.x >= 290 and event.x <= 310 and event.y >= 240 and event.y <= 260:
        case9 = case9 + 1
        caisse = 9
        anim()        
    
    if case1 == 0 and case2 == 0 and case3 == 0 and case4 == 0 and case5 == 0 and case6 == 0 and case7 == 1 and case8 == 2 and case9 == 1:
        fenetre.destroy()
        fenetre1 = Tk()
        fenetre1.geometry("400x375+500+200")
        fenetre1.title("gestionnaire de mot de passe")
        fenetre1.resizable(width=False, height=False)
        color = "#9E9E9E"
        font = tkFont.Font(family='Helvetica', size=16)
        fenetre1.configure(background=color) 
        bouton2 = Button(fenetre1, text="\nQuitter\n", command=quitter)
        bouton2.place(x="8", y="315")
        y = 2
        i = 1
        Labeltexte1 = Label(fenetre1, text="Bienvenue !", background=color, font=font ).pack()
        font = tkFont.Font(family='Helvetica', size=12)
        Labeltexte = Label(fenetre1, text="Après les modifications, faites sauvegarder.", background=color, font=font ).pack()
        button = Button(fenetre1, text = "\nSauvegarder\n", command=config)
        button.place(x="315", y="315")
        entry1 = Entry(fenetre1, width=50)
        entry1.place(x="50",y="50")
        entry2 = Entry(fenetre1, width=50)
        entry2.place(x="50",y="80")
        entry3 = Entry(fenetre1, width=50)
        entry3.place(x="50",y="110")
        entry4 = Entry(fenetre1, width=50)
        entry4.place(x="50",y="140")
        entry5 = Entry(fenetre1, width=50)
        entry5.place(x="50",y="170")
        entry6 = Entry(fenetre1, width=50)
        entry6.place(x="50",y="200")
        entry7 = Entry(fenetre1, width=50)
        entry7.place(x="50",y="230")
        entry8 = Entry(fenetre1, width=50)
        entry8.place(x="50",y="260")
        entry9 = Entry(fenetre1, width=50)
        entry9.place(x="50",y="290")

        p = 1
        texteclair, line = "", ""
        clef= "AQGH854MPIFV32554RGKD'_2FHHFk43)_@HFF65654FSNCHGO8268"
        for line in open("texte.txt", "r"):
            for i in range (0,len(line)):
                caractere=line[i]
                code=ord(caractere)
                decalage=ord(clef[i%len(clef)])
                codeclair=(code-decalage)%256
                caractereclair=chr(codeclair)
                texteclair = texteclair+caractereclair
            line = texteclair
            
            if p == 1:
                entry1.delete(0, END)
                
                entry1.insert(1, line[:(len(line)-1)])
                texte1 = line
            if p == 2:
                entry2.delete(0, END)
                entry2.insert(1, line[:(len(line)-1)])
                texte2 = line
            if p == 3:
                entry3.delete(0, END)
                entry3.insert(1, line[:(len(line)-1)])
                texte3 = line
            if p == 4:
                entry4.delete(0, END)
                entry4.insert(1, line[:(len(line)-1)])
                texte4 = line
            if p == 5:
                entry5.delete(0, END)
                entry5.insert(1, line[:(len(line)-1)])
                texte5 = line
            if p == 6:
                entry6.delete(0, END)
                entry6.insert(1, line[:(len(line)-1)])
                texte6 = line
            if p == 7:
                entry7.delete(0, END)
                entry7.insert(1, line[:(len(line)-1)])
                texte7 = line
            if p == 8:
                entry8.delete(0, END)
                entry8.insert(1, line[:(len(line)-1)])
                texte8 = line
            if p == 9:
                entry9.delete(0, END)
                entry9.insert(1, line)
                texte9 = line
            
            p = p + 1
            texteclair = ""
            
            
            

            
            
            
            
            
def config():
    global tet,entry9, entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, texte1, texte2, texte3, texte4, texte5, texte6, texte7, texte8, texte9
    tkMessageBox.showinfo("Information", "Sauvegarde avec succès")
    textechiffre = ""
    clef= "AQGH854MPIFV32554RGKD'_2FHHFk43)_@HFF65654FSNCHGO8268"
    for i in range(0,len(entry1.get())):
        caractere=entry1.get()[i]
        code=ord(caractere)
        decalage=ord(clef[i%len(clef)])
        codechiffre=(code+decalage)%256
        caracterechiffre=chr(codechiffre)
        textechiffre=textechiffre+caracterechiffre
    texte1 = textechiffre
    textechiffre = ""
    for i in range(0,len(entry2.get())):
        caractere=entry2.get()[i]
        code=ord(caractere)
        decalage=ord(clef[i%len(clef)])
        codechiffre=(code+decalage)%256
        caracterechiffre=chr(codechiffre)
        textechiffre=textechiffre+caracterechiffre
    texte2 = textechiffre
    textechiffre = ""
    for i in range(0,len(entry3.get())):
        caractere=entry3.get()[i]
        code=ord(caractere)
        decalage=ord(clef[i%len(clef)])
        codechiffre=(code+decalage)%256
        caracterechiffre=chr(codechiffre)
        textechiffre=textechiffre+caracterechiffre
    texte3 = textechiffre
    textechiffre = ""
    for i in range(0,len(entry4.get())):
        caractere=entry4.get()[i]
        code=ord(caractere)
        decalage=ord(clef[i%len(clef)])
        codechiffre=(code+decalage)%256
        caracterechiffre=chr(codechiffre)
        textechiffre=textechiffre+caracterechiffre
    texte4 = textechiffre
    textechiffre = ""
    for i in range(0,len(entry5.get())):
        caractere=entry5.get()[i]
        code=ord(caractere)
        decalage=ord(clef[i%len(clef)])
        codechiffre=(code+decalage)%256
        caracterechiffre=chr(codechiffre)
        textechiffre=textechiffre+caracterechiffre
    texte5 = textechiffre
    textechiffre = ""
    for i in range(0,len(entry6.get())):
        caractere=entry6.get()[i]
        code=ord(caractere)
        decalage=ord(clef[i%len(clef)])
        codechiffre=(code+decalage)%256
        caracterechiffre=chr(codechiffre)
        textechiffre=textechiffre+caracterechiffre
    texte6 = textechiffre
    textechiffre = ""
    for i in range(0,len(entry7.get())):
        caractere=entry7.get()[i]
        code=ord(caractere)
        decalage=ord(clef[i%len(clef)])
        codechiffre=(code+decalage)%256
        caracterechiffre=chr(codechiffre)
        textechiffre=textechiffre+caracterechiffre
    texte7 = textechiffre
    textechiffre = ""
    for i in range(0,len(entry8.get())):
        caractere=entry8.get()[i]
        code=ord(caractere)
        decalage=ord(clef[i%len(clef)])
        codechiffre=(code+decalage)%256
        caracterechiffre=chr(codechiffre)
        textechiffre=textechiffre+caracterechiffre
    texte8 = textechiffre
    textechiffre = ""
    for i in range(0,len(entry9.get())):
        caractere=entry9.get()[i]
        code=ord(caractere)
        decalage=ord(clef[i%len(clef)])
        codechiffre=(code+decalage)%256
        caracterechiffre=chr(codechiffre)
        textechiffre=textechiffre+caracterechiffre
    texte9 = textechiffre



    
    tet = texte1 + "\n" + texte2 + "\n" + texte3 + "\n" + texte4 + "\n" + texte5 + "\n" + texte6 + "\n" + texte7 + "\n" + texte8 + "\n" + texte9
    fichierrr = open("texte.txt", "w")
    fichierrr.write(tet)
    
    



        

def recommencer():
    global recommencer1, case1, case2, case3, case4, case5, case6, case7, case8, case9
    case1 = 0
    case2 = 0
    case3 = 0
    case4 = 0
    case5 = 0
    case6 = 0
    case7 = 0
    case8 = 0
    case9 = 0
    recommencer1 = 1
    anim()
        

canvas.bind('<Button-1>',code)

font = tkFont.Font(family='Helvetica', size=20)
bouton1 = Button(fenetre, text = "Recommencer", command=recommencer).place(x="300", y="310")
textemdp = Label(fenetre, text="Dessine pour dévérouiller", font=font, background="#80A29E").place(x="50", y="20")











if y == 2:
        fenetre1.mainloop()
else:
    fenetre.mainloop()

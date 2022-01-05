from tkinter import *





#creation d'une page pour les levels


#je fais une fonction pour faire ouvrir la fenetre level quand le joueur appuie sur une touche 

def level(stats):
    #je met en place les parametre de base de la fenetre

    window = Tk()
    window.title("Level")
    window.geometry('300x300')
    #level et point de competance disponible
    
    tx=Label(window,text="Level {}".format(stats[3]))
    tx.grid(column=0,row=0)
    tx1=Label(window,text="Point de competance disponible {}".format(stats[4]))
    tx1.grid(column=0,row=2)

    #je montre les degats que possde le joueur et ces pv
    lbl = Label(window, text="Les points de degats {}".format(stats[0]))
    lbl.grid(column=0, row=10)
    lbl1=Label(window,text="Les points de vie {}".format(stats[1]))
    lbl1.grid(column=0,row=12)

    #je lui donne le choix d'augumenter ces stats en fonction de ces points de competance 
    spin = Spinbox(window, from_=stats[0], to=stats[0]+stats[4], width=5)
    spin.grid(column=5,row=10)
    spin1=Spinbox(window, from_=stats[1],to=stats[1]+stats[4],width=5)
    spin1.grid(column=5,row=12)


    #je fais une fonction qui permet de valider ces choix 
    def clicked():
        
        x=spin.get()
        if int(x)>stats[0]:

            #calcul permmetant de savoir combien de point de competance il me reste
            i=stats[0]+stats[4]
            stats[4]=i-int(x)
            stats[0]=int(x)
            #mettre a jour les données dans les texte 
            lbl.configure(text="Les points de degats {}".format(stats[0]))
            tx1.configure(text="Point de competance disponible {}".format(stats[4]))
            #mettre a jour les données dans les spin
            spin.configure(from_=stats[0], to=stats[0]+stats[4], width=5)
            spin1.configure(from_=stats[1],to=stats[1]+stats[4],width=5)
    
        



        y=spin1.get()
        if int(y)>stats[1]:

            #calcul permmetant de savoir combien de point de competance il me reste
            i=stats[1]+stats[4]
            stats[4]=i-int(y)
            stats[1]=int(y)
            lbl1.configure(text="Les points de vie {}".format(stats[1]))
            tx1.configure(text="Point de competance disponible {}".format(stats[4]))

            spin.configure(from_=stats[0], to=stats[0]+stats[4], width=5)
            spin1.configure(from_=stats[1],to=stats[1]+stats[4],width=5)

           
        


    
    #je créer le bouton
    btn = Button(window, text="Valide", command=clicked)
    btn.grid(column=8, row=10) 
    btn1=Button(window,text="Valide",command=clicked)
    btn1.grid(column=8,row=12)


    window.mainloop()
    return(stats)



    
    







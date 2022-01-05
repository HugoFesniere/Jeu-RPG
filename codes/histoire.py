from tkinter import * #importe tout de Tkinter
import game

def window_storie():
    window = Tk() #La fenêtre afficher est Tkinter
    window.iconbitmap("../images/soul_logo.ico") #Configure le logo de la fenêtre (.ico)
    window.geometry("1366x768") #Configure la taille de la fenêtre
    window.resizable(height=False,width=False) #Empêche de pouvoir modifier la taille de la fenêtre
    window.title("Light Your Soul") #Configure le nom de la fenêtre
    window.config(background='black')
    background = PhotoImage(file = "../maps/fond-de-jeu.png")
    show_background = Canvas(window, width=1366, height=580, bd=7.5, background = 'black', relief=GROOVE)
    show_background.create_image(683,200,image=background)
    show_background.pack()
    nombre_clic  = IntVar(window,value= 0 ) 
    def add_passage (window,texte_scenario):
        temp= nombre_clic.get()
        if temp == 0 :
            lieu_texte_scenario.config(text="Vous")
            texte_scenario.config(text="*Vous vous relevez*")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 1 :
            lieu_texte_scenario.config(text="...")
            texte_scenario.config(text="-Ahhh un mort vivant !!")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 2 :
            lieu_texte_scenario.config(text="Vous")
            texte_scenario.config(text="*Vous vous dépoussièrez*")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 3 :
            lieu_texte_scenario.config(text="...")
            texte_scenario.config(text="-Oh, mais c’est toi, comment vas-tu ? Pas trop mal je suppose, tu as une meilleure tête que d’habitude.")
            texte_scenario_2.config(text="Quel… Hhmmm… plaisir de te retrouver.")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 4 :
            lieu_texte_scenario.config(text="Vous")
            texte_scenario.config(text="Qui es-tu ?")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 5 :
            lieu_texte_scenario.config(text="...")
            texte_scenario.config(text="Quoi ? Comment ça ?")
            texte_scenario_2.config(text="Tu ne vas pas me dire que tu as oublié ton meilleur pote ? Jacque Asseur")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 6 :
            lieu_texte_scenario.config(text="Vous")
            texte_scenario.config(text="J’ai mal partout, on est où ?")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 7 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Je voie, je suppose que tu as une perte de mémoire à cause de l’accident.")
            texte_scenario_2.config(text="Vue qu’on est meilleur amis… Même si t’en souviens pas sale ingrat… Je vais t’aider…")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 8 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Alors…")
            texte_scenario_2.config(text="Hhmmm…")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 9 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Tu t’appelles comment déjà ?")
            texte_scenario_2.config(text="")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 10 :
            lieu_texte_scenario.config(text="Vous")
            texte_scenario.config(text="...")
            texte_scenario_2.config(text="Juba")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 11 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Haha… comme ma grand-mère.")
            texte_scenario_2.config(text="Espérons que ça revienne à la mode.")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 12 :
            lieu_texte_scenario.config(text="Système")
            texte_scenario.config(text="-@ Vous avez débloquez la capacité : Le seum @-")
            texte_scenario_2.config(text="-@ Vous avez débloquez la capacité : Cassage de Gueule @-")
            nombre_clic.set( nombre_clic.get() + 1 )
        elif temp == 13 :
            lieu_texte_scenario.config(text="Jacque Asseur")
            texte_scenario.config(text="Allez salut")
            texte_scenario_2.config(text="...")
            nombre_clic.set( nombre_clic.get() + 1 )
        else :
            window.destroy()
            game.Game().run()

    lieu_texte_scenario = LabelFrame(window, text="..." ,font=("Super Legend Boy",30), bg= 'black',fg='white',relief=GROOVE, bd=7.5,)
    lieu_texte_scenario.pack(side=BOTTOM)
    texte_scenario=Label(lieu_texte_scenario, text="-Heeeeeyyyyy !",width=78, font=("Super Legend Boy",20) , bg= 'black',fg='white')
    texte_scenario.grid(row=0,column=0)
    texte_scenario_2=Label(lieu_texte_scenario, text="Vous êtes en vie ? Vous m’entendez ?",width=78, font=("Super Legend Boy",20) , bg= 'black',fg='white')
    texte_scenario_2.grid(row=1,column=0)
    bouton_image =PhotoImage( file="../images/play.png").zoom(3) .subsample(35)
    bouton_scenario=Button(lieu_texte_scenario,image=bouton_image,bg='black',bd =0 ,width=85,height=85, highlightthickness= 0, command= lambda :add_passage(window,texte_scenario))
    bouton_scenario.grid(row=0,column=1,rowspan=2,pady=20)
    window.mainloop() #Permet d'avoir la fenêtre ouverte (toujours à la fin)
    
    
    

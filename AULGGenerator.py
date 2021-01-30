import random
from tkinter import *

roles = [
    'Cosmonaute',
    'Cupidon',
    'Inspecteur',
    'Dictateur',
    'Illusionniste',
    'Simple Crewmate',
    'Ancien',
    'Gardien',
    'Héritié/Enfant',
    'Traître',
    'Sauvage',
    'Sauvage Bavarde',
    'Chaman',
    'Sorcier',
    'Duelliste'
]

imposteurs = [
    'Imposteur Saboteur',
    'Imposteur Hackeur',
    'Imposteur Assassin',
    'Imposteur Fou',
    'Imposteur Déserteur'
]

rolesDisponibles = roles
imposteursDisponibles = imposteurs

print('Combien de joueurs ?')
countPlayers = int(input())

joueurs = []

for i in range(countPlayers):
    joueurs.append([""] * 3)

for i in range(countPlayers):
    print('Nom du Joueur '+ str(i+1) + ' :')
    playerName = input()
    joueurs[i][0] = playerName


imposteurSelected = random.randint(0,len(imposteursDisponibles) - 1)

if imposteurs[imposteurSelected] == 'Imposteur Déserteur':
    imposteursPlayers = [["",""],["",""]]
    imposteursPlayers[0][1] = imposteurs[imposteurSelected]
    del imposteursDisponibles[imposteurSelected]
    imposteurSelected = random.randint(0,len(imposteursDisponibles) - 1)
    imposteursPlayers[1][1] = imposteurs[imposteurSelected]
    print("IMPOSTEURS : " + imposteursPlayers[0][1] + " et " + imposteursPlayers[1][1])
    imposteursPointerSelected = [["",""],["",""]]
else:
    imposteursPlayers = [["",""]]
    imposteursPlayers[0][1] = imposteurs[imposteurSelected]
    print("IMPOSTEUR : " + imposteursPlayers[0][1])
    imposteursPointerSelected = [["",""]]

for i in range(len(joueurs)):
    print(str(i) + " : " + joueurs[i][0])

for i in range(len(imposteursPlayers)):
    print("A qui voulez-vous assigner le rôle " + imposteursPlayers[i][1] + " ?")
    choiceAssign = int(input())
    joueurs[choiceAssign][1] = imposteursPlayers[i][1]

"""for i in range(len(imposteursPlayers)):
    print("Qui est l\'imposteur " + str(i) + " ?")
    imposteurPointer = int(input())
    imposteursPointerSelected[i][0] = imposteurPointer

for i in range(len(imposteursPointerSelected)):
    random.randint(0,len(rolesDisponibles) - 1)"""

for i in range(countPlayers):
    if joueurs[i][1] == "":
        roleSelected = random.randint(0,len(rolesDisponibles) - 1)


        roleName = rolesDisponibles[roleSelected]
        joueurs[i][1] = roleName


        if roleName == 'Cosmonaute':
            j = 0
            while j < len(rolesDisponibles):
                if rolesDisponibles[j] == 'Imposteur Déserteur':
                    del rolesDisponibles[j]
                    j = j - 1
                j = j + 1

        if roleName == 'Ancien':
            j = 0
            while j < len(rolesDisponibles):
                if rolesDisponibles[j] == 'Imposteur Assassin' or rolesDisponibles[j] == 'Imposteur Fou':
                    del rolesDisponibles[j]
                    j = j - 1
                j = j + 1


        if roleName == 'Cupidon':
            j = 0
            while j < len(rolesDisponibles):
                if rolesDisponibles[j] == 'Imposteur Déserteur':
                    del rolesDisponibles[j]
                    j = j - 1
                j = j + 1

        if roleName == 'Inspecteur':
            j = 0
            while j < len(rolesDisponibles):
                if rolesDisponibles[j] == 'Imposteur Hackeur':
                    del rolesDisponibles[j]
                    j = j - 1
                j = j + 1


        if roleName == 'Héritié/Enfant':
            x = 0
            while x != 1:
                ParentSelected = random.randint(0,len(joueurs) - 1)
                if ParentSelected != i:
                    joueurs[ParentSelected][2] = 'Parent'
                    x=1


        if roleName == 'Sauvage':
            j = 0
            while j < len(rolesDisponibles):
                if rolesDisponibles[j] == 'Sauvage Bavarde':
                    del rolesDisponibles[j]
                    j = j - 1
                j = j + 1


        if roleName == 'Sauvage Bavarde':
            j = 0
            while j < len(rolesDisponibles):
                if rolesDisponibles[j] == 'Sauvage':
                    del rolesDisponibles[j]
                    j = j - 1
                j = j + 1


        j = 0
        while j < len(rolesDisponibles):
            if rolesDisponibles[j] == roleName:
                del rolesDisponibles[j]
                j = j - 1
            j = j + 1


print("")
print("")
print("")
print("")
print("")
print("")

for i in range(len(joueurs)):
    space = ""
    for j in range(random.randint(0,100)):
        space = space + " "
    print(joueurs[i][0] + " = ||" + joueurs[i][1] + "(" + str(joueurs[i][2]) + ")" + space + "||")

print("")
print("")
print("")
print("")
print("")
print("")



window = Tk()

window.title("Among Us Loup Garou Generator")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(backgroun="black")

listPlayers = Frame(window, bg=("black"))
listPlayers.pack(side=BOTTOM)

label_title = Label(window, text="Generator", font=("Arial", 40), bg="#41B77F", fg="white")
label_title.pack(side=TOP)

for i in range(len(joueurs)):
    Label(listPlayers, text=joueurs[i][0] + " = " + joueurs[i][1] + "(" + str(joueurs[i][2]) + ")", font=("Arial", 20), bg="black", fg="white").pack(expand=YES)

window.mainloop()
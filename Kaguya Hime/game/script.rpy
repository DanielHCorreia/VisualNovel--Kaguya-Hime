# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jogo")
#Cenários principais
image C1 = "C1.png"
image C2 = "C2.png"
image C3 = "C3.png"
image C4 = "C4.png"
image C5 = "C5.png"
image C6 = "C6.png"
image C7 = "C7.png"
image C8 = "C8.png"
image C9 = "C9.png"
image C10 = "C10.png"
#Cenários com itens destacados

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene C1
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.
    "Olá, vamos contar a história de Kaguya Hime"
    "No decorrer do jogo você vai ter que adivinhar o hiragana correspondente ao item em destaque"
    "Bom jogo!"

    # This ends the game.

    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    yene = 0
define e = Character("Jogo")


#style.default.font = "VL Gothic regular.ttf"
#style.default.language = "eastasian"


#Cenários principais
image introducao = "introducao.png"
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
image C1_Bamboo = "/Imagens com itens destacados/C1_Bamboo.png"
image C1_Machado = "/Imagens com itens destacados/C1_Machado.png"
image C1_Passaro = "/Imagens com itens destacados/C1_Passaro.png"

image C2_CorVermelho = "/Imagens com itens destacados/C2_CorVermelho.png"
image C2_Machado = "/Imagens com itens destacados/C2_Machado.png"
image C2_MoedasDeOuro = "/Imagens com itens destacados/C2_MoedasDeOuro.png"

image C3_2 = "/Imagens com itens destacados/C3_2.png"
image C3_Leque = "/Imagens com itens destacados/C3_Leque.png"
image C3_Passaro = "/Imagens com itens destacados/C3_Passaro.png"

image C4_Azul = "/Imagens com itens destacados/C4_Azul.png"
image C4_Rosa = "/Imagens com itens destacados/C4_Rosa.png"
image C4_Vermelho = "/Imagens com itens destacados/C4_Vermelho.png"

image C5_marAzul = "/Imagens com itens destacados/C5_marAzul.png"
image C5_Relampago = "/Imagens com itens destacados/C5_Relampago.png"

image C6_Leque = "/Imagens com itens destacados/C6_Leque.png"
image C6_LuaAmarela = "/Imagens com itens destacados/C6_LuaAmarela.png"
image C6_Vermelho = "/Imagens com itens destacados/C6_Vermelho.png"

image C7_3 = "/Imagens com itens destacados/C7_3.png"
image C7_Amarelo = "/Imagens com itens destacados/C7_Amarelo.png"
image C7_Azul = "/Imagens com itens destacados/C7_Azul.png"

image C8_Amarelo = "/Imagens com itens destacados/C8_Amarelo.png"
image C8_Arco = "/Imagens com itens destacados/C8_Arco.png"
image C8_Flecha = "/Imagens com itens destacados/C8_Flecha.png"

image C9_Azul = "/Imagens com itens destacados/C9_Azul.png"
image C9_Cavalo = "/Imagens com itens destacados/C9_Cavalo.png"
image C9_Nuvem = "/Imagens com itens destacados/C9_Nuvem.png"

image C10_Amarelo = "/Imagens com itens destacados/C10_Amarelo.png"
image C10_Rosa = "/Imagens com itens destacados/C10_Rosa.png"
image C10_Verde = "/Imagens com itens destacados/C10_Verde.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    
    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.
    play music "audio/JapaneseSoundTrack.mp3"
    scene introducao
    "Olá, vamos contar a história de Kaguya Hime"
    "No decorrer do jogo você vai ter que adivinhar o hiragana correspondente ao item em destaque"
    "Bom jogo!"


    label capitulo1:
    scene C1
    "Um dia, um velho cortador de bambu encontrou uma linda menina em uma planta de bambu. Ele a levou para casa."
    scene C1_Bamboo
    "Escolha o Hiragana correto, Qual o nome da planta em destaque?"
    menu: 
        "竹": #Bambu
            "Certo"
            $yene += 100
            "Parabéns, você ganhou [yene] Yenes que podem ser usados para desbloquear novas partes da história."
        "緑": #Verde
            "Errado"
        "黄色": #Amarelo
            "Errado"
            
    
    


    scene C2
    "No dia seguinte, ele encontrou muitas moedas de ouro em uma planta de bambu."
    "Ele e sua esposa cuidaram muito bem da menina. Eles a chamavam de Kaguya Hime."
    scene C3
    "Kaguya Hime cresceu e se tornou uma linda jovem."


    label capitulo2:
    scene C4
    "Muitos príncipes queriam se casar com ela, mas Kaguya Hime não queria se casar com ninguém."
    "Então ela deu a eles uma tarefa muito difícil: trazer a pedra de cristal do peito do Dragão."
    scene C5
    "Os príncipes foram em busca da pedra de cristal, eles lutaram muito com o dragão, mas não conseguiram a pedra de cristal."
    scene C6
    "Kaguya Hime não estava feliz. Ela sempre olhava para a lua cheia e se sentia triste."


    label capitulo3:
    scene C7
    "Um dia Kaguya Hime disse ao cortador de bambu que ela realmente veio da lua e as pessoas da lua logo virão buscá-la."
    scene C8
    "O cortador de bambu não queria que Kaguya Hime fosse embora. Ele pediu aos samurais para protegê-la do povo da lua."
    scene C9
    "Na noite de lua cheia, o povo da lua veio. Eles levaram Kaguya Hime de volta à lua. Os samurais não podiam fazer nada."
    scene C10
    "Kaguya Hime gostou muito do cortador de bambu e das pessoas do mundo. Mas Kaguya Hime pertencia à lua. Ela às vezes volta ao mundo quando é lua cheia."
    # This ends the game.

    return

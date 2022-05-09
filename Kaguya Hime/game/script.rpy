# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    yene = 0
    acertos = 0
    erros = 0
    escolhas = {1: 'とり(tori)', 2: "みどり (midori)", 3: "おの (ono)", 4: "たけ (take)", 5: "あお (ao)",
               6:"くろ (kuro)", 7:"あか (aka)", 8 :"あかいろ (akairo)", 9: "オレンジいろ(orenjiiro)", 10:"や (ya)" }
    resposta = 0
define e = Character("Jogo")


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




        


label mensagem_de_acerto:
            $yene += 100
            $acertos +=1
            "Parabéns a resposta está correta, você ganhou mais 100 Yen."
            "Você está com um total de [yene] Yen"
            return
            
label mensagem_de_erro:
            "Resposta incorreta"
            $erros+=1
            return           


#$resposta = random.randint(1, 10)
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
    "No decorrer do jogo você vai ter que adivinhar a palavra correspondente ao item em destaque"
    "Caso acerte, ganhará 100 yen virtuais, que podem ser usados para desbloquear novas partes da história"
    "Bom jogo!"
    

    label capitulo1:
    scene C1 with dissolve
    "Um dia, um velho cortador de bambu encontrou uma linda menina em uma planta de bambu. Ele a levou para casa."
    scene C1_Bamboo with dissolve
    "Escolha a palavra correta. Qual o nome da planta em destaque?"
    $resposta = escolhas.get(2)
    #$teste = escolhas.get(1)
    menu: 
        "たけ (take)": #Bambu
            "Bambu = たけ (take)"
            call mensagem_de_acerto
        "[resposta]": #Amarelo
            call mensagem_de_erro
        "escolhas.get(2)": #Verde
            call mensagem_de_erro
    
    scene C1_Machado with dissolve
    "Escolha a palavra correta. Qual o nome da ferramenta em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_erro
        "おの (ono)": #Machado
            "Machado = おの (ono)"
            call mensagem_de_acerto
        "たけ (take)": #Bambu
            call mensagem_de_erro

    scene C1_Passaro with dissolve
    #Faltar usar o comando Zoom para deixar o pássaro em evidência no meio da tela
    "Escolha a palavra correta. Qual o nome do animal em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro  


    scene C2 with dissolve
    #Zerar quantidade de yen a cada cena
    "No dia seguinte, ele encontrou muitas moedas de ouro em uma planta de bambu."
    "Ele e sua esposa cuidaram muito bem da menina. Eles a chamavam de Kaguya Hime."
    scene C2_CorVermelho with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C2_Machado with dissolve
    "Escolha a palavra correta. Qual o nome da ferramenta em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C2_MoedasDeOuro with dissolve
    "Escolha a palavra correta. Qual a palavra moeda?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro   
    scene C3 with dissolve
    "Kaguya Hime cresceu e se tornou uma linda jovem."
    scene C3_Leque with dissolve
    "Escolha a palavra correta. Qual o nome do item em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C3_2 with dissolve
    "Escolha a palavra correta. Qual o nome do animel em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C3_Passaro with dissolve
    "Escolha a palavra correta. Qual o nome do animal em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro      


    label capitulo2:
    scene C4 with dissolve
    "Muitos príncipes queriam se casar com ela, mas Kaguya Hime não queria se casar com ninguém."
    "Então ela deu a eles uma tarefa muito difícil: trazer a pedra de cristal do peito do Dragão."
    scene C4_Azul with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C4_Vermelho with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C4_Rosa with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro      


    scene C5 with dissolve
    "Os príncipes foram em busca da pedra de cristal, eles lutaram muito com o dragão, mas não conseguiram a pedra de cristal."
    scene C5_marAzul with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C5_Relampago with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro


    scene C6
    "Kaguya Hime não estava feliz. Ela sempre olhava para a lua cheia e se sentia triste."
    scene C6_Leque with dissolve
    "Escolha a palavra correta. Qual o nome do item em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C6_LuaAmarela with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C6_Vermelho with dissolve
    "Escolha a palavra correta. Qual o nome da item em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro


    label capitulo3:
    scene C7 with dissolve
    "Um dia Kaguya Hime disse ao cortador de bambu que ela realmente veio da lua e as pessoas da lua logo virão buscá-la."
    scene C7_3 with dissolve
    "Escolha a palavra correta. Qual o nome da item em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C7_Amarelo with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C7_Azul with dissolve
    "Escolha a palavra correta. Qual o nome da item em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro


    scene C8
    "O cortador de bambu não queria que Kaguya Hime fosse embora. Ele pediu aos samurais para protegê-la do povo da lua."
    scene C8_Amarelo with dissolve
    "Escolha a palavra correta. Qual o nome da item em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C8_Arco with dissolve
    "Escolha a palavra correta. Qual o nome da item em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C8_Flecha with dissolve
    "Escolha a palavra correta. Qual o nome da item em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro


    scene C9
    "Na noite de lua cheia, o povo da lua veio. Eles levaram Kaguya Hime de volta à lua. Os samurais não podiam fazer nada."
    scene C9_Azul with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C9_Cavalo with dissolve
    "Escolha a palavra correta, qual palavra é equivalente a cavalo?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C9_Nuvem with dissolve
    "Escolha a palavra correta."
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro


    scene C10 with dissolve
    "Kaguya Hime gostou muito do cortador de bambu e das pessoas do mundo. Mas Kaguya Hime pertencia à lua. Ela às vezes volta ao mundo quando é lua cheia."
    scene C10_Amarelo with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C10_Rosa with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    scene C10_Verde with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "とり(tori)": #Pássaro
            call mensagem_de_acerto
        "おの (ono)": #Machado 
            call mensagem_de_erro
        "たけ (take)": #Bambu
            call mensagem_de_erro
    # This ends the game.

    return

# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    yene = 0
    def texto():
        if(1==1):
            ui.textbutton("{color=#FFFFFF} Seus créditos", xpos=50,ypos=50)
            ui.textbutton("{color=#FFFFFF} ¥ [yene]", xpos=50,ypos=100)
    config.overlay_functions.append(texto)
    acertos = 0
    erros = 0
    escolhas =[
    "くろ   (kuro)", "あか    (aka)",  "オレンジいろ(orenjiiro)",
    "すいぶん (suibun)", "かぜ  (kaze)", "くるま  (kuruma)", "  さる   (saru)",
    "いろ    (iro)", "せいりょく (seiryoku)", "おと     (oto)", "いし    (ishi)", "こがね (kogane)",
    "おうごん(ougon)", "くない (kunai)", "ふえたけ (fuetake)", "じょし  (joshi)", "しょうねん  (shounen)",
    "あかちゃん (akachan)", "ちち (chichi)", "はは   (haha)", "そぼ   (sobo)", "おはよう   (ohayou)",
    "ありがとう (arigatou)","ばか   (baka)"]

    respostasCorretas =['たけ   (take)',' おの    (ono)','  とり   (tori)', #Respostas do  C1
    'あかいろ (akairo)','  おの   (ono)',"こうか (kouka)", #Respostas do  C2.
    "はうちわ (hauchiwa)", " とり    (tori)", #Respostas do C3
    " あお     (ao)", 'あかいろ (akairo)', 'ももいろ (momoiro)', #Respostas do  C4
    ' あお     (ao)', "    き      (ki)", #Respostas do  C5
    "はうちわ (hauchiwa)", "    き      (ki)", 'あかいろ (akairo)', #Respostas do  C6
    " さん    (san)", "    き      (ki)",' あお     (ao)',  #Respostas do  C7
    "    き      (ki)", "ゆみ   (yumi)","    や       (ya)", #Respostas do  C8
    ' あお     (ao)', "うま (uma)", "くも    (kumo)", #Respostas do  C9
    "    き      (ki)",'ももいろ (momoiro)', "みどり (midori)"] #Respostas do  C10

    #respostasCorretas =['Bambu = たけ (take)','Machado = おの (ono)','Pássaro = とり (tori)', #Respostas do  C1
    #'Vermelho = あかいろ (akairo)','Machado = おの (ono)',"Moeda = こうか (kouka)", #Respostas do  C2.
    #"Leque japonês = はうちわ (hauchiwa)", "Pássaro = とり (tori)", #Respostas do C3
    #"Azul = あお (ao)", 'Vermelho = あかいろ (akairo)', 'Rosa = ももいろ (momoiro)', #Respostas do  C4
    #'Azul = あお (ao)', "Amarelo = き (ki)", #Respostas do  C5
    #"Leque japonês =  はうちわ (hauchiwa)", "Amarelo = き (ki)", 'Vermelho = あかいろ (akairo)', #Respostas do  C6
    #"Três = さん (san)", "Amarelo = き (ki)",'Azul = あお (ao)',  #Respostas do  C7
    #"Amarelo = き (ki)", "Arco = ゆみ(yumi)","Flecha = や (ya)", #Respostas do  C8
    #'Azul = あお (ao)', "Cavalo = うま (uma)", "Nuvem = くも (kumo)", #Respostas do  C9
    #"Amarelo = き (ki)",'Rosa = ももいろ (momoiro)', "Verde = みどり (midori)"] #Respostas do  C10
#Cenários principais
label importação_de_imagens_e_video:
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
    #image videofinal = Movie(size=(1920,1080), channel = "movie",play="video/kaguyahimetheend.ogv", loop=True)

label mensagem_de_acerto:
            $yene += 100
            $acertos +=1
            "Parabéns a resposta está correta, você ganhou mais 100 Yen."
            "Você está com um total de [yene] Yen"
            label gerarOpcoesAcerto:
            $opcaoErrada1 = renpy.random.choice(escolhas)
            $opcaoErrada2 = renpy.random.choice(escolhas)
            if opcaoErrada1 == opcaoErrada2:
                jump gerarOpcoesAcerto
            return
            
label mensagem_de_erro:
            "Resposta incorreta"
            $erros+=1
            #label gerarOpcoesAcerto:
            $opcaoErrada1 = renpy.random.choice(escolhas)
            $opcaoErrada2 = renpy.random.choice(escolhas)
            if opcaoErrada1 == opcaoErrada2:
                jump gerarOpcoesErro
            return           


#$resposta = random.randint(1, 10)
# The game starts here.
label start:
#Gerar a primeira opção errada
$opcaoErrada1 = renpy.random.choice(escolhas)
$opcaoErrada2 = renpy.random.choice(escolhas)

play music "audio/JapaneseSoundTrack.mp3"
scene introducao
"Olá, vamos contar a história de Kaguya Hime"
"No decorrer do jogo você vai ter que adivinhar a palavra correspondente ao item em destaque"
"Caso acerte, ganhará 100 yen virtuais, que podem ser usados para desbloquear novas partes da história"
"Bom jogo!"
label capitulo1:
    #renpy.movie_cutscene("video/kaguyahimetheend.mp4")
    scene C1 with dissolve
    "Um dia, um velho cortador de bambu encontrou uma linda menina em uma planta de bambu. Ele a levou para casa."
    scene C1_Bamboo with dissolve
    "Escolha a palavra correta. Qual o nome da planta em destaque?"
    menu: 
        "[respostasCorretas[0]]": 
            "Bambu = たけ (take)"
            call mensagem_de_acerto
        "[opcaoErrada1]": 
            call mensagem_de_erro
        "[opcaoErrada2]": 
            call mensagem_de_erro
    scene C1_Machado with dissolve
    "Escolha a palavra correta. Qual o nome da ferramenta em destaque?"
    menu: 
        "[opcaoErrada1]": 
            call mensagem_de_erro
        "[respostasCorretas[1]]": 
            "Machado = おの (ono)"
            call mensagem_de_acerto
        "[opcaoErrada2]": 
            call mensagem_de_erro

    scene C1_Passaro with dissolve
    "Escolha a palavra correta. Qual o nome do animal em destaque?"
    menu: 
        "[respostasCorretas[2]]":
            "Pássaro = とり (tori)" 
            call mensagem_de_acerto
        "[opcaoErrada2]":  
            call mensagem_de_erro
        "[opcaoErrada1]": 
            call mensagem_de_erro  
    scene C2 with dissolve
    "No dia seguinte, ele encontrou muitas moedas de ouro em uma planta de bambu."
    "Ele e sua esposa cuidaram muito bem da menina. Eles a chamavam de Kaguya Hime."
    scene C2_CorVermelho with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[respostasCorretas[3]]":
            'Vermelho = あかいろ (akairo)' 
            call mensagem_de_acerto
    scene C2_Machado with dissolve
    "Escolha a palavra correta. Qual o nome da ferramenta em destaque?"
    menu: 
        "[respostasCorretas[4]]":
            "Machado = おの (ono)"
            call mensagem_de_acerto
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[opcaoErrada2]": 
            call mensagem_de_erro
    scene C2_MoedasDeOuro with dissolve
    "Escolha a palavra correta. Qual a palavra moeda?"
    menu: 
        "[opcaoErrada1]": 
            call mensagem_de_erro
        "[respostasCorretas[5]]":
            'Moeda = こうか (kouka)'  
            call mensagem_de_acerto
        "[opcaoErrada2]": 
            call mensagem_de_erro   
    scene C3 with dissolve
    "Kaguya Hime cresceu e se tornou uma linda jovem."
    scene C3_Leque with dissolve
    "Escolha a palavra correta. Qual o nome do item em destaque?"
    menu: 
        "[respostasCorretas[6]]":
            "Leque japonês = はうちわ (hauchiwa)" 
            call mensagem_de_acerto
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]": 
            call mensagem_de_erro
    scene C3_Passaro with dissolve
    "Escolha a palavra correta. Qual o nome do animal em destaque?"
    menu: 
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]": 
            call mensagem_de_erro
        "[respostasCorretas[7]]":
            "Pássaro = とり (tori)" 
            call mensagem_de_acerto     
    "Para continuar você precisa ter ao menos 600 yen"
    if yene<600 :
        "Você tem apenas [yene] yen. Tente responder novamente as perguntas para ir para a próxima fase"
        jump capitulo1
    else:
        "Parabéns, você pode continuar com a história e seus [yene] yen foram zerados"

    label capitulo2:
    scene C4 with dissolve
    "Muitos príncipes queriam se casar com ela, mas Kaguya Hime não queria se casar com ninguém."
    "Então ela deu a eles uma tarefa muito difícil: trazer a pedra de cristal do peito do Dragão."
    scene C4_Azul with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu:
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[respostasCorretas[8]]":
            "Azul = あお (ao)"  
            call mensagem_de_acerto
        "[opcaoErrada1]": 
            call mensagem_de_erro
    scene C4_Vermelho with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[respostasCorretas[9]]": 
            'Vermelho = あかいろ (akairo)'
            call mensagem_de_acerto
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[opcaoErrada2]": 
            call mensagem_de_erro
    scene C4_Rosa with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[respostasCorretas[10]]":
            'Rosa = ももいろ (momoiro)'
            call mensagem_de_acerto      
    scene C5 with dissolve
    "Os príncipes foram em busca da pedra de cristal, eles lutaram muito com o dragão, mas não conseguiram a pedra de cristal."
    scene C5_marAzul with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu:
        "[opcaoErrada2]": 
                call mensagem_de_erro
        "[opcaoErrada1]":  
                call mensagem_de_erro
        "[respostasCorretas[11]]":
                'Azul = あお (ao)'
                call mensagem_de_acerto
    scene C5_Relampago with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[respostasCorretas[12]]":
            "Amarelo = き (ki)" 
            call mensagem_de_acerto
        "[opcaoErrada1]": 
            call mensagem_de_erro
        "[opcaoErrada2]": 
            call mensagem_de_erro
    scene C6 with dissolve
    "Kaguya Hime não estava feliz. Ela sempre olhava para a lua cheia e se sentia triste."
    scene C6_Leque with dissolve
    "Escolha a palavra correta. Qual o nome do item em destaque?"
    menu: 
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[respostasCorretas[13]]":
            "Leque japonês =  はうちわ (hauchiwa)" 
            call mensagem_de_acerto
    scene C6_LuaAmarela with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[opcaoErrada1]": 
            call mensagem_de_erro
        "[opcaoErrada2]":  
            call mensagem_de_erro
        "[respostasCorretas[14]]":
            "Amarelo = き (ki)" 
            call mensagem_de_acerto
    scene C6_Vermelho with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[opcaoErrada1]": 
            call mensagem_de_erro
        "[respostasCorretas[15]]": 
            'Vermelho = あかいろ (akairo)' 
            call mensagem_de_acerto
        "[opcaoErrada2]": 
            call mensagem_de_erro
    if yene<600 :
        "Você tem apenas [yene] yen. Tente responder novamente as perguntas para ir para a próxima fase"
        jump capitulo2
    else:
        "Parabéns, você pode continuar com a história e seus [yene] yen foram zerados"

    label capitulo3:
    scene C7 with dissolve
    "Um dia Kaguya Hime disse ao cortador de bambu que ela realmente veio da lua e as pessoas da lua logo virão buscá-la."
    scene C7_3 with dissolve
    "Escolha a palavra correta. Quantas pessoas estão em destaque na imagem?"
    menu: 
        "[respostasCorretas[16]]":
            "Três = さん (san)" 
            call mensagem_de_acerto
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[opcaoErrada2]": 
            call mensagem_de_erro
    scene C7_Amarelo with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[respostasCorretas[17]]":
            "Amarelo = き (ki)" 
            call mensagem_de_acerto
    scene C7_Azul with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[respostasCorretas[18]]":
            'Azul = あお (ao)' 
            call mensagem_de_acerto
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[opcaoErrada2]": 
            call mensagem_de_erro
    scene C8 with dissolve
    "O cortador de bambu não queria que Kaguya Hime fosse embora. Ele pediu aos samurais para protegê-la do povo da lua."
    scene C8_Amarelo with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[respostasCorretas[19]]":
            "Amarelo = き (ki)"
            call mensagem_de_acerto
    scene C8_Arco with dissolve
    "Escolha a palavra correta. Qual o nome da item em destaque?"
    menu: 
        "[respostasCorretas[20]]":
            "Arco = ゆみ(yumi)" 
            call mensagem_de_acerto
        "[opcaoErrada2]":  
            call mensagem_de_erro
        "[opcaoErrada1]": 
            call mensagem_de_erro
    scene C8_Flecha with dissolve
    "Escolha a palavra correta. Qual o nome da item em destaque?"
    menu: 
        "[respostasCorretas[21]]":
            "Flecha = や (ya)" 
            call mensagem_de_acerto
        "[opcaoErrada2]":  
            call mensagem_de_erro
        "[opcaoErrada1]": 
            call mensagem_de_erro
    scene C9 with dissolve
    "Na noite de lua cheia, o povo da lua veio. Eles levaram Kaguya Hime de volta à lua. Os samurais não podiam fazer nada."
    scene C9_Azul with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]":  
            call mensagem_de_erro
        "[respostasCorretas[22]]":
            "Azul = あお (ao)" 
            call mensagem_de_acerto
    scene C9_Cavalo with dissolve
    "Escolha a palavra correta, qual palavra é equivalente a : Cavalo?"
    menu: 
        "[respostasCorretas[23]]":
            "Cavalo = うま (uma)" 
            call mensagem_de_acerto
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]": 
            call mensagem_de_erro
    scene C9_Nuvem with dissolve
    "Escolha a palavra correta. qual palavra é equivalente a : Nuvem"
    menu: 
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[respostasCorretas[24]]":
            "Nuvem = くも (kumo)" 
            call mensagem_de_acerto
        "[opcaoErrada1]":
            call mensagem_de_erro
    scene C10 with dissolve
    "Kaguya Hime gostou muito do cortador de bambu e das pessoas do mundo. Mas Kaguya Hime pertencia à lua. Ela às vezes volta ao mundo quando é lua cheia."
    scene C10_Amarelo with dissolve
    "Escolha a palavra correta. Qual o nome da cor da lua em destaque?"
    menu: 
        "[respostasCorretas[25]]":
            "Amarelo = き (ki)" 
            call mensagem_de_acerto
        "[opcaoErrada2]":  
            call mensagem_de_erro
        "[opcaoErrada1]": 
            call mensagem_de_erro
    scene C10_Rosa with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[respostasCorretas[26]]":
            'Rosa = ももいろ (momoiro)' 
            call mensagem_de_acerto
        "[opcaoErrada2]": 
            call mensagem_de_erro
        "[opcaoErrada1]": 
            call mensagem_de_erro
    scene C10_Verde with dissolve
    "Escolha a palavra correta. Qual o nome da cor em destaque?"
    menu: 
        "[respostasCorretas[27]]":
            "Verde = みどり (midori)" 
            call mensagem_de_acerto
        "[opcaoErrada1]": 
            call mensagem_de_erro
        "[opcaoErrada2]": 
            call mensagem_de_erro
    if yene<600 :
        "Você tem apenas [yene] yen. Tente responder novamente as perguntas para ir para a próxima fase"
        jump capitulo3
    else:
        "Parabéns, você terminou o jogo, continue praticando :)"
    return


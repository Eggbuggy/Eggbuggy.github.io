from time import sleep
import random
import webbrowser

name = input("hva heter du? ")
if name == "test":
    print("ok")
else:
    sleep (1)
    print(" yikes, tenk å være navngitt " + name + ", kunne ikke vært meg lol")
    sleep (1)

print( "vel uansett '" + name +"'.")
sleep (1)

number = input("hva er favoritt tallet ditt? ")
if number == "7":
    sleep (1)
    print("ehh.. ok jeg tror du må velge et bedre favoritt tall..")
    sleep (3)
    number = input("velg et bedre tall. ")
    if number == "7":
        print("...")
        sleep (3)
        exit
    else:
        print("bra")
        sleep (2)
if number == "69":
    print("ehhh... ok da..")
    sleep (2)
if number == "420":
    print(" hahahaha du er så humoristisk :|")
    sleep (2)
else:
    print(""+ number +" er ikke et veldig kreativt tall, men ok")
    sleep (2)

game = input("hva type spill liker du da " + name +"? ")
if game == "genshin":
    print("gå deg en tur ute plis")
    sleep (2)
if game == "valorant":
    print("gå deg en tur ute plis")
    sleep (2)
if game == "undertale":
    print("helt riktig")
    sleep (2)
if game == "ingen":
    print("ok")
else:
    print("danm. morra di hadde deg i magen hennes i 9 måneder, fødtte deg, oppdro deg og betalte for skolegangen din. bare for at du skulle ende opp som en " + game + " player.")
    sleep (5)

print("nokk snakk om deg.")
sleep (1)


for count in range (5):
    question =input("spørr meg noe! kan ikke love at jeg svarer på alt da. ")
    
    if question == "hva heter du?":
        print("iallfall ikke "+ name+" heldigvis")
        sleep (2)
        
    if question == "hva er ditt favoritt tall?":
        print("87 solos")
        sleep (2)
        
    if question == "hva er ditt favoritt spill?":
        print("dette")
        sleep (2)
        webbrowser.open("https://poki.com/en/g/pony-dressup")
        
    if question == "hvordan ser du ut?":
        webbrowser.open("https://www.youtube.com/watch?v=EZEfN5z8Mlg")
        
    if question == "hva er ditt favoritt dyr?":
        print("reker!")
        webbrowser.open("https://www.bing.com/images/search?view=detailV2&ccid=tdu6ZiAl&id=BD9425ED14D4CA087186C68DDA8BA94AAD576E68&thid=OIP.tdu6ZiAlRaaWG9-x72oktgHaEM&mediaurl=https%3a%2f%2fgfx.nrk.no%2fUpU454R3nTsNssXmnhPTtwpQ4y8bPihz4t-MgIs_5YNA.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.b5dbba66202545a6961bdfb1ef6a24b6%3frik%3daG5XrUqpi9qNxg%26pid%3dImgRaw%26r%3d0&exph=1133&expw=2000&q=reker+levende&simid=608027864745799126&FORM=IRPRST&ck=F661923D63EE40F4802F59BEF91B4FCA&selectedIndex=1&ajaxhist=0&ajaxserp=0")
        
    if question == "hva gjør du på fritiden din?":
        print("jeg bare sitter her egt")
        
    if question == "nei":
        print("hadet")
        
        exit
    else:
        print("no comment")

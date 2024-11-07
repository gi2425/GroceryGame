#gi cortgrasso
#5/18/2022
#finalproject.py

import random
from graphics import*
import time
from grid import*
import collections 

win=GraphWin("gi's grocery store",800,800)

def glist():
    text=open("grocery store items.txt","r") #list of all possible grocery list items
    textread=text.read()
    words=textread.splitlines()
    
    grocerylist=[] #creates list for random list items to be generated in
    while len(grocerylist)!=5: #until the length of the grocery list reaches 5
        randomnum=random.randrange(0,44) #generates a random number within the amount of possible options
        if words[randomnum] not in grocerylist: #if that number isn't already in the list
            grocerylist.append(words[randomnum]) #it's added to the list
    return grocerylist
temp=glist() #list that isn't a string, so it can be compared to the list of the user-made cart at the end
word=str(temp) #string so that it can be pasted in the graphics screen
grocery_list=word.replace("[","").replace("]","").replace(",","\n\n").replace("'","")


def shoppinglist(): #creates the shopping list that shows up in the corner of the screen
    shoppinglistbackground=Rectangle(Point(0,0),Point(100,200))
    shoppinglistbackground.setFill("white")
    shoppinglistbackground.draw(win)
    
    shoppinglist=Text(Point(50,100),grocery_list)
    shoppinglist.setSize(12)
    shoppinglist.draw(win)

def produceisle(): #produce isle, literally j a ton of graphics, pretty self-explanatory i think
    producebackground=Image(Point(400,400),"producebackground.png")
    producebackground.draw(win)
    producebackground2=Rectangle(Point(200,200),Point(600,600))
    producebackground2.setFill("white")
    producebackground2.draw(win)
    shoppinglist() #pastes shopping list from function above
    producecart=[] #creates list of all items added to the shopping list in the produce isle

    back=Button(win,Point(400,700),100,50,"back")
    back.setColor("pink")
    back.activate()
    
    broccoli=Image(Point(300,300),"broccoli.png")
    broccoli.draw(win)
    addbroccoli=Button(win,Point(300,325),50,25,"add")
    addbroccoli.setColor("pink")
    addbroccoli.activate()

    carrot=Image(Point(400,300),"carrot.png")
    carrot.draw(win)
    addcarrot=Button(win,Point(400,325),50,25,"add")
    addcarrot.setColor("pink")
    addcarrot.activate()

    corn=Image(Point(500,300),"corn.png")
    corn.draw(win)
    addcorn=Button(win,Point(500,325),50,25,"add")
    addcorn.setColor("pink")
    addcorn.activate()

    lettuce=Image(Point(300,400),"lettuce.png")
    lettuce.draw(win)
    addlettuce=Button(win,Point(300,425),50,25,"add")
    addlettuce.setColor("pink")
    addlettuce.activate()

    tomato=Image(Point(400,400),"tomato.png")
    tomato.draw(win)
    addtomato=Button(win,Point(400,425),50,25,"add")
    addtomato.setColor("pink")
    addtomato.activate()

    apple=Image(Point(500,400),"apple.png")
    apple.draw(win)
    addapple=Button(win,Point(500,425),50,25,"add")
    addapple.setColor("pink")
    addapple.activate()

    banana=Image(Point(300,500),"banana.png")
    banana.draw(win)
    addbanana=Button(win,Point(300,525),50,25,"add")
    addbanana.setColor("pink")
    addbanana.activate()

    watermelon=Image(Point(400,500),"watermelon.png")
    watermelon.draw(win)
    addwatermelon=Button(win,Point(400,525),50,25,"add")
    addwatermelon.setColor("pink")
    addwatermelon.activate()

    grapes=Image(Point(500,500),"grapes.png")
    grapes.draw(win)
    addgrapes=Button(win,Point(500,525),50,25,"add")
    addgrapes.setColor("pink")
    addgrapes.activate()

    pt=win.getMouse() #adds to produce cart when pressed
    while not (back.isClicked(pt)):
        if addbroccoli.isClicked(pt):
            producecart.append("broccoli")
        elif addcarrot.isClicked(pt):
            producecart.append("carrots")
        elif addcorn.isClicked(pt):
            producecart.append("corn")
        elif addlettuce.isClicked(pt):
            producecart.append("lettuce")
        elif addtomato.isClicked(pt):
            producecart.append("tomatoes")
        elif addapple.isClicked(pt):
            producecart.append("apples")
        elif addbanana.isClicked(pt):
            producecart.append("banana")
        elif addwatermelon.isClicked(pt):
            producecart.append("watermelon")
        elif addgrapes.isClicked(pt):
            producecart.append("grapes")
        pt=win.getMouse()

    if back.isClicked(pt): #if they click the back button it undraws everything and brings them back to the isle screen
        producebackground.undraw()
        producebackground2.undraw()
        back.undraw()
        broccoli.undraw()
        addbroccoli.undraw()
        carrot.undraw()
        addcarrot.undraw()
        corn.undraw()
        addcorn.undraw()
        lettuce.undraw()
        addlettuce.undraw()
        tomato.undraw()
        addtomato.undraw()
        apple.undraw()
        addapple.undraw()
        banana.undraw()
        addbanana.undraw()
        watermelon.undraw()
        addwatermelon.undraw()
        grapes.undraw()
        addgrapes.undraw()
    return ("back", producecart, "cart")

def dairyandmeatisle(): #same as above, j a different isle
    dairyandmeatbackground=Image(Point(400,400),"dairyandmeatbackground.png")
    dairyandmeatbackground.draw(win)
    dairyandmeatbackground2=Rectangle(Point(200,200),Point(600,600))
    dairyandmeatbackground2.setFill("white")
    dairyandmeatbackground2.draw(win)
    shoppinglist()
    dairyandmeatcart=[]

    back=Button(win,Point(400,750),100,50,"back")
    back.setColor("pink")
    back.activate()
    
    eggs=Image(Point(300,300),"eggs.png")
    eggs.draw(win)
    addeggs=Button(win,Point(300,325),50,25,"add")
    addeggs.setColor("pink")
    addeggs.activate()

    butter=Image(Point(400,300),"butter.png")
    butter.draw(win)
    addbutter=Button(win,Point(400,325),50,25,"add")
    addbutter.setColor("pink")
    addbutter.activate()

    milk=Image(Point(500,300),"milk.png")
    milk.draw(win)
    addmilk=Button(win,Point(500,325),50,25,"add")
    addmilk.setColor("pink")
    addmilk.activate()

    yogurt=Image(Point(300,400),"yogurt.png")
    yogurt.draw(win)
    addyogurt=Button(win,Point(300,425),50,25,"add")
    addyogurt.setColor("pink")
    addyogurt.activate()

    cheese=Image(Point(400,400),"cheese.png")
    cheese.draw(win)
    addcheese=Button(win,Point(400,425),50,25,"add")
    addcheese.setColor("pink")
    addcheese.activate()

    bacon=Image(Point(500,400),"bacon.png")
    bacon.draw(win)
    addbacon=Button(win,Point(500,425),50,25,"add")
    addbacon.setColor("pink")
    addbacon.activate()

    chicken=Image(Point(300,500),"chicken.png")
    chicken.draw(win)
    addchicken=Button(win,Point(300,525),50,25,"add")
    addchicken.setColor("pink")
    addchicken.activate()

    fish=Image(Point(500,500),"fish.png")
    fish.draw(win)
    addfish=Button(win,Point(500,525),50,25,"add")
    addfish.setColor("pink")
    addfish.activate()

    
    pt=win.getMouse()
    while not (back.isClicked(pt)):
        if addeggs.isClicked(pt):
            dairyandmeatcart.append("eggs")
        elif addbutter.isClicked(pt):
            dairyandmeatcart.append("butter")
        elif addmilk.isClicked(pt):
            dairyandmeatcart.append("milk")
        elif addyogurt.isClicked(pt):
            dairyandmeatcart.append("yogurt")
        elif addcheese.isClicked(pt):
            dairyandmeatcart.append("cheese")
        elif addbacon.isClicked(pt):
            dairyandmeatcart.append("bacon")
        elif addchicken.isClicked(pt):
            dairyandmeatcart.append("chicken")
        elif addfish.isClicked(pt):
            dairyandmeatcart.append("fish")
        pt=win.getMouse()
        
    if back.isClicked(pt):
        dairyandmeatbackground.undraw()
        dairyandmeatbackground2.undraw()
        back.undraw()
        eggs.undraw()
        addeggs.undraw()
        butter.undraw()
        addbutter.undraw()
        milk.undraw()
        addmilk.undraw()
        yogurt.undraw()
        addyogurt.undraw()
        cheese.undraw()
        addcheese.undraw()
        bacon.undraw()
        addbacon.undraw()
        chicken.undraw()
        addchicken.undraw()
        fish.undraw()
        addfish.undraw()
    return ("back", dairyandmeatcart, "cart")

def bakeryandcookingisle(): #same as above, j a different isle
    bakeryandcookinggoodsbackground=Image(Point(400,400),"bakeryandcookinggoodsbackground.png")
    bakeryandcookinggoodsbackground.draw(win)
    bakeryandcookinggoodsbackground2=Rectangle(Point(200,200),Point(600,600))
    bakeryandcookinggoodsbackground2.setFill("white")
    bakeryandcookinggoodsbackground2.draw(win)
    shoppinglist()
    bakeryandcookinggoodscart=[]

    back=Button(win,Point(400,700),100,50,"back")
    back.setColor("pink")
    back.activate()

    salt=Image(Point(300,300),"salt.png")
    salt.draw(win)
    addsalt=Button(win,Point(300,325),50,25,"add")
    addsalt.setColor("pink")
    addsalt.activate()

    donut=Image(Point(400,300),"donut.png")
    donut.draw(win)
    adddonut=Button(win,Point(400,325),50,25,"add")
    adddonut.setColor("pink")
    adddonut.activate()

    pie=Image(Point(500,300),"pie.png")
    pie.draw(win)
    addpie=Button(win,Point(500,325),50,25,"add")
    addpie.setColor("pink")
    addpie.activate()

    flour=Image(Point(300,400),"flour.png")
    flour.draw(win)
    addflour=Button(win,Point(300,425),50,25,"add")
    addflour.setColor("pink")
    addflour.activate()

    sugar=Image(Point(400,400),"sugar.png")
    sugar.draw(win)
    addsugar=Button(win,Point(400,425),50,25,"add")
    addsugar.setColor("pink")
    addsugar.activate()

    cookies=Image(Point(500,400),"cookies.png")
    cookies.draw(win)
    addcookies=Button(win,Point(500,425),50,25,"add")
    addcookies.setColor("pink")
    addcookies.activate()

    bagels=Image(Point(300,500),"bagels.png")
    bagels.draw(win)
    addbagels=Button(win,Point(300,525),50,25,"add")
    addbagels.setColor("pink")
    addbagels.activate()

    pasta=Image(Point(400,500),"pasta.png")
    pasta.draw(win)
    addpasta=Button(win,Point(400,525),50,25,"add")
    addpasta.setColor("pink")
    addpasta.activate()

    macncheese=Image(Point(500,500),"mac&cheese.png")
    macncheese.draw(win)
    addmacncheese=Button(win,Point(500,525),50,25,"add")
    addmacncheese.setColor("pink")
    addmacncheese.activate()

    pt=win.getMouse()
    while not (back.isClicked(pt)):
        if addsalt.isClicked(pt):
            bakeryandcookinggoodscart.append("salt")
        elif adddonut.isClicked(pt):
            bakeryandcookinggoodscart.append("donut")
        elif addpie.isClicked(pt):
            bakeryandcookinggoodscart.append("pie")
        elif addflour.isClicked(pt):
            bakeryandcookinggoodscart.append("flour")
        elif addsugar.isClicked(pt):
            bakeryandcookinggoodscart.append("sugar")
        elif addcookies.isClicked(pt):
            bakeryandcookinggoodscart.append("cookies")
        elif addbagels.isClicked(pt):
            bakeryandcookinggoodscart.append("bagels")
        elif addpasta.isClicked(pt):
            bakeryandcookinggoodscart.append("pasta")
        elif addmacncheese.isClicked(pt):
            bakeryandcookinggoodscart.append("mac & cheese")
        pt=win.getMouse()
        
    if back.isClicked(pt):
        bakeryandcookinggoodsbackground.undraw()
        bakeryandcookinggoodsbackground2.undraw()
        back.undraw()
        salt.undraw()
        addsalt.undraw()
        donut.undraw()
        adddonut.undraw()
        pie.undraw()
        addpie.undraw()
        flour.undraw()
        addflour.undraw()
        sugar.undraw()
        addsugar.undraw()
        cookies.undraw()
        addcookies.undraw()
        bagels.undraw()
        addbagels.undraw()
        pasta.undraw()
        addpasta.undraw()
        macncheese.undraw()
        addmacncheese.undraw()
    return ("back", bakeryandcookinggoodscart, "cart")

def snacksandcondimentsisle(): #same as above, j a different isle
    snacksandcondimentsbackground=Image(Point(400,400),"snacksandcondimentsbackground.png")
    snacksandcondimentsbackground.draw(win)
    snacksandcondimentsbackground2=Rectangle(Point(200,200),Point(600,600))
    snacksandcondimentsbackground2.setFill("white")
    snacksandcondimentsbackground2.draw(win)
    shoppinglist()
    snacksandcondimentscart=[]

    back=Button(win,Point(400,700),100,50,"back")
    back.setColor("pink")
    back.activate()

    bbqsauce=Image(Point(300,300),"bbqsauce.png")
    bbqsauce.draw(win)
    addbbqsauce=Button(win,Point(300,325),50,25,"add")
    addbbqsauce.setColor("pink")
    addbbqsauce.activate()

    jam=Image(Point(400,300),"jam.png")
    jam.draw(win)
    addjam=Button(win,Point(400,325),50,25,"add")
    addjam.setColor("pink")
    addjam.activate()

    ketchup=Image(Point(500,300),"ketchup.png")
    ketchup.draw(win)
    addketchup=Button(win,Point(500,325),50,25,"add")
    addketchup.setColor("pink")
    addketchup.activate()

    maplesyrup=Image(Point(300,400),"maplesyrup.png")
    maplesyrup.draw(win)
    addmaplesyrup=Button(win,Point(300,425),50,25,"add")
    addmaplesyrup.setColor("pink")
    addmaplesyrup.activate()

    popcorn=Image(Point(400,400),"popcorn.png")
    popcorn.draw(win)
    addpopcorn=Button(win,Point(400,425),50,25,"add")
    addpopcorn.setColor("pink")
    addpopcorn.activate()

    pretzels=Image(Point(500,400),"pretzels.png")
    pretzels.draw(win)
    addpretzels=Button(win,Point(500,425),50,25,"add")
    addpretzels.setColor("pink")
    addpretzels.activate()

    peanutbutter=Image(Point(400,500),"peanutbutter.png")
    peanutbutter.draw(win)
    addpeanutbutter=Button(win,Point(400,525),50,25,"add")
    addpeanutbutter.setColor("pink")
    addpeanutbutter.activate()

    pt=win.getMouse()
    while not (back.isClicked(pt)):
        if addbbqsauce.isClicked(pt):
            snacksandcondimentscart.append("bbq sauce")
        elif addjam.isClicked(pt):
            snacksandcondimentscart.append("jam")
        elif addketchup.isClicked(pt):
            snacksandcondimentscart.append("ketchup")
        elif addmaplesyrup.isClicked(pt):
            snacksandcondimentscart.append("maple syrup")
        elif addpopcorn.isClicked(pt):
            snacksandcondimentscart.append("popcorn")
        elif addpretzels.isClicked(pt):
            snacksandcondimentscart.append("pretzels")
        elif addpeanutbutter.isClicked(pt):
            snacksandcondimentscart.append("peanut butter")
        pt=win.getMouse()
        
    if back.isClicked(pt):
        snacksandcondimentsbackground.undraw()
        snacksandcondimentsbackground2.undraw()
        back.undraw()
        bbqsauce.undraw()
        addbbqsauce.undraw()
        jam.undraw()
        addjam.undraw()
        ketchup.undraw()
        addketchup.undraw()
        maplesyrup.undraw()
        addmaplesyrup.undraw()
        popcorn.undraw()
        addpopcorn.undraw()
        pretzels.undraw()
        addpretzels.undraw()
        peanutbutter.undraw()
        addpeanutbutter.undraw()
    return ("back", snacksandcondimentscart)

def cannedfoodandgrainsisle(): #same as above, j a different isle
    cannedfoodandgrainsbackground=Image(Point(400,400),"cannedfoodandgrainsbackground.png")
    cannedfoodandgrainsbackground.draw(win)
    cannedfoodandgrainsbackground2=Rectangle(Point(200,300),Point(600,500))
    cannedfoodandgrainsbackground2.setFill("white")
    cannedfoodandgrainsbackground2.draw(win)
    shoppinglist()
    cannedfoodandgrainscart=[]

    back=Button(win,Point(400,700),100,50,"back")
    back.setColor("pink")
    back.activate()

    rice=Image(Point(300,400),"rice.png")
    rice.draw(win)
    addrice=Button(win,Point(300,425),50,25,"add")
    addrice.setColor("pink")
    addrice.activate()

    olives=Image(Point(400,400),"olives.png")
    olives.draw(win)
    addolives=Button(win,Point(400,425),50,25,"add")
    addolives.setColor("pink")
    addolives.activate()

    pickles=Image(Point(500,400),"pickles.png")
    pickles.draw(win)
    addpickles=Button(win,Point(500,425),50,25,"add")
    addpickles.setColor("pink")
    addpickles.activate()

    pt=win.getMouse()
    while not (back.isClicked(pt)):
        if addrice.isClicked(pt):
            cannedfoodandgrainscart.append("rice")
        elif addolives.isClicked(pt):
            cannedfoodandgrainscart.append("olives")
        elif addpickles.isClicked(pt):
            cannedfoodandgrainscart.append("pickles")
        pt=win.getMouse()
        
    if back.isClicked(pt):
        cannedfoodandgrainsbackground.undraw()
        cannedfoodandgrainsbackground2.undraw()
        back.undraw()
        rice.undraw()
        addrice.undraw()
        olives.undraw()
        addolives.undraw()
        pickles.undraw()
        addpickles.undraw()
    return ("back", cannedfoodandgrainscart)


def frozenisle(): #same as above, j a different isle
    frozenbackground=Image(Point(400,400),"frozenbackground.png")
    frozenbackground.draw(win)
    frozenbackground2=Rectangle(Point(250,300),Point(550,500))
    frozenbackground2.setFill("white")
    frozenbackground2.draw(win)
    shoppinglist()
    frozencart=[]

    back=Button(win,Point(400,700),100,50,"back")
    back.setColor("pink")
    back.activate()

    icecream=Image(Point(350,400),"icecream.png")
    icecream.draw(win)
    addicecream=Button(win,Point(350,425),50,25,"add")
    addicecream.setColor("pink")
    addicecream.activate()

    popsicle=Image(Point(450,400),"popsicle.png")
    popsicle.draw(win)
    addpopsicle=Button(win,Point(450,425),50,25,"add")
    addpopsicle.setColor("pink")
    addpopsicle.activate()

    pt=win.getMouse()
    while not (back.isClicked(pt)):
        if addicecream.isClicked(pt):
            frozencart.append("ice cream")
        elif addpopsicle.isClicked(pt):
            frozencart.append("popsicles")
        pt=win.getMouse()
        
    if back.isClicked(pt):
        frozenbackground.undraw()
        frozenbackground2.undraw()
        back.undraw()
        icecream.undraw()
        addicecream.undraw()
        popsicle.undraw()
        addpopsicle.undraw()
    return ("back", frozencart, "cart")

def beveragesandcerealsisle(): #same as above, j a different isle
    beveragesandcerealsbackground=Image(Point(400,400),"beveragesandcerealsbackground.png")
    beveragesandcerealsbackground.draw(win)
    beveragesandcerealsbackground2=Rectangle(Point(200,300),Point(600,500))
    beveragesandcerealsbackground2.setFill("white")
    beveragesandcerealsbackground2.draw(win)
    shoppinglist()
    beveragesandcerealscart=[]

    back=Button(win,Point(400,700),100,50,"back")
    back.setColor("pink")
    back.activate()
    
    orangejuice=Image(Point(300,400),"orangejuice.png")
    orangejuice.draw(win)
    addorangejuice=Button(win,Point(300,425),50,25,"add")
    addorangejuice.setColor("pink")
    addorangejuice.activate()

    applejuice=Image(Point(400,400),"applejuice.png")
    applejuice.draw(win)
    addapplejuice=Button(win,Point(400,425),50,25,"add")
    addapplejuice.setColor("pink")
    addapplejuice.activate()

    cereal=Image(Point(500,400),"cereal.png")
    cereal.draw(win)
    addcereal=Button(win,Point(500,425),50,25,"add")
    addcereal.setColor("pink")
    addcereal.activate()

    pt=win.getMouse()
    while not (back.isClicked(pt)):
        if addorangejuice.isClicked(pt):
            beveragesandcerealscart.append("orange juice")
        elif addapplejuice.isClicked(pt):
            beveragesandcerealscart.append("apple juice")
        elif addcereal.isClicked(pt):
            beveragesandcerealscart.append("cereal")
        pt=win.getMouse()
        
    if back.isClicked(pt):
        beveragesandcerealsbackground.undraw()
        beveragesandcerealsbackground2.undraw()
        back.undraw()
        orangejuice.undraw()
        addorangejuice.undraw()
        applejuice.undraw()
        addapplejuice.undraw()
        cereal.undraw()
        addcereal.undraw()
    return ("back", beveragesandcerealscart, "cart")

def paperandcleaninggoodsisle(): #same as above, j a different isle
    paperandcleaninggoodsbackground=Image(Point(400,400),"paperandcleaninggoodsbackground.png")
    paperandcleaninggoodsbackground.draw(win)
    paperandcleaninggoodsbackground2=Rectangle(Point(200,300),Point(600,500))
    paperandcleaninggoodsbackground2.setFill("white")
    paperandcleaninggoodsbackground2.draw(win)
    shoppinglist()
    paperandcleaninggoodscart=[]

    back=Button(win,Point(400,700),100,50,"back")
    back.setColor("pink")
    back.activate()

    toothpaste=Image(Point(300,400),"toothpaste.png")
    toothpaste.draw(win)
    addtoothpaste=Button(win,Point(300,425),50,25,"add")
    addtoothpaste.setColor("pink")
    addtoothpaste.activate()

    toiletpaper=Image(Point(400,400),"toiletpaper.png")
    toiletpaper.draw(win)
    addtoiletpaper=Button(win,Point(400,425),50,25,"add")
    addtoiletpaper.setColor("pink")
    addtoiletpaper.activate()

    papertowels=Image(Point(500,400),"papertowels.png")
    papertowels.draw(win)
    addpapertowels=Button(win,Point(500,425),50,25,"add")
    addpapertowels.setColor("pink")
    addpapertowels.activate()

    pt=win.getMouse()
    while not (back.isClicked(pt)):
        if addtoothpaste.isClicked(pt):
            paperandcleaninggoodscart.append("toothpaste")
        elif addtoiletpaper.isClicked(pt):
            paperandcleaninggoodscart.append("toilet paper")
        elif addpapertowels.isClicked(pt):
            paperandcleaninggoodscart.append("paper towels")
        pt=win.getMouse()
        
    if back.isClicked(pt):
        paperandcleaninggoodsbackground.undraw()
        paperandcleaninggoodsbackground2.undraw()
        back.undraw()
        toothpaste.undraw()
        addtoothpaste.undraw()
        toiletpaper.undraw()
        addtoiletpaper.undraw()
        papertowels.undraw()
        addpapertowels.undraw()
    return ("back", paperandcleaninggoodscart, "cart")


def isles(): #the screen that shows all possible isles, literally just graphics
    cart=Button(win,Point(750,50),50,25,"cart")
    cart.setColor("pink")
    cart.activate()
    
    isle1v=Rectangle(Point(100,0),Point(800,1))
    isle1v.setFill("black")
    isle1v.draw(win)
    produce=Button(win,Point(400,50),200,50,"produce")
    produce.setColor("pink")
    produce.activate()

    isle2v=Rectangle(Point(100,100),Point(800,101))
    isle2v.setFill("black")
    isle2v.draw(win)
    dairyandmeat=Button(win,Point(400,150),200,50,"dairy, meat, and frozen goods")
    dairyandmeat.setColor("pink")
    dairyandmeat.activate()

    isle3v=Rectangle(Point(0,200),Point(800,201))
    isle3v.setFill("black")
    isle3v.draw(win)
    bakeryandcookinggoods=Button(win,Point(400,250),200,50,"bakery and cooking goods")
    bakeryandcookinggoods.setColor("pink")
    bakeryandcookinggoods.activate()

    isle4v=Rectangle(Point(0,300),Point(800,301))
    isle4v.setFill("black")
    isle4v.draw(win)
    snacksandcondiments=Button(win,Point(400,350),200,50,"snacks and condiments")
    snacksandcondiments.setColor("pink")
    snacksandcondiments.activate()

    isle5v=Rectangle(Point(0,400),Point(800,401))
    isle5v.setFill("black")
    isle5v.draw(win)
    cannedfoodandgrains=Button(win,Point(400,450),200,50,"canned food and grains")
    cannedfoodandgrains.setColor("pink")
    cannedfoodandgrains.activate()

    isle6v=Rectangle(Point(0,500),Point(800,501))
    isle6v.setFill("black")
    isle6v.draw(win)
    frozen=Button(win,Point(400,550),200,50,"frozen")
    frozen.setColor("pink")
    frozen.activate()

    isle7v=Rectangle(Point(0,600),Point(800,601))
    isle7v.setFill("black")
    isle7v.draw(win)
    beveragesandcereals=Button(win,Point(400,650),200,50,"beverages and cereals")
    beveragesandcereals.setColor("pink")
    beveragesandcereals.activate()

    isle8v=Rectangle(Point(0,700),Point(800,701))
    isle8v.setFill("black")
    isle8v.draw(win)
    paperandcleaninggoods=Button(win,Point(400,750),200,50,"paper and cleaning goods")
    paperandcleaninggoods.setColor("pink")
    paperandcleaninggoods.activate()

    isle8=Rectangle(Point(0,799),Point(800,800))
    isle8.setFill("black")
    isle8.draw(win)

    pt=win.getMouse() #everything below is just undrawing stuff when isles are clicked
    while not (cart.isClicked(pt) or produce.isClicked(pt) or dairyandmeat.isClicked(pt) or bakeryandcookinggoods.isClicked(pt) or snacksandcondiments.isClicked(pt) or cannedfoodandgrains.isClicked(pt) or frozen.isClicked(pt) or beveragesandcereals.isClicked(pt) or paperandcleaninggoods.isClicked(pt)):
        pt=win.getMouse()
    if produce.isClicked(pt):
        isle1v.undraw()
        produce.undraw()
        isle2v.undraw()
        dairyandmeat.undraw()
        isle3v.undraw()
        bakeryandcookinggoods.undraw()
        isle4v.undraw()
        snacksandcondiments.undraw()
        isle5v.undraw()
        cannedfoodandgrains.undraw()
        isle6v.undraw()
        frozen.undraw()
        isle7v.undraw()
        beveragesandcereals.undraw()
        isle8v.undraw()
        paperandcleaninggoods.undraw()
        isle8.undraw()
        cart.undraw()
        return "produce"
    elif dairyandmeat.isClicked(pt):
        isle1v.undraw()
        produce.undraw()
        isle2v.undraw()
        dairyandmeat.undraw()
        isle3v.undraw()
        bakeryandcookinggoods.undraw()
        isle4v.undraw()
        snacksandcondiments.undraw()
        isle5v.undraw()
        cannedfoodandgrains.undraw()
        isle6v.undraw()
        frozen.undraw()
        isle7v.undraw()
        beveragesandcereals.undraw()
        isle8v.undraw()
        paperandcleaninggoods.undraw()
        isle8.undraw()
        cart.undraw()
        return "dairyandmeat"
    elif bakeryandcookinggoods.isClicked(pt):
        isle1v.undraw()
        produce.undraw()
        isle2v.undraw()
        dairyandmeat.undraw()
        isle3v.undraw()
        bakeryandcookinggoods.undraw()
        isle4v.undraw()
        snacksandcondiments.undraw()
        isle5v.undraw()
        cannedfoodandgrains.undraw()
        isle6v.undraw()
        frozen.undraw()
        isle7v.undraw()
        beveragesandcereals.undraw()
        isle8v.undraw()
        paperandcleaninggoods.undraw()
        isle8.undraw()
        cart.undraw()
        return "bakeryandcooking"
    elif snacksandcondiments.isClicked(pt):
        isle1v.undraw()
        produce.undraw()
        isle2v.undraw()
        dairyandmeat.undraw()
        isle3v.undraw()
        bakeryandcookinggoods.undraw()
        isle4v.undraw()
        snacksandcondiments.undraw()
        isle5v.undraw()
        cannedfoodandgrains.undraw()
        isle6v.undraw()
        frozen.undraw()
        isle7v.undraw()
        beveragesandcereals.undraw()
        isle8v.undraw()
        paperandcleaninggoods.undraw()
        isle8.undraw()
        cart.undraw()
        return "snacksandcondiments"
    elif cannedfoodandgrains.isClicked(pt):
        isle1v.undraw()
        produce.undraw()
        isle2v.undraw()
        dairyandmeat.undraw()
        isle3v.undraw()
        bakeryandcookinggoods.undraw()
        isle4v.undraw()
        snacksandcondiments.undraw()
        isle5v.undraw()
        cannedfoodandgrains.undraw()
        isle6v.undraw()
        frozen.undraw()
        isle7v.undraw()
        beveragesandcereals.undraw()
        isle8v.undraw()
        paperandcleaninggoods.undraw()
        isle8.undraw()
        cart.undraw()
        return "cannedandgrains"
    elif frozen.isClicked(pt):
        isle1v.undraw()
        produce.undraw()
        isle2v.undraw()
        dairyandmeat.undraw()
        isle3v.undraw()
        bakeryandcookinggoods.undraw()
        isle4v.undraw()
        snacksandcondiments.undraw()
        isle5v.undraw()
        cannedfoodandgrains.undraw()
        isle6v.undraw()
        frozen.undraw()
        isle7v.undraw()
        beveragesandcereals.undraw()
        isle8v.undraw()
        paperandcleaninggoods.undraw()
        isle8.undraw()
        cart.undraw()
        return "frozen"
    elif beveragesandcereals.isClicked(pt):
        isle1v.undraw()
        produce.undraw()
        isle2v.undraw()
        dairyandmeat.undraw()
        isle3v.undraw()
        bakeryandcookinggoods.undraw()
        isle4v.undraw()
        snacksandcondiments.undraw()
        isle5v.undraw()
        cannedfoodandgrains.undraw()
        isle6v.undraw()
        frozen.undraw()
        isle7v.undraw()
        beveragesandcereals.undraw()
        isle8v.undraw()
        paperandcleaninggoods.undraw()
        isle8.undraw()
        cart.undraw()
        return "beverageandcereal"
    elif paperandcleaninggoods.isClicked(pt):
        isle1v.undraw()
        produce.undraw()
        isle2v.undraw()
        dairyandmeat.undraw()
        isle3v.undraw()
        bakeryandcookinggoods.undraw()
        isle4v.undraw()
        snacksandcondiments.undraw()
        isle5v.undraw()
        cannedfoodandgrains.undraw()
        isle6v.undraw()
        frozen.undraw()
        isle7v.undraw()
        beveragesandcereals.undraw()
        isle8v.undraw()
        paperandcleaninggoods.undraw()
        isle8.undraw()
        cart.undraw()
        return "paperandcleaning"
    elif cart.isClicked(pt): #this is the shopping cart, that will be explained more below
        isle1v.undraw()
        produce.undraw()
        isle2v.undraw()
        dairyandmeat.undraw()
        isle3v.undraw()
        bakeryandcookinggoods.undraw()
        isle4v.undraw()
        snacksandcondiments.undraw()
        isle5v.undraw()
        cannedfoodandgrains.undraw()
        isle6v.undraw()
        frozen.undraw()
        isle7v.undraw()
        beveragesandcereals.undraw()
        isle8v.undraw()
        paperandcleaninggoods.undraw()
        isle8.undraw()
        cart.undraw()
        return "shoppingcart"
    

    

def entrance(): #entrance to the grocery store, just graphics
    entry=Image(Point(400,400),"grocerystoreentrance.png")
    entry.draw(win)
    woman=Image(Point(600,450),"womanstanding.gif")
    woman.draw(win)
    giface=Image(Point(595,155),"giface.gif")
    giface.draw(win)
    
    textbubble=Rectangle(Point(375,175),Point(550,250))
    textbubble.setFill("white")
    textbubble.draw(win)
    textbubbletext=Text(Point(462.5,215),"look in the upper left corner,\nyou literally JUST saw that list.\n\ni need ALL of those items.\nDON'T. GET. THEM. WRONG!!!!!!")
    textbubbletext.draw(win)

    shoppinglist()

    enter=Button(win,Point(400,700),150,100,"enter")
    enter.setColor("pink")
    enter.setSize(18)
    enter.activate()
    pt=win.getMouse()
    
    while not enter.isClicked(pt):
        pt=win.getMouse()
    if enter.isClicked(pt):
        entry.undraw()
        woman.undraw()
        giface.undraw()
        textbubble.undraw()
        textbubbletext.undraw()
        enter.undraw()
        return "isles"

def rules(): #rules, just graphics
    rulestext=Text(Point(400,200),"gi's grocery store rules\n\ngoal:\nsuccessfully and accurately purchase all items on your given grocery list.\n\ngameplay:\n1. you will be given a list of 5\
 randomly generated grocery store items, you will\nthen enter the store and navigate the isles based on what you need to purchase.\n\n2. while shopping, you will be able to view the current items\
 in your cart and\nremove accidentally added items.\n\n3. once you have successfully found and added each item to your cart,\nyou will then be able to check out by pressing the\ncheck-out button on\
 the bottom ofthe screen.\n\n4. the cashier will scan all of your items and give you your final score!\n\nenjoy!")
    rulestext.setSize(18)
    rulestext.draw(win)
    back=Button(win,Point(400,700),100,50,"back")
    back.setColor("pink")
    back.activate()
    pt=win.getMouse()
    while not back.isClicked(pt):
        pt=win.getMouse()
    if back.isClicked(pt):
        rulestext.undraw()
        back.undraw()
        return "opening"

def listreveal(): #the screen that reveals the shopping list, again, just graphics
    shoppinglist=Image(Point(400,400),"list.png")
    shoppinglist.draw(win)

    reveal=Button(win,Point(400,400),150,100,"click to reveal\nyour shopping list!")
    reveal.setColor("pink")
    reveal.setSize(14)
    reveal.activate()
    pt=win.getMouse()
    while not reveal.isClicked(pt):
        pt=win.getMouse()
    if reveal.isClicked(pt):
        reveal.undraw()
        listtext=Text(Point(400,400),grocery_list)
        listtext.setSize(24)
        listtext.draw(win)
        cont=Button(win,Point(400,700),100,50,"continue")
        cont.setColor("pink")
        cont.activate()
        while not cont.isClicked(pt):
            pt=win.getMouse()
        if cont.isClicked(pt):
            shoppinglist.undraw()
            listtext.undraw()
            cont.undraw()
            return "entrance"
        
    
def opening(): #the opening screen, graphics  
    gisgrocery=Image(Point(400,400),"gisgrocerystore.png")
    gisgrocery.draw(win)
    
    welcomebox=Rectangle(Point(200,550),Point(600,650))
    welcomebox.setFill("pink")
    welcomebox.draw(win)
    
    welcome=Text(Point(400,600),"welcome to gi's grocery store!\n click rules to read the rules, or click start to play!")
    welcome.setSize(18)
    welcome.draw(win)
    
    rulesb=Button(win,Point(300,700),100,50,"rules")
    rulesb.setColor("pink")
    rulesb.activate()
    
    startb=Button(win,Point(500,700),100,50,"start")
    startb.setColor("pink")
    startb.activate()

    pt=win.getMouse()
    while not (rulesb.isClicked(pt) or startb.isClicked(pt)):
        pt=win.getMouse()
    if rulesb.isClicked(pt):
        gisgrocery.undraw()
        welcomebox.undraw()
        welcome.undraw()
        rulesb.undraw()
        startb.undraw()
        return "rules"
    elif startb.isClicked(pt):
        gisgrocery.undraw()
        welcomebox.undraw()
        welcome.undraw()
        rulesb.undraw()
        startb.undraw()
        return "start"
    

def main():
    start=True #makes it so it knows when main is starting
    while start==True:
        cart=[] #cart that compiles all items added from all isles
        opens=opening() #goes to the opening screen
        if opens=="rule": #if they click rules it goes to rules
            rule=rules()
            if rule=="opening": #if they click back from the rules it goes back to opening
                opens=opening()
        elif opens=="start": #if they click start from opening then it goes to the list reveal
            listr=listreveal()
            if listr=="entrance": #once they press continue from list reveal it goes to the entry screen
                enter=entrance()
                if enter=="isles": #after they press enter, it goes to the isles
                    x = True #while x is true it allows them to go back and forth between isles
                    while x == True:
                        isle=isles()
                        if isle=="produce": #produce isle, appends whatever they add to the produce isle once they return to the main isles screen
                            fruitsnveggies=produceisle()
                            if fruitsnveggies[0]=="back":
                                cart+=fruitsnveggies[1]
                                continue
                        elif isle=="dairyandmeat": #same as above, just different isle
                            novegan=dairyandmeatisle()
                            if novegan[0]=="back":
                                cart+=novegan[1]
                                continue
                        elif isle=="bakeryandcooking": #same as above, just different isle
                            yumpastries=bakeryandcookingisle()
                            if yumpastries[0]=="back":
                                cart+=yumpastries[1]
                                continue
                        elif isle=="snacksandcondiments": #same as above, just different isle
                            snackingandtopping=snacksandcondimentsisle()
                            if snackingandtopping[0]=="back":
                                cart+=snackingandtopping[1]
                                continue
                        elif isle=="cannedandgrains": #same as above, just different isle
                            nonperishable=cannedfoodandgrainsisle()
                            if nonperishable[0]=="back":
                                cart+=nonperishable[1]
                                continue
                        elif isle=="frozen": #same as above, just different isle
                            brrrr=frozenisle()
                            if brrrr[0]=="back":
                                cart+=brrrr[1]
                                continue
                        elif isle=="beverageandcereal": #same as above, just different isle
                            slurp=beveragesandcerealsisle()
                            if slurp[0]=="back":
                                cart+=slurp[1]
                                continue
                        elif isle=="paperandcleaning": #same as above, just different isle
                            squeaky=paperandcleaninggoodsisle()
                            if squeaky[0]=="back":
                                cart+=squeaky[1]
                                continue
                        elif isle=="shoppingcart": #code for when they open the shopping cart
                            background=Rectangle(Point(200,100),Point(600,700))
                            background.setFill("white")
                            background.draw(win)

                            back=Button(win,Point(400,750),50,25,"back")
                            back.setColor("pink")
                            back.activate()

                            checkout=Button(win,Point(400,650),50,25,"checkout")
                            checkout.setColor("pink")
                            checkout.activate()

                            toptext=Text(Point(400,150),"cart\nclick an item to remove it")
                            toptext.draw(win)
                            x=400
                            y=200
                            buttons=[]
                            for item in cart: #draws a button for each item in the cart
                                y2=y+50
                                itemb=Button(win,Point(x,y2),75,25,item)
                                itemb.setColor("pink")
                                itemb.activate()
                                buttons.append(itemb)
                                y=y2
                            pt=win.getMouse()
                            while not (back.isClicked(pt) or checkout.isClicked(pt)):
                                for item in buttons: #if the button is clicked, it removes it from the master cart list
                                    if item.isClicked(pt):
                                        #print(cart)
                                        #print(item.returnName().getText())
                                        cart.remove(item.returnName().getText())
                                        item.undraw()
                                pt=win.getMouse()
                            if back.isClicked(pt): #if they click back, it returns to the isle screen
                                background.undraw()
                                back.undraw()
                                checkout.undraw()
                                toptext.undraw()
                                for item in buttons:
                                    item.undraw()
                                x=True
                            if checkout.isClicked(pt): #if they click checkout, it moves to the checkout screen
                                background.undraw()
                                back.undraw()
                                checkout.undraw()
                                toptext.undraw()
                                for item in buttons:
                                    item.undraw()

                                #graphics for the checkout screen
                                close=Button(win,Point(400,750),50,25,"close")
                                close.setColor("pink")
                                close.activate()

                                cartbackground=Rectangle(Point(700,0),Point(800,200))
                                cartbackground.setFill("white")
                                cartbackground.draw(win)
        
                                cartlist=Text(Point(750,100),"\n\n".join(cart))
                                cartlist.setSize(12)
                                cartlist.draw(win)
                                
                                kanye=Image(Point(640,390),"kanye.png")
                                kanye.draw(win)

                                cashier=Image(Point(600,500),"cashier.png")
                                cashier.draw(win)

                                listside=Text(Point(50,215),"your grocery list")
                                listside.draw(win)

                                cartside=Text(Point(750,215),"your cart")
                                cartside.draw(win)


                                if sorted(cart)==sorted(temp): #checks if the cart and the grocery list match, in any order, if it does, they win, and the game ends
                                    winner=Text(Point(400,300),"congratulations! your cart matches your list!")
                                    winner.draw(win)
                                    pt=win.getMouse()
                                    while not close.isClicked(pt):
                                        pt=win.getMouse()
                                    if close.isClicked(pt):
                                        start==False
                                        win.close()
                                        return
                                else: #if it does not match, it gives them the option to restart
                                    loser=Text(Point(400,300),"you were literally shown the list the whole time how did you get it wrong??\ntry again maybe you'll get it right.")
                                    loser.draw(win)
                                    restart=Button(win,Point(400,700),50,25,"restart")
                                    restart.setColor("pink")
                                    restart.activate()
                                    
                                    pt=win.getMouse()
                                    while not (restart.isClicked(pt) or close.isClicked(pt)):
                                        pt=win.getMouse()
                                    if restart.isClicked(pt): #if restart is clicked, it restarts with the same list
                                        clear(win)
                                        start==True
                                        continue
                                    elif close.isClicked(pt): 
                                        start==False
                                        win.close()
                                        return
                            

def clear(win): #function to clear everything from the window
    for item in win.items[:]:
        item.undraw()
    win.update()
                                

                                    
main()




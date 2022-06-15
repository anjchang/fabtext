# This file takes the words from the Apolllo 11 sourcecode
# and remaps each word into a 10x10 pixel of a
#  shade of gray based on the length of the word
#  Todo is to create a word to color lookup table

w, h = 64,64
wordarray= [["" for x in range(w)] for y in range(h)] 
def setup():
    size(630, 630)
    global img, words,wordarray
    words =loadStrings("allwordsinorder.txt")
    count=0
    for word in words:
        if len(word)>count:
            count=len(word)
    print(len(words),sqrt(len(words))) #number of total words
    print(63*63)
    img = createImage(230, 230, ARGB)
    pixCount = len(img.pixels)
    for i in range(pixCount):
        a = map(i, 0, pixCount, 255, 0)
        img.pixels[i] = color(0, 153, 204, a)
def draw():
    global words,wordarray

    count=0;x=0;y=0;xind=0;yind=0
    for word in words:
        colind = map(len(word),0,32,0,255)
        fill(colind)
        
        xind=(xind+1) % 64
        if xind%64==0:
            yind=(yind+1) % 64
        x=xind*10
        y=yind*10
        wordarray[xind][yind]=word
        rect(x,y,10,10)
        #print(x,y,xind,yind,word)
        
def mousePressed():
    global wordarray
    x=int(mouseX/100)*10
    y=int(mouseY/100)*10
    print(x,y)
    #for i in range(64):
    #    for j in range(64):
    #        if i>60 and j>60:
    print(wordarray[x][y])
def mouseMoved():
    global wordarray
    x=int(round(mouseX/100)*10)
    y=int(round(mouseY/100)*10)
    print(x,y)
    if len(wordarray[x][y])>0:
        text(wordarray[x][y],x,y)
       #print( wordarray[x][y])
        
    

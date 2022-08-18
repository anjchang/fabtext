# This file takes the words from the Apolllo 11 sourcecode
# and remaps each word into a 10x10 pixel of a
#  shade of gray based on the length of the word
#  Todo is to create a word to color lookup table

w, h = 64,64
#palette = ["#D9C6B0", "#314650", "#2D4761", "#45718C", "#B6E1F2"]
palette = ["#00FFFF","#FF00FF","#FFFF00","#F0000F","#0F00FF","#FF00FF","#FF00FF"]
freqwords = ["TCF","TC","TS","MPAC","EXTEND","DXCH","INDEX"]
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
    print(63*63,count) #wordpixels, longest word length
    textAlign(CENTER,CENTER)
    #strokeWeight(8)
    noStroke()
        
def draw():
    global words,wordarray,freqwords,palette
    found=False
    count=0;x=0;y=0;xind=0;yind=0
    for word in words: #look at all words in array
        wordcategory = map(min(len(word),6),1,6,0,255) #number of letter to grayscale
        for term in freqwords:
            if (word.lower() == term.lower()): #word is in freqword
                found = True  #substitute a color we like
                fill(palette[freqwords.index(term)])
            else:
                fill(wordcategory) #just use the gray based on length
            if found:
                break;
        
        xind=(xind+1) % 64
        if xind%64==0:
            yind=(yind+1) % 64
        #layout
        x=xind*10
        y=yind*10
        wordarray[xind][yind]=word
        rect(x,y,10,10)
        # if found:        
        #     print(xind,yind,term,word,palette[freqwords.index(term)],freqwords.index(term))
        # else:
        #     continue
        #     print(xind,yind,term,word)
    
        found = False
    saveFrame("lunar3.png")
    #exit()
def mousePressed():
    global wordarray
    displayWord(mouseX,mouseY)
        
def displayWord(a,b):
    x=int(a/100)*10
    y=int(b/100)*10
    textSize(40)

    pushMatrix()
    translate(x*10,y*10)
    
    tstart=millis()
    tcount=0
    while tcount<1000:
        if len(wordarray[x][y])>0:
            for i in range(-10,2):
                fill(255)
                text(wordarray[x][y], 20+i+x,20+y);
                text(wordarray[x][y], 20+x,20+i+y);
            fill(0)
            text(wordarray[x][y],x,y)
        else:
            print("noword")
        tcount=millis()-tstart
    popMatrix()
       #print( wordarray[x][y])
def mouseMoved():
    global wordarray
    x=int(round(mouseX/100)*10)
    y=int(round(mouseY/100)*10)
    #displayWord(x,y)
    print( wordarray[x][y])
    #print(x,y)
    
        
    

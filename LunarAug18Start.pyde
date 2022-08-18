add_library('sound')
#this indexes correctly
img = None
imgNumbers = [] #array of pixel sounds
noteToPlay = [0] * 5
file = [] #list of sound files
posx = (0, 128, 256, 384, 512) #position of "key notes"
def setup():

    global img,index,imgNumbers, trigger,sqpx,sqcol,row
    size(1280, 720) #main window
    background(255)
    #add our sound files to file array
    for i in range(5):
        file.append(SoundFile(this, "%d.wav" % (i+1)))
    img = loadImage("lunar.png")
    print("wait for loading")
    for i in range(img.width * img.height): #go through pixels
        c = img.pixels[i] # color of that pixel
        x = map(c, color(0), color(255), 0, 4) #map color to sounds
        #print(c,x)
        imgNumbers.append(floor(x))
        # each pixel = a float from 0 to 5, match available sounds

    print(len(imgNumbers)) #number of pixels in our image 396900
    output = createWriter("lunarNumbers.txt")
    for note in imgNumbers:
        output.print(note) # Write the datum to the file
    output.flush()# Writes the remaining data to the file
    output.close()# Finishes the file
    
    
    trigger = millis()
    sqpx=10 #each square is 10x10 pixels
    sqcol=63 #63x63 squares on each side
    row=0 #starting row
    #index=len(imgNumbers)/2
    #index =0
    index=int(random(len(imgNumbers)))
    noStroke()
    #630, 630, 396900
    print("done Loading ",img.width , img.height, img.width * img.height)

def draw():
    global img,index,imgNumbers, trigger,sqpx,sqcol,row
    translate(325,45)
    image(img,0,0)
    noStroke()
    
    if index>=len(imgNumbers): #end of the image; quite
        index=0
        row=0
        col=0
        print("loop around")
        
    if (millis()>trigger):
        note=imgNumbers[index];
        file[note].play()
        col = int(index/(sqpx))%sqcol
        if (row==0):
            row = int(index/(sqcol*sqpx*sqpx))
        fill(100,255,100,80)
        strokeWeight(5)
        stroke(0,255,0)
        ellipse(col*sqpx,row*sqpx,sqpx,sqpx)
        stroke(255,0,255)
        ellipse(col*sqpx,row*sqpx,sqpx,sqpx)
        print(index,row,col,note)
    
        if col==62:
            row=row+1
            index=(sqpx*row*sqcol*sqpx)+sqpx #need to jump to 2801
            print("new",index,row,col)
        else:
            index= index+sqpx #goto next square at right
        
                
    if trigger < millis():
        #trigger = millis() + 100
       trigger = millis() + int(random(400,1000))
        

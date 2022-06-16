add_library('sound')

img = None
imgNumbers = [] #array of pixel sounds
noteToPlay = [0] * 5
file = [] #list of sound files
posx = (0, 128, 256, 384, 512) #position of "key notes"
playSound = [1] * 5  

def setup():
    global index,img, imgNumbers,trigger
    size(630, 700)
    background(255)
    #add our sound files to file array
    for i in range(5):
        file.append(SoundFile(this, "%d.wav" % (i+1)))

    img = loadImage("lunar.png")
    #print(img.width,img.height)
    #exit()
  
    for i in range(img.width * img.height): #go through pixels
        c = img.pixels[i] # color of that pixel
        x = map(c, color(0), color(255), 0, 4) #map color to sounds
        imgNumbers.append(floor(x))
        # each pixel = a float from 0 to 5, match available sounds
    #print(len(imgNumbers)) #number of pixels in our image
    #print(imgNumbers[60:70],file)
    index = 0
    trigger = millis()
    noStroke()

def draw():
    global trigger, index,img,file
    image(img, 0, 0)  #draw the image
    fill(0,255,0,0)
    stroke(0,255,0)
    strokeWeight(10)
    rect((index%63)*10,(int(index/63)%63)*10,10,10)
    if (millis() > trigger):  #every time
        
        fill(255)
        rect(0, 640, 630, 50)
        #take five pixels
        noteToPlay[0] = imgNumbers[index]
        noteToPlay[1] = imgNumbers[index + 1]
        noteToPlay[2] = imgNumbers[index + 2]
        noteToPlay[3] = imgNumbers[index + 3]
        noteToPlay[4] = imgNumbers[index + 4]
        
        for i in range(4):
            if noteToPlay[i] != noteToPlay[i + 1]: #when the notes differ
                note = noteToPlay[i]
                print(noteToPlay[i],noteToPlay[i + 1],index)
                file[note].play()
                fill(int(random(255)), int(random(255)), int(random(255)))
                rect(posx[i], 640, 128, 50)
        playSound[i] = int(random(0,2))
        
        fill(0,255,0,0)
        stroke(0,255,0)
        strokeWeight(10)
        rect((index%63)*10,(int(index/63)%63)*10,10,10)
        index = (index + 1) % len(imgNumbers)
        print(index,i)
        
    if trigger < millis():   #a time between 400-800ms
        trigger = millis() +  400 #int(random(400, 800)) #400
    

import pyscreenshot as ImageGrab

if __name__ == '__main__':
    # part of the screen
    im = ImageGrab.grab(bbox=(350, 110, 1000, 510))  # X1,Y1,X2,Y2
    im.show()
    im.save('/home/olivier/atelier/ruzzle/data/tests/r.tiff')
#-#
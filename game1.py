from pygame import *



window = display.set_mode((700, 500))
display.set_caption("First application")
window.fill((255, 100, 50))
background = transform.scale(image.load("fail_1.jpg"), (700,500))
window.blit(background,(0,0))

'''height=60
width=40
x=5
y=500-height-5
draw.rect(window,(0,0,255),(x,y,width,height))
'''
x=100
y=100
merlin = transform.scale(image.load('shutterstock_783589810_frame-32.png'), (100, 100))
window.blit(merlin, (x, y))

display.update()

run=True
while run:
    time.delay(20)
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key==K_LEFT:
                print('left')
                
            elif e.key==K_RIGHT:
                print('right')
            elif e.key==K_UP:
                print('up')
            elif e.key==K_DOWN:
                print('down')    
        if e.type == QUIT:
            quit()
            run=False

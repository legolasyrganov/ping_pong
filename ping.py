from pygame import *
init()

display.set_caption("Ping_pong")
window = display.set_mode((700, 500))
background = transform.scale(image.load("r.png"), (700, 500))

clock = time.Clock()


game = True
while game:
    window.blit(background, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick()
from figura_class import Pelota,Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")




cronometro = pg.time.Clock()

pelota = Pelota(400,300)
raqueta1 = Raqueta(10,300)
raqueta2 = Raqueta(790,300)

raqueta1.vy = 5
pelota.vx = 4



game_over = False

while not game_over:
    
    vt = cronometro.tick(60)#variable para controlar la velocidad entre fotogramas
    #print(vt)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    raqueta1.mover(pg.K_w,pg.K_s)#mover raqueta1 izquierda
    raqueta2.mover(pg.K_UP,pg.K_DOWN)#mover raqueta2 derecha
    pelota.mover()#mover pelota

    pantalla_principal.fill((0,128,94))#pintado de pantalla
 
    pelota.marcador(pantalla_principal)#pintado de marcador
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=2)#pintando linea blanca
    pelota.dibujar(pantalla_principal)#pintado de pelota
    raqueta1.dibujar(pantalla_principal)#pintado de raqueta1
    raqueta2.dibujar(pantalla_principal)#pintado de raqueta2
    
    if pelota.posicionX() > 0 and pelota.posicionX() < 20 and pelota.posicionY() < raqueta1.posicionY() and pelota.posicionY() > raqueta1.posicionY()-100:
        pelota.posicionX *= -1
        pelota.posicionY *= -1


    pg.display.flip()
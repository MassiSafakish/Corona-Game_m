import pygame,sys,random,time

from pygame.constants import K_DOWN, K_UP, MOUSEMOTION, K_a, K_d, K_w, K_x

pygame.init()

width=800
height=600

gameDisplay=pygame.display.set_mode((width,height))

pygame.display.set_caption('Corona Game')
#RGB color
clock=pygame.time.Clock()
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
white=(255,255,255)
pink=(255,0,127)
yello=(255,255,0)
black=(0,0,0)
e_pos=[random.randint(0,700),0]
p_pos=[e_pos]
speed=10
speed2=40
corona_pos=[350,500]
corona_w=75
corona_h=75
speed3=20
size=10
score=0
virus_w=75
virus_h=75
game_over=False
music_game=False
font1=pygame.font.Font(None,100)
font2=pygame.font.Font(None,60)
font3=pygame.font.Font(None,50)
font4=pygame.font.Font(None , 250)


def repet(d_pos):
    a=random.randint(0,10)
    if len(d_pos)<=10 and a<1 :
        x_pos=random.randint(0,700)
        y_pos=0
        d_pos.append([x_pos,y_pos])
def draw(d_pos,r):
    for enomy in d_pos:
        
        virus=pygame.image.load('6.jpg')
        virus_size=pygame.transform.scale(virus,(virus_w,virus_h))
        gameDisplay.blit(virus_size,(enomy[0],enomy[1]))
       
        if r>=50<200:
            
            virus2=pygame.image.load('10.png')
            virus_size2=pygame.transform.scale(virus2,(virus_w,virus_h))
            gameDisplay.blit(virus_size2,(enomy[0],enomy[1]))
            
        if r>=200<400:
            
            virus3=pygame.image.load('11.jpg')
            virus_size3=pygame.transform.scale(virus3,(virus_w,virus_h))
            gameDisplay.blit(virus_size3,(enomy[0],enomy[1]))
            
                
        
def motion(d_pos):
    for mot in d_pos:
          if (mot[0] == mot[0]) and (mot[1] <= 600):
            mot[1] += speed
          if mot[1]==600:
            mot[1]=0 
def update(d_pos):
    for index,y in enumerate(d_pos):
        if 0<=y[1]<600:
            y[1]+=10
        else:
            d_pos.pop(index)
def prize(d_pos,scr):
    for s in d_pos:
        if s[1]>525:
            scr+=1
    return scr
def check_col(d_pos) :
    for d in d_pos :
        if (corona_pos[0]<=d[0]<(corona_pos[0]+75)) or (d[0]<=corona_pos[0]<(d[0]+75)):
            if (corona_pos[1]<=d[1]<(corona_pos[1]+75)) or (d[1]<=corona_pos[1]<(d[1]+75)):
             
             return True
        else:
            return False
def level(sr,spd):

    if 0<=sr<50:
      spd=7
   
    elif 50<=sr<100:
      spd=20
        
    elif 100<=sr<200:
      spd=25
        
    else:
      spd=15
    return spd
def game_opening(b):
    music_game=pygame.mixer.music.load('DANCE-MONKEY_TONES-AND-I.mp3')
    paus=pygame.mixer.music.play(-1)
    t_s4=font4.render("3",True,red)
    gameDisplay.blit(t_s4,(350,240))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)
    t_s4=font4.render("2",True,red)
    gameDisplay.blit(t_s4,(350,240))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)
    t_s4=font4.render("1",True,red)
    gameDisplay.blit(t_s4,(350,240))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)
    t_s4=font4.render("Go",True,green)
    gameDisplay.blit(t_s4,(290,240))
    pygame.display.update()
    time.sleep(1)
    gameDisplay.fill(black)

score4=game_opening(score)
while not game_over:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_d:
                corona_pos[0]+=speed2
            if corona_pos[0]>725:
                corona_pos[0]=725
            if event.key ==K_a:
                corona_pos[0] -=speed2
            if corona_pos[0]<0:
                corona_pos[0]=0
            if event.key ==K_x:
                corona_pos[1]+=speed2
            if corona_pos[1]>525:
                corona_pos[1]=525
            if event.key== K_w:
                corona_pos[1]-=speed2
            if corona_pos[1]<0:
                corona_pos[1]=0
        
        if event.type ==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                corona_pos[0]-=speed3
            if corona_pos[0]<0:
                corona_pos[0]=0
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==3:
                  corona_pos[0]+=speed3
                if corona_pos[0]>725:
                    x_corona=725
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==4:
                    corona_w+=size
                    corona_h+=size
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==5:
                 corona_w-=size
                 corona_h-=size
                 if (corona_w<0) or (corona_h<0):
                     corona_w=75
                     corona_h=75
    if check_col(p_pos):
        t_s=font1.render('Game Over!',True,pink)
        t_s3=font3.render("your score is:" + str(score),True,red)
        gameDisplay.blit(t_s3,(250,340))
        gameDisplay.blit(t_s,(200,270))
        pygame.display.update()
        time.sleep(3)
        game_over=True
        break 
        
    icon=pygame.image.load('icon1.jpg')
    pygame.display.set_icon(icon)
    gameDisplay.fill(white)
    
    bg=pygame.image.load('5.jpg')
    BG=pygame.transform.scale(bg,(width,height))
    gameDisplay.blit(BG,(0,0))
    char=pygame.image.load('4.jpg')
    CHAR=pygame.transform.scale(char,(corona_w,corona_h))
    gameDisplay.blit(CHAR,(corona_pos[0],corona_pos[1]))

    if 50<=score<100:
        background=pygame.image.load('13.png')
        background2=pygame.transform.scale(background,(width,height))
        gameDisplay.blit(background2,(0,0))
        char=pygame.image.load('4.jpg')
        CHAR=pygame.transform.scale(char,(corona_w,corona_h))
        gameDisplay.blit(CHAR,(corona_pos[0],corona_pos[1]))
    if 100<=score<200:
        background=pygame.image.load('12.jpg')
        background2=pygame.transform.scale(background,(width,height))
        gameDisplay.blit(background2,(0,0))
        char=pygame.image.load('4.jpg')
        CHAR=pygame.transform.scale(char,(corona_w,corona_h))
        gameDisplay.blit(CHAR,(corona_pos[0],corona_pos[1]))
    motion(p_pos)
    
    repet(p_pos)
    score2=draw(p_pos,score)
    update(p_pos)
    score=prize(p_pos,score)
    t_s2=font2.render("score:" + str(score),True,green)
    gameDisplay.blit(t_s2,(0,5))
    speed=level(score,speed)
    pygame.display.update()
    clock.tick(150)
# Import thư viện
import pygame ,random
pygame.init()
# setup screen
SC = pygame.display.set_mode((600,600))
# Create caption
pygame.display.set_caption("Fruity Game")
# Khởi tạo các biến 
PINK = (238,138,248)
RED = (255,0,0)
BROWN = (142,64,58)
BLACK = (0,0,0)
bowl_x = 250
sau_rieng_x = random.randint(0,565)
sau_rieng_y = 0
sau_rieng_drop = 3
score = 0
font = pygame.font.Font('04B_19.TTF',20)
font_over = pygame.font.Font('04B_19.TTF',70)
sau_rieng_image = pygame.image.load(r'sau_rieng.png')
sau_rieng_image = pygame.transform.scale(sau_rieng_image,(35,35))
bowl_image = pygame.image.load(r'bowl.png')
bowl_image = pygame.transform.scale(bowl_image,(100,50))
background_image = pygame.image.load(r'Blue Sky.png')
background_image = pygame.transform.scale(background_image,(600,600))
running = True
Clock = pygame.time.Clock()
while running : 
    # Thiết lập thời gian rơi
    Clock.tick(60)
    # màu màn hình
    SC.blit(background_image,(0,0))
    # Vẽ cái chén 
    #bowl = pygame.draw.rect(SC,RED,(bowl_x,550,100,50))
    bowl = SC.blit(bowl_image,(bowl_x,550))
    # Vẽ trái cây 
    #sau_rieng = pygame.draw.rect(SC,RED,(sau_rieng_x,sau_rieng_y,35,35))
    sau_rieng = SC.blit(sau_rieng_image,(sau_rieng_x,sau_rieng_y))
    # Câu lệnh để tương tác
    if bowl_x <= 0:
       bowl_x = 0 
    if bowl_x >= 500:
       bowl_x = 500
    sau_rieng_y = sau_rieng_y + sau_rieng_drop
    # Vẽ nền check va chạm
    ground = pygame.draw.rect(SC,BROWN,(0,599,600,1))
    # tính điểm 
    if sau_rieng.colliderect(bowl):
        sau_rieng_y = 0 
        sau_rieng_x = random.randint(0,565)
        score = score + 1 
    if sau_rieng.colliderect(ground):
        sau_rieng_drop = 0
        score_txt2 = font_over.render('Game Over',True,BLACK)
        SC.blit(score_txt2,(110,270))
    # Hiển thị điểm 
    score_txt = font.render('SCORE:'+str(score),True,BLACK)
    SC.blit(score_txt,(5,5))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               bowl_x = bowl_x - 60 # Di chuyển sang trái
            if event.key == pygame.K_RIGHT:
               bowl_x = bowl_x + 60 # Di chuyển sang phải
    # Câu lệnh hiển thị lên màn hình nếu ko có câu lệnh này các dòng trên sẽ ko hiển thị trên cửa sổ pygame
    pygame.display.flip()
pygame.quit()
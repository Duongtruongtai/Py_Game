# Import thư viện
import pygame
pygame.init()
clock = pygame.time.Clock()
# Create tiêu đề và icon game
pygame.display.set_caption("Dino Game")
icon = pygame.image.load(r'assets\dinosaur.png')
# Screen Game
screen = pygame.display.set_mode((600,300))
# Load Music 
sound1 = pygame.mixer.Sound(r'sound\tick.wav')
sound2 = pygame.mixer.Sound(r'sound\te.wav')
# Load Image
bg = pygame.image.load(r'assets\background.jpg').convert()
tree = pygame.image.load(r'assets\tree.png').convert_alpha()
dino = pygame.image.load(r'assets\dinosaur.png').convert_alpha()
# Khởi tạo 
score,hscore = 0,0
bg_x, bg_y = 0,0 
tree_x, tree_y = 550,230
dino_x, dino_y = 10,230
x_def = 5
y_def = 7 # Tốc độ rơi của dino
jump = False
gameplay = True
# Hàm check vc 
def check_vc():
   if dino_hcn.colliderect(tree_hcn):
      pygame.mixer.Sound.play(sound2)
      return False
   return True
# Đưa điểm vào 
game_font = pygame.font.Font('04B_19.TTF',20)
def score_view():
   if gameplay:
      score_txt = game_font.render(f'Score: {int(score)}',True,(0,191,255))
      screen.blit(score_txt,(250,50))
      hscore_txt = game_font.render(f'High Score: {int(hscore)}',True,(0,191,255))
      screen.blit(score_txt,(250,100))
   else:
      score_txt = game_font.render(f'Score: {int(score)}',True,(0,191,255))
      screen.blit(score_txt,(250,70))
      hscore_txt = game_font.render(f'High Score: {int(hscore)}',True,(0,191,255))
      screen.blit(score_txt,(250,100))

# Vòng lặp xử lý game 
running = True 
while running:
    # Chình FPS
    clock.tick(70)
    for evnet in pygame.event.get():
        if evnet.type == pygame.QUIT:
            running = False
        if evnet.type == pygame.KEYDOWN:
            if evnet.key == pygame.K_SPACE and gameplay:
               if dino_y == 230:
                jump = True
                pygame.mixer.Sound.play(sound1)
            if evnet.key == pygame.K_SPACE and gameplay == False :
               gameplay = True
    if gameplay:               
      # bg 
      bg_hcn = screen.blit(bg,(bg_x,bg_y))
      bg2_hcn = screen.blit(bg,(bg_x,bg_y))
      bg_x -= x_def
      if bg_x == -600 : bg_x = 0
      #tree
      tree_hcn = screen.blit(tree,(tree_x,tree_y))
      tree_x -= x_def
      if tree_x == -20 : tree_x = 550
      #dino
      dino_hcn = screen.blit(dino,(dino_x,dino_y))
      if dino_y >= 80 and jump:
         dino_y -= y_def
      else:
         jump = False 
      if dino_y < 230 and jump == False:
         dino_y += y_def
      score += 0.01 
      if hscore < score : hscore = score
      gameplay = check_vc()
      score_view()
    else:
       # Reset game
      
       bg_x, bg_y = 0,0 
       tree_x, tree_y = 550,230
       dino_x, dino_y = 10,230
       bg_hcn = screen.blit(bg,(bg_x,bg_y))
       tree_hcn = screen.blit(tree,(tree_x,tree_y))
       dino_hcn = screen.blit(dino,(dino_x,dino_y))
       score = 0
       score_view()
    pygame.display.update()

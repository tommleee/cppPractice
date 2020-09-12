import pygame
pygame.init()

#화면 크기
screenWidth = 480
screenHeight = 640
screen = pygame.display.set_mode((screenWidth, screenHeight))

#화면 타이틀
pygame.display.set_caption("Nado game") #game name

running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하는가
        if event.type == pygame.QUIT:
            running = False
        
    
#pygame 종료
pygame.quit()
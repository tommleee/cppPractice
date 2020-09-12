import pygame
pygame.init()

#화면 크기
screenWidth = 480
screenHeight = 640
screen = pygame.display.set_mode((screenWidth, screenHeight))

#화면 타이틀
pygame.display.set_caption("Nado game") #game name

#배경 불러오기
background = pygame.image.load("/Users/tomlee/dev/pythonWorkspace/pygame_basic/background.png")
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하는가
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0)) #배경 그리기

    pygame.display.update() #게임화면 다시 그리기

    
#pygame 종료
pygame.quit()
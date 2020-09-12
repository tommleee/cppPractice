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

#스프라이트 (캐릭터) 불러오기
character = pygame.image.load("/Users/tomlee/dev/pythonWorkspace/pygame_basic/character.png")
characterSize = character.get_rect().size #이미지의 크기를 구해옴
characterWidth = characterSize[0] #캐릭터 가로크기
characterHeight = characterSize[1] #캐릭터 세로크기
characterXPos = screenWidth / 2 - (characterWidth / 2) #캐릭터 x 좌표
characterYPos = screenHeight - characterHeight #캐릭터 y 좌표





running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하는가
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (characterXPos, characterYPos))

    pygame.display.update() #게임화면 다시 그리기

    
#pygame 종료
pygame.quit()
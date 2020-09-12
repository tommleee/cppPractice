import pygame
pygame.init()

#화면 크기
screenWidth = 480
screenHeight = 640
screen = pygame.display.set_mode((screenWidth, screenHeight))

#화면 타이틀
pygame.display.set_caption("Nado game") #game name

#FPS
clock = pygame.time.Clock()

#배경 불러오기
background = pygame.image.load("/Users/tomlee/dev/pythonWorkspace/pygame_basic/background.png")

#스프라이트 (캐릭터) 불러오기
character = pygame.image.load("/Users/tomlee/dev/pythonWorkspace/pygame_basic/character.png")
characterSize = character.get_rect().size #이미지의 크기를 구해옴
characterWidth = characterSize[0] #캐릭터 가로크기
characterHeight = characterSize[1] #캐릭터 세로크기
characterXPos = screenWidth / 2 - (characterWidth / 2) #캐릭터 x 좌표
characterYPos = screenHeight - characterHeight #캐릭터 y 좌표

#이동할 좌표
toX = 0
toY = 0

#이동 속도
characterSpeed = 0.4

#적 캐릭터
enemy = pygame.image.load("/Users/tomlee/dev/pythonWorkspace/pygame_basic/enemy.png")
enemySize = enemy.get_rect().size #이미지의 크기를 구해옴
enemyWidth = enemySize[0] #캐릭터 가로크기
enemyHeight = enemySize[1] #캐릭터 세로크기 
enemyXPos = (screenWidth / 2) - (enemyWidth / 2) #캐릭터 x 좌표
enemyYPos = (screenHeight / 2) - (enemyHeight / 2) #캐릭터 y 좌표

#폰트 정의
gameFont = pygame.font.Font(None, 40) #폰트 생성 (None = default)

#총 시간
totalTime = 10

#시간 계산
startTicks = pygame.time.get_ticks()


#이벤트 루프
running = True #게임이 진행중인가
while running:
    dt = clock.tick(60) #dt = delta  = 초당 프레임 수 
    
    for event in pygame.event.get(): #어떤 이벤트가 발생하는가
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                toX -= characterSpeed
            elif event.key == pygame.K_RIGHT:
                toX += characterSpeed
            elif event.key == pygame.K_UP:    
                toY -= characterSpeed            
            elif event.key == pygame.K_DOWN:
                toY += characterSpeed

        if event.type == pygame.KEYUP: #방향키를 뗀 후
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                toX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                toY = 0
    
    characterXPos += toX * dt 
    characterYPos += toY * dt

    #가로 경계
    if characterXPos < 0:
        characterXPos = 0
    elif characterXPos > screenWidth - characterWidth:
        characterXPos = screenWidth - characterWidth
    
    #세로 경계
    if characterYPos < 0:
        characterYPos = 0
    elif characterYPos > screenHeight - characterHeight:
        characterYPos = screenHeight - characterHeight

    #충돌 좌표 업데이트
    characterRect = character.get_rect()
    characterRect.left = characterXPos
    characterRect.top = characterYPos
    
    enemyRect = enemy.get_rect()
    enemyRect.left = enemyXPos
    enemyRect.top = enemyYPos


    #충돌 체크
    if characterRect.colliderect(enemyRect):
        print("충돌 했어요")
        running = False
    
    
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (characterXPos, characterYPos))
    screen.blit(enemy, (enemyXPos, enemyYPos))

    #타이머
    #경과시간 계산
    elapsedTime = (pygame.time.get_ticks() - startTicks) / 1000 #경과시간(ms)을 1000으로 나누면 초단위

    timer = gameFont.render(str(int(totalTime - elapsedTime)), True, (255, 255, 255))
                    #render(출력할 글자, True, 글자색상)
    screen.blit(timer,(10, 10))
    if (totalTime - elapsedTime) <= 0:
        print("TIME OUT!")
        running = False

    pygame.display.update() #게임화면 다시 그리기

pygame.time.delay(2000) #2000ms 대기 = 2초
    
#pygame 종료
pygame.quit()
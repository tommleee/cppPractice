import pygame
import random

pygame.init() 

#화면 크기
screenWidth = 480
screenHeight = 640
screen = pygame.display.set_mode((screenWidth, screenHeight))

#화면 타이틀
pygame.display.set_caption("똥피하기 게임") #game name

#FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트..)
background = pygame.image.load("/Users/tomlee/dev/pythonWorkspace/pygame_basic/background.png")

#character
character = pygame.image.load("/Users/tomlee/dev/pythonWorkspace/pygame_basic/character.png")
characterSize = character.get_rect().size
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXPos = screenWidth / 2 - (characterWidth / 2)
characterYPos = screenHeight - characterHeight
characterSpeed = 0.4

#enemy
enemy = pygame.image.load("/Users/tomlee/dev/pythonWorkspace/pygame_basic/enemy.png")
enemySize = enemy.get_rect().size
enemyWidth = enemySize[0]
enemyHeight = enemySize[1]
enemyXPos = random.randint(0, screenWidth - enemyWidth)
enemyYPos = 0 - enemyHeight
enemySpeed = 0.6

toX = 0

gameFont = pygame.font.Font(None, 40)

gameScore = 0


#이벤트 루프
running = True #게임이 진행중인가
while running:
    dt = clock.tick(60) #dt = delta  = 초당 프레임 수 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    
    for event in pygame.event.get(): #어떤 이벤트가 발생하는가
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                toX -= characterSpeed
            elif event.key == pygame.K_RIGHT:
                toX += characterSpeed
        
        if event.type == pygame.KEYUP: #방향키를 뗀 후
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                toX = 0

    characterXPos += toX * dt
    enemyYPos += enemySpeed * dt

    # 3. 게임 캐릭터 위치 정의
    if characterXPos < 0:
        characterXPos = 0
    elif characterXPos > screenWidth - characterWidth:
        characterXPos = screenWidth - characterWidth

    if characterYPos > screenHeight - characterHeight:
        characterYPos = screenHeight - characterHeight
    
    if enemyYPos > screenHeight:
        enemyYPos = 0
        enemyXPos = random.randint(0, (screenWidth - enemyWidth))
        gameScore += 1

    
    # 4. 충돌 처리
    characterRect = character.get_rect()
    characterRect.left = characterXPos
    characterRect.top = characterYPos

    enemyRect = enemy.get_rect()
    enemyRect.left = enemyXPos
    enemyRect.top = enemyYPos

    if characterRect.colliderect(enemyRect):
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (characterXPos, characterYPos))
    screen.blit(enemy, (enemyXPos, enemyYPos))

    scoreBoard = gameFont.render(str(int(gameScore)), True, (255, 255, 255))
    screen.blit(scoreBoard, (10,10))

    if gameScore == 20:
        running = False

    pygame.display.update() #게임화면 다시 그리기
    
# 6. 게임 종료
pygame.quit()
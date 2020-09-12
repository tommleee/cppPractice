import os
import pygame

############################################################################################################################################################
# 기본 초기화
pygame.init() 

#화면 크기
screenWidth = 640
screenHeight = 480
screen = pygame.display.set_mode((screenWidth, screenHeight))

#화면 타이틀
pygame.display.set_caption("PANG!") #game name

#FPS
clock = pygame.time.Clock()
############################################################################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트..)
currentPath = os.path.dirname(__file__) #현재 파일의 위치 반환
imagePath = os.path.join(currentPath, "images") #images 폴더 위치 반환

#배경
background = pygame.image.load(os.path.join(imagePath, "background.png"))

#스테이지
stage = pygame.image.load(os.path.join(imagePath, "stage.png"))
stageSize = stage.get_rect().size
stageHeight = stageSize[1]

#캐릭터
character = pygame.image.load(os.path.join(imagePath, "character.png"))
characterSize = character.get_rect().size
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXPos = (screenWidth / 2) - (characterWidth / 2)
characterYPos = screenHeight - characterHeight - stageHeight

#이벤트 루프
running = True #게임이 진행중인가
while running:
    dt = clock.tick(60) #dt = delta  = 초당 프레임 수 

    # 2. 이벤트 처리 (키보드, 마우스 등)
    
    for event in pygame.event.get(): #어떤 이벤트가 발생하는가
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYUP: #방향키를 뗀 후
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                toX = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                toY = 0
    
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(stage, (0,screenHeight - stageHeight))
    screen.blit(character, (characterXPos, characterYPos))

    pygame.display.update() #게임화면 다시 그리기
    
# 6. 게임 종료
pygame.quit()
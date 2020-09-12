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

#캐릭터 이동방향
characterToX = 0

#캐릭터 속도
characterSpeed = 5

#무기
weapon = pygame.image.load(os.path.join(imagePath, "weapon.png"))
weaponSize = weapon.get_rect().size
weaponWidth = weaponSize[0]

#무기는 한번에 여러발 발사 가능
weapons = []

#무기 이동 속도
weaponSpeed = 10

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
                characterToX -= characterSpeed
            elif event.key == pygame.K_RIGHT:
                characterToX += characterSpeed
            elif event.key == pygame.K_SPACE:
                weaponXPos = characterXPos + (characterWidth / 2) - (weaponWidth / 2)
                weaponYPos = characterYPos
                weapons.append([weaponXPos, weaponYPos])
        
        if event.type == pygame.KEYUP: #방향키를 뗀 후
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                characterToX = 0
    
    # 3. 게임 캐릭터 위치 정의
    characterXPos += characterToX

    if characterXPos < 0:
        characterXPos = 0
    elif characterXPos > screenWidth - characterWidth:
        characterXPos = screenWidth - characterWidth

    #무기위치 조정
    weapons = [ [w[0], w[1] - weaponSpeed] for w in weapons]
    
    #천장에 닿는 무기 없애기
    weapons = [ [w[0], w[1] - weaponSpeed] for w in weapons if w[1] > -50]
    # 4. 충돌 처리
    
    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    for weaponXPos, weaponYPos in weapons:
        screen.blit(weapon, (weaponXPos, weaponYPos))
    screen.blit(stage, (0,screenHeight - stageHeight))
    screen.blit(character, (characterXPos, characterYPos))


    pygame.display.update() #게임화면 다시 그리기
    
# 6. 게임 종료
pygame.quit()
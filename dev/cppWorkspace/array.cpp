#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int main() {
 
    srand(time(NULL));
    printf("\n\n아빠는 대머리 게엠\n\n");
    int answer;
    int treatment = rand() % 4;

    int crntShowBottle = 0; //이번 게임에 보여줄 병 갯수
    int prevShowBottle = 0; //앞 게임에 보여준 병 갯수

    for(int i = 1; i <= 3; i++) {
        int bottle[4] = {0, 0, 0, 0};
        do {
            crntShowBottle = rand() % 2 + 2;

        } while(crntShowBottle == prevShowBottle);
        
        int isIncluded = 0; //보여줄 병 중에 발모제가 포함 되었는지 여부
        printf(" > %d 번째 시도: ", i);

        //보여줄 병 종류 선택
        for(int j = 0; j < crntShowBottle; j++) {
            int randBottle = rand() % 4; //0부터 3까지
            
            //아직 선택되지 않은 병이면, 선택처리
            if(bottle[randBottle] == 0) {
                bottle[randBottle] = 1;
                if(randBottle == treatment) {
                    isIncluded = 1;
                }
            }
            //이미 선택된 병이면, 중복이므로 다시 선택
            else {
                j--;
            }         
        }

        //사용자에게 문제 표시
        for(int k = 0; k < 4; k++) {
            if(bottle[k] == 1)
                printf("%d ", k + 1);
        }
        printf(" 물약을 머리에 바릅니다.\n\n");

        if(isIncluded == 1) {
            printf(" >> 성공! 머리가 났어요 !!\n");
        }
        else {
            printf(" >> 실패! 머리가 나지 않았어요. \n");
        }

        printf("\n 계속하려면 아무거나 누르세요.");
        getchar();
    }

    printf("\n\n발모제는 몇번일까요? ");
    scanf("%d", &answer);

    if(answer == treatment + 1) {
        printf("\n >> 정답입니다!\n");
    }  
    else{
        printf("\n >> 떙! 틀렸어요. 정답은 %d 입니다. \n", treatment + 1);
    }
    

}
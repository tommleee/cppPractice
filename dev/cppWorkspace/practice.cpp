#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int getRandNumber(int level);
void showQuestion(int, int, int);
void success();
void fail();

int main_function() {

    srand(time(NULL));
    int count = 0;  
    for(int i = 1; i <= 5; i++) {
        int num1 = getRandNumber(i);
        int num2 = getRandNumber(i);
        showQuestion(i, num1, num2);

        int answer = -1;
        scanf("%d", &answer);
        if (answer == -1)
        {
            printf("프로그램을 종료합니다\n");
            exit(0);
        }
        else if(answer == num1 * num2) {
            success();
            count++;
        }
        else {
            fail();
        }
    }       

    printf("\n\n 당신은 5개의 비밀번호 중 %d 개를 맞췄습니다.\n", count);
}

void success() {
    printf("\n Good!");
}

void fail() {
    printf("\n Fail!");
}

int getRandNumber(int level) {
    return rand() % (level * 7) + 1;
}


void showQuestion(int level, int num1, int num2) {
    printf("\n\n\n########## %d 번째 비밀번호 ##########\n", level);
    printf("\n\t%d x %d 는? \n\n", num1, num2);
    printf("##################################\n");
    printf("\n비밀번호를 입력하세요. (종료: -1) >> \n");

}
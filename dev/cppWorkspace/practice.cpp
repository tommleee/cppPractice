#include <iostream>
#include <time.h>

using namespace std;


int main() {

    srand((unsigned int) time(0));

    int array[9] = {};
    for (int i = 0; i < 9; i++) {
        array[i] = i + 1;
    }

    int temp, idx1, idx2;
    for(int i = 0; i < 50; i++) {
        idx1 = rand() % 9;
        idx2 = rand() % 9;

        temp = array[idx1];
        array[idx1] = array[idx2];
        array[idx2] = temp;
    }
    cout << "* " << "* " << "* " << endl;

    int strike = 0 , ball = 0;
    int input[3];
    int inning = 1;

    while(true) {
        
        cout << inning << "회" << endl;
        cout << "1 ~ 9 사이의 숫자중 숫자 3개를 입력하세요(0: 종료) : \n";
        cin >> input[0] >> input[1] >> input[2];

        if(input[0] == 0 || input[1] == 0 || input[2] == 0)
            break;
        else if(0 > input[0] || input[0] > 9 || 0 > input[1] || input[1] > 9 || 0 > input[2] || input[2] > 9 ) {
            cout << "다시 입력하세요. (1 과 9 사이의 숫자)" << endl;
            continue;
        }

        else if(input[0] == input[1] || input[0] == input[2] || input[1] == input[2]) {
            cout << "중복돤 숫자를 입력하셨습니다. 다시 입력하세요." << endl;
            continue;
        }

        strike = ball = 0;

        for(int i = 0; i < 3; i++) {
            for(int j = 0; j < 3; j++) {
                if(array[i] == input[j]) {
                    if(i == j)
                        ++strike;
                    else
                        ++ball;
                    break;
                }
            }
        }

        if(strike == 3) {
            cout << "숫자를 모두 맞췄습니다!" << endl;
            break;
        } 
        else if(strike == 0 && ball == 0) {
            cout << "OUT!" << endl;
        } 
        else {
            cout << strike << " strike(s) / " << ball << " ball(s)" << endl;
            inning++;
        }


    }

    cout << "Game Finished!!\n";

    return 0;

}
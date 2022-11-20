#include <stdio.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>
#include <stdlib.h>
#include <ctype.h>

void init() {
    system("");
    system("color");
    srand(time(NULL));
    cls();
    
}

int randint(int start, int end) {
    int r;
    while (1) {
        r = rand();
        if (r < (end + 1) && r > (start - 1)) {
            return r;
        } else {
            int i;
            for (i=10;i<1000000001;i = i * 10) {
                if ((r / i) < end + 1 && (r/i) > start - 1) {
                    return r / i;
                } else {
                    continue;
                }
            }
        }
    }
}
void cls() {
    
    system("clear");
}

void wait4ret(char* prompt) {
    char garbage[100];
    printf("%s...",prompt);
    fgets(&garbage,100,stdin);
}

int is_number(char* data,int allownegatives, int allowdecimal) {
    int dec = 0;
    int neg = 0;
    //Returns 0 on yes, 1 on no.
    if (data[0] == 45 && allownegatives == 0) {
        return 1;
    } else if (data[0] == 45) {
        neg += 1;
    }
    for (int i = 0; i < strlen(data) - 2;i = i + 1) { // len -2 to cut off newline and EOF
        if (!(data[i] == 20 || data[i] == 10)) {
            //Ignoring newlines and whitespace
            if (data[i] == 46) {
                dec += 1; //Only allow one decimal otherwise ILLEGAL
                if (allowdecimal == 0){
                    return 1;
                }
                continue;
            } else {
                if (isdigit(data[i])!=0) {
                    continue;
                } else {
                    return 1;
                }
            }
            
        }
    }
    return 0;
}

double getnuminput(int allownegatives) {
    //Allow negatives must be 0 to forbid
    char *ptr;
    while (1) {
        printf(">>>");
        char data[64];// Assuming noone would enter a number longer than this (must overflow limit at some point)
        fgets(&data,64,stdin);
        if (is_number(data,allownegatives,1)==0) {
            return strtod(data,&ptr);
        } else {
            printf("\033[F                        \r"); // Going back a line
        }
        
    }
}

void addsys(int questions, int lown, int highn) {
    cls();

    printf("Questions: %i\nRange: %i-%i\n",questions,lown,highn);

    wait4ret("\nPress enter to begin");
    double sttime = 0.0;
    struct timeval start,end;
    gettimeofday(&start,NULL);
    int i;
    int correct = 0;
    int wrong = 0;
    int q0[questions];
    cls();
    for (i = 1;i < (questions + 1); i = i + 1) {
        
        printf("Question %d:\n",i);
        int bgx;
        int bgy;
        int answ;
        int iters = 0;
        while (1) //This loop is to prevent duplicate questions because RNG is biased to one
        {
            iters += 1;
            int doagain = 0;
            bgx = randint(lown,highn);
            bgy = randint(lown,highn);
            answ = bgx + bgy;
            if (!(questions > (highn - lown)*(highn - lown))) {// Allowing duplicates if there are more questions than possible answers
                int j;
                for (j = 0; j < (i - 1);j = j + 1) {
                    if (q0[j] == answ) {
                        doagain = 1;
                        break;
                    }
                }
                if (doagain == 1) {
                    //printf("Doing Again\n");//For debug
                    if (iters > 100) {
                        break; //Giving up and allowing duplicates if more than 100 iterations
                    }
                    continue;
                }
                break;
            }
            else {
                break; //NO MORE INFINITE LOOP
            }
        }
        
        q0[i-1] = answ;
        printf("%d + %d\n",bgx,bgy);
        double answer = getnuminput(0);
        if (answer == answ) {
            printf("You got it correct!\n");
            correct += 1;
        } else {
            printf("You got it wrong.\n");
            wrong += 1;
        }
        sleep(1);
        cls();
    }
    gettimeofday(&end,NULL);
    sttime = end.tv_sec - start.tv_sec;
    printf("Time: %.0f seconds\n",sttime);
    printf("Correct Answers: %i\n",correct);
    printf("Incorrect Answers: %i\n",wrong);
    printf("Correct Rate (%i answers): %f%%\n",questions,(correct/questions)*100.0);
    wait4ret("Press Enter to continue");
}

int chkr() {
    char iin[100];
    //Return 0 to exit nicely
    //Return -1 to continue
    printf("0: Exit\n1: Adding\n\n>>>");
    fgets(&iin,100,stdin);
    if (strcmp(iin,"0\n")== 0) {
        return 0;
    } else if (strcmp(iin,"1\n")==0) {
        addsys(5,0,10);
    }
    cls();
    return -1;
}

int main() {
    init();
    
    while (1) {
        int u = chkr();
        if (u == 0) {
            break;
        }
    }
    return 0;
}
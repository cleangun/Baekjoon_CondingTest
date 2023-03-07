#include <stdio.h>
void main()
{
    int i, answer, score = 0, num, correct;
    for (i = 0; i < 5; i++) {
        correct = 0;
        num = 0;
        while (num < 3 && !correct) { // 덧셈문제제출 문장
            printf("%d + %d = ", i * i, i * 10); scanf_s("%d", &answer);
            if (answer == (i * i) + (i * 10)) {
                printf("Correct!!\n");
                correct = 1;
                score += (20 - num * 3);
            }
            else
                printf("try again!!! \n"); num++;

        }
    } printf("당신의 덧셈성적은 ? %d\n", score);
}
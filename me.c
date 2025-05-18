#include <stdio.h>

int twice( int input);
int thrice(int input);

int main(int argc, char **args)
{
int x = 20;
printf("x=%d\n",x); //20


int y;
printf("y=%d\n",y); //current value of y which could be anything

y = twice(x); // passing a copy of x into function "twice"
printf("twice y=%d\n",y); // 40

printf("x=%d\n",x); // 20

}

int twice( int input)
{
    return 2*input;
}


int thrice( int input)
{
    return 3*input;
}
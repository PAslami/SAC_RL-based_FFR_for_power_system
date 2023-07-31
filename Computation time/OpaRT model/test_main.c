/*
Filename:       test_main.c
Written by:     Niranjan Bhujel
Date:           Feb 5, 2023
*/

#include <stdio.h>
#include "test_call.h"

int main(int argc, char const *argv[])
{
    float x[3] = {0.1, 0.06, 0.09};
    // float u[1] = {0.1};
    float y[256];

    call_net(x,  y);

    printf("%f\n", y[0]);

    // for (int i = 0; i < 1; i++)
    // {
    //     printf("%f\n", y[i]);
    // }

    return 0;
}

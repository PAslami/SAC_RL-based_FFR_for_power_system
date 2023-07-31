/*
Filename:       layers.c
Written by:     Niranjan Bhujel
Date:           Feb 5, 2023
Description:    Function to call layers of neural network
*/

#include "cores.h"

void dense_call(float *W, float *b, float *x, float *y, void (*activation)(float *, int, int), int nx, int ny)
{
    mat_vec(W, x, b, y, ny, nx);
    activation(y, 0, ny);
}

void concatenate_call(float *x1, float *x2, float *y, int nx1, int nx2)
{
    int i;

    for (i = 0; i < nx1; i++)
    {
        y[i] = x1[i];
    }

    for (i = 0; i < nx2; i++)
    {
        y[nx1 + i] = x2[i];
    }
}
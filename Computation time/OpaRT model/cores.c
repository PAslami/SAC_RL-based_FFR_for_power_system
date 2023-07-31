/*
Filename:       cores.c
Written by:     Niranjan Bhujel
Date:           Feb 5, 2023
Description:    Function containing basic operation required to build neural network.
*/

#include <math.h>

void mat_vec(float *A, float *x, float *y, float *z, const int M, const int N)
{
    int i, j;

    float tmp[M];

    for (i = 0; i < M; i++)
    {
        tmp[i] = y[i];
        for (j = 0; j < N; j++)
        {
            tmp[i] += A[i * N + j] * x[j];
        }
    }

    for (i = 0; i < M; i++)
    {
        z[i] = tmp[i];
    }
}

void tanh_activation(float *x, int start, int N)
{
    int i;
    for (i = start; i < start + N; i++)
    {
        x[i] = tanhf(x[i]);
    }
}

void relu_activation(float *x, int start, int N)
{
    int i;
    for (i = start; i < start + N; i++)
    {
        x[i] = x[i] >= 0 ? x[i] : 0;
    }
}

void linear_activation(float *x, int start, int N)
{
}


void rk4_integrate(void (*fc)(float *, float *, float *), float Ts, float *x0, float *u0, const int nx, float *x)
{
    void add_vec_scalar(float *x, float a, float *y, float *z, int nx)
    {
        int i;
        for (i = 0; i < nx; i++)
        {
            z[i] = x[i] + a * y[i];
        }
    }
    
    float k1[nx], k2[nx], k3[nx], k4[nx];
    float xtmp[nx];
    int i;

    fc(x0, u0, k1);

    add_vec_scalar(x0, Ts / 2, k1, xtmp, nx);
    fc(xtmp, u0, k2);

    add_vec_scalar(x0, Ts / 2, k2, xtmp, nx);
    fc(xtmp, u0, k3);

    add_vec_scalar(x0, Ts, k3, xtmp, nx);
    fc(xtmp, u0, k4);

    for (i = 0; i < nx; i++)
    {
        x[i] = x0[i] + Ts / 6 * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]);
    }
}

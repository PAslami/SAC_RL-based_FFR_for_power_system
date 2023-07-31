/*
Filename:       cores.h
Written by:     Niranjan Bhujel
Date:           Feb 5, 2023
Description:    Function containing basic operation required to build neural network.
*/

#include <math.h>

#ifndef cores_h
#define cores_h

/**
 * @brief Function to perform matrix vector product. z = A*x + y
 *
 * @param A matrix A of size MxN
 * @param x vector x of size M
 * @param y vector y of size M
 * @param z vector z of size M
 * @param M number of row in A
 * @param N number of column in A
 */
void mat_vec(float *A, float *x, float *y, float *z, const int M, const int N);

/**
 * @brief Function to apply tanh activation function on vector
 *
 * @param x vector where the activation function is to be applied
 * @param start start index from where the activation function needs to be applied
 * @param N number of elements from index start where the activation function needs to be applied
 */
void tanh_activation(float *x, int start, int N);

/**
 * @brief Function to apply relu activation function on vector
 *
 * @param x vector where the activation function is to be applied
 * @param start start index from where the activation function needs to be applied
 * @param N number of elements from index start where the activation function needs to be applied
 */
void relu_activation(float *x, int start, int N);

/**
 * @brief Function to apply linear activation function on vector
 *
 * @param x vector where the activation function is to be applied
 * @param start start index the from where activation function needs to be applied
 * @param N number of elements from index start where the activation function needs to be applied
 */
void linear_activation(float *x, int start, int N);

/**
 * @brief Function to integrate differential equations of form dot{x} = f(x, u) using runge-kutta method of order 4
 * 
 * @param fc function to be integrated. Arguments to fc should be: x0, u0, dotx.
 * @param Ts step-time
 * @param x0 state at given time
 * @param u0 control input at given time
 * @param nx size of state vector
 * @param x state at next time-step (filled by this function)
 */
void rk4_integrate(void (*fc)(float *, float *, float *), float Ts, float *x0, float *u0, const int nx, float *x);

#endif
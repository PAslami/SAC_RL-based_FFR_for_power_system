/*
Filename:       layers.h
Written by:     Niranjan Bhujel
Date:           Feb 5, 2023
Description:    Function to call layers of neural network
*/

#include "cores.h"

#ifndef layers_h
#define layers_h

/**
 * @brief Call to dense layer
 *
 * @param W weight matrix of size ny x nx
 * @param b bias vector of size ny
 * @param x input vector
 * @param y output vector
 * @param activation activation function
 * @param nx size of input
 * @param ny size of output
 */
void dense_call(float *W, float *b, float *x, float *y, void (*activation)(float *, int, int), int nx, int ny);


/**
 * @brief Call to concatenate layer
 * 
 * @param x1 first input
 * @param x2 second input
 * @param y output
 * @param nx1 size of first input
 * @param nx2 size of second input
 */
void concatenate_call(float *x1, float *x2, float *y, int nx1, int nx2);

#endif

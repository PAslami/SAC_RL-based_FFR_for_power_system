/*
Filename:       freq_model_interface.h
Written by:     Niranjan Bhujel
Date:           2022-11-01
*/

#ifndef freq_model_interface_h
#define freq_model_interface_h

#include "sim_code/freq_model.h"

void initialize(double *u, double *L, double *t_step, double *x_est, double *x);

void one_step(double *u, double *L, double *t_step, double *x_est, double *x);

#endif
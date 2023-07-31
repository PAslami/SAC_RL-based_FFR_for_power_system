/*
Filename:       freq_model_interface.c
Written by:     Niranjan Bhujel
Date:           2022-11-01
*/

#include <stdio.h>
#include "sim_code/freq_model.h"
#include "freq_model_interface.h"

#if defined(_WIN32) || defined(_WIN64)
#define EXPORT __declspec(dllexport)
#define IMPORT __declspec(dllimport)
#elif defined(__linux__)
#define EXPORT __attribute__((visibility("default")))
#define IMPORT
#else
#define EXPORT
#define IMPORT
#pragma warning Unknown dynamic link import/export semantics.
#endif

EXPORT void initialize(double *u, double *L, double *t_step, double *x_est, double *x)
{
    // freopen ("nul", "w", stdout);
    
    freq_model_U.u = u[0];
    
    freq_model_U.L = L[0];
    
    freq_model_U.t_step = t_step[0];
    
    freq_model_initialize();
    freq_model_output();
    
    for (int i = 0; i < 3; i++)
    {
        x_est[i] = freq_model_Y.x_est[i];
    }
    for (int i = 0; i < 2; i++)
    {
        x[i] = freq_model_Y.x[i];
    }
}

EXPORT void one_step(double *u, double *L, double *t_step, double *x_est, double *x)
{
    // freopen ("nul", "w", stdout);
    
    freq_model_U.u = u[0];
    
    freq_model_U.L = L[0];
    
    freq_model_U.t_step = t_step[0];
    
    freq_model_update();
    freq_model_output();
    
    for (int i = 0; i < 3; i++)
    {
        x_est[i] = freq_model_Y.x_est[i];
    }
    
    for (int i = 0; i < 2; i++)
    {
        x[i] = freq_model_Y.x[i];
    }
    
}
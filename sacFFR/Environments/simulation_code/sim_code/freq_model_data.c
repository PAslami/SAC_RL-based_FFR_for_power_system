/*
 * freq_model_data.c
 *
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * Code generation for model "freq_model".
 *
 * Model version              : 1.8
 * Simulink Coder version : 9.3 (R2020a) 18-Nov-2019
 * C source code generated on : Sun Oct 16 21:22:18 2022
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objective: Execution efficiency
 * Validation result: Not run
 */

#include "freq_model.h"
#include "freq_model_private.h"

/* Block parameters (default storage) */
P_freq_model_T freq_model_P = {
  /* Expression: 0
   * Referenced by: '<Root>/Unit Delay2'
   */
  0.0,

  /* Computed Parameter: StateSpace1_A
   * Referenced by: '<Root>/State-Space1'
   */
  { 1.0, -25.018749999999997, -5.00375 },

  /* Computed Parameter: StateSpace1_B
   * Referenced by: '<Root>/State-Space1'
   */
  1.25,

  /* Computed Parameter: StateSpace1_C
   * Referenced by: '<Root>/State-Space1'
   */
  { 1.0, 1.0 },

  /* Expression: 0
   * Referenced by: '<Root>/State-Space1'
   */
  0.0,

  /* Expression: 0
   * Referenced by: '<Root>/Unit Delay1'
   */
  0.0,

  /* Expression: 1*diag([1, 1, 1])
   * Referenced by: '<Root>/Unit Delay'
   */
  { 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0 },

  /* Expression: 1e-8
   * Referenced by: '<Root>/Constant4'
   */
  1.0E-8,

  /* Expression: 1e-8
   * Referenced by: '<Root>/Constant5'
   */
  1.0E-8,

  /* Expression: 1e-2
   * Referenced by: '<Root>/Constant6'
   */
  0.01,

  /* Expression: 1e-8
   * Referenced by: '<Root>/Constant7'
   */
  1.0E-8,

  /* Computed Parameter: TransferFcn14_A
   * Referenced by: '<Root>/Transfer Fcn14'
   */
  -5.0,

  /* Computed Parameter: TransferFcn14_C
   * Referenced by: '<Root>/Transfer Fcn14'
   */
  5.0,

  /* Expression: 1
   * Referenced by: '<Root>/Constant'
   */
  1.0,

  /* Computed Parameter: TransferFcn1_A
   * Referenced by: '<Root>/Transfer Fcn1'
   */
  -0.0,

  /* Computed Parameter: TransferFcn1_C
   * Referenced by: '<Root>/Transfer Fcn1'
   */
  -1.8
};

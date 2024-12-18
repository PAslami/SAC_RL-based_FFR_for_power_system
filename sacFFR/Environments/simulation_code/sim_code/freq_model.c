/*
 * freq_model.c
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

/* Block signals (default storage) */
B_freq_model_T freq_model_B;

/* Continuous states */
X_freq_model_T freq_model_X;

/* Block states (default storage) */
DW_freq_model_T freq_model_DW;

/* External inputs (root inport signals with default storage) */
ExtU_freq_model_T freq_model_U;

/* External outputs (root outports fed by signals with default storage) */
ExtY_freq_model_T freq_model_Y;

/* Real-time model */
RT_MODEL_freq_model_T freq_model_M_;
RT_MODEL_freq_model_T *const freq_model_M = &freq_model_M_;

/*
 * This function updates continuous states using the ODE4 fixed-step
 * solver algorithm
 */
static void rt_ertODEUpdateContinuousStates(RTWSolverInfo *si )
{
  time_T t = rtsiGetT(si);
  time_T tnew = rtsiGetSolverStopTime(si);
  time_T h = rtsiGetStepSize(si);
  real_T *x = rtsiGetContStates(si);
  ODE4_IntgData *id = (ODE4_IntgData *)rtsiGetSolverData(si);
  real_T *y = id->y;
  real_T *f0 = id->f[0];
  real_T *f1 = id->f[1];
  real_T *f2 = id->f[2];
  real_T *f3 = id->f[3];
  real_T temp;
  int_T i;
  int_T nXc = 4;
  rtsiSetSimTimeStep(si,MINOR_TIME_STEP);

  /* Save the state values at time t in y, we'll use x as ynew. */
  (void) memcpy(y, x,
                (uint_T)nXc*sizeof(real_T));

  /* Assumes that rtsiSetT and ModelOutputs are up-to-date */
  /* f0 = f(t,y) */
  rtsiSetdX(si, f0);
  freq_model_derivatives();

  /* f1 = f(t + (h/2), y + (h/2)*f0) */
  temp = 0.5 * h;
  for (i = 0; i < nXc; i++) {
    x[i] = y[i] + (temp*f0[i]);
  }

  rtsiSetT(si, t + temp);
  rtsiSetdX(si, f1);
  freq_model_output();
  freq_model_derivatives();

  /* f2 = f(t + (h/2), y + (h/2)*f1) */
  for (i = 0; i < nXc; i++) {
    x[i] = y[i] + (temp*f1[i]);
  }

  rtsiSetdX(si, f2);
  freq_model_output();
  freq_model_derivatives();

  /* f3 = f(t + h, y + h*f2) */
  for (i = 0; i < nXc; i++) {
    x[i] = y[i] + (h*f2[i]);
  }

  rtsiSetT(si, tnew);
  rtsiSetdX(si, f3);
  freq_model_output();
  freq_model_derivatives();

  /* tnew = t + h
     ynew = y + (h/6)*(f0 + 2*f1 + 2*f2 + 2*f3) */
  temp = h / 6.0;
  for (i = 0; i < nXc; i++) {
    x[i] = y[i] + temp*(f0[i] + 2.0*f1[i] + 2.0*f2[i] + f3[i]);
  }

  rtsiSetSimTimeStep(si,MAJOR_TIME_STEP);
}

/* Model output function */
void freq_model_output(void)
{
  real_T tmp;
  if (rtmIsMajorTimeStep(freq_model_M)) {
    /* set solver stop time */
    if (!(freq_model_M->Timing.clockTick0+1)) {
      rtsiSetSolverStopTime(&freq_model_M->solverInfo,
                            ((freq_model_M->Timing.clockTickH0 + 1) *
        freq_model_M->Timing.stepSize0 * 4294967296.0));
    } else {
      rtsiSetSolverStopTime(&freq_model_M->solverInfo,
                            ((freq_model_M->Timing.clockTick0 + 1) *
        freq_model_M->Timing.stepSize0 + freq_model_M->Timing.clockTickH0 *
        freq_model_M->Timing.stepSize0 * 4294967296.0));
    }
  }                                    /* end MajorTimeStep */

  /* Update absolute time of base rate at minor time step */
  if (rtmIsMinorTimeStep(freq_model_M)) {
    freq_model_M->Timing.t[0] = rtsiGetT(&freq_model_M->solverInfo);
  }

  /* StateSpace: '<Root>/State-Space1' */
  freq_model_B.StateSpace1[0] = 0.0;
  freq_model_B.StateSpace1[1] = 0.0;
  freq_model_B.StateSpace1[0] += freq_model_P.StateSpace1_C[0] *
    freq_model_X.StateSpace1_CSTATE[0];
  freq_model_B.StateSpace1[1] += freq_model_P.StateSpace1_C[1] *
    freq_model_X.StateSpace1_CSTATE[1];
  if (rtmIsMajorTimeStep(freq_model_M)) {
    /* UnitDelay: '<Root>/Unit Delay2' */
    freq_model_B.UnitDelay2 = freq_model_DW.UnitDelay2_DSTATE;

    /* UnitDelay: '<Root>/Unit Delay1' */
    freq_model_B.UnitDelay1[0] = freq_model_DW.UnitDelay1_DSTATE[0];
    freq_model_B.UnitDelay1[1] = freq_model_DW.UnitDelay1_DSTATE[1];
    freq_model_B.UnitDelay1[2] = freq_model_DW.UnitDelay1_DSTATE[2];

    /* UnitDelay: '<Root>/Unit Delay' */
    memcpy(&freq_model_B.UnitDelay[0], &freq_model_DW.UnitDelay_DSTATE[0], 9U *
           sizeof(real_T));

    /* S-Function (KF_Sfun): '<Root>/S-Function Builder' incorporates:
     *  Constant: '<Root>/Constant4'
     *  Constant: '<Root>/Constant5'
     *  Constant: '<Root>/Constant6'
     *  Constant: '<Root>/Constant7'
     *  Outport: '<Root>/x_est'
     */
    KF_Sfun_Outputs_wrapper(&freq_model_B.UnitDelay2, &freq_model_B.StateSpace1
      [0], &freq_model_B.UnitDelay1[0], &freq_model_B.UnitDelay[0],
      &freq_model_P.Constant4_Value, &freq_model_P.Constant5_Value,
      &freq_model_P.Constant6_Value, &freq_model_P.Constant7_Value,
      &freq_model_Y.x_est[0], &freq_model_B.SFunctionBuilder_o2[0]);
  }

  /* Outport: '<Root>/x' */
  freq_model_Y.x[0] = freq_model_B.StateSpace1[0];
  freq_model_Y.x[1] = freq_model_B.StateSpace1[1];
  if (rtmIsMajorTimeStep(freq_model_M)) {
  }

  /* MATLAB Function: '<Root>/MATLAB Function' incorporates:
   *  Clock: '<Root>/Clock'
   *  Constant: '<Root>/Constant'
   *  Inport: '<Root>/L'
   */
  if (freq_model_M->Timing.t[0] >= freq_model_P.Constant_Value) {
    tmp = freq_model_U.L;
  } else {
    tmp = 0.0;
  }

  /* End of MATLAB Function: '<Root>/MATLAB Function' */

  /* Sum: '<Root>/Add1' incorporates:
   *  Inport: '<Root>/u'
   *  TransferFcn: '<Root>/Transfer Fcn14'
   */
  freq_model_B.Add1 = (freq_model_P.TransferFcn14_C *
                       freq_model_X.TransferFcn14_CSTATE + freq_model_U.u) - tmp;

  /* TransferFcn: '<Root>/Transfer Fcn1' */
  freq_model_B.TransferFcn1 = 0.0;
  freq_model_B.TransferFcn1 += freq_model_P.TransferFcn1_C *
    freq_model_X.TransferFcn1_CSTATE;
}

/* Model update function */
void freq_model_update(void)
{
  if (rtmIsMajorTimeStep(freq_model_M)) {
    /* Update for UnitDelay: '<Root>/Unit Delay2' incorporates:
     *  Inport: '<Root>/u'
     */
    freq_model_DW.UnitDelay2_DSTATE = freq_model_U.u;

    /* Update for UnitDelay: '<Root>/Unit Delay1' incorporates:
     *  Outport: '<Root>/x_est'
     */
    freq_model_DW.UnitDelay1_DSTATE[0] = freq_model_Y.x_est[0];
    freq_model_DW.UnitDelay1_DSTATE[1] = freq_model_Y.x_est[1];
    freq_model_DW.UnitDelay1_DSTATE[2] = freq_model_Y.x_est[2];

    /* Update for UnitDelay: '<Root>/Unit Delay' */
    memcpy(&freq_model_DW.UnitDelay_DSTATE[0],
           &freq_model_B.SFunctionBuilder_o2[0], 9U * sizeof(real_T));
  }

  /* signal main to stop simulation */
  {                                    /* Sample time: [0.0s, 0.0s] */
    if ((rtmGetTFinal(freq_model_M)!=-1) &&
        !((rtmGetTFinal(freq_model_M)-(((freq_model_M->Timing.clockTick1+
             freq_model_M->Timing.clockTickH1* 4294967296.0)) * 0.02)) >
          (((freq_model_M->Timing.clockTick1+freq_model_M->Timing.clockTickH1*
             4294967296.0)) * 0.02) * (DBL_EPSILON))) {
      rtmSetErrorStatus(freq_model_M, "Simulation finished");
    }
  }

  if (rtmIsMajorTimeStep(freq_model_M)) {
    rt_ertODEUpdateContinuousStates(&freq_model_M->solverInfo);
  }

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++freq_model_M->Timing.clockTick0)) {
    ++freq_model_M->Timing.clockTickH0;
  }

  freq_model_M->Timing.t[0] = rtsiGetSolverStopTime(&freq_model_M->solverInfo);

  {
    /* Update absolute timer for sample time: [0.02s, 0.0s] */
    /* The "clockTick1" counts the number of times the code of this task has
     * been executed. The resolution of this integer timer is 0.02, which is the step size
     * of the task. Size of "clockTick1" ensures timer will not overflow during the
     * application lifespan selected.
     * Timer of this task consists of two 32 bit unsigned integers.
     * The two integers represent the low bits Timing.clockTick1 and the high bits
     * Timing.clockTickH1. When the low bit overflows to 0, the high bits increment.
     */
    freq_model_M->Timing.clockTick1++;
    if (!freq_model_M->Timing.clockTick1) {
      freq_model_M->Timing.clockTickH1++;
    }
  }
}

/* Derivatives for root system: '<Root>' */
void freq_model_derivatives(void)
{
  XDot_freq_model_T *_rtXdot;
  _rtXdot = ((XDot_freq_model_T *) freq_model_M->derivs);

  /* Derivatives for StateSpace: '<Root>/State-Space1' */
  _rtXdot->StateSpace1_CSTATE[0] = 0.0;
  _rtXdot->StateSpace1_CSTATE[1] = 0.0;
  _rtXdot->StateSpace1_CSTATE[0] += freq_model_P.StateSpace1_A[0] *
    freq_model_X.StateSpace1_CSTATE[1];
  _rtXdot->StateSpace1_CSTATE[1] += freq_model_P.StateSpace1_A[1] *
    freq_model_X.StateSpace1_CSTATE[0];
  _rtXdot->StateSpace1_CSTATE[1] += freq_model_P.StateSpace1_A[2] *
    freq_model_X.StateSpace1_CSTATE[1];
  _rtXdot->StateSpace1_CSTATE[1] += freq_model_P.StateSpace1_B *
    freq_model_B.Add1;

  /* Derivatives for TransferFcn: '<Root>/Transfer Fcn14' */
  _rtXdot->TransferFcn14_CSTATE = 0.0;
  _rtXdot->TransferFcn14_CSTATE += freq_model_P.TransferFcn14_A *
    freq_model_X.TransferFcn14_CSTATE;
  _rtXdot->TransferFcn14_CSTATE += freq_model_B.TransferFcn1;

  /* Derivatives for TransferFcn: '<Root>/Transfer Fcn1' */
  _rtXdot->TransferFcn1_CSTATE = 0.0;
  _rtXdot->TransferFcn1_CSTATE += freq_model_P.TransferFcn1_A *
    freq_model_X.TransferFcn1_CSTATE;
  _rtXdot->TransferFcn1_CSTATE += freq_model_B.StateSpace1[0];
}

/* Model initialize function */
void freq_model_initialize(void)
{
  /* Registration code */

  /* initialize non-finites */
  rt_InitInfAndNaN(sizeof(real_T));

  /* initialize real-time model */
  (void) memset((void *)freq_model_M, 0,
                sizeof(RT_MODEL_freq_model_T));

  {
    /* Setup solver object */
    rtsiSetSimTimeStepPtr(&freq_model_M->solverInfo,
                          &freq_model_M->Timing.simTimeStep);
    rtsiSetTPtr(&freq_model_M->solverInfo, &rtmGetTPtr(freq_model_M));
    rtsiSetStepSizePtr(&freq_model_M->solverInfo,
                       &freq_model_M->Timing.stepSize0);
    rtsiSetdXPtr(&freq_model_M->solverInfo, &freq_model_M->derivs);
    rtsiSetContStatesPtr(&freq_model_M->solverInfo, (real_T **)
                         &freq_model_M->contStates);
    rtsiSetNumContStatesPtr(&freq_model_M->solverInfo,
      &freq_model_M->Sizes.numContStates);
    rtsiSetNumPeriodicContStatesPtr(&freq_model_M->solverInfo,
      &freq_model_M->Sizes.numPeriodicContStates);
    rtsiSetPeriodicContStateIndicesPtr(&freq_model_M->solverInfo,
      &freq_model_M->periodicContStateIndices);
    rtsiSetPeriodicContStateRangesPtr(&freq_model_M->solverInfo,
      &freq_model_M->periodicContStateRanges);
    rtsiSetErrorStatusPtr(&freq_model_M->solverInfo, (&rtmGetErrorStatus
      (freq_model_M)));
    rtsiSetRTModelPtr(&freq_model_M->solverInfo, freq_model_M);
  }

  rtsiSetSimTimeStep(&freq_model_M->solverInfo, MAJOR_TIME_STEP);
  freq_model_M->intgData.y = freq_model_M->odeY;
  freq_model_M->intgData.f[0] = freq_model_M->odeF[0];
  freq_model_M->intgData.f[1] = freq_model_M->odeF[1];
  freq_model_M->intgData.f[2] = freq_model_M->odeF[2];
  freq_model_M->intgData.f[3] = freq_model_M->odeF[3];
  freq_model_M->contStates = ((X_freq_model_T *) &freq_model_X);
  rtsiSetSolverData(&freq_model_M->solverInfo, (void *)&freq_model_M->intgData);
  rtsiSetSolverName(&freq_model_M->solverInfo,"ode4");
  rtmSetTPtr(freq_model_M, &freq_model_M->Timing.tArray[0]);
  rtmSetTFinal(freq_model_M, 50.0);
  freq_model_M->Timing.stepSize0 = 0.02;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    rt_DataLoggingInfo.loggingInterval = NULL;
    freq_model_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(freq_model_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(freq_model_M->rtwLogInfo, (NULL));
    rtliSetLogT(freq_model_M->rtwLogInfo, "tout");
    rtliSetLogX(freq_model_M->rtwLogInfo, "");
    rtliSetLogXFinal(freq_model_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(freq_model_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(freq_model_M->rtwLogInfo, 4);
    rtliSetLogMaxRows(freq_model_M->rtwLogInfo, 0);
    rtliSetLogDecimation(freq_model_M->rtwLogInfo, 1);
    rtliSetLogY(freq_model_M->rtwLogInfo, "");
    rtliSetLogYSignalInfo(freq_model_M->rtwLogInfo, (NULL));
    rtliSetLogYSignalPtrs(freq_model_M->rtwLogInfo, (NULL));
  }

  /* block I/O */
  (void) memset(((void *) &freq_model_B), 0,
                sizeof(B_freq_model_T));

  /* states (continuous) */
  {
    (void) memset((void *)&freq_model_X, 0,
                  sizeof(X_freq_model_T));
  }

  /* states (dwork) */
  (void) memset((void *)&freq_model_DW, 0,
                sizeof(DW_freq_model_T));

  /* external inputs */
  (void)memset(&freq_model_U, 0, sizeof(ExtU_freq_model_T));

  /* external outputs */
  (void) memset((void *)&freq_model_Y, 0,
                sizeof(ExtY_freq_model_T));

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(freq_model_M->rtwLogInfo, 0.0, rtmGetTFinal
    (freq_model_M), freq_model_M->Timing.stepSize0, (&rtmGetErrorStatus
    (freq_model_M)));

  /* InitializeConditions for UnitDelay: '<Root>/Unit Delay2' */
  freq_model_DW.UnitDelay2_DSTATE = freq_model_P.UnitDelay2_InitialCondition;

  /* InitializeConditions for StateSpace: '<Root>/State-Space1' */
  freq_model_X.StateSpace1_CSTATE[0] = freq_model_P.StateSpace1_InitialCondition;
  freq_model_X.StateSpace1_CSTATE[1] = freq_model_P.StateSpace1_InitialCondition;

  /* InitializeConditions for UnitDelay: '<Root>/Unit Delay1' */
  freq_model_DW.UnitDelay1_DSTATE[0] = freq_model_P.UnitDelay1_InitialCondition;
  freq_model_DW.UnitDelay1_DSTATE[1] = freq_model_P.UnitDelay1_InitialCondition;
  freq_model_DW.UnitDelay1_DSTATE[2] = freq_model_P.UnitDelay1_InitialCondition;

  /* InitializeConditions for UnitDelay: '<Root>/Unit Delay' */
  memcpy(&freq_model_DW.UnitDelay_DSTATE[0],
         &freq_model_P.UnitDelay_InitialCondition[0], 9U * sizeof(real_T));

  /* InitializeConditions for TransferFcn: '<Root>/Transfer Fcn14' */
  freq_model_X.TransferFcn14_CSTATE = 0.0;

  /* InitializeConditions for TransferFcn: '<Root>/Transfer Fcn1' */
  freq_model_X.TransferFcn1_CSTATE = 0.0;
}

/* Model terminate function */
void freq_model_terminate(void)
{
  /* (no terminate code required) */
}

/*
 * freq_model.h
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

#ifndef RTW_HEADER_freq_model_h_
#define RTW_HEADER_freq_model_h_
#include <string.h>
#include <float.h>
#include <stddef.h>
#ifndef freq_model_COMMON_INCLUDES_
# define freq_model_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "rtw_continuous.h"
#include "rtw_solver.h"
#include "rt_logging.h"
#endif                                 /* freq_model_COMMON_INCLUDES_ */

#include "freq_model_types.h"

/* Shared type includes */
#include "multiword_types.h"
#include "rt_nonfinite.h"

/* Macros for accessing real-time model data structure */
#ifndef rtmGetContStateDisabled
# define rtmGetContStateDisabled(rtm)  ((rtm)->contStateDisabled)
#endif

#ifndef rtmSetContStateDisabled
# define rtmSetContStateDisabled(rtm, val) ((rtm)->contStateDisabled = (val))
#endif

#ifndef rtmGetContStates
# define rtmGetContStates(rtm)         ((rtm)->contStates)
#endif

#ifndef rtmSetContStates
# define rtmSetContStates(rtm, val)    ((rtm)->contStates = (val))
#endif

#ifndef rtmGetContTimeOutputInconsistentWithStateAtMajorStepFlag
# define rtmGetContTimeOutputInconsistentWithStateAtMajorStepFlag(rtm) ((rtm)->CTOutputIncnstWithState)
#endif

#ifndef rtmSetContTimeOutputInconsistentWithStateAtMajorStepFlag
# define rtmSetContTimeOutputInconsistentWithStateAtMajorStepFlag(rtm, val) ((rtm)->CTOutputIncnstWithState = (val))
#endif

#ifndef rtmGetDerivCacheNeedsReset
# define rtmGetDerivCacheNeedsReset(rtm) ((rtm)->derivCacheNeedsReset)
#endif

#ifndef rtmSetDerivCacheNeedsReset
# define rtmSetDerivCacheNeedsReset(rtm, val) ((rtm)->derivCacheNeedsReset = (val))
#endif

#ifndef rtmGetFinalTime
# define rtmGetFinalTime(rtm)          ((rtm)->Timing.tFinal)
#endif

#ifndef rtmGetIntgData
# define rtmGetIntgData(rtm)           ((rtm)->intgData)
#endif

#ifndef rtmSetIntgData
# define rtmSetIntgData(rtm, val)      ((rtm)->intgData = (val))
#endif

#ifndef rtmGetOdeF
# define rtmGetOdeF(rtm)               ((rtm)->odeF)
#endif

#ifndef rtmSetOdeF
# define rtmSetOdeF(rtm, val)          ((rtm)->odeF = (val))
#endif

#ifndef rtmGetOdeY
# define rtmGetOdeY(rtm)               ((rtm)->odeY)
#endif

#ifndef rtmSetOdeY
# define rtmSetOdeY(rtm, val)          ((rtm)->odeY = (val))
#endif

#ifndef rtmGetPeriodicContStateIndices
# define rtmGetPeriodicContStateIndices(rtm) ((rtm)->periodicContStateIndices)
#endif

#ifndef rtmSetPeriodicContStateIndices
# define rtmSetPeriodicContStateIndices(rtm, val) ((rtm)->periodicContStateIndices = (val))
#endif

#ifndef rtmGetPeriodicContStateRanges
# define rtmGetPeriodicContStateRanges(rtm) ((rtm)->periodicContStateRanges)
#endif

#ifndef rtmSetPeriodicContStateRanges
# define rtmSetPeriodicContStateRanges(rtm, val) ((rtm)->periodicContStateRanges = (val))
#endif

#ifndef rtmGetRTWLogInfo
# define rtmGetRTWLogInfo(rtm)         ((rtm)->rtwLogInfo)
#endif

#ifndef rtmGetZCCacheNeedsReset
# define rtmGetZCCacheNeedsReset(rtm)  ((rtm)->zCCacheNeedsReset)
#endif

#ifndef rtmSetZCCacheNeedsReset
# define rtmSetZCCacheNeedsReset(rtm, val) ((rtm)->zCCacheNeedsReset = (val))
#endif

#ifndef rtmGetdX
# define rtmGetdX(rtm)                 ((rtm)->derivs)
#endif

#ifndef rtmSetdX
# define rtmSetdX(rtm, val)            ((rtm)->derivs = (val))
#endif

#ifndef rtmGetErrorStatus
# define rtmGetErrorStatus(rtm)        ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
# define rtmSetErrorStatus(rtm, val)   ((rtm)->errorStatus = (val))
#endif

#ifndef rtmGetStopRequested
# define rtmGetStopRequested(rtm)      ((rtm)->Timing.stopRequestedFlag)
#endif

#ifndef rtmSetStopRequested
# define rtmSetStopRequested(rtm, val) ((rtm)->Timing.stopRequestedFlag = (val))
#endif

#ifndef rtmGetStopRequestedPtr
# define rtmGetStopRequestedPtr(rtm)   (&((rtm)->Timing.stopRequestedFlag))
#endif

#ifndef rtmGetT
# define rtmGetT(rtm)                  (rtmGetTPtr((rtm))[0])
#endif

#ifndef rtmGetTFinal
# define rtmGetTFinal(rtm)             ((rtm)->Timing.tFinal)
#endif

#ifndef rtmGetTPtr
# define rtmGetTPtr(rtm)               ((rtm)->Timing.t)
#endif

/* Block signals (default storage) */
typedef struct {
  real_T UnitDelay2;                   /* '<Root>/Unit Delay2' */
  real_T StateSpace1[2];               /* '<Root>/State-Space1' */
  real_T UnitDelay1[3];                /* '<Root>/Unit Delay1' */
  real_T UnitDelay[9];                 /* '<Root>/Unit Delay' */
  real_T SFunctionBuilder_o2[9];       /* '<Root>/S-Function Builder' */
  real_T Add1;                         /* '<Root>/Add1' */
  real_T TransferFcn1;                 /* '<Root>/Transfer Fcn1' */
} B_freq_model_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  real_T UnitDelay2_DSTATE;            /* '<Root>/Unit Delay2' */
  real_T UnitDelay1_DSTATE[3];         /* '<Root>/Unit Delay1' */
  real_T UnitDelay_DSTATE[9];          /* '<Root>/Unit Delay' */
} DW_freq_model_T;

/* Continuous states (default storage) */
typedef struct {
  real_T StateSpace1_CSTATE[2];        /* '<Root>/State-Space1' */
  real_T TransferFcn14_CSTATE;         /* '<Root>/Transfer Fcn14' */
  real_T TransferFcn1_CSTATE;          /* '<Root>/Transfer Fcn1' */
} X_freq_model_T;

/* State derivatives (default storage) */
typedef struct {
  real_T StateSpace1_CSTATE[2];        /* '<Root>/State-Space1' */
  real_T TransferFcn14_CSTATE;         /* '<Root>/Transfer Fcn14' */
  real_T TransferFcn1_CSTATE;          /* '<Root>/Transfer Fcn1' */
} XDot_freq_model_T;

/* State disabled  */
typedef struct {
  boolean_T StateSpace1_CSTATE[2];     /* '<Root>/State-Space1' */
  boolean_T TransferFcn14_CSTATE;      /* '<Root>/Transfer Fcn14' */
  boolean_T TransferFcn1_CSTATE;       /* '<Root>/Transfer Fcn1' */
} XDis_freq_model_T;

#ifndef ODE4_INTG
#define ODE4_INTG

/* ODE4 Integration Data */
typedef struct {
  real_T *y;                           /* output */
  real_T *f[4];                        /* derivatives */
} ODE4_IntgData;

#endif

/* External inputs (root inport signals with default storage) */
typedef struct {
  real_T u;                            /* '<Root>/u' */
  real_T L;                            /* '<Root>/L' */
} ExtU_freq_model_T;

/* External outputs (root outports fed by signals with default storage) */
typedef struct {
  real_T x_est[3];                     /* '<Root>/x_est' */
  real_T x[2];                         /* '<Root>/x' */
} ExtY_freq_model_T;

/* Parameters (default storage) */
struct P_freq_model_T_ {
  real_T UnitDelay2_InitialCondition;  /* Expression: 0
                                        * Referenced by: '<Root>/Unit Delay2'
                                        */
  real_T StateSpace1_A[3];             /* Computed Parameter: StateSpace1_A
                                        * Referenced by: '<Root>/State-Space1'
                                        */
  real_T StateSpace1_B;                /* Computed Parameter: StateSpace1_B
                                        * Referenced by: '<Root>/State-Space1'
                                        */
  real_T StateSpace1_C[2];             /* Computed Parameter: StateSpace1_C
                                        * Referenced by: '<Root>/State-Space1'
                                        */
  real_T StateSpace1_InitialCondition; /* Expression: 0
                                        * Referenced by: '<Root>/State-Space1'
                                        */
  real_T UnitDelay1_InitialCondition;  /* Expression: 0
                                        * Referenced by: '<Root>/Unit Delay1'
                                        */
  real_T UnitDelay_InitialCondition[9];/* Expression: 1*diag([1, 1, 1])
                                        * Referenced by: '<Root>/Unit Delay'
                                        */
  real_T Constant4_Value;              /* Expression: 1e-8
                                        * Referenced by: '<Root>/Constant4'
                                        */
  real_T Constant5_Value;              /* Expression: 1e-8
                                        * Referenced by: '<Root>/Constant5'
                                        */
  real_T Constant6_Value;              /* Expression: 1e-2
                                        * Referenced by: '<Root>/Constant6'
                                        */
  real_T Constant7_Value;              /* Expression: 1e-8
                                        * Referenced by: '<Root>/Constant7'
                                        */
  real_T TransferFcn14_A;              /* Computed Parameter: TransferFcn14_A
                                        * Referenced by: '<Root>/Transfer Fcn14'
                                        */
  real_T TransferFcn14_C;              /* Computed Parameter: TransferFcn14_C
                                        * Referenced by: '<Root>/Transfer Fcn14'
                                        */
  real_T Constant_Value;               /* Expression: 1
                                        * Referenced by: '<Root>/Constant'
                                        */
  real_T TransferFcn1_A;               /* Computed Parameter: TransferFcn1_A
                                        * Referenced by: '<Root>/Transfer Fcn1'
                                        */
  real_T TransferFcn1_C;               /* Computed Parameter: TransferFcn1_C
                                        * Referenced by: '<Root>/Transfer Fcn1'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_freq_model_T {
  const char_T *errorStatus;
  RTWLogInfo *rtwLogInfo;
  RTWSolverInfo solverInfo;
  X_freq_model_T *contStates;
  int_T *periodicContStateIndices;
  real_T *periodicContStateRanges;
  real_T *derivs;
  boolean_T *contStateDisabled;
  boolean_T zCCacheNeedsReset;
  boolean_T derivCacheNeedsReset;
  boolean_T CTOutputIncnstWithState;
  real_T odeY[4];
  real_T odeF[4][4];
  ODE4_IntgData intgData;

  /*
   * Sizes:
   * The following substructure contains sizes information
   * for many of the model attributes such as inputs, outputs,
   * dwork, sample times, etc.
   */
  struct {
    int_T numContStates;
    int_T numPeriodicContStates;
    int_T numSampTimes;
  } Sizes;

  /*
   * Timing:
   * The following substructure contains information regarding
   * the timing information for the model.
   */
  struct {
    uint32_T clockTick0;
    uint32_T clockTickH0;
    time_T stepSize0;
    uint32_T clockTick1;
    uint32_T clockTickH1;
    time_T tFinal;
    SimTimeStep simTimeStep;
    boolean_T stopRequestedFlag;
    time_T *t;
    time_T tArray[2];
  } Timing;
};

/* Block parameters (default storage) */
extern P_freq_model_T freq_model_P;

/* Block signals (default storage) */
extern B_freq_model_T freq_model_B;

/* Continuous states (default storage) */
extern X_freq_model_T freq_model_X;

/* Block states (default storage) */
extern DW_freq_model_T freq_model_DW;

/* External inputs (root inport signals with default storage) */
extern ExtU_freq_model_T freq_model_U;

/* External outputs (root outports fed by signals with default storage) */
extern ExtY_freq_model_T freq_model_Y;

/* Model entry point functions */
extern void freq_model_initialize(void);
extern void freq_model_output(void);
extern void freq_model_update(void);
extern void freq_model_terminate(void);

/* Real-time Model object */
extern RT_MODEL_freq_model_T *const freq_model_M;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'freq_model'
 * '<S1>'   : 'freq_model/MATLAB Function'
 */
#endif                                 /* RTW_HEADER_freq_model_h_ */

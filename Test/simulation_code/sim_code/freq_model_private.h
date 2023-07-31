/*
 * freq_model_private.h
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

#ifndef RTW_HEADER_freq_model_private_h_
#define RTW_HEADER_freq_model_private_h_
#include "rtwtypes.h"
#include "builtin_typeid_types.h"
#include "multiword_types.h"

/* Private macros used by the generated code to access rtModel */
#ifndef rtmIsMajorTimeStep
# define rtmIsMajorTimeStep(rtm)       (((rtm)->Timing.simTimeStep) == MAJOR_TIME_STEP)
#endif

#ifndef rtmIsMinorTimeStep
# define rtmIsMinorTimeStep(rtm)       (((rtm)->Timing.simTimeStep) == MINOR_TIME_STEP)
#endif

#ifndef rtmSetTFinal
# define rtmSetTFinal(rtm, val)        ((rtm)->Timing.tFinal = (val))
#endif

#ifndef rtmSetTPtr
# define rtmSetTPtr(rtm, val)          ((rtm)->Timing.t = (val))
#endif

#ifdef __cplusplus

extern "C" {

#endif

  extern void KF_Sfun_Start_wrapper(void);
  extern void KF_Sfun_Outputs_wrapper(const real_T *u,
    const real_T *y,
    const real_T *xhatp,
    const real_T *Pkp,
    const real_T *Q11,
    const real_T *Q22,
    const real_T *Q33,
    const real_T *R,
    real_T *xhat,
    real_T *Phat);
  extern void KF_Sfun_Terminate_wrapper(void);

#ifdef __cplusplus

}
#endif

/* private model entry point functions */
extern void freq_model_derivatives(void);

#endif                                 /* RTW_HEADER_freq_model_private_h_ */

/* This file was automatically generated by CasADi.
   The CasADi copyright holders make no ownership claim of its contents. */
#ifdef __cplusplus
extern "C" {
#endif

/* How to prefix internal symbols */
#ifdef CASADI_CODEGEN_PREFIX
  #define CASADI_NAMESPACE_CONCAT(NS, ID) _CASADI_NAMESPACE_CONCAT(NS, ID)
  #define _CASADI_NAMESPACE_CONCAT(NS, ID) NS ## ID
  #define CASADI_PREFIX(ID) CASADI_NAMESPACE_CONCAT(CODEGEN_PREFIX, ID)
#else
  #define CASADI_PREFIX(ID) EKF_Func_ ## ID
#endif

#include <math.h>

#ifndef casadi_real
#define casadi_real double
#endif

#ifndef casadi_int
#define casadi_int long long int
#endif

/* Add prefix to internal symbols */
#define casadi_f0 CASADI_PREFIX(f0)
#define casadi_s0 CASADI_PREFIX(s0)
#define casadi_s1 CASADI_PREFIX(s1)
#define casadi_s2 CASADI_PREFIX(s2)

/* Symbol visibility in DLLs */
#ifndef CASADI_SYMBOL_EXPORT
  #if defined(_WIN32) || defined(__WIN32__) || defined(__CYGWIN__)
    #if defined(STATIC_LINKED)
      #define CASADI_SYMBOL_EXPORT
    #else
      #define CASADI_SYMBOL_EXPORT __declspec(dllexport)
    #endif
  #elif defined(__GNUC__) && defined(GCC_HASCLASSVISIBILITY)
    #define CASADI_SYMBOL_EXPORT __attribute__ ((visibility ("default")))
  #else
    #define CASADI_SYMBOL_EXPORT
  #endif
#endif

static const casadi_int casadi_s0[5] = {1, 1, 0, 1, 0};
static const casadi_int casadi_s1[7] = {3, 1, 0, 3, 0, 1, 2};
static const casadi_int casadi_s2[15] = {3, 3, 0, 3, 6, 9, 0, 1, 2, 0, 1, 2, 0, 1, 2};

/* EKF_Func:(u,y,xhatp[3],Pkp[3x3],Q11,Q22,Q33,R)->(xhat[3],Phat[3x3]) */
static int casadi_f0(const casadi_real** arg, casadi_real** res, casadi_int* iw, casadi_real* w, int mem) {
  casadi_real a0, a1, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a2, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a3, a30, a31, a32, a33, a34, a35, a4, a5, a6, a7, a8, a9;
  a0=arg[2]? arg[2][0] : 0;
  a1=3.3333333333333335e-003;
  a2=arg[2]? arg[2][1] : 0;
  a3=2.;
  a4=1.0000000000000000e-002;
  a5=-2.6874999999999996e+001;
  a6=(a5*a0);
  a7=5.3750000000000000e+000;
  a8=(a7*a2);
  a6=(a6-a8);
  a8=1.2500000000000000e+000;
  a9=arg[2]? arg[2][2] : 0;
  a10=arg[0]? arg[0][0] : 0;
  a11=(a9-a10);
  a11=(a8*a11);
  a6=(a6-a11);
  a11=(a4*a6);
  a11=(a2+a11);
  a12=(a3*a11);
  a12=(a2+a12);
  a13=(a4*a2);
  a13=(a0+a13);
  a13=(a5*a13);
  a14=(a7*a11);
  a13=(a13-a14);
  a14=(a9-a10);
  a14=(a8*a14);
  a13=(a13-a14);
  a14=(a4*a13);
  a14=(a2+a14);
  a15=(a3*a14);
  a12=(a12+a15);
  a15=2.0000000000000000e-002;
  a4=(a4*a11);
  a4=(a0+a4);
  a4=(a5*a4);
  a11=(a7*a14);
  a4=(a4-a11);
  a11=(a9-a10);
  a11=(a8*a11);
  a4=(a4-a11);
  a11=(a15*a4);
  a11=(a2+a11);
  a12=(a12+a11);
  a12=(a1*a12);
  a12=(a0+a12);
  a16=9.9481724303385421e-001;
  a17=arg[3]? arg[3][0] : 0;
  a18=(a16*a17);
  a19=1.8928578294270835e-002;
  a20=arg[3]? arg[3][1] : 0;
  a21=(a19*a20);
  a18=(a18+a21);
  a21=-2.4105846354166669e-004;
  a22=arg[3]? arg[3][2] : 0;
  a23=(a21*a22);
  a18=(a18+a23);
  a23=(a16*a18);
  a24=arg[3]? arg[3][3] : 0;
  a25=(a16*a24);
  a26=arg[3]? arg[3][4] : 0;
  a27=(a19*a26);
  a25=(a25+a27);
  a27=arg[3]? arg[3][5] : 0;
  a28=(a21*a27);
  a25=(a25+a28);
  a28=(a19*a25);
  a23=(a23+a28);
  a28=arg[3]? arg[3][6] : 0;
  a29=(a16*a28);
  a30=arg[3]? arg[3][7] : 0;
  a31=(a19*a30);
  a29=(a29+a31);
  a31=arg[3]? arg[3][8] : 0;
  a32=(a21*a31);
  a29=(a29+a32);
  a32=(a21*a29);
  a23=(a23+a32);
  a32=arg[4]? arg[4][0] : 0;
  a23=(a23+a32);
  a32=arg[7]? arg[7][0] : 0;
  a32=(a23+a32);
  a33=(a23/a32);
  a34=arg[1]? arg[1][0] : 0;
  a34=(a34-a12);
  a35=(a33*a34);
  a12=(a12+a35);
  if (res[0]!=0) res[0][0]=a12;
  a13=(a3*a13);
  a6=(a6+a13);
  a3=(a3*a4);
  a6=(a6+a3);
  a15=(a15*a14);
  a0=(a0+a15);
  a5=(a5*a0);
  a7=(a7*a11);
  a5=(a5-a7);
  a10=(a9-a10);
  a8=(a8*a10);
  a5=(a5-a8);
  a6=(a6+a5);
  a1=(a1*a6);
  a2=(a2+a1);
  a1=-5.0870554165852866e-001;
  a17=(a1*a17);
  a6=8.9307613470214842e-001;
  a20=(a6*a20);
  a17=(a17+a20);
  a20=-2.3660722867838546e-002;
  a5=(a20*a22);
  a17=(a17+a5);
  a5=(a16*a17);
  a24=(a1*a24);
  a26=(a6*a26);
  a24=(a24+a26);
  a26=(a20*a27);
  a24=(a24+a26);
  a26=(a19*a24);
  a5=(a5+a26);
  a28=(a1*a28);
  a30=(a6*a30);
  a28=(a28+a30);
  a30=(a20*a31);
  a28=(a28+a30);
  a30=(a21*a28);
  a5=(a5+a30);
  a30=(a5/a32);
  a26=(a30*a34);
  a2=(a2+a26);
  if (res[0]!=0) res[0][1]=a2;
  a16=(a16*a22);
  a19=(a19*a27);
  a16=(a16+a19);
  a21=(a21*a31);
  a16=(a16+a21);
  a32=(a16/a32);
  a34=(a32*a34);
  a9=(a9+a34);
  if (res[0]!=0) res[0][2]=a9;
  a9=1.;
  a9=(a9-a33);
  a33=(a9*a23);
  if (res[1]!=0) res[1][0]=a33;
  a33=(a30*a23);
  a5=(a5-a33);
  if (res[1]!=0) res[1][1]=a5;
  a23=(a32*a23);
  a16=(a16-a23);
  if (res[1]!=0) res[1][2]=a16;
  a18=(a1*a18);
  a25=(a6*a25);
  a18=(a18+a25);
  a25=(a20*a29);
  a18=(a18+a25);
  a25=(a9*a18);
  if (res[1]!=0) res[1][3]=a25;
  a17=(a1*a17);
  a24=(a6*a24);
  a17=(a17+a24);
  a24=(a20*a28);
  a17=(a17+a24);
  a24=arg[5]? arg[5][0] : 0;
  a17=(a17+a24);
  a24=(a30*a18);
  a17=(a17-a24);
  if (res[1]!=0) res[1][4]=a17;
  a1=(a1*a22);
  a6=(a6*a27);
  a1=(a1+a6);
  a20=(a20*a31);
  a1=(a1+a20);
  a18=(a32*a18);
  a1=(a1-a18);
  if (res[1]!=0) res[1][5]=a1;
  a9=(a9*a29);
  if (res[1]!=0) res[1][6]=a9;
  a30=(a30*a29);
  a28=(a28-a30);
  if (res[1]!=0) res[1][7]=a28;
  a28=arg[6]? arg[6][0] : 0;
  a31=(a31+a28);
  a32=(a32*a29);
  a31=(a31-a32);
  if (res[1]!=0) res[1][8]=a31;
  return 0;
}

CASADI_SYMBOL_EXPORT int EKF_Func(const casadi_real** arg, casadi_real** res, casadi_int* iw, casadi_real* w, int mem){
  return casadi_f0(arg, res, iw, w, mem);
}

CASADI_SYMBOL_EXPORT int EKF_Func_alloc_mem(void) {
  return 0;
}

CASADI_SYMBOL_EXPORT int EKF_Func_init_mem(int mem) {
  return 0;
}

CASADI_SYMBOL_EXPORT void EKF_Func_free_mem(int mem) {
}

CASADI_SYMBOL_EXPORT int EKF_Func_checkout(void) {
  return 0;
}

CASADI_SYMBOL_EXPORT void EKF_Func_release(int mem) {
}

CASADI_SYMBOL_EXPORT void EKF_Func_incref(void) {
}

CASADI_SYMBOL_EXPORT void EKF_Func_decref(void) {
}

CASADI_SYMBOL_EXPORT casadi_int EKF_Func_n_in(void) { return 8;}

CASADI_SYMBOL_EXPORT casadi_int EKF_Func_n_out(void) { return 2;}

CASADI_SYMBOL_EXPORT casadi_real EKF_Func_default_in(casadi_int i){
  switch (i) {
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT const char* EKF_Func_name_in(casadi_int i){
  switch (i) {
    case 0: return "u";
    case 1: return "y";
    case 2: return "xhatp";
    case 3: return "Pkp";
    case 4: return "Q11";
    case 5: return "Q22";
    case 6: return "Q33";
    case 7: return "R";
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT const char* EKF_Func_name_out(casadi_int i){
  switch (i) {
    case 0: return "xhat";
    case 1: return "Phat";
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT const casadi_int* EKF_Func_sparsity_in(casadi_int i) {
  switch (i) {
    case 0: return casadi_s0;
    case 1: return casadi_s0;
    case 2: return casadi_s1;
    case 3: return casadi_s2;
    case 4: return casadi_s0;
    case 5: return casadi_s0;
    case 6: return casadi_s0;
    case 7: return casadi_s0;
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT const casadi_int* EKF_Func_sparsity_out(casadi_int i) {
  switch (i) {
    case 0: return casadi_s1;
    case 1: return casadi_s2;
    default: return 0;
  }
}

CASADI_SYMBOL_EXPORT int EKF_Func_work(casadi_int *sz_arg, casadi_int* sz_res, casadi_int *sz_iw, casadi_int *sz_w) {
  if (sz_arg) *sz_arg = 8;
  if (sz_res) *sz_res = 2;
  if (sz_iw) *sz_iw = 0;
  if (sz_w) *sz_w = 0;
  return 0;
}


#ifdef __cplusplus
} /* extern "C" */
#endif
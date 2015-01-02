#include <stdio.h>
void dc3d0_(float *alpha, float *x, float *y, float *z, float *depth, float *dip, float *pot1, float *pot2, float *pot3, float *pot4, 
float *ux, float *uy, float *uz, float *uxx, float *uyx, float *uzx, float *uxy, float *uyy, float *uzy, float *uxz, float *uyz, float *uzz, int *iret);
float ux(float alpha, float x, float y, float z, float depth, float dip, float pot1, float pot2, float pot3, float pot4)
{
  float ux, uy, uz, uxx, uyx, uzx, uxy, uyy, uzy, uxz, uyz, uzz;
  int iret;
  dc3d0_(&alpha, &x, &y, &z, &depth, &dip, &pot1, &pot2, &pot3, &pot4,
  &ux, &uy, &uz, &uxx, &uyx, &uzx, &uxy, &uyy, &uzy, &uxz, &uyz, &uzz, &iret);
  return ux;
}
float uy(float alpha, float x, float y, float z, float depth, float dip, float pot1, float pot2, float pot3, float pot4)
{
  float ux, uy, uz, uxx, uyx, uzx, uxy, uyy, uzy, uxz, uyz, uzz;
  int iret;
  dc3d0_(&alpha, &x, &y, &z, &depth, &dip, &pot1, &pot2, &pot3, &pot4,
  &ux, &uy, &uz, &uxx, &uyx, &uzx, &uxy, &uyy, &uzy, &uxz, &uyz, &uzz, &iret);
  return uy;
}
float uz(float alpha, float x, float y, float z, float depth, float dip, float pot1, float pot2, float pot3, float pot4)
{
  float ux, uy, uz, uxx, uyx, uzx, uxy, uyy, uzy, uxz, uyz, uzz;
  int iret;
  dc3d0_(&alpha, &x, &y, &z, &depth, &dip, &pot1, &pot2, &pot3, &pot4,
  &ux, &uy, &uz, &uxx, &uyx, &uzx, &uxy, &uyy, &uzy, &uxz, &uyz, &uzz, &iret);
  return uz;
}
int iret(float alpha, float x, float y, float z, float depth, float dip, float pot1, float pot2, float pot3, float pot4)
{
  float ux, uy, uz, uxx, uyx, uzx, uxy, uyy, uzy, uxz, uyz, uzz;
  int iret;
  dc3d0_(&alpha, &x, &y, &z, &depth, &dip, &pot1, &pot2, &pot3, &pot4,
  &ux, &uy, &uz, &uxx, &uyx, &uzx, &uxy, &uyy, &uzy, &uxz, &uyz, &uzz, &iret);
  return iret;
}


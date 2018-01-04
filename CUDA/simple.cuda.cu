/* Introduction to CUDA GPU programming
 *
 * https://devblogs.nvidia.com/parallelforall/even-easier-introduction-cuda/
 */

#include <iostream>
#include <math.h>

// function to add the elements of two arrays
// __global__ tells the complier that this function
// runs on the GPU. In CUDA a function with __global__
// is known as a kernel
//
__global__
void add(int n, float *x, float *y)
{
  for (int i = 0; i < n; i++)
      y[i] = x[i] + y[i];
}

int main(void)
{
  int N = 1<<20; // 1M elements
  float *x, *y;
  cudaMallocManaged(&x, N*sizeof(float));
  cudaMallocManaged(&y, N*sizeof(float));
  // Old memory allocation
  //float *x = new float[N];
  //float *y = new float[N];

  // initialize x and y arrays on the host
  for (int i = 0; i < N; i++) {
    x[i] = 1.0f;
    y[i] = 2.0f;
  }

  // Run kernel on 1M elements on the CPU
  //add(N, x, y);
  // launch with 1 GPU thread
  add<<<1, 1>>>(N, x, y);

  // Wait for GPU to finish before accessing on host
  cudaDeviceSynchronize();

  // Check for errors (all values should be 3.0f)
  float maxError = 0.0f;
  for (int i = 0; i < N; i++)
    maxError = fmax(maxError, fabs(y[i]-3.0f));
  std::cout << "Max error: " << maxError << std::endl;

  // Free memory
  //delete [] x;
  //delete [] y;
  cudaFree(x);
  cudaFree(y);

  return 0;
}

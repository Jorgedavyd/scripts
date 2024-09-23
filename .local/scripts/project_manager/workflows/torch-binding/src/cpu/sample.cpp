#include "sample.h"

torch::Tensor fCPU(torch::Tensor input) {};

torch::Tensor bCPU(torch::Tensor grad_output, torch::Tensor input) {};

#ifndef WITH_CUDA
torch::Tensor forward(torch::Tensor input) {
    return fCPU(input);
}

torch::Tensor backward(torch::Tensor grad_output, torch::Tensor input) {
    return bCPU(grad_output, input);
}
#endif

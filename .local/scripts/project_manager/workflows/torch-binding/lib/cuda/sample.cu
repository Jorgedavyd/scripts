#include "sample.h"

template <typename scalar_t>
__global__ void fK() {};

template <typename scalar_t>
__global__ void bK() {};

template <typename scalar_t, unsigned int B, unsigned int T, cudaStream_t S>
torch::Tensor forward() {
    // CHECK_INPUT(sample);
    // torch::Tensor output = torch::empty_like()

    AT_DISPATCH_FLOATING_TYPES(DtypeTraits<scalar_t>.torch_t, "forward", ([&] {
        fK<scalar_t><<<B, T, 0, S>>>();
    }));
    CUDA_CHECK_KERNEL();

    return output;
}

template <typename scalar_t, unsigned int B, unsigned int T, cudaStream_t S>
torch::Tensor backward() {
    //CHECK_INPUT(sample);
    // torch::Tensor grad_input = torch::empty_like()

    AT_DISPATCH_FLOATING_TYPES(DtypeTraits<scalar_t>.torch_t, "backward", ([&] {
        bK<scalar_t><<<B, T, 0, S>>>();
    }));
    CUDA_CHECK_KERNEL();

    return grad_input;
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
    m.def("forward", &forward, "forward pass");
    m.def("backward", &backward, "backward pass");
}

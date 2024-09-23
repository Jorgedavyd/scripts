#pragma once
#include <torch/extension.h>
#include <typeTraits.h>

#ifdef WITH_CUDA
#define CHECK_CUDA(x) TORCH_CHECK(x.device().is_cuda(), #x " must be a CUDA tensor")
#define CHECK_CONTIGUOUS(x) TORCH_CHECK(x.is_contiguous(), #x " must be contiguous")
#define CHECK_INPUT(x) CHECK_CUDA(x); CHECK_CONTIGUOUS(x)
#else
#define CHECK_INPUT(x) TORCH_CHECK(x.is_contiguous(), #x " must be contiguous")
#endif

torch::Tensor forward();
torch::Tensor backward();

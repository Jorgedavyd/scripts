#pragma once
#include <torch/extension.h>
#include <type_traits>

#ifndef TYPETRAITS_H
#define TYPETRAITS_H

template <typename scalar_t>
constexpr torch::Dtype infer_dtype() {
    if constexpr (std::is_same_v<scalar_t, float>) {
        return torch::kFloat32;
    } else if constexpr (std::is_same_v<scalar_t, double>) {
        return torch::kFloat64;
    } else if constexpr (std::is_same_v<scalar_t, int>) {
        return torch::kInt32;
    } else {
        static_assert(sizeof(scalar_t) == 0, "Unsupported dtype.");
    }
}

template <typename T>
struct DtypeTraits {
    typedef T scalar_t;
    static constexpr torch::Dtype torch_t = infer_dtype<T>(); // Infers torch dtype based on scalar type
};

#endif // TYPETRAITS_H

from sample._C import forward, backward
from torch.autograd import Function
from torch import Tensor

__all__ = ["sample"]

class Sample(Function):
    @staticmethod
    def backward(*args) -> Tensor:
        return backward(*args)
    @staticmethod
    def forward(*args) -> Tensor:
        return forward(*args)

def sample(*args) -> Tensor:
    return Sample.apply(*args)

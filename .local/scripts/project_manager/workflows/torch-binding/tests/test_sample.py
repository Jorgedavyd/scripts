from sample import Sample
from torch import nn, Tensor
import torch

def test_cuda() -> None:
    sample_input: Tensor = torch.randn(...).cuda()
    model: nn.Module = Sample(...).cuda()
    assert (tuple(model(sample_input).shape.detach()) == (1,1,1))

def test_cpu() -> None:
    sample_input: Tensor = torch.randn(...)
    model: nn.Module = Sample(...)
    assert (tuple(model(sample_input).shape.detach()) == (1,1,1))

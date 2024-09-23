from .functional import sample
from torch import Tensor, nn

__all__ = ["Sample"]

class Sample(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        ## ...
    def forward(self, *args) -> Tensor:
        return sample(*args)

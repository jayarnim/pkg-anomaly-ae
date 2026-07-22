from .criterion import build_criterion
from .engine import Engine
import torch.nn as nn
from ...config.config.trainer import ValCfg


def build_val(
    model: nn.Module, 
    cfg: ValCfg,
) -> Engine:
    kwargs = dict(
        model=model,
        criterion=build_criterion(cfg.criterion),
    )
    return Engine(**kwargs)
from typing import Literal
import pandas as pd
from . import dataloader
from .dataloader.registry import DATALOADER_REGISTRY
from torch.utils.data import DataLoader
from ..config.config.dataloader import DataloaderCfg


def build_dataloader(
    df: pd.DataFrame,
    y_col: str,
    task: Literal["opt", "msr"],
    cfg: DataloaderCfg,
) -> DataLoader:
    kwargs = dict(
        df=df,
        y_col=y_col,
        **vars(cfg),
    )
    func = DATALOADER_REGISTRY[task]
    return func(**kwargs)
from dataclasses import dataclass
from core.config.config.criterion import *


@dataclass
class EvaluatorCfg:
    criterion: CriterionCfg
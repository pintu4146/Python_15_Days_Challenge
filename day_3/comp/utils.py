
import sys
from functools import wraps
from typing import Callable, Any


def compute_memory(fuc: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(fuc)
    def wrrapper(*arg, **kwargs):
        print('going to compute memory for function')
        result = fuc()

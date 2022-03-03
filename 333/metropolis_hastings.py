from typing import Callable

import numpy as np


def metropolis_hastings(
    f: Callable, x_0: float = 0.0, n_samples: int = 10000
) -> np.ndarray:
    """Implements the metropolis-hastings algorithm with a normal distribution as proposal function.

    Args:
        f (Callable): An arbitrary probability density function
            that is used to calculate the acceptance ratio alpha=f(x_next)/f(x_t).
            f has to accept a single parameter x and return the function value for x.
        x_0 (float, optional): The first observation to start from.
        n_samples (int, optional): Number of samples to be drawn. Defaults to 10000.

    Returns:
        (np.ndarray): Drawn samples from the target distribution.
    """
    if n_samples <= 0:
        raise ValueError
    x = np.arange(n_samples, dtype=np.float64)
    x[0] = x_0
    for i in range(0, n_samples-1):
        x_next = np.random.normal(x[i], 1.)
        if np.random.random_sample() < min(1, f(x_next)/f(x[i])):
            x[i+1] = x_next
        else:
            x[i+1] = x[i]
    return x

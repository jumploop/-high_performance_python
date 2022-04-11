#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from multiprocessing import Pool

import numpy as np


def calculate_pi(nbr_samples):
    # set random seed for numpy in each new process
    # else the fork will mean they all share the same state
    np.random.seed()
    xs = np.random.uniform(0, 1, nbr_samples)
    ys = np.random.uniform(0, 1, nbr_samples)
    estimate_inside_quarter_unit_circle = (xs * xs + ys * ys) <= 1
    return np.sum(estimate_inside_quarter_unit_circle)


if __name__ == '__main__':
    nbr_samples_in_total = 1e8
    nbr_parallel_blocks = 4
    pool = Pool(processes=nbr_parallel_blocks)
    nbr_samples_per_worker = int(nbr_samples_in_total / nbr_parallel_blocks)
    print(f"Making {nbr_samples_per_worker} samples per worker")
    nbr_trials_per_process = [nbr_samples_per_worker] * nbr_parallel_blocks
    t1 = time.time()
    nbr_in_unit_circles = pool.map(calculate_pi, nbr_trials_per_process)
    pi_estimate = float(sum(nbr_in_unit_circles) * 4 )/ nbr_samples_in_total
    print("Estimated pi", pi_estimate)
    print("Delta:", time.time() - t1)

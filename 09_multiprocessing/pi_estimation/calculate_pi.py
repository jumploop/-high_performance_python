#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time
from multiprocessing import Pool


def calculate_pi(nbr_estimates):
    nbr_trials_in_quarter_unit_circle = 0
    for step in range(int(nbr_estimates)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        is_in_unit_circle = x * x + y * y <= 1.0
        nbr_trials_in_quarter_unit_circle += is_in_unit_circle
    return nbr_trials_in_quarter_unit_circle


if __name__ == '__main__':
    nbr_samples_in_total = 1e8
    nbr_parallel_blocks = 4
    pool = Pool(processes=nbr_parallel_blocks)
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parallel_blocks
    print("Making {} samples per worker".format(nbr_samples_per_worker))
    nbr_trials_per_process = [nbr_samples_per_worker] * nbr_parallel_blocks
    t1 = time.time()
    nbr_in_unit_circles = pool.map(calculate_pi, nbr_trials_per_process)
    pi_estimate = sum(nbr_in_unit_circles) * 4 / nbr_samples_in_total
    print("Estimated pi", pi_estimate)
    print("Delta:", time.time() - t1)

import multiprocessing
# python -m timeit -s "import ex2_nolock" "ex2_nolock.run_workers()"
# 12ms


def work(value, max_count):
    for _ in range(max_count):
        value.value += 1


def run_workers():
    NBR_PROCESSES = 4
    MAX_COUNT_PER_PROCESS = 1000
    total_expected_count = NBR_PROCESSES * MAX_COUNT_PER_PROCESS
    processes = []
    value = multiprocessing.Value('i', 0)
    for _ in range(NBR_PROCESSES):
        p = multiprocessing.Process(target=work, args=(value, MAX_COUNT_PER_PROCESS))
        p.start()
        processes.append(p)

    # wait for the processes to finish
    for p in processes:
        p.join()

    # print the final value
    print(f"Expecting to see a count of {total_expected_count}")
    print(f"We have counted to {value.value}")

if __name__ == "__main__":
    run_workers()

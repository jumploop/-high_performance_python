import multiprocessing
import os
# python -m timeit -s "import ex1_nolock" "ex1_nolock.run_workers()"
# 71ms

MAX_COUNT_PER_PROCESS = 1000
FILENAME = "count.txt"


def work(filename, max_count):
    for _ in range(max_count):
        f = open(filename, "r")
        try:
            nbr = int(f.read())
        except ValueError as err:
            print("File is empty, starting to count from 0, error: " + str(err))
            nbr = 0
        with open(filename, "w") as f:
            f.write(str(nbr + 1) + '\n')


def run_workers():
    NBR_PROCESSES = 4
    total_expected_count = NBR_PROCESSES * MAX_COUNT_PER_PROCESS
    print(
        f"Starting {NBR_PROCESSES} process(es) to count to {total_expected_count}"
    )

    # reset counter
    f = open(FILENAME, "w")
    f.close()

    processes = []
    for _ in range(NBR_PROCESSES):
        p = multiprocessing.Process(target=work, args=(FILENAME, MAX_COUNT_PER_PROCESS))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print(f"Expecting to see a count of {total_expected_count}")
    print(f"{FILENAME} contains:")
    os.system(f'more {FILENAME}')


if __name__ == "__main__":
    run_workers()

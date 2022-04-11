import time
import timeit
import text_example
import memory_profiler
import bisect


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


if __name__ == "__main__":
    print("RAM at start {:0.1f}MiB".format(memory_profiler.memory_usage()[0]))
    t1 = time.time()
    words = list(text_example.readers)
    print(f"Loading {len(words)} words")
    t2 = time.time()
    print("RAM after creating list {:0.1f}MiB, took {:0.1f}s".format(memory_profiler.memory_usage()[0], t2 - t1))
    print(f"The list contains {len(words)} words")
    words.sort()
    t3 = time.time()
    print("Sorting list took {:0.1f}s".format(t3 - t2))

    assert 'Zwiebel' in words
    time_cost = sum(timeit.repeat(stmt="index(words, u'Zwiebel')",
                                  setup="from __main__ import words, index",
                                  number=1,
                                  repeat=10000))
    print("Summed time to lookup word {:0.4f}s".format(time_cost))

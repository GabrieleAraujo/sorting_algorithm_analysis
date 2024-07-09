import csv
import sys
from datetime import datetime
import tracemalloc

from sorting_algorithms import (
    merge_sort, quick_sort_last, quick_sort_random, quick_sort_median, tim_sort,
    measure_best_case_performance, measure_worst_case_performance, measure_average_case_performance
)

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n_values = [int(n) for n in lines[0].strip().split(',')]
        algorithms = lines[1].strip().split(',')
    return n_values, algorithms

def bytes_to_mb(bytes):
    return bytes / (1024 * 1024)

def log_performance(csvwriter, csvfile, now, algorithm, n, case, time_taken, memory_used):
    result = [now, algorithm, n, case, time_taken, bytes_to_mb(memory_used)]
    csvwriter.writerow(result)
    csvfile.flush()
    print(result)
    sys.stdout.flush()

def main():
    n_values, algorithms = parse_input('ent.txt')

    sorting_algorithms = {
        'merge_sort': merge_sort,
        'quick_sort_last': quick_sort_last,
        'quick_sort_random': quick_sort_random,
        'quick_sort_median': quick_sort_median,
        'tim_sort': tim_sort,
    }

    with open('results.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        if csvfile.tell() == 0:
            csvwriter.writerow(["data", "algoritmo", "n", "caso", "tempo", "memoria (MB)"])

        for n in n_values:
            for algorithm in algorithms:
                alg_func = sorting_algorithms[algorithm]

                for case, measure_func in [('best', measure_best_case_performance),
                                           ('worst', measure_worst_case_performance),
                                           ('average', measure_average_case_performance)]:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    time_taken, memory_used = measure_func(alg_func, n)
                    log_performance(csvwriter, csvfile, now, algorithm, n, case, time_taken, memory_used)

                    tracemalloc.stop()
                    tracemalloc.clear_traces()

if __name__ == "__main__":
    main()

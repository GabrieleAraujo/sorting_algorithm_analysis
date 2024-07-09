
[![GitHub issues](https://img.shields.io/github/issues/GabrieleAraujo/sorting_algorithm_analysis)](https://github.com/GabrieleAraujo/sorting_algorithm_analysis/issues) 
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-yellow.svg?style=flat-square)](https://github.com/GabrieleAraujo/sorting_algorithm_analysis/pulls) 
[![HitCount](https://views.whatilearened.today/views/github/GabrieleAraujo/sorting_algorithm_analysis.svg)](https://github.com/GabrieleAraujo/sorting_algorithm_analysis) 
[![website coderjojo.github.io](https://img.shields.io/website-up-down-yellow-red/http/coderjojo.github.io/creative-profile-readme.svg)](GabrieleAraujo)


<h1 align="center">
  <br>
   Sorting Algorithm Analysis
  <br>
</h1>

<h4 align="center">The objective of this project is to compare the performance of three sorting algorithms: Mergesort, Quicksort, and Timsort.</h4>

<p align="center">
  <a href="#algorithms">Algorithms</a> •
  <a href="#contents">Contents</a> •
  <a href="#usage">Usage</a> •
  <a href="#author">Author</a>
</p>

## Algorithms
The comparison was conducted considering execution time and memory usage in different scenarios: best case, worst case, and average case.

| **Name**     | **Best**        | **Average**      | **Worst**        | **Memory**   | **Stable** | **Method**             |
|--------------|-----------------|------------------|------------------|--------------|------------|------------------------|
| Merge Sort   | O(n log n) | O(n log n)  | O(n log n)  | O(n)    | Yes        | Merging                |
| Quick Sort   | O(n log n) | O(n log n)  | O(n<sup>2</sup>)       | O(log n)| No         | Partitioning           |
| Tim Sort     | O(n)        | O(n log n)  | O(n log n)  | O(n)     | Yes        | Insertion & Merging    |

*Adapted from [Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm)*

## Contents

1. **main.py**: Main script for executing and analyzing sorting algorithms.
2. **plot_time.py** and **plot_memory.py**: Script for generating graphs from the obtained results.
3. **sorting_algorithms.py**: Implementations of the sorting algorithms.
4. **result_final.csv**: CSV file containing the performance test results of the algorithms.
5. **ent.txt**: Input file (explanation of the content needed).

- Python 3.11v was used. The following libraries/modules were imported:

``` python
import csv
import sys
import numpy as np
import pandas as pd
import random
import tracemalloc
import timeit
import matplotlib.pyplot as plt
from datetime import datetime
```


## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/GabrieleAraujo/sorting_algorithm_analysis.git
    cd sorting_algorithm_analysis
    ```

2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the main script to perform the performance tests:
    ```sh
    python main.py
    ```

4. Generate graphs from the results:
    ```sh
    python plot_time.py
    ```

## Author

[Gabriele S. Araújo](https://github.com/GabrieleAraujo)

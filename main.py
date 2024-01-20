import timeit
import random


from sorts_funcs.insertion_sort import insertion_sort
from sorts_funcs.merge_sort import merge_sort
from sorts_funcs.bubble_sort import bubble_sort
from sorts_funcs.quicksort import quicksort
from sorts_funcs.selection_sort import selection_sort
from sorts_funcs.shell_sort import shell_sort
from sorts_funcs.radix_sort import radix_sort


# insertion_sort, merge_sort, default python sort
if __name__ == "__main__":
    # prepare for results table
    results = {
        "insertion_sort": {"title": "Insertion Sort"},
        "merge_sort": {"title": "Merge Sort"},
        "timsort_def": {"title": "Timsort def sorted"},
        "timsort_method": {"title": "Timsort method sort"},
        "bubble_sort": {"title": "Bubble sort"},
        "selection_sort": {"title": "Selection sort"},
        "quicksort": {"title": "Quicksort"},
        "radix_sort": {"title": "Radix sort"},
        "shell_sort": {"title": "Shell sort"},
    }

    for key in results:
        results[key]["small_data"] = None
        results[key]["medium_data"] = None

    small_data_len = 1000
    medium_data_len = 10000
    small_data = [random.randint(0, small_data_len) for _ in range(small_data_len)]
    medium_data = [random.randint(0, medium_data_len) for _ in range(medium_data_len)]

    results["merge_sort"]["small_data"] = timeit.timeit(
        lambda: merge_sort(small_data[:]), number=10
    )
    results["merge_sort"]["medium_data"] = timeit.timeit(
        lambda: merge_sort(medium_data[:]), number=10
    )

    results["insertion_sort"]["small_data"] = timeit.timeit(
        lambda: insertion_sort(small_data[:]), number=10
    )
    results["insertion_sort"]["medium_data"] = timeit.timeit(
        lambda: insertion_sort(medium_data[:]), number=10
    )

    results["timsort_def"]["small_data"] = timeit.timeit(
        lambda: sorted(small_data[:]), number=10
    )
    results["timsort_def"]["medium_data"] = timeit.timeit(
        lambda: sorted(medium_data[:]), number=10
    )

    results["timsort_method"]["small_data"] = timeit.timeit(
        lambda: small_data[:].sort(), number=10
    )
    results["timsort_method"]["medium_data"] = timeit.timeit(
        lambda: medium_data[:].sort(), number=10
    )

    results["bubble_sort"]["small_data"] = timeit.timeit(
        lambda: bubble_sort(small_data[:]), number=10
    )
    results["bubble_sort"]["medium_data"] = timeit.timeit(
        lambda: bubble_sort(medium_data[:]), number=10
    )

    results["quicksort"]["small_data"] = timeit.timeit(
        lambda: quicksort(small_data[:]), number=10
    )
    results["quicksort"]["medium_data"] = timeit.timeit(
        lambda: quicksort(medium_data[:]), number=10
    )

    results["selection_sort"]["small_data"] = timeit.timeit(
        lambda: selection_sort(small_data[:]), number=10
    )
    results["selection_sort"]["medium_data"] = timeit.timeit(
        lambda: selection_sort(medium_data[:]), number=10
    )

    results["shell_sort"]["small_data"] = timeit.timeit(
        lambda: shell_sort(small_data[:]), number=10
    )
    results["shell_sort"]["medium_data"] = timeit.timeit(
        lambda: shell_sort(medium_data[:]), number=10
    )

    results["radix_sort"]["small_data"] = timeit.timeit(
        lambda: radix_sort(small_data[:]), number=10
    )
    results["radix_sort"]["medium_data"] = timeit.timeit(
        lambda: radix_sort(medium_data[:]), number=10
    )


print(
    f"{'Algo name': <20} | {'Sort ' + str(small_data_len) + ' items time':<20} | {'Sort ' + str(medium_data_len) + ' items time':<20}"
)

for key, item in results.items():
    try:
        print(
            f"{item['title']: <20} | {item['small_data']:<20.5f} | {item['medium_data']:<20.5f}"
        )
    except:
        pass

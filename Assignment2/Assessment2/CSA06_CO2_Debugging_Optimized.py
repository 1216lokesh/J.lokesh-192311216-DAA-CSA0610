"""SentinelOps SOC alert-triage module — corrected and optimized.

Implements:
1. Stable severity sorting (highest severity first).
2. Blocklist membership checks.
3. Brute-force all-occurrences signature matching.
4. Closest pair of login coordinates using squared Euclidean distance.

Coordinates are assumed to be planar x/y coordinates in kilometres, as specified
by the assignment. For geographic latitude/longitude, use a geodesic distance.
"""

from __future__ import annotations

import random
import time
from typing import Iterable, Sequence, TypeVar

Alert = tuple[str, int]
Point = tuple[float, float]
T = TypeVar("T")


def sort_alerts(alerts: list[Alert]) -> list[Alert]:
    """Stable insertion sort by severity descending; ties keep arrival order."""
    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1
        while j >= 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1
        alerts[j + 1] = key
    return alerts


def is_blocked(blocklist: Iterable[str], ip: str) -> bool:
    """Return True if ip is blocked. Convert to a set for repeated lookups."""
    if isinstance(blocklist, set):
        return ip in blocklist
    return ip in set(blocklist)


def find_signature(log: str, pattern: str) -> list[int]:
    """Return every start index where pattern occurs in log, including overlaps."""
    if pattern == "":
        # Define empty pattern as matching at every boundary of the string.
        return list(range(len(log) + 1))
    n, m = len(log), len(pattern)
    hits = []
    for i in range(n - m + 1):
        j = 0
        while j < m and log[i + j] == pattern[j]:
            j += 1
        if j == m:
            hits.append(i)
    return hits


def closest_logins(events: Sequence[Point]) -> tuple[tuple[int, int] | None, float]:
    """Return indices of the closest distinct pair and their Euclidean distance.

    Uses squared distances to avoid square roots inside the pairwise loop.
    Each unordered pair is examined exactly once. If fewer than two events
    are supplied, returns (None, infinity).
    """
    n = len(events)
    if n < 2:
        return None, float("inf")

    best_pair = (0, 1)
    x0, y0 = events[0]
    x1, y1 = events[1]
    best_squared = (x0 - x1) ** 2 + (y0 - y1) ** 2

    for i in range(n - 1):
        xi, yi = events[i]
        for j in range(i + 1, n):
            xj, yj = events[j]
            squared = (xi - xj) ** 2 + (yi - yj) ** 2
            if squared < best_squared:
                best_squared = squared
                best_pair = (i, j)

    return best_pair, best_squared ** 0.5


def closest_logins_counted(events: Sequence[Point]) -> tuple[tuple[int, int] | None, float, int]:
    """Brute-force closest pair with a distance-computation counter."""
    n = len(events)
    if n < 2:
        return None, float("inf"), 0

    best_pair = (0, 1)
    x0, y0 = events[0]
    x1, y1 = events[1]
    best_squared = (x0 - x1) ** 2 + (y0 - y1) ** 2
    computations = 1

    for i in range(n - 1):
        xi, yi = events[i]
        for j in range(i + 1, n):
            if i == 0 and j == 1:
                continue
            xj, yj = events[j]
            squared = (xi - xj) ** 2 + (yi - yj) ** 2
            computations += 1
            if squared < best_squared:
                best_squared = squared
                best_pair = (i, j)

    return best_pair, best_squared ** 0.5, computations


def closest_logins_sorted_pruned(events: Sequence[Point]) -> tuple[tuple[int, int] | None, float, int]:
    """Optimized exact closest pair using x-sorting and strip pruning.

    This implementation is intended for planar coordinates. It first sorts
    points by x, recursively solves each half, then checks only points in the
    dividing strip whose y separation can improve the current best distance.
    The strip is sorted by y at each recursion, giving O(n log^2 n) time.
    """
    n = len(events)
    if n < 2:
        return None, float("inf"), 0

    points = sorted((x, y, idx) for idx, (x, y) in enumerate(events))
    computations = 0

    def squared_distance(a, b):
        nonlocal computations
        computations += 1
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    def brute(points_part):
        best_sq = float("inf")
        best_pair = None
        for i in range(len(points_part) - 1):
            for j in range(i + 1, len(points_part)):
                d2 = squared_distance(points_part[i], points_part[j])
                if d2 < best_sq:
                    best_sq = d2
                    best_pair = (points_part[i][2], points_part[j][2])
        return best_pair, best_sq

    def solve(px):
        n_part = len(px)
        if n_part <= 3:
            return brute(px)

        mid = n_part // 2
        mid_x = px[mid][0]
        left_pair, left_sq = solve(px[:mid])
        right_pair, right_sq = solve(px[mid:])

        if left_sq <= right_sq:
            best_pair, best_sq = left_pair, left_sq
        else:
            best_pair, best_sq = right_pair, right_sq

        strip = [p for p in px if (p[0] - mid_x) ** 2 < best_sq]
        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) ** 2 < best_sq:
                d2 = squared_distance(strip[i], strip[j])
                if d2 < best_sq:
                    best_sq = d2
                    best_pair = (strip[i][2], strip[j][2])
                j += 1
        return best_pair, best_sq

    pair, best_squared = solve(points)
    return pair, best_squared ** 0.5, computations


def run_tests() -> None:
    """Run normal and boundary tests for each function."""
    print("TEST HARNESS")
    alerts = [("A1", 3), ("A2", 9), ("A3", 5), ("A4", 9), ("A5", 1)]
    assert sort_alerts(alerts.copy()) == [
        ("A2", 9), ("A4", 9), ("A3", 5), ("A1", 3), ("A5", 1)
    ]
    assert sort_alerts([]) == []
    assert sort_alerts([("x", 2), ("y", 2)]) == [("x", 2), ("y", 2)]
    print("sort_alerts: PASS (ordering, stability, empty list, equal severities)")

    blocklist = ["10.0.0.5", "10.0.0.9", "172.16.4.2"]
    assert is_blocked(blocklist, "10.0.0.9") is True
    assert is_blocked(blocklist, "8.8.8.8") is False
    assert is_blocked([], "8.8.8.8") is False
    assert is_blocked(set(), "8.8.8.8") is False
    print("is_blocked: PASS (present, absent, empty blocklist)")

    assert find_signature("FAILFAIXFAIL", "FAIL") == [0, 8]
    assert find_signature("ABCEND", "END") == [3]
    assert find_signature("ABC", "LONGER") == []
    assert find_signature("", "A") == []
    assert find_signature("AAAA", "AA") == [0, 1, 2]
    print("find_signature: PASS (multiple, end, longer pattern, overlap, empty text)")

    events = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    pair, dist = closest_logins(events)
    assert pair is not None and abs(dist - (2 ** 0.5)) < 1e-9
    assert closest_logins([]) == (None, float("inf"))
    assert closest_logins([(1, 2)]) == (None, float("inf"))
    brute_pair, brute_dist, _ = closest_logins_counted(events)
    fast_pair, fast_dist, _ = closest_logins_sorted_pruned(events)
    assert abs(brute_dist - fast_dist) < 1e-9
    print("closest_logins: PASS (normal case, fewer than two events, agrees with optimized method)")


def demo_assignment_data() -> None:
    print("\nASSIGNMENT SAMPLE DATA")
    alerts = [("A1", 3), ("A2", 9), ("A3", 5), ("A4", 9), ("A5", 1)]
    blocklist = ["10.0.0.5", "10.0.0.9", "172.16.4.2"]
    queries = ["10.0.0.9", "10.0.0.5", "8.8.8.8"]
    log, pattern = "FAILFAIXFAIL", "FAIL"
    events = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

    print("Sorted alerts:", sort_alerts(alerts.copy()))
    blocked = set(blocklist)
    print("Blocklist results:", {ip: is_blocked(blocked, ip) for ip in queries})
    print(f"Signature hits in {log!r} for {pattern!r}:", find_signature(log, pattern))
    print("Closest login pair and distance:", closest_logins(events))


def performance_comparison() -> None:
    """Compare closest-pair distance computation counts for 1,000–8,000 events."""
    print("\nCLOSEST-PAIR PERFORMANCE COMPARISON")
    print("Note: brute-force is O(n^2); sorted/pruned method is O(n log^2 n).")
    rng = random.Random(42)

    for n in (1000, 2000, 4000, 8000):
        events = [(rng.random() * 10000, rng.random() * 10000) for _ in range(n)]

        start = time.perf_counter()
        _, _, brute_count = closest_logins_counted(events)
        brute_seconds = time.perf_counter() - start

        start = time.perf_counter()
        _, _, optimized_count = closest_logins_sorted_pruned(events)
        optimized_seconds = time.perf_counter() - start

        print(
            f"n={n}: brute distance calculations={brute_count:,}, "
            f"time={brute_seconds:.4f}s; optimized distance calculations={optimized_count:,}, "
            f"time={optimized_seconds:.4f}s"
        )


def insertion_sort_comparisons(values: list[Alert]) -> int:
    """Count key comparisons in insertion sort, for before/after input patterns."""
    a = values.copy()
    comparisons = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j][1] < key[1]:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return comparisons


def compare_insertion_sort_inputs() -> None:
    rng = random.Random(42)
    n = 2000
    random_severities = [rng.randint(1, 10) for _ in range(n)]
    nearly_sorted_severities = list(range(n, 0, -1))
    # Desired descending order: nearly sorted descending list with a few local swaps.
    for k in range(0, n - 1, 200):
        nearly_sorted_severities[k], nearly_sorted_severities[k + 1] = (
            nearly_sorted_severities[k + 1], nearly_sorted_severities[k]
        )
    random_alerts = [(f"R{i}", s) for i, s in enumerate(random_severities)]
    nearly_alerts = [(f"N{i}", s) for i, s in enumerate(nearly_sorted_severities)]
    print("\nINSERTION-SORT COMPARISON COUNTS (n=2000)")
    print("Nearly sorted severity data:", insertion_sort_comparisons(nearly_alerts))
    print("Random severity data:", insertion_sort_comparisons(random_alerts))


if __name__ == "__main__":
    run_tests()
    demo_assignment_data()
    compare_insertion_sort_inputs()
    performance_comparison()

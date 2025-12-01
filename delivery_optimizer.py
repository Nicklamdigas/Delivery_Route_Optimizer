"""
Delivery Route Optimization System
Student Project: Algorithm Design & Analysis

This program implements Merge Sort and Binary Search algorithms
to optimize delivery routes for a logistics company.
"""

import time
import random
from typing import List, Tuple


class DeliveryOptimizer:
    """
    A class to handle delivery route optimization using
    Merge Sort and Binary Search algorithms.
    """
    
    def __init__(self):
        self.delivery_points = []
        self.sorted_points = []
        
    def merge_sort(self, arr: List[int]) -> List[int]:
        """
        Merge Sort implementation
        Time Complexity: O(n log n) in all cases
        Space Complexity: O(n)
        """
        if len(arr) <= 1:
            return arr
            
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """Helper method to merge two sorted arrays"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    def binary_search(self, arr: List[int], target: int) -> Tuple[bool, int, int]:
        """
        Binary Search implementation
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Returns: (found, index, comparisons_made)
        """
        left, right = 0, len(arr) - 1
        comparisons = 0
        
        while left <= right:
            comparisons += 1
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return (True, mid, comparisons)
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return (False, -1, comparisons)
    
    def load_delivery_points(self, points: List[int]):
        """Load delivery points into the system"""
        self.delivery_points = points.copy()
        
    def optimize_route(self) -> List[int]:
        """Sort delivery points for optimal route"""
        self.sorted_points = self.merge_sort(self.delivery_points.copy())
        return self.sorted_points
    
    def find_delivery_point(self, point: int) -> Tuple[bool, int, int]:
        """Search for a specific delivery point"""
        if not self.sorted_points:
            self.optimize_route()
        return self.binary_search(self.sorted_points, point)


def demo_basic_functionality():
    """Demonstrate basic sorting and searching"""
    print("=" * 70)
    print("DELIVERY ROUTE OPTIMIZATION - DEMO")
    print("=" * 70)
    print()
    
    # Sample delivery points (house numbers)
    delivery_points = [145, 23, 678, 89, 234, 12, 456, 789, 34, 567, 123, 890, 45]
    
    print("Original Delivery Points:")
    print(delivery_points)
    print(f"Total: {len(delivery_points)} points")
    print()
    
    # Create optimizer and sort
    optimizer = DeliveryOptimizer()
    optimizer.load_delivery_points(delivery_points)
    
    print("Sorting delivery route...")
    sorted_points = optimizer.optimize_route()
    print("Sorted Route:")
    print(sorted_points)
    print()
    
    # Search demonstrations
    print("-" * 70)
    print("SEARCH DEMONSTRATIONS")
    print("-" * 70)
    print()
    
    search_targets = [234, 12, 999, 567, 1]
    
    for target in search_targets:
        found, index, comparisons = optimizer.find_delivery_point(target)
        if found:
            print(f"Point {target}: FOUND at index {index} ({comparisons} comparisons)")
        else:
            print(f"Point {target}: NOT FOUND ({comparisons} comparisons)")
    
    print()


def measure_performance(size: int) -> dict:
    """Measure algorithm performance for a given input size"""
    optimizer = DeliveryOptimizer()
    
    # Generate random delivery points
    points = random.sample(range(1, size * 10), size)
    optimizer.load_delivery_points(points)
    
    # Measure sorting time
    start = time.perf_counter()
    sorted_points = optimizer.optimize_route()
    sort_time = time.perf_counter() - start
    
    # Measure search performance
    num_searches = 10
    search_targets = random.sample(sorted_points, min(num_searches, len(sorted_points)))
    total_comparisons = 0
    
    for target in search_targets:
        _, _, comparisons = optimizer.find_delivery_point(target)
        total_comparisons += comparisons
    
    avg_comparisons = total_comparisons / len(search_targets)
    
    return {
        'size': size,
        'sort_time': sort_time,
        'avg_comparisons': avg_comparisons
    }


def performance_evaluation():
    """Test performance with different input sizes"""
    print("=" * 70)
    print("PERFORMANCE EVALUATION")
    print("=" * 70)
    print()
    
    test_sizes = [10, 100, 1000, 5000, 10000]
    
    print(f"{'Size':<10} {'Sort Time (s)':<20} {'Avg Comparisons':<20}")
    print("-" * 70)
    
    for size in test_sizes:
        result = measure_performance(size)
        print(f"{result['size']:<10} {result['sort_time']:<20.8f} {result['avg_comparisons']:<20.2f}")
    
    print()
    print("Analysis:")
    print("- Merge Sort shows O(n log n) behavior")
    print("- Binary Search comparisons grow logarithmically")
    print("- Both algorithms scale well with larger datasets")
    print()


def main():
    """Main program execution"""
    print()
    demo_basic_functionality()
    performance_evaluation()
    print("=" * 70)
    print("DEMO COMPLETE")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()

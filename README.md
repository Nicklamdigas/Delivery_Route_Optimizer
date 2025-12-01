# Delivery Route Optimization

Algorithm Design & Analysis Project - Implementing efficient sorting and searching algorithms for delivery route optimization.

## Project Overview

This project solves a real-world problem for delivery companies: optimizing parcel delivery routes by efficiently sorting delivery points and quickly searching for specific addresses.

**Algorithms Used:**
- **Merge Sort** - O(n log n) sorting algorithm
- **Binary Search** - O(log n) search algorithm

## Problem Statement

A delivery company needs to:
1. Sort delivery points (house numbers) efficiently
2. Search for specific delivery addresses quickly
3. Handle growing delivery networks effectively

## Implementation

**Language:** Python 3

**Main File:** `delivery_optimizer.py`

### Key Features
- Merge Sort for guaranteed O(n log n) performance
- Binary Search for O(log n) lookup speed
- Performance testing with datasets from 10 to 10,000 items
- Visual performance graphs

## How to Run

```bash
# Run the main program
python delivery_optimizer.py

# Generate performance graphs (requires matplotlib)
python generate_graphs.py
```

## Sample Output

**Input:** [145, 23, 678, 89, 234, 12, 456, 789, 34, 567, 123, 890, 45]

**Sorted:** [12, 23, 34, 45, 89, 123, 145, 234, 456, 567, 678, 789, 890]

**Search Results:**
- Point 234: FOUND at index 7 (3 comparisons)
- Point 567: FOUND at index 9 (2 comparisons)
- Point 999: NOT FOUND (4 comparisons)

## Performance Results

| Size | Sort Time (s) | Avg Comparisons |
|------|--------------|-----------------|
| 10 | 0.000059 | 2.9 |
| 100 | 0.000708 | 5.4 |
| 1,000 | 0.004990 | 9.8 |
| 5,000 | 0.035361 | 11.0 |
| 10,000 | 0.070263 | 13.2 |

## Complexity Analysis

### Merge Sort
- **Best Case:** O(n log n)
- **Average Case:** O(n log n)
- **Worst Case:** O(n log n)
- **Space:** O(n)

### Binary Search
- **Best Case:** O(1)
- **Average Case:** O(log n)
- **Worst Case:** O(log n)
- **Space:** O(1)

## Why These Algorithms?

**Merge Sort:**
- Guaranteed performance - no worst case degradation
- Stable sorting maintains order
- Efficient for large datasets

**Binary Search:**
- Extremely fast - 10,000 items needs only ~13 comparisons
- Minimal memory usage
- Perfect for sorted data

## Project Structure

```
delivery-optimization-project/
├── delivery_optimizer.py      # Main implementation
├── generate_graphs.py         # Graph generation
├── analysis.md                # Detailed analysis
├── screenshots/               # Output screenshots
└── README.md                  # This file
```

## Requirements

```
Python 3.7+
matplotlib (for graphs)
numpy (for graphs)
```

## Installation

```bash
pip install matplotlib numpy
```

## Author

[Nicholas Ndungu Mathenge BSE-01-0109/2025]


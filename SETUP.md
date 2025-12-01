# Delivery Optimization Project - Setup Guide

## Quick Start

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd delivery-optimization-project
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the program**
```bash
python delivery_optimizer.py
```

4. **Generate graphs** (optional)
```bash
python generate_graphs.py
```

## What You'll See

The program will:
- Sort 13 delivery points
- Search for specific addresses
- Show performance with different dataset sizes
- Display execution times and comparisons

## Files

- `delivery_optimizer.py` - Main program
- `generate_graphs.py` - Creates performance visualizations
- `ANALYSIS.md` - Detailed algorithm analysis
- `README.md` - Project overview

## Example Output

```
Original Delivery Points:
[145, 23, 678, 89, 234, 12, 456, 789, 34, 567, 123, 890, 45]

Sorted Route:
[12, 23, 34, 45, 89, 123, 145, 234, 456, 567, 678, 789, 890]

Point 234: FOUND at index 7 (3 comparisons)
```

## Requirements

- Python 3.7 or higher
- matplotlib (for graphs)
- numpy (for graphs)

## Notes

This is a student project for Algorithm Design & Analysis course.
The implementation demonstrates Merge Sort and Binary Search algorithms
applied to a real-world delivery optimization problem.

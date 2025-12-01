"""
Graph Generator for Performance Analysis
Generates visual charts to demonstrate algorithm performance
"""

import matplotlib.pyplot as plt
import numpy as np


def create_performance_graphs():
    """Generate performance comparison graphs"""
    
    # Performance data from testing
    sizes = [10, 100, 1000, 5000, 10000]
    sort_times = [0.00005910, 0.00070840, 0.00499000, 0.03536100, 0.07026300]
    search_comparisons = [2.90, 5.40, 9.80, 11.00, 13.20]
    
    # Create subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle('Delivery Route Optimization - Performance Analysis', 
                 fontsize=14, fontweight='bold')
    
    # Graph 1: Sorting Performance
    ax1.plot(sizes, sort_times, 'b-o', linewidth=2, markersize=6)
    ax1.set_xlabel('Number of Delivery Points')
    ax1.set_ylabel('Sort Time (seconds)')
    ax1.set_title('Merge Sort Performance')
    ax1.grid(True, alpha=0.3)
    
    # Graph 2: Search Comparisons
    ax2.plot(sizes, search_comparisons, 'g-s', linewidth=2, markersize=6)
    ax2.set_xlabel('Number of Delivery Points')
    ax2.set_ylabel('Average Comparisons')
    ax2.set_title('Binary Search Performance')
    ax2.grid(True, alpha=0.3)
    
    # Add theoretical curve
    theoretical = [np.log2(n) for n in sizes]
    ax2.plot(sizes, theoretical, 'r--', linewidth=2, alpha=0.7, label='O(log n)')
    ax2.legend()
    
    # Graph 3: Log scale sorting
    ax3.loglog(sizes, sort_times, 'b-o', linewidth=2, markersize=6)
    ax3.set_xlabel('Delivery Points (log scale)')
    ax3.set_ylabel('Sort Time (log scale)')
    ax3.set_title('Merge Sort - Log Scale')
    ax3.grid(True, alpha=0.3)
    
    # Graph 4: Algorithm comparison
    linear_comparisons = [n/2 for n in sizes]
    ax4.plot(sizes, search_comparisons, 'g-o', linewidth=2, markersize=6, 
             label='Binary Search O(log n)')
    ax4.plot(sizes, linear_comparisons, 'r-s', linewidth=2, markersize=6, 
             label='Linear Search O(n)')
    ax4.set_xlabel('Number of Delivery Points')
    ax4.set_ylabel('Average Comparisons')
    ax4.set_title('Search Algorithm Comparison')
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    
    plt.tight_layout()
    plt.savefig('performance_analysis.png', dpi=300, bbox_inches='tight')
    print("Saved: performance_analysis.png")
    
    # Complexity comparison chart
    fig2, ax = plt.subplots(figsize=(10, 6))
    
    n_range = np.linspace(1, 10000, 1000)
    
    # Different complexity curves (normalized)
    o_1 = np.ones_like(n_range)
    o_logn = np.log2(n_range)
    o_n = n_range
    o_nlogn = n_range * np.log2(n_range)
    o_n2 = n_range ** 2
    
    # Normalize for better visualization
    o_1 = o_1 / o_1[0]
    o_logn = o_logn / o_logn[-1] * 10
    o_n = o_n / o_n[-1] * 100
    o_nlogn = o_nlogn / o_nlogn[-1] * 1000
    o_n2 = o_n2 / o_n2[-1] * 10000
    
    ax.plot(n_range, o_1, label='O(1)', linewidth=2)
    ax.plot(n_range, o_logn, label='O(log n) - Binary Search', linewidth=2)
    ax.plot(n_range, o_n, label='O(n)', linewidth=2)
    ax.plot(n_range, o_nlogn, label='O(n log n) - Merge Sort', linewidth=2)
    ax.plot(n_range, o_n2, label='O(n²)', linewidth=2, linestyle='--')
    
    ax.set_xlabel('Input Size (n)', fontweight='bold')
    ax.set_ylabel('Operations (normalized)', fontweight='bold')
    ax.set_title('Algorithm Complexity Comparison', fontweight='bold', fontsize=13)
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 100])
    
    plt.tight_layout()
    plt.savefig('complexity_comparison.png', dpi=300, bbox_inches='tight')
    print("Saved: complexity_comparison.png")
    
    print("\nGraphs generated successfully!")


if __name__ == "__main__":
    print("Generating performance graphs...")
    create_performance_graphs()

# Optimized Memory Allocation using TSP Search Algorithms

## Objective

Traditional memory allocation methods, such as the best-fit algorithm, often result in high fragmentation and inefficient memory usage. This project aims to enhance memory allocation efficiency and reduce fragmentation by applying search algorithms derived from the Travelling Salesman Problem (TSP). The goal is to outperform traditional best-fit algorithms by dynamically optimizing memory block allocation for minimal fragmentation and faster access times.

---

## Problem Statement

Memory allocation inefficiencies, such as internal and external fragmentation, impact the performance of modern systems. Traditional approaches like best-fit can leave memory in a fragmented state, reducing usable space over time. By leveraging TSP-inspired algorithms, this project seeks to ensure:
- Reduced fragmentation.
- Faster memory access times.
- Improved overall memory utilization.

---

## Planning

### Algorithm Overview

1. **Nearest Neighbor (NN) Algorithm**  
   - Start with an initial memory block and allocate the nearest block until all requests are fulfilled.

2. **2-Opt Algorithm**  
   - Begin with a random memory allocation sequence and iteratively optimize it by swapping two blocks to find a more efficient sequence.

3. **Christofides Algorithm**  
   - Use heuristics such as minimum spanning trees and Eulerian circuits to achieve near-optimal memory allocation.

---

## Procedure

1. **Define Memory Blocks**  
   - Specify memory blocks with attributes such as size, status (allocated/free), and location.

2. **Apply TSP-Based Algorithms**  
   - Use the selected TSP algorithms to determine an optimal sequence for allocating memory blocks.

3. **Simulate Memory Allocation**  
   - Test the allocation sequence on a series of memory requests, ensuring minimal fragmentation.

4. **Measure Performance**  
   - Compare TSP-based algorithms against traditional methods using metrics such as:
     - **Access Time**: Time required to allocate or access memory.
     - **Memory Utilization**: Percentage of memory used efficiently.
     - **Fragmentation**: Amount of memory wasted due to fragmentation.

---

## Features

- Implements TSP-inspired algorithms for dynamic memory allocation optimization.
- Simulates real-world memory allocation scenarios with requests for allocation and deallocation.
- Provides a comparative analysis of TSP algorithms and traditional methods (e.g., best-fit).

---

## Technologies Used

- **Programming Language**: Python
- **Algorithms**: Nearest Neighbor, 2-Opt, Christofides
- **Libraries**: NumPy, Matplotlib, SciPy (for simulations and analysis)

---

## Getting Started

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/sms32/optimized-memory-allocation
   cd optimized-memory-allocation

2. **Run the Simulation**
Execute the main script to test memory allocation:
```
   python main.py
```

## Future Enhancements

- Incorporate machine learning for adaptive algorithm selection based on workload.
- Expand the simulation to include real-world data sets and memory management scenarios.
- Optimize algorithm implementations for larger-scale memory systems.

## Result
<img src="https://github.com/user-attachments/assets/d96db281-3283-4764-918a-0a82e53e3ae1" width="1000" height="500">

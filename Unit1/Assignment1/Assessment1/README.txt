============================================================
DESIGN AND ANALYSIS OF ALGORITHMS – ASSIGNMENT 1
SCALABILITY AUDIT OF AN E-COMMERCE PLATFORM
============================================================

1. PROJECT INFORMATION
----------------------

Course Name    : Design and Analysis of Algorithms
Course Code    : CSA06
Assessment     : CO1 – Assessment Tool 1
Assignment     : IT Application-Based Problem Solving
Project Title  : Scalability Audit of an E-Commerce Platform
Platform Name  : ShopSphere

2. PROJECT OVERVIEW
-------------------

This project analyzes the efficiency and scalability of the backend
modules of an e-commerce platform named ShopSphere.

The platform manages a large product catalogue, processes API
requests, searches for products, generates recommendations, and
performs sales analytics.

The initial catalogue contains 100,000 products and may grow to
1,000,000 products. Therefore, it is important to analyze the
time complexity, space complexity, operation counts, and estimated
execution time of each module.

The main objective is to identify inefficient algorithms and
recommend suitable improvements for handling larger datasets.

3. PROJECT OBJECTIVES
---------------------

1. Identify the input size and basic operation of each module.
2. Calculate the exact number of operations where possible.
3. Determine time and auxiliary space complexities.
4. Solve recurrence relations using substitution and the
   Master Theorem.
5. Compare sequential search and binary search.
6. Analyze best-case, average-case, and worst-case performance.
7. Prove asymptotic bounds using Big-O and Theta notation.
8. Estimate execution times for large product catalogues.
9. Check whether the modules fit within the nightly processing
   window.
10. Recommend algorithmic improvements to increase scalability.

4. MODULE DESCRIPTION
---------------------

M1 – DUPLICATE-LISTING DETECTOR

Purpose:
Identifies duplicate product listings using product titles and
seller names.

Algorithm:
Compares each product with the remaining products in the catalogue.

Complexity:
Time Complexity: Θ(n²)
Auxiliary Space: Θ(1), excluding duplicate marks and output storage.

Improvement:
Use a hash-based data structure with the product title and seller
as the key to reduce expected processing time to Θ(n).

M2 – API RATE LIMITER

Purpose:
Audits API requests using a loop whose counter doubles after each
iteration.

Algorithm:
The counter starts at 1 and doubles until it becomes greater than
or equal to n. Each iteration performs a number of audit operations
equal to the current counter.

Complexity:
Time Complexity: Θ(n)
Auxiliary Space: Θ(1)

Important Result:
The total audit count is a geometric series, not n log n.
For n = 1,024, the exact number of audit operations is 1,023.

M3 – PRODUCT SEARCH

Purpose:
Finds a target product in the product catalogue.

Algorithms:
S1 – Sequential Search
S2 – Binary Search

Sequential Search:
Scans products one by one until the target is found or the list
ends.

Time Complexity:
Best Case: Θ(1)
Average Case: Θ(n)
Worst Case: Θ(n)

Binary Search:
Searches a sorted product index by repeatedly dividing the search
range into two halves.

Time Complexity:
Best Case: Θ(1)
Average and Worst Cases: Θ(log n)

Auxiliary Space:
Iterative Binary Search: Θ(1)
Recursive Binary Search: Θ(log n)

Improvement:
Maintain a sorted product index to support efficient binary search.

M4 – RECOMMENDATION ENGINE

Purpose:
Analyzes product data to generate recommendations.

Current Design:
T(n) = 4T(n/2) + n

Time Complexity:
Θ(n²)

Redesigned Version:
T(n) = 2T(n/2) + n

Time Complexity:
Θ(n log n)

Improvement:
Reduce unnecessary replication and optimize the processing of
subproblems to improve scalability.

M5 – SALES ANALYTICS ENGINE

Purpose:
Processes sales data and generates analytical results.

Recurrence:
T(n) = 2T(n/2) + n log n

Time Complexity:
Θ(n log² n)

Separate Report Generator:
f(n) = 3n² + 10n log n + 50

Asymptotic Complexity:
Θ(n²)

Improvement:
Optimize report generation and consider incremental processing
to avoid repeating expensive calculations.

5. INPUT DATA AND ASSUMPTIONS
-----------------------------

Initial Catalogue Size : 100,000 products
Future Catalogue Size  : 1,000,000 products
Operation Rate        : 10 basic operations per second
Nightly Processing    : 10 minutes
Maximum Operations    : 6,000 basic operations

The running-time estimates use the operation rate specified in
the assignment. Actual execution time may differ depending on
hardware, programming language, and implementation details.

Recurrence calculations that require powers of two may use the
next power of two as an approximation when the input size is not
a power of two. Such estimates should be identified accordingly.

6. ALGORITHMIC ANALYSIS
-----------------------

The assignment uses the following concepts:

1. Time Complexity:
   Measures how the number of operations grows with input size.

2. Space Complexity:
   Measures the additional memory required by an algorithm.

3. Big-O Notation:
   Represents an asymptotic upper bound.

4. Theta Notation:
   Represents a tight asymptotic bound.

5. Recurrence Relations:
   Describe the running time of recursive algorithms.

6. Master Theorem:
   Helps solve recurrence relations of the form
   T(n) = aT(n/b) + f(n), when its conditions apply.

7. Best, Average, and Worst Cases:
   Describe algorithm performance under different input conditions.

7. NIGHTLY PROCESSING ANALYSIS
------------------------------

The nightly processing window is 10 minutes.

Given:
10 basic operations per second

Available operations:
10 × 10 × 60 = 6,000 operations

Each module's estimated operation count must be compared with
6,000 operations to determine whether it fits the processing window.

Quadratic algorithms become expensive as the catalogue grows.
Therefore, M1 and the current M4 design require particular
attention. The final conclusion should be based on the calculated
operation counts and clearly stated assumptions.

8. EXPECTED DELIVERABLES
------------------------

The repository contains the following assignment materials:

1. README.txt
   Project overview, objectives, module descriptions, assumptions,
   and repository information.

2. calculations.py
   Python program used to verify operation counts and complexity
   calculations.

3. Output.txt
   Text file containing the output generated by the Python program.

4. Pseudocode.txt
   Pseudocode describing the main algorithms and modules.

5. Solution_Report.pdf
   Detailed answers, derivations, recurrence solutions, complexity
   proofs, execution-time estimates, and recommendations.

6. Output.png
   Screenshot of the actual program output, if required.

7. calculations.ipynb
   Optional Google Colab notebook containing the code and execution
   results.

9. HOW TO RUN THE PYTHON PROGRAM
--------------------------------

Option 1 – Google Colab:

1. Open Google Colab.
2. Create a new notebook.
3. Paste the contents of calculations.py into a code cell.
4. Run the cell.
5. Review the generated operation counts and complexity results.
6. Save the output as Output.txt if required.

Option 2 – Local Python Environment:

1. Install Python 3.
2. Open a terminal in the folder containing calculations.py.
3. Run the command:

   python calculations.py

4. Review the output displayed in the terminal.

10. RECOMMENDATIONS
-------------------

1. Replace the nested duplicate-comparison algorithm with hashing.
2. Use binary search on a properly maintained sorted index.
3. Reduce unnecessary replication in the recommendation engine.
4. Optimize sales analytics and report generation.
5. Consider incremental processing for large datasets.
6. Compare operation estimates with the nightly processing limit.
7. Validate all calculations before including them in the final report.
8. Clearly distinguish theoretical operation estimates from actual
   measured execution times.

11. CONCLUSION
--------------

This assignment evaluates the scalability of five important
e-commerce backend modules using algorithm analysis.

The analysis demonstrates that algorithm selection has a major
impact on performance as the product catalogue grows. Quadratic
algorithms require particular attention, while logarithmic and
near-linear approaches generally scale more efficiently.

The results and recommendations can help improve ShopSphere's
processing efficiency and support future catalogue growth.

============================================================
END OF README
============================================================

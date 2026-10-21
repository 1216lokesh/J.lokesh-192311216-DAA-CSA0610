DAA ASSIGNMENT 2 — README
Design and Analysis of Algorithms (DAA)
Questions 1–7 | Python Implementation and Pseudocode

============================================================
1. PROJECT OVERVIEW
============================================================

This project contains implementations and pseudocode for seven
Design and Analysis of Algorithms (DAA) problems. The programs
demonstrate sorting, searching, string matching, computational
geometry, exhaustive search, and divide-and-conquer techniques.

The project is intended for academic learning and algorithm analysis.
It reports outputs such as sorted arrays, search positions, comparison
counts, closest point pairs, distances, and selected packages.

============================================================
2. FILES INCLUDED
============================================================

1. DAA_Assignment_2_All_Codes.py
   Contains the Python implementations for Questions 1–7.

2. DAA_Assignment_2_All_Pseudocodes.txt
   Contains pseudocode for the algorithms in Questions 1–7.

3. README.txt
   Describes the project, its algorithms, how to run the programs,
   and how to understand their outputs.

4. All_Outputs.txt (optional generated output file)
   May be created if the code is adapted to save program output to a
   text file. The Python file provided prints output to the console by
   default; it does not automatically create All_Outputs.txt.

============================================================
3. SOFTWARE REQUIREMENTS
============================================================

- Python 3.8 or later is recommended.
- Google Colab, IDLE, PyCharm, or Visual Studio Code can be used.
- No third-party Python packages are required. The code uses standard
  Python modules such as math, random, time, and itertools.

============================================================
4. QUESTIONS AND ALGORITHMS
============================================================

Q1. Sorting Algorithm Comparison
Algorithms:
- Selection Sort
- Bubble Sort
- Insertion Sort

Purpose:
Sorts test arrays and compares the number of element comparisons and
swaps or movements. The test datasets include reverse-sorted,
nearly-sorted, and duplicate-value arrays.

Typical time complexity:
- Selection Sort: O(n^2)
- Bubble Sort: O(n^2) worst case; the early-stop version can finish
  in O(n) when the array is already sorted.
- Insertion Sort: O(n^2) worst case; O(n) best case for an already
  sorted array.

Q2. Sequential Search
Purpose:
Checks each list element from the beginning until the target is found
or the list ends. It reports the target index and number of comparisons.

Time complexity:
- Best case: O(1)
- Average and worst case: O(n)

Q3. Brute-Force String Matching
Purpose:
Slides a pattern across a text and compares characters at each
possible starting position. It reports the first matching position,
or that the pattern was not found, and the character comparison count.

Time complexity:
- Worst case: O((n - m + 1) × m), where n is the text length and m
  is the pattern length.
- Commonly written as O(nm).

Q4. Brute-Force Closest Pair of Points
Purpose:
Checks every pair of points and calculates their Euclidean distance.
It returns the closest pair, the minimum distance, and the number of
distance calculations.

Time complexity:
- O(n^2), because every pair is checked.
- The number of pairs is n(n - 1) / 2.

Q5. Brute-Force Convex Hull
Purpose:
Examines pairs of points and tests whether all other points lie on
one side of the line through the pair. Candidate boundary points are
collected and ordered around the boundary.

Time complexity:
- The straightforward triple-loop approach is O(n^3), excluding the
  final ordering step.
- Ordering the hull points adds sorting work.

Q6. Exhaustive Package Selection (0/1 Knapsack)
Purpose:
Checks every possible subset of packages. A subset is considered
valid when its total weight does not exceed the capacity. The valid
subset with the greatest total value is selected.

Time complexity:
- O(n × 2^n), because all 2^n subsets are checked and each subset
  may inspect n packages.
- This approach is suitable for small input sizes, not large datasets.

Q7. Divide-and-Conquer Closest Pair of Points
Purpose:
Sorts points by x-coordinate, divides them into halves, solves each
half recursively, and checks points close to the dividing line.

Implementation note:
The provided Python implementation sorts the strip by y-coordinate
at each recursive call. Therefore, its expected time complexity is
O(n log^2 n), rather than the optimized O(n log n) version.

============================================================
5. HOW TO RUN THE PYTHON PROGRAM
============================================================

OPTION A — Google Colab
1. Download DAA_Assignment_2_All_Codes.py.
2. Open https://colab.research.google.com/.
3. Create a new notebook.
4. Upload the Python file using the Files panel, or copy its code
   into a code cell.
5. If the file is uploaded, run it with:

   %run /content/DAA_Assignment_2_All_Codes.py

6. Run the cell and review the output for Q1 through Q7.

OPTION B — Visual Studio Code
1. Install Python 3 if it is not already installed.
2. Open the folder containing the .py file in VS Code.
3. Open a terminal in that folder.
4. Run:

   python DAA_Assignment_2_All_Codes.py

   On some Windows systems, use:

   py DAA_Assignment_2_All_Codes.py

5. Review the results printed in the terminal.

OPTION C — Command Prompt or Terminal
1. Change directory to the folder containing the file.
2. Run:

   python DAA_Assignment_2_All_Codes.py

============================================================
6. HOW TO READ THE OUTPUT
============================================================

Q1:
Shows each input dataset and the sorted result from each algorithm,
along with comparison counts and swaps/movements.

Q2:
Shows whether each target was found, its zero-based index if found,
and the number of comparisons. Index 0 means the first element.

Q3:
Shows the text, pattern, first matching position if present, and
the number of character comparisons. Position 0 means the first
character of the text.

Q4:
Shows the closest pair of points, their Euclidean distance, the
number of pairwise distance calculations, and sample timing results
for larger randomly generated datasets.

Q5:
Shows the sample input points and the points identified as the
convex hull boundary. Points inside the hull are not boundary points.

Q6:
Shows the selected package names, total weight, and total value.
The total weight will not exceed the stated capacity.

Q7:
Shows the closest pair and minimum distance using the divide-and-
conquer method.

Note:
Timing measurements depend on the computer or Colab runtime and may
vary between runs. Random test data may also change unless a fixed
random seed is used.

============================================================
7. HOW TO RUN OR USE THE PSEUDOCODE
============================================================

The pseudocode file is a language-independent description of the
algorithms. It is provided for reading, reporting, and comparison
with the Python implementations. It is not directly executable by
Python. Use the .py file to run the algorithms.

============================================================
8. UPLOADING THE PROJECT TO GITHUB
============================================================

1. Create or open your GitHub repository.
2. Add the following files:
   - DAA_Assignment_2_All_Codes.py
   - DAA_Assignment_2_All_Pseudocodes.txt
   - README.txt
3. Commit the files with a clear message, for example:
   "Add DAA Assignment 2 algorithms and pseudocode"

If using Git from a terminal, run these commands from the project
folder after creating or cloning your repository:

   git add DAA_Assignment_2_All_Codes.py
   git add DAA_Assignment_2_All_Pseudocodes.txt
   git add README.txt
   git commit -m "Add DAA Assignment 2 algorithms and pseudocode"
   git push

If the repository has not yet been connected to a remote, configure
the repository's GitHub remote URL before running git push.

============================================================
9. EXPECTED PROJECT LEARNING OUTCOMES
============================================================

After completing this project, a student should be able to:
- Implement and compare basic sorting algorithms.
- Explain sequential search and brute-force string matching.
- Measure the cost of checking all pairs of points.
- Describe the basic brute-force convex hull approach.
- Explain exhaustive search for the 0/1 knapsack problem.
- Describe recursive divide-and-conquer for closest-pair problems.
- Relate algorithm design choices to time complexity.

============================================================
10. IMPORTANT NOTES
============================================================

- The program uses zero-based indexing for search and string positions.
- The code's operation counts follow the counting rules implemented
  in each function; different textbooks may count operations differently.
- Exhaustive package selection has exponential running time and should
  be tested with small numbers of packages.
- The convex hull code is a simple educational brute-force approach;
  special cases involving many collinear points may need extra care
  depending on the exact definition required by the assignment.
- The divide-and-conquer closest-pair implementation is educational
  and uses O(n log^2 n) expected time because it re-sorts each strip.
- Verify that the question statements and sample inputs match your
  instructor's assignment before submitting.

END OF README

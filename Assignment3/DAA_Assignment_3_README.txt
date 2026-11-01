README — DAA ASSIGNMENT 3 (CO3)
Design and Analysis of Algorithms | Pair Work | Total: 50 Marks

PROJECT FILES
- DAA_Assignment_3_All_Codes.py: Python implementations and experiments.
- DAA_Assignment_3_All_Pseudocodes.txt: pseudocode for Q1–Q6.
- DAA_Assignment_3_README.txt: this guide.
- DAA_Assignment_3_All_Outputs.pdf: consolidated outputs.

ASSIGNMENT COVERAGE
Q1 (6 marks): Pairwise tournament Max/Min and Binary Search, with comparisons.
Q2 (7 marks): Merge Sort and Quick Sort (last-element pivot), partition sizes,
comparisons, and maximum recursion depth on balanced-style and unbalanced data.
Q3 (7 marks): Standard recursive multiplication and Karatsuba, correctness,
base multiplication counts, and repeated timing by digit length.
Q4 (7 marks): Conventional and Strassen matrix multiplication, zero-padding,
cutoff, correctness, multiplication counts, and timings.
Q5 (6 marks): Brute-force and divide-and-conquer closest pair, with equivalent
datasets, distance calculations, and timing.
Q6 (7 marks): QuickSelect versus Median of Medians for k-th smallest; Meet-in-
the-Middle Subset Sum and comparison with exhaustive subset search.

GOOGLE COLAB
1. Download DAA_Assignment_3_All_Codes.py.
2. Open https://colab.research.google.com/ and create a notebook.
3. Upload the .py file in the Files panel.
4. Run:
   %run /content/DAA_Assignment_3_All_Codes.py
5. Use the actual measured values printed by your Colab run in your report.

VS CODE
Install Python 3.10+, open the project folder and run:
   python DAA_Assignment_3_All_Codes.py

COMPLEXITY SUMMARY
- Pairwise Max/Min: at most ceil(3n/2)-2 comparisons; O(n).
- Binary Search: O(log n), requires sorted input.
- Merge Sort: O(n log n) time, O(n) auxiliary space.
- Quick Sort: average O(n log n), worst O(n^2); depth depends on pivot balance.
- Standard recursive multiplication: O(n^2) digit-level recurrence;
  Karatsuba: O(n^log2(3)) ≈ O(n^1.585).
- Conventional matrix multiplication: O(n^3); Strassen: O(n^log2(7))
  ≈ O(n^2.807), but overhead can dominate small matrices.
- Closest Pair: brute force O(n^2); 2D divide and conquer O(n log n).
- QuickSelect: expected O(n), worst O(n^2); Median of Medians worst-case O(n).
- Meet-in-the-Middle Subset Sum: approximately O(2^(n/2)) time and memory.

EXPERIMENTAL NOTES
Timing varies with hardware, Python version, and system load. Do not copy
timings from another computer. Python's built-in integer multiplication is
highly optimized; the recursive multiplication routines are educational.
Strassen can be slower on small matrices due to recursion, additions,
padding and memory allocation. Quick Sort deliberately uses the last item
as pivot to expose balanced and unbalanced partitions. Coordinates are
treated as 2D Cartesian points. Selection uses zero-based k.

PAIR-WORK REQUIREMENT
Both students must understand all questions. Fill in the partner's name and
registration number. Follow the assignment's alternating individual
responsibilities while jointly implementing and testing every question.

GITHUB
   git add DAA_Assignment_3_All_Codes.py
   git add DAA_Assignment_3_All_Pseudocodes.txt
   git add DAA_Assignment_3_README.txt
   git commit -m "Add DAA Assignment 3 CO3 algorithms"
   git push

END OF README

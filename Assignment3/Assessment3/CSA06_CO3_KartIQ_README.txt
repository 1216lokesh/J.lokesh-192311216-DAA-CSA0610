README — CSA06 CO3: KARTIQ RETAIL DATA ANALYTICS CASE STUDY

Student Name: J. Lokesh
Registration Number: 192311216
Course: CSA06 — Design and Analysis of Algorithms
Outcome: CO3 — Divide and Conquer
Mode: Individual

FILES
1. CSA06_CO3_KartIQ_All_Codes.py — Python implementation and test harness.
2. CSA06_CO3_KartIQ_All_Pseudocodes.txt — pseudocodes and recurrences.
3. CSA06_CO3_KartIQ_README.txt — this guide.
4. CSA06_CO3_KartIQ_All_Outputs.pdf — captured program outputs.

CASE STUDY MODULES
Module 1 — Nightly Order Consolidation:
Stable Merge Sort sorts orders by timestamp and preserves arrival order
when timestamps are equal. The sample order trace and comparison count
are printed by the program. Merge Sort is O(n log n), requires O(n)
auxiliary memory in the usual array implementation. If data does not fit
RAM, use external merge sort: sort memory-sized chunks into runs and
merge those runs sequentially from disk.

Module 2 — Live Seller Leaderboard:
The supplied implementation uses first-element-pivot Quick Sort, which
can create highly unbalanced partitions on already ordered or nearly
ordered data. The code replaces it with randomized three-way Quick Sort.
Expected time is O(n log n), worst case O(n^2), and recursion stack is
O(log n) expected. For nearly sorted data with only a few changed scores,
an adaptive stable sort such as Timsort or an incremental data structure
may be even more suitable. Randomization reduces input-order dependence.

Module 3 — Order Lookup:
Binary search requires the timestamp-sorted list from Module 1.
A lower-bound variant returns the first matching timestamp, including
when multiple orders share that timestamp. Time is O(log n), extra
space O(1). For 10,000,000 records, maximum lower-bound iterations are
about ceil(log2(10,000,001)) = 24, plus a final equality check.

Module 4 — Recommendation Scores:
The code implements Strassen's seven products and reconstruction
expressions, verifies the 2x2 sample, and compares operation counts.
For n=1024, conventional multiplication uses n^3 = 1,073,741,824
scalar multiplications. Strassen uses 7^10 = 282,475,249 scalar
multiplications in the ideal recurrence. Strassen may still be slower
for small matrices due to additions/subtractions, recursion, padding,
memory allocation and cache behaviour. A practical hybrid uses
conventional multiplication below a tuned cutoff and Strassen above it.

HOW TO RUN IN GOOGLE COLAB
1. Download CSA06_CO3_KartIQ_All_Codes.py.
2. Open Google Colab and create a notebook.
3. Upload the Python file through the Files panel.
4. Run:
   %run /content/CSA06_CO3_KartIQ_All_Codes.py
5. The program prints sample traces, comparison estimates and validation.

HOW TO RUN IN VS CODE
Install Python 3.10 or later. Open the folder in VS Code and run:
   python CSA06_CO3_KartIQ_All_Codes.py
Only Python standard-library modules are used.

COMPLEXITY SUMMARY
- Stable Merge Sort: O(n log n) time, O(n) auxiliary memory.
- Randomized three-way Quick Sort: O(n log n) expected, O(n^2) worst.
- First-occurrence Binary Search: O(log n) time, O(1) extra space.
- Strassen: O(n^log2(7)) approximately O(n^2.807); conventional
  multiplication is O(n^3).

DESIGN TRADE-OFFS
- Merge Sort is stable and predictable but needs extra memory. Use external
  merge sort when the order file exceeds RAM.
- Randomized Quick Sort avoids dependence on the first element but still
  has a theoretical quadratic worst case. Use a library introspective sort
  or heap-based strategy when worst-case guarantees are mandatory.
- Binary Search is fast but only works on sorted data. Maintain the
  consolidated sorted index or use a database index if updates dominate.
- Strassen reduces multiplication count but increases additions and
  memory traffic. Raise/lower the cutoff based on measurements on the
  production hardware.

IMPORTANT
Timing depends on the execution environment. Use actual Colab timings if
your instructor requests measured values. The analytical estimates for
10,000,000 records and 1,024 matrices are theoretical calculations.
The assessment is individual; ensure you can explain every module.

GITHUB
   git add CSA06_CO3_KartIQ_All_Codes.py
   git add CSA06_CO3_KartIQ_All_Pseudocodes.txt
   git add CSA06_CO3_KartIQ_README.txt
   git commit -m "Add CSA06 CO3 KartIQ D&C case study"
   git push

END OF README

# DESIGN AND ANALYSIS OF ALGORITHMS
# ASSIGNMENT 1

## PROJECT TITLE
Design, Analyse and Validate an Efficient Search Strategy for a Large-Scale Student Record System

## 1. INTRODUCTION

Searching is an important operation in computer science that helps locate specific information from a collection of data. In educational institutions, student record systems contain details such as student ID, name, department, and academic information. Searching these records efficiently is necessary to provide quick access to student information.

When the number of student records increases, a simple search method may require more time to find a particular record. Therefore, different searching algorithms must be designed, implemented, and analysed to identify an efficient solution.

This project implements and compares Iterative Linear Search, Recursive Binary Search, and Hash-Based Search. Their theoretical time complexities and practical execution times are evaluated using different dataset sizes.

## 2. OBJECTIVES

The main objectives of this project are:

- To design and implement three different searching algorithms.
- To understand iterative and recursive problem-solving approaches.
- To identify the basic operation performed by each algorithm.
- To analyse best-case, average-case, and worst-case time complexities.
- To study asymptotic notations such as Big-O, Big-Omega, and Big-Theta.
- To formulate and solve the recurrence relation for recursive binary search.
- To test the algorithms with datasets of different sizes.
- To compare theoretical complexity with experimental execution time.
- To recommend a suitable searching strategy for a large-scale student record system.

## 3. ALGORITHMS IMPLEMENTED

### 3.1 Iterative Linear Search

Linear Search checks each student record one by one until the target student ID is found or the list ends.

The algorithm does not require sorted data. It is easy to implement and suitable for small or unsorted datasets.

**Time Complexity:**
- Best case: O(1)
- Average case: O(n)
- Worst case: O(n)

**Space Complexity:** O(1) auxiliary space.

### 3.2 Recursive Binary Search

Binary Search repeatedly divides the search range into two halves. It compares the target student ID with the middle record and continues searching only in the relevant half.

The student records must be sorted by student ID before this algorithm is used.

**Time Complexity:**
- Best case: O(1)
- Average case: O(log n)
- Worst case: O(log n)

**Space Complexity:** O(log n) auxiliary space for recursive calls.

Sorting the records separately generally takes O(n log n) time using an efficient comparison-based sorting algorithm.

### 3.3 Hash-Based Search

Hash-Based Search uses a hash table to store student records using student IDs as keys. A hash function helps locate the relevant entry quickly.

After the hash table is constructed, a student record can usually be retrieved without scanning the entire dataset.

**Time Complexity:**
- Average search case: O(1)
- Worst search case: O(n), depending on collisions and implementation.
- Expected hash-table construction time: O(n).

**Space Complexity:** O(n) additional space for storing the hash table.

## 4. SOFTWARE AND TOOLS REQUIRED

The following tools are used in this project:

- **Programming Language:** Python 3
- **Online Coding Platform:** Google Colab
- **Version Control and Code Hosting:** GitHub
- **Data Storage for Results:** CSV file
- **Performance Measurement:** Python time measurement functions
- **Result Analysis:** Execution-time tables and graphs.

Google Colab allows the program to be executed through a web browser without installing Python locally.

## 5. DATASET SIZES

The algorithms are evaluated using the following dataset sizes:

1. 1,000 student records
2. 10,000 student records
3. 100,000 student records
4. 1,000,000 student records

Each student record contains a unique student ID or equivalent search key. The same dataset and target-selection conditions should be used where appropriate to ensure a fair comparison.

## 6. METHODOLOGY

The project follows these steps:

1. Generate student records for each required dataset size.
2. Select a target student ID for searching.
3. Implement Iterative Linear Search.
4. Sort records by student ID and implement Recursive Binary Search.
5. Construct a hash table and implement Hash-Based Search.
6. Measure the execution time of each search operation.
7. Measure preprocessing costs, such as sorting and hash-table construction, separately.
8. Record the experimental results in a CSV file.
9. Compare the measured results with theoretical time complexity.
10. Identify the most appropriate algorithm for the student record system.

For reliable results, repeated measurements and consistent test conditions should be used.

## 7. THEORETICAL ANALYSIS

The theoretical performance of an algorithm describes how its resource requirements change as the input size increases.

### Linear Search

In the worst case, the algorithm checks all n records.

T(n) = O(n)

### Binary Search

In each recursive call, the search range is reduced approximately by half.

T(n) = T(n/2) + O(1)

Solving the recurrence gives:

T(n) = O(log n)

### Hash-Based Search

Hash-table lookup takes expected constant time when the hash function distributes keys effectively and collisions are managed appropriately.

Expected search time = O(1)

However, hash-table construction requires processing the records and generally takes expected O(n) time.

## 8. EXPERIMENTAL PERFORMANCE EVALUATION

The execution times of the three algorithms are recorded for all four dataset sizes.

The results are stored in the file named `results.csv`.

The comparison considers:

- Dataset size.
- Linear search execution time.
- Sorting time.
- Binary search execution time.
- Hash-table construction time.
- Hash-based search execution time.

The experimental results are used to understand how the algorithms behave as the number of records increases.

Actual execution times depend on the computer or online execution environment, implementation details, and the search target. Therefore, measured values should be reported from the program output rather than estimated or invented.

## 9. COMPARISON OF ALGORITHMS

### Linear Search
- Simple to implement.
- Works with sorted and unsorted records.
- Does not require preprocessing.
- Becomes slower as the dataset grows.

### Binary Search
- Efficient for large, sorted datasets.
- Requires records to be sorted by the search key.
- Has logarithmic search complexity.
- Sorting costs should be considered when records are not already sorted.

### Hash-Based Search
- Provides expected constant-time lookup.
- Requires additional memory for the hash table.
- Has a construction cost before searching.
- Is suitable when many searches reuse the same hash table.

## 10. APPLICATION SCENARIO

Consider a student record system containing 1,000,000 records and receiving approximately 50,000 search requests per hour. New records are added once per day.

Since many searches are performed against a dataset that changes relatively infrequently, maintaining a reusable hash table or another indexed data structure may reduce repeated lookup costs.

The final recommendation should consider the experimental results, construction costs, memory requirements, and how the system handles daily updates.

## 11. EXPECTED OUTCOMES

The project is expected to demonstrate that:

- Linear Search has linear worst-case time complexity.
- Binary Search offers logarithmic search time when records are sorted.
- Hash-Based Search provides expected constant-time lookup after preprocessing.
- Preprocessing can affect the total cost of a search strategy.
- Experimental performance should be compared with theoretical analysis.
- The best algorithm depends on dataset size, update frequency, number of searches, and memory constraints.

## 12. CONCLUSION

This project analyses three searching algorithms for a large-scale student record system. Iterative Linear Search provides a simple solution for small or unsorted datasets. Recursive Binary Search is effective when records are maintained in sorted order. Hash-Based Search is a strong candidate when a large number of lookups are performed against a reusable index.

By combining mathematical analysis with experimental measurements, the project evaluates algorithm efficiency and supports an evidence-based recommendation for the given application.

## 13. PROJECT FILES

The repository may contain the following files:

- `assignment1.py` – Python implementation of the searching algorithms.
- `pseudocode.txt` – Pseudocode for the algorithms.
- `results.csv` – Experimental performance measurements.
- `README.txt` – Project description and instructions.
- `Assignment_Report.pdf` – Detailed assignment report.
- `Screenshots/` – Screenshots of program execution and results.

Only files that have actually been created should be included in the final submission.

## 14. HOW TO EXECUTE THE PROJECT

1. Open Google Colab in a web browser.
2. Create a new Python notebook.
3. Copy the program from `assignment1.py` into a code cell.
4. Run the code.
5. Check the execution times displayed by the program.
6. Confirm that `results.csv` is generated successfully.
7. Download the CSV file if required.
8. Upload the source code, pseudocode, results, and final report to the GitHub repository.

## 15. REFERENCES

- Course materials for Design and Analysis of Algorithms.
- Python 3 documentation: https://docs.python.org/3/
- Google Colab: https://colab.research.google.com/
- GitHub documentation: https://docs.github.com/

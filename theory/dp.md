---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
marp: false
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
---

![bg left:35% 70%](https://talently.tech/wp-content/uploads/2019/07/talently-logo-1.svg)

# Recursion and Dynamic Programming

Alexander Ocsa

www.linkedin.com/in/aocsa/

---

# Goals

1. Understand the use of recursion as a tool to solve and analyze computational problems
2. Understand Dynamic Programming (DP) concepts to identify this kinds of problems by recursion
3. Analyze the runtime and space complexity of these solutions

---

# Introduction

Divide-and-conquer algorithms partition the problem into independent subproblems, then solve the subproblems recursively, and finally combine their solution to solve the original problem.

![bg right:70% 80%](http://static1.squarespace.com/static/59d9b2749f8dce3ebe4e676d/59ef45141f318d66e6930c0d/5bb2832a0852291dc258cca0/1538426064716/divide-and-conquer.png)

---

## Divide and conquer: Merge sort

**Divide** array into two subarrays (trivial).
**Conquer** recursively sort each subarray.
**Combine** solutions in linear time.

![bg right:55% 80%](https://www.geeksforgeeks.org/wp-content/uploads/Merge-Sort-Tutorial.png)

$$
\begin{aligned}
   T(n) &= 2 T(n/2) + O(n) \\
   T(n) &= O(n\lg n)
\end{aligned}
$$

---

# Dynamic Programming

- Dynamic programming is a design technique similar to divide-and-conquer.
- Is applicable when the subproblems are not independent, that is, when subproblems share subsubproblems.
- A dynamic-programming algorithms solve every subproblem just one and then saves its answer in a table.
- Thereby avoiding the work of recomputing the answer every time the subsubproblem is encountered.

---

Dynamic Programming
Paradigm: Divide and conquer + Overlapping subproblems + optimal substructure

Methodoly

Memoization

- Top-down approach
  Tabulation
- Botton-up approach

Divide and conquer

Divides a problem into simpler version of itself
Applies solution for smaller subproblem to the larger problem
combines answer to subproblems (recursive)

Dynamic Programming Algorithms

- Breaks a problem down into is subproblems
- The subproblemas are overlapping of recurring; DP will calculate them only once and saver their values
- Sacrifies space to save time by remembering old subproblems values

Dynamic programming is similar to divide & conquer in taht is solves a problem by dividing it into sub-problems. However, in the DP paradigm, the larger problem is solved by solving and remembering overlapping sub-proboems, which are reused repeatdly in the process.

We can use memoization to remember the problems that we have seen before and already solved.

![Alt text](https://miro.medium.com/max/1660/1*kLRo_yTxgPLSEs4V4ILPYQ.jpeg)

![Alt text](https://miro.medium.com/max/1822/1*0qBx2NAsplMp7lRZZwundQ.jpeg)

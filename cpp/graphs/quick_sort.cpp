// divide-and-conquer.cpp : Defines the entry point for the application.
//
#include <vector>
#include <iostream>
#include <algorithm>

int partition(std::vector<int> &A, int begin, int end, int pivot_index) {
// A = [10, 20, 13, 7, 2, 12, 11, 9, 1]
// A = [10, 7, 13, 20, 2, 12, 11, 9, 1]
// A = [10, 7, 2, 20, 13, 12, 11, 9, 1]
// A = [10, 7, 2, 9, 13, 12, 11, 20, 1]
// A = [10, 7, 2, 9, 1, 12, 11, 20, 13]
// A = [1, 7, 2, 9, x, 12, 11, 20, 13]
  std::swap(A[begin], A[pivot_index]);
  int x = A[begin];
  int i = begin;
  for (int j = begin + 1; j <= end; j++) {
    if (A[j] <= x) {
      i++;
      std::swap(A[i], A[j]);
    }
  }
  std::swap(A[i], A[begin]);
  return i;
}

int quick_select(std::vector<int> &A, int begin, int end, int k) {
  if (begin == end) {
    return A[begin];
  }else if (begin < end) {
    int pivot_index = begin; // rand(begin, end)
    int mid = partition(A, begin, end, pivot_index);
    if (mid == k) {
      return A[k];
    }
    if (k < mid) {
      return quick_select(A, begin, mid - 1, k);
    }
    else {
      return quick_select(A, mid + 1, end, k);
    }
  }
}
void quick_sort(std::vector<int>& S, int begin, int end) {
  if (begin < end) {
    int pivot_index = begin; // rand(begin, end)
    int mid = partition(S, begin, end, pivot_index);
    quick_sort(S, begin, mid - 1);
    quick_sort(S, mid+1, end);
  }
}

int main()
{
  std::vector<int> values = { 5, 7, 2, 9, 1 };
  auto median = quick_select(values, 0, values.size() - 1, 0);
  std::cout << "median: " << median << std::endl;

  quick_sort(values, 0, values.size() - 1);

  std::cout << "values: " << values.size() << std::endl;
  for (size_t i = 0; i < values.size(); i++)
  {
    std::cout << values[i] << std::endl;
  } 
  return 0;
}

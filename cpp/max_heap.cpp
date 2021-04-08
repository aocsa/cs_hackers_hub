#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <cstring>


//value of the parent node is greater than or equal to the value of its left and right child.
// We use an array to represent a maxheap. The root element is arr[0]. For an index i we have

// https://i1.wp.com/golangbyexample.com/wp-content/uploads/2019/12/Max-Heap.png?resize=201%2C191&ssl=1

// Arr[i]: 
// Arr[(i-1)/2] Returns the parent node. 
// Arr[(2*i)+1] Returns the left child node. 
// Arr[(2*i)+2] Returns the right child node.
struct MaxHeap  { 
    std::vector<int> heap_array;
    int size;
    int max_size; 
    MaxHeap(int max_size) 
        : heap_array(max_size), max_size{max_size}, size{0} 
    {

    }

    void insert(int item) {
        if (size >= max_size) {
            return ;
        }
        heap_array[size] = item;
        size++;

        int current = size;
        while (heap_array[current] > heap_array[parent(current)]) {
            std::swap(heap_array[current], heap_array[parent(current)]);
            current = parent(current);
        }
    }

    int parent(int index) {
        return index / 2;
    } 

    void print()
    {
        for (int i = 1; i <= size / 2; i++) {
            std::cout <<
                " PARENT : " + std::to_string(heap_array[i])
                + " LEFT CHILD : " + std::to_string(heap_array[2 * i])
                + " RIGHT CHILD :" + std::to_string(heap_array[2 * i + 1]);
            std::cout << std::endl;
        }
    }
  
};

int main(){
    // auto maxHeap = {9,4,7,1,-2,6,5};
    // auto result = {-2,1,5,9,4,6,7};

    MaxHeap maxHeap = new MaxHeap(15);
    maxHeap.insert(5);
    maxHeap.insert(3);
    maxHeap.insert(17);
    maxHeap.insert(10);
    maxHeap.insert(84);
    maxHeap.insert(19);
    maxHeap.insert(6);
    maxHeap.insert(22);
    maxHeap.insert(9);
    maxHeap.print();
}

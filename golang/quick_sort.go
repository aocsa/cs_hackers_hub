package main

import (
	"fmt"
	"math/rand"
)

func partition(arr []int) int {
	pivot_index := rand.Intn(len(arr))
	arr[pivot_index], arr[0] = arr[0], arr[pivot_index]

	// {5, 3, 7, 2, 10}
	// pivot_index = 0
	// x = 5
	// i = 0
	// {5, 3, 7, 2, 10}
	// {5, 3, 7, 2, 10}
	//
	i := 0 // new pivot
	x := arr[pivot_index]
	// skip and increase j if  arr[j] > x and then swap
	// i current less arr[i] <= x
	for j := 1; j < len(arr); j++ {
		if arr[j] <= x {
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
	return i
}

func quick_sort_slices(arr []int) {
	if len(arr) > 0 {
		mid := partition(arr)
		quick_sort_slices(arr[0:mid])
		quick_sort_slices(arr[mid+1:])
	}
}

func quick_sort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	fmt.Println(">>input")
	printArray(arr)
	pivot := arr[0]
	left := []int{}
	right := []int{}
	for i := range arr {
		if i == 0 {
			continue
		}
		if arr[i] < pivot {
			left = append(left, arr[i])
		} else {
			right = append(right, arr[i])
		}
	}
	fmt.Println("left:")
	printArray(left)
	fmt.Println("right:")
	printArray(right)
	l := quick_sort(left)
	r := quick_sort(right)
	t := append(l, pivot)
	z := append(t, r...)
	printArray(z)
	return z
}

func printArray(arr []int) {
	for i := range arr {
		fmt.Print(arr[i], ",")
	}
	fmt.Println()
}

func main() {
	arr := []int{5, 3, 7, 2, 10}
	printArray(arr)

	r := quick_sort(arr)
	fmt.Println("output:")
	printArray(r)

	for i := 0; i < len(r); i++ {
		fmt.Println(i, r[i:])
	}

	arr2 := []int{5, 3, 7, 2, 10}
	printArray(arr2)
	quick_sort_slices(arr2)
	fmt.Println("sorted:")
	printArray(arr2)
}

package main

import (
	"fmt"
)

func merge(arr []int, mid int) []int {
	result := []int{}
	var i, j = 0, mid
	n := len(arr)
	for len(result) < n {
		if arr[i] < arr[j] {
			result = append(result, arr[i])
			i += 1
		} else {
			result = append(result, arr[j])
			j += 1
		}
		if i == mid {
			result = append(result, arr[j:]...)
		}
		if j == n {
			result = append(result, arr[i:mid]...)
		}
	}
	return result
}

func merge_sort(arr []int) {

	if len(arr) > 1 {
		mid := len(arr) / 2
		merge_sort(arr[:mid])
		merge_sort(arr[mid:])
		ret := merge(arr, mid)
		for i := range arr {
			arr[i] = ret[i]
		}
	}
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
	merge_sort(arr)
	fmt.Println("sorted:")
	printArray(arr)
}

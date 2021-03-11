package main

import "fmt"

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
}

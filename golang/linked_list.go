package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

func NewNode(value int) *Node {
	return &Node{
		value: value,
		next:  nil,
	}
}

type LinkedList struct {
	head, tail *Node
}

func NewList() *LinkedList {
	return &LinkedList{
		head: nil,
		tail: nil,
	}
}

func (self *LinkedList) Insert(value int) {
	if self.head == nil {
		self.head = NewNode(value)
		self.tail = self.head
		return
	}
	new_node := NewNode(value)
	var prev_ptr *Node = nil
	ptr := self.head
	for ptr != nil && value > ptr.value {
		prev_ptr = ptr
		ptr = ptr.next
	}
	if prev_ptr != nil {
		prev_ptr.next = new_node
	}
	new_node.next = ptr

	if prev_ptr == nil {
		self.head = new_node
	}
	if ptr == nil {
		self.tail = new_node
	}
}

func (self *LinkedList) Print() {
	ptr := self.head
	for ptr != nil {
		fmt.Print(ptr.value)
		ptr = ptr.next
	}
	fmt.Println()
}

func main() {
	fmt.Println("hello world!")

	l := NewList()
	l.Insert(1)
	l.Insert(0)
	l.Insert(3)
	l.Insert(2)
	l.Print()
}

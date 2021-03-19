package main

import (
	"errors"
	"fmt"
)

type Node struct {
	key        string
	value      int
	next, prev *Node
}

func NewNode(key string, value int) *Node {
	return &Node{
		key:   key,
		value: value,
		next:  nil,
		prev:  nil,
	}
}
func NewEmptyNode() *Node {
	return &Node{
		key:   "0",
		value: 0,
		next:  nil,
		prev:  nil,
	}
}

type LinkedList struct {
	head, tail *Node
}

func NewList() *LinkedList {
	list := &LinkedList{
		head: NewEmptyNode(),
		tail: NewEmptyNode(),
	}
	list.head.next = list.tail
	list.tail.prev = list.head
	return list
}

func (self *LinkedList) insert(new_node *Node, prev *Node, curr *Node) {
	prev.next = new_node
	curr.prev = new_node
	new_node.next = curr
	new_node.prev = prev
}

func (self *LinkedList) first() *Node {
	return self.head.next
}

func (self *LinkedList) push_front(node *Node) {
	self.insert(node, self.head, self.head.next)
}

func (self *LinkedList) remove_last() *Node {
	return self.remove_node(self.tail.prev)
}

func (self *LinkedList) remove_node(ptr *Node) *Node {
	ptr.prev.next = ptr.next
	ptr.next.prev = ptr.prev
	return ptr
}

type LRUCache struct {
	heap *LinkedList
	dicc map[string]*Node
	size int
}

func NewLRUCache(size int) *LRUCache {
	return &LRUCache{
		heap: NewList(),
		dicc: make(map[string]*Node),
		size: size,
	}
}

func (self *LRUCache) Insert(key string, value int) {
	new_node := NewNode(key, value)
	if len(self.dicc) < self.size {
		self.heap.push_front(new_node)
		self.dicc[key] = new_node
	} else {
		self.heap.push_front(new_node)
		self.dicc[key] = new_node
		old_node := self.heap.remove_last()
		delete(self.dicc, old_node.key)
	}
}

func (self *LRUCache) GetValueFromKey(key string) (int, error) {
	if ptr, ok := self.dicc[key]; ok {
		self.heap.remove_node(ptr)
		self.heap.push_front(ptr)
		return ptr.value, nil
	}
	return -1, errors.New("no value for key")
}

func (self *LRUCache) GetMostRecentKey() (string, bool) {
	if len(self.dicc) > 0 {
		return self.heap.first().key, true
	}
	return "", false
}

func main() {
	fmt.Println("hello world!")

	// All operations below are performed sequentially.
	cache := NewLRUCache(3) // instantiate an LRUCache of size 3
	cache.Insert("b", 2)
	cache.Insert("a", 1)
	cache.Insert("c", 3)
	if k, ok := cache.GetMostRecentKey(); ok { //// "c" was the most recently inserted key
		fmt.Println(k)
	}
	cache.GetValueFromKey("a") //: 1
	cache.GetMostRecentKey()   // "a" // "a" was the most recently retrieved key
	cache.Insert("d", 4)       // the cache had 3 entries; the least recently
	cache.GetValueFromKey("b") // None // "b" was evicted in the previous operation
	cache.Insert("a", 5)       // "a" already exists in the cache so its valu
	cache.GetValueFromKey("a") //: 5*/
}

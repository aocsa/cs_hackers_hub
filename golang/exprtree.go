package main

import (
	"fmt"
)

type AbstractNode interface {
	compute() float32
}

type NumberNode struct {
	number float32
	left   AbstractNode
	right  AbstractNode
}

func (self *NumberNode) compute() float32 {
	return self.number
}

type OpNode struct {
	op    string
	left  AbstractNode
	right AbstractNode
}

func (self *OpNode) compute() float32 {
	a := self.left.compute()
	b := self.right.compute()
	switch self.op {
	case "+":
		return a + b

	case "-":
		return a - b

	case "*":
		return a * b

	case "/":
		return a / b
	default:
		fmt.Printf("operator: ", self.op, " not recognized")
	}
	return -1
}

type ExpressionTree struct {
	root AbstractNode
}

// 5*3 + 2 - 6/3
func BuildExpressionTree(expr string) *ExpressionTree {
	left := &OpNode{
		op: "+",
		left: &OpNode{
			op: "*",
			left: &NumberNode{
				number: 5,
			},
			right: &NumberNode{
				number: 3,
			},
		},
		right: &NumberNode{
			number: 2,
		},
	}

	right := &OpNode{
		op: "/",
		left: &NumberNode{
			number: 6,
		},
		right: &NumberNode{
			number: 3,
		},
	}
	tree := &OpNode{
		op:    "-",
		left:  left,
		right: right,
	}
	return &ExpressionTree{
		root: tree,
	}
}

func (self *ExpressionTree) compute() float32 {
	return self.root.compute()
}

func main() {
	expr_tree := BuildExpressionTree("5*3 + 2 - 6/3")
	fmt.Println(expr_tree.compute())
}

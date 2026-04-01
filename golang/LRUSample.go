
package main

import "fmt"

type Node struct {
		prev * Node
		value int
		key string
		next * Node
}

type List struct {
	head *Node
	tail *Node
}

func (l *List) pushFront(newNode *Node)  {
    //fmt.Println("Nuevo nodo : ",newNode.value)

    if l.head == nil && l.tail == nil{
       //creando nodos centinelas
	   l.head = new(Node)
	   l.tail = new(Node)
	   // conexion
	   l.head.next = newNode
	   l.tail.prev = newNode
	   newNode.prev = l.head
	   newNode.next = l.tail

	}else{

		l.head.next.prev = newNode
		newNode.next = l.head.next
		l.head.next = newNode
		newNode.prev = l.head
	}
}

func (l *List) removeRef(ptrNode *Node) *Node{
	ptrNode.prev.next = ptrNode.next
	ptrNode.next.prev = ptrNode.prev
	return ptrNode
}

func (l *List) removeLast() (last *Node) {
	last = l.tail.prev
	return l.removeRef(last)
}

func (l *List) firstValue() (first string){
	first = l.head.next.key
	return first
}

func (l *List) PrintNode(){
	fmt.Println("Printings nodes")
	iter := l.head.next
	for iter.next != nil {
		fmt.Printf("value : %v\n",iter.value)
		iter = iter.next
	}
}


type LRUcache struct {
	 l *List
	 size int
	 dicc map[string] * Node
}

func (LR *LRUcache) initialize(tam int){
	LR.dicc = make(map[string] * Node)
	LR.l = new(List)
	LR.size = tam
}

func (LR *LRUcache) insert(key string, val int){
	if len(LR.dicc) < LR.size {
		newNode := &Node{nil,val,key,nil}
		LR.l.pushFront(newNode)
		LR.dicc[key] = newNode
	}else{
		newNode := &Node{nil,val,key,nil}
		LR.l.pushFront(newNode)
		LR.dicc[key] = newNode
		LR.l.removeLast()
		delete(LR.dicc, key)
	}
}

func (LR *LRUcache) getValueFromKey(key string) int{
	_, prs := LR.dicc[key]
	if prs != false {
		nodetmp := LR.dicc[key]
		LR.l.removeRef(nodetmp)
		LR.l.pushFront(nodetmp)
		return nodetmp.value
	}
	return -1
}

func (LR *LRUcache) getMostRecently() string{
	if len(LR.dicc) >0 {
		return LR.l.firstValue()
	}
	return ""
}

func main() {

     LR := new(LRUcache)
     LR.initialize(3)
     LR.insert("a",10)
	   LR.insert("b",15)
	   LR.insert("c",30)
     LR.insert("a",40)

     fmt.Println(LR.getValueFromKey("b"))//15
     fmt.Println(LR.getMostRecently()) //b

}

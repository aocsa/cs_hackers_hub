#include <memory>
#include <iostream>


template <class T>
class AVLTree{
	private:
		class NodeAVL{
			public:
  				int fe;
				T data;
				NodeAVL* izq,*der;
			public:
				NodeAVL(T dat){
					data = dat;
					izq = der = 0;
					fe = 0;
				}
				~NodeAVL(){
					if(izq)	
						delete(izq);
					if(der)	
						delete(der);
				}
				void print(int level = 0){
					if(der)	der->print(level+1);
					for (size_t i = 0; i < level; i++)
                    {
                        std::cout << "...." ;
                    }
                    std::cout << data << std::endl;
					if(izq)	izq->print(level+1);
				}
			friend class AVLTree<T>;
		};

		NodeAVL* root;
		int balance;

	public:
		class iterator{
			private:
				NodeAVL* current;
			public:
				iterator(NodeAVL* node){	current = node;		}
				iterator(){}
				void move_left(){	current = current->izq;	}
				void move_right(){	current = current->der;	}
				T& operator*(){	return current->data; }
				bool operator==(iterator obj){	return (current==obj.current);	}
		        bool operator!=(iterator obj){	return (current!=obj.current);	}
			    bool isInLef(){	return (current->izq==0 && current->der==0);	}
	     	friend class AVLTree<T>;
		};
		AVLTree();
		~AVLTree();
		iterator begin(){	return root;	}
		void insert(iterator&,T);
		void insert(T data) {
            iterator out;
            insert(out, data); 
        }

		void print(){	root->print();	}
		bool search(iterator&,T);
	protected:
		void rotate_rrr(NodeAVL **);
		void rotate_rl(NodeAVL **);
		void rotate_ll(NodeAVL **);
		void rotate_lr(NodeAVL **);
		void insert(iterator&,NodeAVL*&,T);
		bool search(NodeAVL*&,T);
};

template <class T>
AVLTree<T>::AVLTree(){ root = 0; balance = 0; }

template <class T>
AVLTree<T>::~AVLTree(){ 
	delete(root);
}

template <class T>
void AVLTree<T>::rotate_rrr(NodeAVL** Iterator){
	NodeAVL* tmp = (*Iterator)->der;
	tmp->fe = 0;
	(*Iterator)->fe = 0;
	(*Iterator)->der = tmp->izq;
	tmp->izq = (*Iterator);
	*Iterator = tmp;
}	

template <class T>
void AVLTree<T>::rotate_rl(NodeAVL** Iterator){
	NodeAVL* tmp = (*Iterator)->der->izq;

	switch(tmp->fe){
			case -1:	(*Iterator)->fe = 0;	(*Iterator)->der->fe = 1;	break;
			case 0:		(*Iterator)->fe = 0;	(*Iterator)->der->fe = 0;	break;
			case 1:		(*Iterator)->fe = -1;	(*Iterator)->der->fe = 0;	break;
	}
	tmp->fe = 0;

	(*Iterator)->der->izq = tmp->der;
	tmp->der = (*Iterator)->der;
	(*Iterator)->der = tmp->izq;
	tmp->izq = (*Iterator);
	*Iterator = tmp;
}

template <class T>
void AVLTree<T>::rotate_ll(NodeAVL** Iterator){
	NodeAVL* tmp = (*Iterator)->izq;
	tmp->fe = 0;
	(*Iterator)->fe = 0;
	(*Iterator)->izq = tmp->der;
	tmp->der = (*Iterator);
	*Iterator = tmp;
}

template <class T>
void AVLTree<T>::rotate_lr(NodeAVL** Iterator){
	NodeAVL* tmp = (*Iterator)->izq->der;
	switch(tmp->fe){
		case -1:	(*Iterator)->izq->fe = 0;		(*Iterator)->fe = 1;	break;
		case 0:		(*Iterator)->izq->fe = 0;		(*Iterator)->fe = 0;	break;
		case 1:		(*Iterator)->izq->fe = -1;		(*Iterator)->fe = 0;	break;
	}
	tmp->fe = 0;
	
	(*Iterator)->izq->der = tmp->izq;
	tmp->izq = (*Iterator)->izq;
	(*Iterator)->izq = tmp->der;
	tmp->der = (*Iterator);
	*Iterator = tmp;
}

template <class T>
void AVLTree<T>::insert(iterator& obj,T data){
	obj = NULL;
	insert(obj,root,data);
}

template <class T>
void AVLTree<T>::insert(iterator& object,NodeAVL*& Iterador,T data){
	if(Iterador==NULL){
		Iterador = new NodeAVL(data);
		balance = 1;
		object = Iterador;
	}
	else
		if(Iterador->data>data){
			insert(object,Iterador->izq,data);
			if(balance==1){
				Iterador->fe--;
				if(Iterador->fe==0)	balance = 0;
				if(Iterador->fe==-2){
					if(Iterador->izq->fe==1)	rotate_lr(&Iterador);
					else	rotate_ll(&Iterador);
					balance = 0;
				}
			}
		}
		else
			if(Iterador->data<data){
				insert(object,Iterador->der,data);
				if(balance==1){
					Iterador->fe++;
					if(Iterador->fe==0)	balance = 0;
					if(Iterador->fe==2){
						if(Iterador->der->fe==1)	rotate_rrr(&Iterador);
						else	rotate_rl(&Iterador);
						balance = 0;
					}
				}
			}
			else{
				balance = 0;
				object = Iterador;
			}
}

template <class T>
bool AVLTree<T>::search(iterator& obj,T data){
	return (search(obj.current,data));
}

template <class T>
bool AVLTree<T>::search(NodeAVL*& iterador,T data){
	while(iterador)
		if(iterador->data>data)	iterador = iterador->izq;
		else if(iterador->data<data)	iterador = iterador->der;
		else return true;
	return false;
}


 int main() {
    AVLTree<int> tree;
    for (size_t i = 0; i < 10; i++)
    {
        /* code */
        tree.insert(i);
        tree.print();
        std::cout << "**************************************\n";
    }
    return 0;
 }
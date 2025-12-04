class Node{
    int data;
    Node next;
    Node(int value){
        data=value;
        next = null;
    }
}
class stack{
    Node top;
    stack(){
        top=null;
    }
    void push(int value){
        Node newNode= new Node(value);
        newNode.next=top;
        top=newNode;
        System.out.println(value+"pushed to stack");
    }
    int pop(){
        if(top==null){
            System.out.println("stack underflow");
            return -1;
        }
        int popped=top.data;
        top=top.next;
        System.out.println(popped+"popped from stack");
        return popped;
    }
    int peek(){
        if(top==null){
            System.out.println("stack is empty");
            return -1;
        }
        return top.data;
    }
    boolean isEmpty(){
        return top==null;
    }
    void display(){
        if (top==null) {
            System.out.println("empty");
            return;
        }
        System.out.println("stack elements");
        Node curr=top;
        while (curr!=null) {
            System.out.println(curr.data+"");
            curr=curr.next;
        }
        System.out.println();
    }
}
public class StackLinkedList {
    public static void main(String[] args) {
        stack s = new stack();
        s.push(10);
        s.push(20);
        s.push(30);
        s.display();
        System.out.println(s.peek());
        s.pop();
        s.display();
        System.out.println(s.isEmpty());
        s.pop();
        s.pop();
        s.pop();
    }
}

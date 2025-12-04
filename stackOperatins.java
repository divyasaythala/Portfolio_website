class StackOperations{
    int top;
    int maxsize;
    int[] arr;
    StackOperations(int size){
        maxsize=size;
        arr=new int[maxsize];
        top=-1;
    }
    void push(int value){
        if(top==maxsize-1){
            System.out.println("stack overflow");
        }else{
            arr[++top]=value;
            System.out.println(value+"push to stack");
        }
    }
    int pop(){
        if (top==-1) {
            System.out.println("stack underflow");
            return -1;
        }else{
            int popped = arr[top--];
            System.out.println(popped+"popped from stack");
            return popped;
        }
    }
    int peek(){
        if (top==-1) {
            System.out.println("stack is empty");
            return -1;
        }
        return arr[top];
    }
    boolean isEmpty(){
        return top==-1;
    }
    int size(){
        if (top==-1) {
            System.out.println("empty");
            return -1;
        }
        return arr.length;
    }
    void display(){
        if (top==-1) {
            System.out.println("empty");
            return;
            
        }
        System.out.println("stack elements:");
        for (int i = 0; i <  top+1; i++) {
            System.out.println(arr[i]+" ");
        }
        System.out.println();
    }
}
public class stackOperatins {
    public static void main(String[] args){
        StackOperations s = new StackOperations(5);
        s.push(10);
        s.push(20);
        s.push(30);
        s.display();
        System.out.println("top element:"+s.peek());
        s.isEmpty();
        s.pop();
        s.display();
        s.pop();
        s.pop();
        s.pop();


    }
    
}

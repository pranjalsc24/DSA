// class MyQueue {
//     private Stack<Integer> inStack;
//         private Stack<Integer> outStack;
//     public MyQueue() {
//         inStack = new Stack<>();
//         outStack = new Stack<>();
//     }
    
//     public void push(int x) {
//        inStack.push(x); 
//     }
    
//     public int pop() {
//         if (outStack.isEmpty()) {
//             while (!inStack.isEmpty()) {
//                 outStack.push(inStack.pop());
//             }
//         }
        
//         return outStack.pop();
//     }
    
//     public int peek() {
//         if (outStack.isEmpty()) {
//             while (!inStack.isEmpty()) {
//                 outStack.push(inStack.pop());
//             }
//         }
//         return outStack.peek();
//     }
    
//     public boolean empty() {
//          return inStack.isEmpty() && outStack.isEmpty();
//     }
// }

// /**
//  * Your MyQueue object will be instantiated and called as such:
//  * MyQueue obj = new MyQueue();
//  * obj.push(x);
//  * int param_2 = obj.pop();
//  * int param_3 = obj.peek();
//  * boolean param_4 = obj.empty();
//  */










// class MyQueue(object):
//     def __init__(self):
//         self.in_stk = []
//         self.out_stk = []
// 	# Push element x to the back of queue...
//     def push(self, x):
//         self.in_stk.append(x)
// 	# Remove the element from the front of the queue and returns it...
//     def pop(self):
//         self.peek()
//         return self.out_stk.pop()
// 	# Get the front element...
//     def peek(self):
//         if not self.out_stk:
//             while self.in_stk:
//                 self.out_stk.append(self.in_stk.pop())
//         return self.out_stk[-1]
// 	# Return whether the queue is empty...
//     def empty(self):
//         return not self.in_stk and not self.out_stk
// # Your MyQueue object will be instantiated and called as such:
// # obj = MyQueue()
// # obj.push(x)
// # param_2 = obj.pop()
// # param_3 = obj.peek()
// # param_4 = obj.empty()
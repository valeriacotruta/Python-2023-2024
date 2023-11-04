from Stack import Stack
from Queue import Queue
from Matrix import Matrix

stack = Stack()
stack.push(1)
stack.push(12)
stack.push(123)
print("Actual state of the stack:", stack.get_stack())
stack.pop()
print("Actual state of the stack:", stack.get_stack())
print("The element from the top: ", stack.peek())
stack.pop()
stack.pop()
print("Actual state of the stack:", stack.get_stack())
print("The element from the top: ", stack.peek(), "\n")

queue = Queue()
queue.push(1)
queue.push(12)
queue.push(123)
print("Actual state of the queue:", queue.get_queue())
queue.pop()
print("Actual state of the queue:", queue.get_queue())
print("The head element: ", queue.peek(), "\n")

N = 2
M = 2
matrix = Matrix(N, M)
matrix.set_element(0, 0, 1)
matrix.set_element(0, 1, 3)
matrix.set_element(1, 0, 4)
matrix.set_element(1, 1, 2)

print("New state of the matrix:")
matrix.print_matrix(None)

transposed_matrix = matrix.transpose()
print("Transposed matrix: ")
matrix.print_matrix(transposed_matrix)

print("The result of multiplication: ")
matrix.print_matrix(matrix.multiply_with(transposed_matrix))


def multiply_by_2(element):
    return lambda x: x * element


print("Apply function on matrix:")
matrix.print_matrix(matrix.apply_function(multiply_by_2(2)))


import DS.Stack as Stack
import DS.Queue as Queue
import FormatString as Format
import error as e

# class to convert infix expression to postfix expression.

class InfixToPostfix(e.Error):
    def __init__(self, expr: str):
        super().__init__()
        f = Format.FormatString(expr)
        f.remove_space()
        f.format_number()
        f.to_int()
        self.__expr = f.get_expr()
        self.__operator_stack = Stack.Stack()
        self.__output_queue = Queue.Queue()
        self.__operators = ('+', '-', '*', '/', '^')
        self.__postfix_expr = list()
        self.__precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
        self.__associativity = {'^': 'RIGHT', '*': 'LEFT', '/': 'LEFT', '+': 'LEFT', '-': 'LEFT'}

    def get_expr(self):
        return self.__expr

    def set_expr(self, expr):
        f = Format.FormatString(expr)
        f.remove_space()
        f.format_number()
        f.to_int()
        self.__expr = f.get_expr()
        self.__operator_stack = Stack.Stack()
        self.__output_queue = Queue.Queue()
        self.__postfix_expr = list()

    def get_postfix_expr(self) -> list:
        return self.__postfix_expr

    def ERROR(self, statement: str) -> None:
        print(statement)

    # method to get postfix expr as string
    def get_postfix_expr_str(self) -> str:
        postfix_expr = str()
        for token in self.__postfix_expr:
            if len(token) > 1:
                postfix_expr += '(' + token + ')'
            else:
                postfix_expr += token
        return postfix_expr

    # method to convert infix to postfix expression
    def convert(self):
        for token in self.__expr:
            if Format.is_real_num(token):
                self.__output_queue.enqueue(token)
            elif token in self.__operators:
                while (self.__operator_stack.count() != 0) and (self.__operator_stack.peek() != '(') and \
                        (self.__precedence.get(self.__operator_stack.peek()) >= self.__precedence.get(token)) and \
                        (self.__associativity.get(token) == 'LEFT'):
                    s = self.__operator_stack.pop()
                    self.__output_queue.enqueue(s)
                self.__operator_stack.push(token)
            elif token == '(':
                self.__operator_stack.push(token)
            elif token == ')':
                while (self.__operator_stack.count() != 0) and (self.__operator_stack.peek() != '('):
                    if self.__operator_stack.count() == 1:
                        self.ERROR("mismatched parenthesis")
                        break
                    else:
                        op = self.__operator_stack.pop()
                        self.__output_queue.enqueue(op)
                if self.__operator_stack.peek() == '(':
                    self.__operator_stack.pop()
            else:
                self.ERROR("Invalid expression")
                break
        while self.__operator_stack.count() != 0:
            if self.__operator_stack.peek() == '(':
                self.ERROR("Mismatched parenthesis")
                break
            else:
                op = self.__operator_stack.pop()
                self.__output_queue.enqueue(op)
        while self.__output_queue.count() != 0:
            element = self.__output_queue.dequeue()
            self.__postfix_expr.append(element)


# test code
if __name__ == '__main__':
    e = input("Enter the expr: ")
    converter = InfixToPostfix(e)
    print("formatted expr = ", converter.get_expr())
    print("postfix expr = ", converter.get_postfix_expr())
    converter.set_expr(e)
    print("expr after set using setter() = ", converter.get_expr())
    print("postfix expr = ", converter.get_postfix_expr())
    converter.convert()
    print("expr after called convert() = ", converter.get_expr())
    print("postfix expr after convert() = ", converter.get_postfix_expr())
    print("postfix expr str = ", converter.get_postfix_expr_str())

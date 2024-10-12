from typing import Any

from FormatString import is_real_num
import DS.Stack as Stack

import InfixToPostfix as ItoP


# class to evaluate postfix expression.

class PostfixEvaluator(ItoP.InfixToPostfix):
    def __init__(self, postfix_expr: list, infix_expr=""):
        super().__init__(infix_expr)
        self.__postfix_expr = postfix_expr
        self.__stack = Stack.Stack()
        self.__result = float()

    def set_postfix_expr(self, expr):
        self.__postfix_expr = expr
        self.__stack = Stack.Stack()
        self.__result = float()

    def get_result(self) -> float:
        return self.__result

    def ERROR(self, statement: str) -> None:
        print(statement)

    def evaluate(self) -> float | None | Any:
        for token in self.__postfix_expr:
            if is_real_num(token):
                operand = float(token)
                self.__stack.push(operand)
            else:
                operator = token
                if self.__stack.count() >= 2:
                    match operator:
                        case '+':
                            op2 = self.__stack.pop()
                            op1 = self.__stack.pop()
                            self.__result = op1 + op2
                            self.__stack.push(self.__result)
                        case '-':
                            op2 = self.__stack.pop()
                            op1 = self.__stack.pop()
                            self.__result = op1 - op2
                            self.__stack.push(self.__result)
                        case '*':
                            op2 = self.__stack.pop()
                            op1 = self.__stack.pop()
                            self.__result = op1 * op2
                            self.__stack.push(self.__result)
                        case '/':
                            op2 = self.__stack.pop()
                            op1 = self.__stack.pop()
                            self.__result = op1 / op2
                            self.__stack.push(self.__result)
                        case '^':
                            op2 = self.__stack.pop()
                            op1 = self.__stack.pop()
                            self.__result = op1 ** op2
                            self.__stack.push(self.__result)
                        case _:
                            self.ERROR("Invalid expression")
                            return
                else:
                    self.ERROR("Invalid expression")
                    return
        return self.__result


# test code
if __name__ == '__main__':
    i = input("Enter the expr separated with space: ")
    e = i.split(sep=" ")
    evaluator = PostfixEvaluator(e)
    print("postfix expr = ", evaluator.get_postfix_expr())
    print("result = ", evaluator.evaluate())
    evaluator.set_postfix_expr(e)
    print("result = ", evaluator.evaluate())
    print("result = ", evaluator.get_result())

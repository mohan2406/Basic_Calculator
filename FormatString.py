# function to find if the given argument is real number ex: "50.32" or "-34.0" or "+2" is real numbers so this
# function returns a boolean value true else false.

def is_real_num(num: str):
    for token in num:
        if token.isdecimal():
            return True
    return False


# class to format the given expression to be parsed correctly by the InfixToPostfix parser

class FormatString:
    def __init__(self, expr: str):
        self.__expr = expr

    def get_expr(self):
        return self.__expr

    def set_expr(self, expr: str):
        self.__expr = expr

    # function to remove space in the __expr attribute
    def remove_space(self):
        expr = list()
        for token in self.__expr:
            if not token.isspace():
                expr.append(token)
        self.__expr = expr

    # function to join separated digits in the __expr attribute. (i.e) '1', '2' to '12'->twelve
    def format_number(self):
        expr = list()
        whole_num = str()

        for index, token in enumerate(self.__expr):
            if token.isdecimal() or token == '.':
                if (index + 1) == len(self.__expr):
                    whole_num += token
                    expr.append(whole_num)
                    whole_num = ""
                    continue
                if self.__expr[index + 1].isdecimal() or self.__expr[index + 1] == '.':
                    whole_num += token
                else:
                    whole_num += token
                    expr.append(whole_num)
                    whole_num = ""
            else:
                expr.append(token)
        self.__expr = expr

    # function to identify and convert integer as negative or positive integers
    def to_int(self):
        integer = str()
        expr = list()
        updated = False
        unary_operators = ('-', '+')

        for index, token in enumerate(self.__expr):
            if index == 0:
                if token in unary_operators and is_real_num(self.__expr[index + 1]):
                    integer += token + self.__expr[index + 1]
                    expr.append(integer)
                    integer = ''
                    updated = True
                    continue
                else:
                    expr.append(token)
                    continue
            if (index + 1) == len(self.__expr):
                expr.append(token)
                continue
            if (token in unary_operators) and \
                    (not (is_real_num(self.__expr[index - 1]))) and \
                    (is_real_num(self.__expr[index + 1])):
                integer += token + self.__expr[index + 1]
                expr.append(integer)
                integer = ''
                updated = True
                continue
            if not updated:
                expr.append(token)
            updated = False

        self.__expr = expr


# test code

if __name__ == '__main__':
    e = input("Enter the expr: ")

    is_real = is_real_num(e)
    print("expr is real = ", is_real)

    f = FormatString(e)
    f.remove_space()
    print("expr without space = ", f.get_expr())
    f.set_expr(e)
    print("assigned new expr = ", f.get_expr())
    f.remove_space()
    print("expr without space = ", f.get_expr())
    f.format_number()
    print("formatted expression = ", f.get_expr())
    f.to_int()
    print("final expr = ", f.get_expr())

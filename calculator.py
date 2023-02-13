# Umit Kilinc

def parse_expression(string):
    # store the results and the current expression, and store the current word.
    stack = []
    current_list = []
    current_word = ""

    # loop through each character in the input string
    for char in string:
        if char == "(":
            # if the current word is not empty, add it to the current list
            if current_word:
                current_list.append(current_word)
                current_word = ""
            # push the current list to the stack and start a new list
            stack.append(current_list)
            current_list = []
        elif char == " ":
            # if the current word is not empty, add it to the current list
            if current_word:
                current_list.append(current_word)
                current_word = ""
        elif char == ")":
            # if the current word is not empty, add it to the current list
            if current_word:
                current_list.append(current_word)
                current_word = ""
            # pop the last list from the stack and append the current list to it
            last_list = stack.pop()
            last_list.append(current_list)
            current_list = last_list
        else:
            # add the character to the current word
            current_word += char
    # if the current word is not empty, add it to the current list
    if current_word:
        current_list.append(current_word)
    # return the first item in the current list (which is the final result)
    return current_list[0]


def evaluate_expression(expression):
    # get the operator from the first item in the expression
    operator = expression[0]
    if operator == "add":
        # if the operator is "add", return the sum of the rest of the items
        return sum(map(evaluate_expression, expression[1:]))
    elif operator == "multiply":
        # if the operator is "multiply", return the product of the rest of the items
        result = 1
        for operand in expression[1:]:
            result *= evaluate_expression(operand)
        return result
    elif operator.isdigit():
        # if the operator is a digit, return it as an integer
        return int(operator)
    else:
        # if the operator is unknown, raise an error
        raise ValueError(f"Unknown operator: {operator}")


if __name__ == "__main__":
    # repeat until the user enters "quit" or "exit"
    while True:
        print("-----Enter 'quit' or 'exit' to exit.-----")
        sexpr_str = input("-->Enter an S-expression: ")
        if sexpr_str in ["quit", "exit"]:
            break
        # parse the input string into an S-expression
        sexpr = parse_expression(sexpr_str)
        # evaluate the S-expression and print the result
        result = evaluate_expression(sexpr)
        print(f"Result: {result}")

def arithmetic_arranger(problems, val=False):
  
    # return error if there are more than 5 problems   
    if len(problems) > 5:
        return "Error: Too many problems."

    # create empty lists
    first_operand = []
    operators = []
    second_operand = []
    dashes = []
    results = []

    # create empty strings
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    # this loops iterates over a list of problems,
    # splits each problem into 3 variables (first_number, operator and second_number)
    # then if elif statements checks whether numbers contain only digits
    # and if so whether they aren't more than 4 digits.
    # finally, it checks whether the operator is "+" or "-"
    for i in range(len(problems)):
        first_number = problems[i].split(" ")[0]
        operator = problems[i].split(" ")[1]
        second_number = problems[i].split(" ")[2]

        if not first_number.isdigit() or not second_number.isdigit():
            return "Error: Numbers must only contain digits."
        elif len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif operator == "*" or operator == "/":
            return "Error: Operator must be '+' or '-'."
        else:
            first_operand.append(int(first_number))
            second_operand.append(int(second_number))
            operators.append(operator)
            dashes.append("-")

    for i in range(len(operators)):
        if operators[i] == "+":
            results.append(first_operand[i] + second_operand[i])
        else:
            results.append(first_operand[i] - second_operand[i])

    for i in range(len(operators)):
        first_operand[i] = str(first_operand[i])
        second_operand[i] = str(second_operand[i])
        results[i] = str(results[i])
        space = " "
        width = max(len(first_operand[i]), len(second_operand[i]))

        line1 = line1 + first_operand[i].rjust(width + 2) + space * 4
        line2 = line2 + operators[i] + " " + second_operand[i].rjust(width) + space * 4
        line3 = line3 + dashes[i] * (width + 2) + space * 4
        line4 = line4 + results[i].rjust(width + 2) + space * 4

    if val:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip()
    else:
        arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()

    return arranged_problems
def arithmetic_arranger(problems, want_anses = False):

    # case 3: test_too_many_problems
    if (len(problems) > 5):
        return "Error: Too many problems."

    # case 4: test_incorrect_operator
    if (any(True if "/" in problem or "*" in problem else False for problem in problems)):
        return "Error: Operator must be '+' or '-'."

    # case 5: test_too_many_digits
    for problem in problems:
        problem = problem.split()
        if (any(True if len(num) > 4 else False for num in problem)):
            return "Error: Numbers cannot be more than four digits."

    # case 6: test_only_digits
    for problem in problems:
        if (any(True if num.isalpha() else False for num in problem)):
            return "Error: Numbers must only contain digits."

    # store data for problems
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    # obtain respective data from problems
    for problem in problems:
        num1, op, num2 = problem.split()
        if op == "+":
            ans = str(int(num1) + int(num2))
        elif op == "-":
            ans = str(int(num1) - int(num2))
        length = max(len(num1), len(num2))
        dash ="-" * (length + 2)
        
        # store data to list
        line1 = line1 + num1.rjust(length + 2) + "    "
        line2 = line2 + op + num2.rjust(length + 1) + "    "
        line3 = line3 + dash + "    "
        line4  = line4 + ans.rjust(length + 2) + "    "

    # remove trailing space
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()
    
    # initialize arranged_problems
    if want_anses is True:
        arranged_problems = f"{line1}\n{line2}\n{line3}\n{line4}"
    else:
        arranged_problems = f"{line1}\n{line2}\n{line3}"

    return arranged_problems
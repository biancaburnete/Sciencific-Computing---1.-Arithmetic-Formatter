def arithmetic_arranger(problems, results=False):

  #Set maximum of 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

  #Set empty rows      
    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''
        
  #Assign values to operator and operands using "split" method 
    for i, problem in enumerate(problems):
        no1, op, no2 = problem.split()

  #Set operators to be "+" or "-"
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

  #Set operators to be digits using "isdigit" method
        if no1.isdigit == False or no2.isdigit() == False:
            return 'Error: Numbers must only contain digits.'

  #Set maximum four digits for each operand
        if len(no1) > 4 or len(no2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

  #Arithmetical Operations
        if op == '+':
            result = int(no1) + int(no2)
        else:
            result = int(no1) - int(no2) 

  #Spacing conditions
        spaces = max(len(no1), len(no2)) + 2

  #Contructing rows
        r1 += no1.rjust(spaces)
        r2 += op + no2.rjust(spaces-1)
        r3 += '-' * (spaces)
        r4 += str(result).rjust(spaces)

  #Check if it is the last problem and add space
        if i < len(problems) - 1:
          r1 += ' ' * 4
          r2 += ' ' * 4
          r3 += ' ' * 4
          r4 += ' ' * 4

  #Result conditions:
    arranged_problems = r1 + "\n" + r2 + "\n" + r3

    if results:
        arranged_problems += "\n" + r4

    return arranged_problems



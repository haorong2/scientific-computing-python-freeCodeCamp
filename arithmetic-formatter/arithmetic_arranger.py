def arithmetic_arranger(problems, isDisplay=False):
  # Check for too many problem
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = []
  answers = []

  max_widths = [] # keep track of the maximum widths of each problem
  
  for problem in problems:
    operands = problem.split()
    num1, operator, num2 = operands
  
    # Check for valid operator
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
  
    # Check for valid operands, only contain digits
    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."
  
    # Check for valid operands, digits length should not exceed 4
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
  
    # Calculate the correct answer
    if operator == '+':
      answer = str(int(num1) + int(num2))
      answers.append(answer)
    elif operator == '-':
      answer = str(int(num1) - int(num2))
      answers.append(answer)
  
  
    max_width = max(len(num1), len(num2)) + 2
    max_widths.append(max_width)
  
    problem_line = f"{num1:>{max_width}}\n{operator} {num2:>{max_width-2}}\n{'-'*max_width}\n{answer:>{max_width}}"
    arranged_problems.append(problem_line)
  
  formatted_output = ""
  for i in range(3):
    for idx, problem in enumerate(arranged_problems):
      # if outputing the last element, don't need the "    ".
      if idx < len(arranged_problems) - 1:
        formatted_output += problem.split('\n')[i] + "    "
      else:
        formatted_output += problem.split('\n')[i]
    # last row don't need the "\n"
    if i < 2:
      formatted_output += "\n"
  
  if isDisplay:
    # Answers display need to print at next line.
    formatted_output += "\n"
    for idx, problem in enumerate(arranged_problems):
      if idx < len(arranged_problems) - 1:
        formatted_output += problem.split('\n')[3] + "    "
      else:
        formatted_output += problem.split('\n')[3]
    
  
  return formatted_output
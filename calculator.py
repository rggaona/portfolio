from replit import clear
from art import logo_calculator


def add (n1, n2):
  return n1 + n2

def subtr (n1, n2):
  return n1 - n2

def multi (n1, n2):
  return n1 * n2

def divide (n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtr,
  "*" : multi,
  "/" : divide
}
def calculator():
  print(logo_calculator)
  num1 = float(input("what is the first number?: "))
  round(num1, 2)
  for symbol in operations:
    print(symbol)
  continuar = True

  while continuar == True:
    operation_symbol = (input("Pick an operation: "))
    num2 = float(input("what is the next number?: "))
    round(num2, 2)
    answer = round(operations[operation_symbol](num1,num2),2)

    print(f"{num1} {operation_symbol} { num2} = {answer}")

    decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if decision == "y":
      num1 = answer
    else:
      continuar = False
      clear()
      calculator()
calculator()

num1,num2 = map(int,input("Enter Two Numbers:").split())
opt = input()

match opt:
  case '+':
    print("Addition:",num1+num2)
  case '-':
    print("Subtraction:",num1-num2)
  case '*':
    print("Multiplication:",num1*num2)
  case '/':
    print("Division:",num1/num2)
  case '%':
    print("Modulus:",num1%num2)

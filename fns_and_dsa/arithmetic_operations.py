def perform_operation (num1, num2, operation):
  print("Arithmetic Operations")
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
  match operation:
    case 'add':
      result = num1 + num2
      print(f"Result: {result}")
    case 'subtract':
      result = num1 - num2
      print(f"Result: {result}")
    case "multiply':
      result = num1 * num2 
      print(f"Result: {result}")
    case "divide":
        if num2 == 0:
          print("DIVISION BY ZERO ERROR")
        else:
          result = num1/num2
          print(f"Result: {result}")
    if __name__ == "__main__":
        main()




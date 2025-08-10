# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Performs addition without accessing class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Accesses class attribute before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()

import math
import sympy as sp 
class Limit :
	def __init__(self,numerator,denominator,x):
 # Initializes the Limit object with a numerator, denominator (both polynomials), and an x-value.
		self.x =x
		self.numerator = numerator
		self.denominator = denominator
	def calculate_derivatives(self,function):
		# Calculating the derivative of a polynomial function when x approaches a concrete value.
		derivative = {}
		for power,coeff in function.items(): # power present for key and coeff present for value in "dictionary" polynomial
			if power > 0:
				derivative[power-1] = power*coeff
		return derivative
	def calculate_limit_polynomial(self,function,x):
		 # Evaluates the limit of a polynomial at the given x-value
		value = 0
		for power,coeff in function.items():
			value += coeff * self.x ** power
		return value
	def calculate_limit_rational(self, attempts = 10):
		 # Calculates the limit of a rational function by evaluating both polynomials at x
         # and applying L'Hôpital's Rule if necessary.
		curr_numerator =  self.numerator.copy()
		curr_denominator = self.denominator.copy()
		for i in range(attempts):
			value_limit_numerator = self.calculate_limit_polynomial(curr_numerator,self.x) # Calculate limit of numerator at the given x-value
			value_limit_denominator = self.calculate_limit_polynomial(curr_denominator,self.x) # Calculate limit of denominator at the given x-value
			if value_limit_numerator != 0 and value_limit_denominator != 0:
				return value_limit_numerator / value_limit_denominator
			elif value_limit_numerator == 0 and value_limit_denominator != 0:
				return 0 
			elif value_limit_numerator != 0 and value_limit_denominator == 0:
				return "Infinity"
			else:
				curr_numerator = self.calculate_derivatives(curr_numerator)
				curr_denominator = self.calculate_derivatives(curr_denominator)
				
			# Using L'Hopital's rule when value_limit_numerator and value_limit_denominator equal 0
	def __str__(self): # __str__ method string presentation
		msg = " Begin calculating limit."
		return msg
class FunctionLimit:
	def __init__(self,numerator,denominator,x_value):
		self.x = sp.Symbol('x') # Using sympy to create a symbol for x
		self.numerator = sp.sympify(numerator) # Convert the numerator to a sympy expression
		self.denominator = sp.sympify(denominator) # Convert the denominator to a sympy expression
		self.x_value = x_value # The x-value at which to evaluate the limit
	def calculate_limit(self,direction = '+'):
		# Calculate the limit of a function as x approaches a specific value.
		return sp.limit(self.numerator / self.denominator, self.x, self.x_value, dir=direction)
def calculate_limit_polynomial(function,x):
	# Calculates the value of a polynomial at a specific x-value.
		value = 0
		for power,coeff in function.items():
			value += coeff * x ** power
		return value
def create_function(n):
	# Asks the user to input coefficients for each term of the polynomial, from x^0 up to x^n.
	function = {}
	for i in range(n+1):
		function[i] = int(input("Enter the cofficient  : "))
	return function
def print_function(dict_coeff):
    visualized_function = ""
    for power in sorted(dict_coeff.keys(), reverse=True):
        coeff = dict_coeff[power]
        if coeff == 0:
            continue
        term = f"{coeff}x^{power}" if power != 0 else f"{coeff}"
        if visualized_function != "":
            visualized_function += " + "
        visualized_function += term
    return visualized_function
ask_user =input("Choose 'Poly' for polynomial or 'Rati' for Rational or 'Function' for function: ").strip() # Ask the user to choose between polynomial or rational function or function
if ask_user == "Function":
	numerator = input("Enter the numerator of the function: ")
	denominator = input("Enter the denominator of the function: ")
	x = int(input("Calculate the limit as x approaches: "))
	function_limit = FunctionLimit(numerator, denominator, x)
	value = function_limit.calculate_limit()
	print(f"The limit of the function as x approaches {x} is {value}")
elif ask_user == "Poly":
	n = int(input("Enter the degree of the polynomial: "))
	x = int(input("Calculate the limit of the polynomial at x approaches: "))
	if n <= 0:
		print("Degree should not be negative.")
	else:
		function_for_polynomial  = create_function(n)# Create polynomial function
		print("Polynomial you want to calculate limit is ",print_function(function_for_polynomial))
		value =  calculate_limit_polynomial(function_for_polynomial , x) # Calculate limit of this polynomial function
		print("The limit of the polynomial when  x approaches ", x, "is", value)
elif ask_user == "Rati":
	n = int(input("Enter the degree of the numerator: ")) # Ask the user for degree of numerator
	m = int(input( "Enter the degree of the denominator: ")) # Ask the user for degree of denominator
	x = int(input("Calculate the limit as x approaches: ")) # Ask the user for x approach concrete value.
	if n <= 0 or m <=0:
		print("Degrees of numerator and denominator should not be negative.")
	else:
		numerator = create_function(n) # Create numerator of rational function
		denominator = create_function(m) # Create denominator of rational function
		print(f"Rational function you want to calculate limit is: ({print_function(numerator)}) / ({print_function(denominator)})")
		rational_function = Limit(numerator,denominator,x) # Create an object ( rational_function ) of Limit Class
		value = rational_function.calculate_limit_rational() # Calculate the limit based on calculate_limit_rational class in Limit Class
		print("The limit of the rational function as x approaches", x, "is", value)
else:
	print("Invalid choice. Please choose 'Poly' or 'Rati")
with open("Limit.txt","w") as myfile:
	if ask_user == "Poly" and n >0 :
		myfile.write(f"Polynomial you want to calculate limit is  {print_function(function_for_polynomial)}\n")
		myfile.write(f"The limit of the polynomial as x approaches {x} is {value}\n")
		myfile.write("Calculate limit is so easy ^-^. Bingo!! You scored 100 in Math121 ! See you again")
	elif ask_user == "Poly" and n <= 0:
		myfile.write("Degree should not be negative")
	elif ask_user == "Rati" and n>0 and m>0:
		myfile.write(f"Rational function you want to calculate limit is  ({print_function(numerator)}) / ({print_function(denominator)})\n")
		myfile.write(f"The limit of the rational function as x approaches {x} is {value}\n")
		myfile.write("Calculate limit is so easy ^-^ .Bingo!! You scored 100 in Math121 ! See you again ")
	elif ask_user == "Rati" and (n<0 or m<0):
		myfile.write("Degrees of numerator and denominator should not be negative. ")
	else :
		myfile.write("Invalid choice . Let's type Poly or Rati")



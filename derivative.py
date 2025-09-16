import math
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
'''class FunctionLimit:
	def __init__(self,numerator,denominator,x_value):
		self.x = sp.Symbol('x') # Using sympy to create a symbol for x
		self.numerator = sp.sympify(numerator) # Convert the numerator to a sympy expression
		self.denominator = sp.sympify(denominator) # Convert the denominator to a sympy expression
		self.x_value = x_value # The x-value at which to evaluate the limit
	def calculate_limit(self,direction = '+'):
		# Calculate the limit of a function as x approaches a specific value.
		return sp.limit(self.numerator / self.denominator, self.x, self.x_value, dir=direction)'''
class Polynomial:
	def __init__(self,function,x):
		self.function = function
		self.x = x
	def calculate_limit_polynomial(self):
		# Calculates the value of a polynomial at a specific x-value.
		value = 0
		for power,coeff in self.function.items():
			value += coeff * self.x ** power
		return value
	def calculate_derivatives(self):
		# Calculating the derivative of a polynomial function when x approaches a concrete value.
		value = 0
		for power,coeff in function.items(): # power present for key and coeff present for value in "dictionary" polynomial
			if power > 0:
				value += coeff * (power) * self.x**(power-1)
		return value
	def derivatives(self):
		result = {}
		for power, coeff in self.function.items():
			if power > 0:
				result[power-1] = coeff * (power-1)
		s = ""
		for power , coeff in result:
			if coeff == 0:
				continue
			elif power ==0:
				s+= f"{coeff}"
			elif power == 1:
				s += f"{coeff}x + "
			else:
				s+= f"{coeff}x^{power} + "
		return s.rstrip(" + ")
			
class Integral:
	def __init__(self,function, a = None,b = None):
		self.function = self.function 
		self.a = a
		self.b = b
	def function_at_point(self,x):
		value = 0
		for power, coeff in self.function:
			new_power = power + 1
			new_coeff = coeff // new_power
			value += (new_coef * (self.x ** new_power))
		return value 
	def evaluate_function(self):
		return self.function_at_point(self.b) - self.function_at_point(self.a)
	def create_function(self):
		value = {}
		for power, coeff in self.function:
			new_power = power + 1
			new_coeff = coeff // new_power
			value[new_power] =  new_coeff
		s = ""
		for power , coeff in value:
			if coeff == 0:
				continue
			elif power ==0:
				s+= f"{coeff}"
			elif power == 1:
				s += f"{coeff}x + "
			else:
				s+= f"{coeff}x^{power} + "
		return s.rstrip(" + ") 
		
				
	
	
		

'''| Thành phần              | Công nghệ                              |
| ----------------------- | -------------------------------------- |
| Giao diện người dùng    | Tkinter                                |
| Lưu trữ lịch sử         | SQLite                                 |
| Vẽ biểu đồ hàm số       | Matplotlib                             |
| Nhập biểu thức nâng cao | SymPy                                  |
| Xuất kết quả ra file    | CSV, PDF                               |
| Giao diện đẹp hơn       | ttkbootstrap, customtkinter            |
| Quản lý dự án tốt hơn   | Chia module + cấu trúc thư mục rõ ràng |'''

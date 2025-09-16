class Evaluate:
	def __init__(self,expr):
		self.s = expr
	def evaluate(self):
		lyst =[]
		stack =[]     
		operators = "+-*/"
		temp = ""
		for i in range(len(s)):
			if s[i]!= " ":
				if s[i] in operators:
					if temp:
						lyst.append(int(temp))
					lyst.append(s[i])
					temp =""
				else:
					temp += s[i]
		if temp:
			lyst.append(int(temp))
		i =0
		while i < len(lyst):
			if lyst[i] == "*" or lyst[i] == "/":
				prev = stack.pop()
				if lyst[i] == "*":
					stack.append(prev * lyst[i+1])
                
				elif lyst[i] == "/":
					stack.append(prev // lyst[i+1])
				i+=2
			else:
				stack.append(lyst[i])
				i+=1
		result = stack[0]  
		i = 1
		while i < len(stack):
			op = stack[i]
			i+=1
			num = stack[i]
			if op == "+":
				result += num
			elif op == "-":
				result -= num
			i += 1
    
		return result

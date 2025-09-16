import tkinter as tk
from tkinter import messagebox, ttk
from derivative import Limit, Polynomial, Integral
from eval_expr import Evaluate
class MathApp:
	def __init__(self,root):
		self.root = root
		self.root.title("Basic Calculator - Caculus")
		self.options = ["Evaluate Expressions", "Calculate Polynomical Limit" , "Calculate Rational Limit", "Calculate Polynomial Integral", "Calculate Polynomial Derivative", "Find derivative", "Find Integral"]
		self.operation = tk.StringVar(value = self.options[0])
		
		ttk.Label(root, text = "Choose option:").pack()
		self.op_menu = ttk.Combobox(root, values = self.options,  textvariable = self.operation, state = "readonly")
		#Create a combobox in root window. Choose one value in that box then operation will be assigned with that choice
		self.op_menu.pack()
		self.use_degree_input = tk.BooleanVar(value=False)
		ttk.Checkbutton(root, text="Enter Polynomial by  degree", variable=self.use_degree_input, command=self.update_visibility).pack(pady=5)

        # === Nhập theo degree ===
		self.degree_frame = ttk.Frame(root)
		self.degree_label = ttk.Label(self.degree_frame, text="Degree:")
		self.degree_label.grid(row=0, column=0)
		self.degree_entry = ttk.Entry(self.degree_frame, width=5)
		self.degree_entry.grid(row=0, column=1)
		self.generate_btn = ttk.Button(self.degree_frame, text="Coefficient", command=self.generate_coeff_inputs)
		self.generate_btn.grid(row=0, column=2)
		self.degree_frame.pack(pady=5)

		self.coeff_inputs_frame = ttk.Frame(root)
		self.coeff_inputs_frame.pack()

		self.a_label = ttk.Label(root, text="a:")
		self.a_entry = ttk.Entry(root, width=10)
		self.b_label = ttk.Label(root, text="b:")
		self.b_entry = ttk.Entry(root, width=10)

    # Tạo label + entry cho denominator (dạng phân thức)
		self.den_expr_label = ttk.Label(root, text="Denominator:")
		self.den_expr_entry = ttk.Entry(root, width=60)

        # === x ===
		self.x_label = ttk.Label(root, text="x:")
		self.x_entry = ttk.Entry(root)
		self.x_label.pack()
		self.x_entry.pack()

        # === Nút thực hiện ===
		ttk.Button(root, text="Thực hiện", command=self.calculate).pack(pady=10)

        # === Kết quả ===
		self.result_text = tk.Text(root, height=8, width=70)
		self.result_text.pack()

        # === Binding ===
		self.update_visibility()
		self.op_menu.bind("<<ComboboxSelected>>", lambda e: self.update_visibility())

        # === Danh sách Entry hệ số (sinh tự động) ===
		self.coeff_entries = {}

	def update_visibility(self):
		op = self.operation.get()

    # Ẩn hết trước để reset
		self.a_label.pack_forget()
		self.a_entry.pack_forget()
		self.b_label.pack_forget()
		self.b_entry.pack_forget()
		self.den_expr_label.pack_forget()
		self.den_expr_entry.pack_forget()
		self.x_label.pack_forget()
		self.x_entry.pack_forget()

		# Show widget tương ứng
		if op == "Find Integral":
			# integral cần a,b, không cần x hay denominator
			self.a_label.pack()
			self.a_entry.pack()
			self.b_label.pack()
			self.b_entry.pack()

		elif op == "Calculate Rational Limit":
			# cần denominator và x
			self.den_expr_label.pack()
			self.den_expr_entry.pack()
			self.x_label.pack()
			self.x_entry.pack()

		elif op in ["Evaluate Expressions", "Calculate Polynomical Limit", "Calculate Polynomial Integral", "Calculate Polynomial derivative", "Find derivative"]:
			# chỉ cần x thôi
			self.x_label.pack()
			self.x_entry.pack()

	def generate_coeff_inputs(self):
		for widget in self.coeff_inputs_frame.winfo_children():
			widget.destroy()
		self.coeff_entries = {}

		try:
			degree = int(self.degree_entry.get())
		except:
			messagebox.showerror("Error", "Degree has to be integer.")
			return

		for i in range(degree, -1, -1):
			label = ttk.Label(self.coeff_inputs_frame, text=f"Coefficient x^{i}:")
			label.grid(row=0, column=degree - i * 2)
			entry = ttk.Entry(self.coeff_inputs_frame, width=6)
			entry.grid(row=0, column=degree - i * 2 + 1)
			self.coeff_entries[i] = entry

	def get_poly_from_inputs(self):
		poly = {}
		for power, entry in self.coeff_entries.items():
			try:
				coeff = float(entry.get())
			except:
				coeff = 0.0
			poly[power] = coeff
		return poly

	def calculate(self):
		self.result_text.delete("1.0", tk.END)
		try:
			use_degree = self.use_degree_input.get()
			if use_degree:
				poly = self.get_poly_from_inputs()
			else:
				raise Exception("Error in entering degree")

			op = self.operation.get()

			if op == "Evaluate Expressions":
				x = float(self.x_entry.get())
				function = Polynomial(poly,x)
				result = function.calculate_limit_polynomial(poly, x)
				self.result_text.insert(tk.END, f"f({x}) = {result}")
			elif op == "Find derivative":
				fuction = Polynomial(poly)
				derived = function.derivatives()
				self.result_text.insert(tk.END, f"Derivative: {derived}")
			elif op == "Calculate Polynomial Derivative":
				x = float(self.x_entry.get())
				function = Polynomial(poly,x)
				derived = function.derivatives(poly)
				self.result_text.insert(tk.END, f"Derivative: {derived}")

			elif op == "Find Integral":
				integ = Integral(poly)
				self.result_text.insert(tk.END, f"Integral: {integ.create_function()} + C")
             
			elif op == "Calculate Polynomial Integral":
				a = float(self.a_entry.get())
				b = float(self.b_entry.get())
				integ = Integral(poly,a,b)
				self.result_text,insert(tk.END, f"Integral : {integ.evaluate_function()}")

			elif op == "Calculate Polynomical Limit":
				x = float(self.x_entry.get())
				lim = Polynomial(poly,x)
				result = lim.calculate_limit_polynomial(poly, x)
				self.result_text.insert(tk.END, f"lim f(x) when x → {x} = {result}")

			elif op == "Calculate Rational Limit":
				denom = self.den_expr_entry.get()
				x = float(self.x_entry.get())
				lim = Limit(poly,demom,x)
				result = lim.calculate_limit_rational(poly, denom, x)
				self.result_text.insert(tk.END, f"lim f(x)/g(x) when  x → {x} = {result}")

		except Exception as e:
			messagebox.showerror("Error", f"Error Handling: {str(e)}")
		
root = tk.Tk()
s = MathApp(root)
tk.mainloop()

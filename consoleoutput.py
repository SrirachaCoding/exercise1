def println(inputs, *repeats):
	"""
	Attempting to create a print and repeat function.
	"""
	for _ in range((repeats if repeats else 1)):
		print(">%s" %(inputs) )
		return;

functions = [println]

println ("Example console output")
println ("punctuation: !@#$%^&*()_+=-/.,<>{}")
println ("end of line.")

for _ in functions:
	print (_.__name__,_.__doc__)



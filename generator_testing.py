#Basic generator functions

#Yield single output
def generator(input):
	for i in input:
		yield i

output = generator([1,2,3,4,5])

print(next(output)) #prints 1 
print(next(output)) #prints 2
print(next(output)) #prints 3
print(next(output)) #prints 4
#Prints StopIteration if at end

for item in output:
	print(item)

def preprocessor_func(input):
	return input+1

#Yield slice of array of batch_size
batch_size = 2
def generator_list(input=input, batch_size=batch_size):
	out_arr=[]
	for i in input:
		output = preprocessor_func(i)
		out_arr.insert(i, output)
		if len(out_arr) >= batch_size:
			yield out_arr
			out_arr=[]

a = [1,2,3,4,5,6,7]
output = generator_list(a)

for x in output:
	print(x)




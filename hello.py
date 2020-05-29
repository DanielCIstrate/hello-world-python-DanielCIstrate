#Task 1 - Hello world function implementation

def hello_world():
    return "Hello, World!"


"""returns "Hello, World!" without printing the function"""
message = hello_world()
"""indicates output for task 1"""
print("1.")
"""test"""
print(message)
print()



#Task 2 - 'hello(name)' function

def hello(name):
    if name == None or name == "":
        return 'Hello, World!'
    return 'Hello, ' + name + '!'

"""separates second task output from first."""
print("2.")

""" if you want to try the code yourself:"""

name = input("Insert a name: ")
print("Output: ", hello(name))



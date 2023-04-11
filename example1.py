#!python3

"""
Functions can have some default values in input parameters.  When a default value is specified,
it does not have to be included in the program.  To specify a default value, you use the following
notation in your function definition:
"""

def multiply(x=2):
  # this function multiples the input parameter x by 5.
  # by default, the value for x is 2
  # this function does not need to return a value, but we can
  # include a return None statement to show it has no output
  
    print(x*5)
    return None

def divide(x=2)
  # or we can have the function return nothing
  print(x/5)
  return
    
    

def main():
  multiply()
  multiply(3)
  multiply(4)

  divide()
  divide(10)
  divide(20)


if __name__ == "__main__":
  main()

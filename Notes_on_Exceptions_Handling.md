## Exception Handling
- When an error occurs at runtime, it can be refferred as throwing an exception.
- when an exception occurs, python ends the program and prints information about the exception.
- some exceptions occur due to causes outside of the program.
- These exceptions  need to be handled by our python code so the program doesn't crash when they occur.

-Two funcations that can cause a valueerror exception.
  int(data)
    - when it can't convert the data argument to an integer
  float(data)
    - when it can't convert the data argument to a floating-point number.

### A 'try' statement to handle one type of exception.
- syntax
   try:
     block # it may throw an exception
   except [exceptionNAME]:
      block # HANDLE THE EXCEPTION
- if we don't code the name of an exception type in 


### handling multiple exceptions
- The hierarchy of five common exception.
    Exception
      OSerror
          fileexisterror
          filenotfounderror
      valueerror  

**Note:** The 'except' clause must be coded in sequence starting with the most specific exception and ending with the most general exception.

### A 'try' statement to handle multiple exceptions.
- Syntax:
   try:
      blo


### The complete 'except' clause syntax
- syntax: 
    except [ExceptionName] [as variable]: 
        block

- Later we can inspect the variable to which Exception is assigned.

### The 'exit()' function
- The exit() function from the 'sys' module exits the python program.

### complete 'try' statement with 'finally' clause'
- Syntax:
     try:
       block
    except [ExceptionName] [as variable]:
        block
    except [ExceptionName] [as variable]:
        block
    finally:
        block

- A 'finally' clause is always executed, even if an exception occurs or a return statement is executed in the 'try' clause.
- Generally, the 'finally' clause is defined for clean-up actions manually.

### Rasing an exception
- To raise an exception, we can use a 'raise' statement that creates an exception object.

      




     
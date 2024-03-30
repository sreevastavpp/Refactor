# Refactor 

This repo is based on the **Refactoring** book by Martin Flower. Code examples have been converted from `JavaScript` to `Python`. 

## Repalce Temp with Query 

### Motivation

One use of temporary variables is to capture the value of some code in order to refer to it later in a function. Using a temp allows me to refer to the value while explaining its meaning and avoiding repeating the code that calculates it. But while using a variable is handy, it can often be worthwhile to go a step further and use a function instead.

- Check that the variable is determined entirely before it's used, and the code that calculates it does not yield a different value whenever it is used.
- If the variable isn't read-only, and can be made read-only, do so.
- Test.
- Extract the assignment of the variable into a function.
- If the variable and the function cannot share a name, use a temporary name for the function.
- Ensure the extracted function is free of side effects. If not, use Separate Query from Modifier.
- Test.
- Use Inline Variable to remove the temp.
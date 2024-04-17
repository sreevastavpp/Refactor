# Refactor 

This repo is based on the **Refactoring** book by Martin Flower. Code examples have been converted from `JavaScript` to `Python`. 

- **When you have to add a feature to a program but the code is not structured in a convenient way, first refactor the program to make it easy to add the feature, then add the feature.**

- **Before you start refactoring, make sure you have a solid suite of tests. These tests must be self-checking.**

- **Refactoring changes the programs in small steps, so if you make a mistake, it is easy to find where the bug is.**

## Extract Funcion 

If you have to spend effort looking at a fragment of code and figuring out **"what"** it's doing, then you should extract it into a function and name the function after the **“what.”** 

Extract Function is one of the most common refactorings. 
- Look at a fragment of code, understand what it is doing.
- Then extract it into its own function named after its purpose.

Some people are concerned about short functions because they worry about the performance cost of a function call. :question:

When you see fragments of code in a larger function that start with a comment to say what they do. The comment is often a good hint for the name of the function when you extract that fragment.

### Methodology

- Create a new function, and name it after the intent of the function.
    - If the language supports nested functions, nest the extracted function inside the source function. That will reduce the amount of out-of-scope variables to deal with after the next couple of steps
- Copy the extracted code from the source function into the new target function.
- Scan the extracted code for references to any variables that are local in scope to the source function and will not be in scope for the extracted function. Pass them as parameters.
    -  Find that too many local variables are being assigned by the extracted code. It's better to abandon the extraction at this point.
- Compile after all variables are dealt with.
- Replace the extracted code in the source function with a call to the target function.
- Test.
- Look for other code that's the same or similar to the code just extracted, and consider using Replace Inline Code with Function Call to call the new function.

## Repalce Temp with Query 

One use of temporary variables is to capture the value of some code in order to refer to it later in a function. Using a temp allows me to refer to the value while explaining its meaning and avoiding repeating the code that calculates it. But while using a variable is handy, it can often be worthwhile to go a step further and use a function instead.

### Methodology

- Check that the variable is determined entirely before it's used, and the code that calculates it does not yield a different value whenever it is used.
- If the variable isn't read-only, and can be made read-only, do so.
- Test.
- Extract the assignment of the variable into a function.
- If the variable and the function cannot share a name, use a temporary name for the function.
- Ensure the extracted function is free of side effects. If not, use Separate Query from Modifier.
- Test.
- Use Inline Variable to remove the temp.

## Change Functin Declaration

- aka:	Rename Function
- aka:	Change Signature

## Split Phase

Run into code that's dealing with two different things? 
Look for a way to split it into separate modules. Divide the behavior into two sequential phases. A good example of this is when you have some processing whose inputs don't reflect the model you need to carry out the logic. 

### Methodology

- Extract the second phase code into its own function.
- Test.
- Introduce an intermediate data structure as an additional argument to the extracted function.
- Test.
- Examine each parameter of the extracted second phase. If it is used by first phase, move it to the intermediate data structure. Test after each move.
    - Sometimes, a parameter should not be used by the second phase. In this case, extract the results of each usage of the parameter into a field of the intermediate data structure and use Move Statements to Callers on the line that populates it.
- Apply Extract Function on the first-phase code, returning the intermediate data structure.

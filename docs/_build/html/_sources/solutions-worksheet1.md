---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Worksheet 1 Solutions

````{solution} running-terminal
:label: running-terminal-solution

To run *numbers.py* in terminal do:
``` 
python numbers.py
```
You will then be asked to input a number in the terminal.  Continue entering numbers until you enter -1
````

```{solution-start} for-words-exercise
:label: for-words-exercise-solution
```

```{code-cell} ipython3
l = ["keep", "calm", "and", "carry", "on"]

for i in range(len(l)):
    print(i, l[i])
```
```{solution-end}
```

```{solution-start} odd-even
:label: odd-even-solution
```
```{code-cell} ipython3
#initialise empty lists
even, odd = [], []

for i in range(10):          
    if i % 2 == 0:           
        even.append(i)       
        continue             
    odd.append(i)            

print(f"The program has identified {len(even)} even numbers {even}")
print(f"The program has identified {len(odd)} odd numbers {odd}")
```
```{solution-end}
```

```{solution-start} calculator
:label: calculator-solution
```

```{code-block}
while True:                                         #1
   print("1. Addition")                             #2
   print("2. Subtraction")                          #3
   print("3. Exit")                                 #4
   print("Choose operation (1-3): ", end="")        #5
   opt = int(input())                               #6
   if opt>=1 and opt<=2:                            #7
      num1 = float(input("Enter first number:"))    #8
      num2 = float(input("Enter second number:"))   #9
   if opt==1:                                       #10
      print("Result:", num1 + num2)                 #11
   elif opt==2:                                     #12
      print("Result:", num1 - num2)                 #13
   elif opt==3:                                     #14
      break                                         #15
   else:                                            #16
      print("No option available")                  #17
   print()                                          #18
                                                    #19
print("Thank you, bye!")                            #20
```
The first line is an **infinite loop** which means that the loop will iterate forever since 
`True` is specified instead of a condition.  This will not be the case however, as in the `if` statement we have a `break` in line 15, which 
stops the loop if the user chooses 3 as an option in the calculator.  Note again the indentation of the code.  The last line is not 
indented under the loop, so it will run after execution of the loop has finished.  

```{solution-end}
```


```{solution-start} half-pyramid
:label: half-pyramid-solution
```
This is one way of printing a half-pyramid.

```{code-cell} ipython3
# this is the outer loop that takes care of rows
for i in range(5):
    # this is inner loop that handles the number of asterisks to print
    for j in range(i+1):
        print("* ", end="")  #end="" argument makes sure that no newline is printed which is the default - check documetation
    # this is so that a newline is printed after the * are printed in each row
    # Note: it is not in the inner loop, but it is executed in the outer loop
    print()
```
```{solution-end}
```

```{solution-start} full-pyramid
:label: full-pyramid-solution
```
Below is one way of printing a full pyramid:
```{code-cell} ipython3
rows = 5
spaces = rows - 1

# outer loop to process rows
for i in range(0, rows):
    # inner loop to print asteriks
    for j in range(0, spaces):
        print(end=" ") 

    # inner loop to handle number of columns
    for j in range(0, i + 1):
        # printing stars
        print("* ", end="")
    
    spaces = spaces - 1
    print()
```
```{solution-end}
```

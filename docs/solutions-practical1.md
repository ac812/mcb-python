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

# Practical 1 Solutions

```{solution} markdown1
:label: markdown1-solution
:class: dropdown

Link to [notebook1.ipynb](https://github.com/ac812/mcb-python/blob/master/docs/notebook-solutions/notebook1.ipynb)
```

```{solution} markdown2
:label: markdown2-solution
:class: dropdown

Link to [notebook2.ipynb](https://github.com/ac812/mcb-python/blob/master/docs/notebook-solutions/notebook2.ipynb)
```


```{solution} arithmetic-operators
:label: arithmetic-operators-solution
:class: dropdown

a. Solutions are in {numref}`numeric-operators-table`.  
b. `8 + (10 + 4**3 + 2)`
```

```{solution-start} variables-types
:label: variables-types-solution
:class: dropdown
```

```{code-cell} python
# 1
a = b = 10

# 2
print("a is", a, "of type", type(a))
print("b is", b, "of type", type(b))

#3
a=22

#4
print("a is", a, "of type", type(a))
print("b is", b, "of type", type(b))

#5
c = a/3

#6
print(f"c is {c:.2f} of type {type(c)}")

#7
d = int(c)

#8 when converting a decimal number to int, the fractional part of the number is lost 
print("d is", d, "of type", type(d))
```
```{solution-end}
```


```{solution-start} exploring-lists
:label: exploring-lists-solution
:class: dropdown
```

```{code-cell} python
#1
l = [55, 92, 110, 66, 75, 45, 40, 57, 55, 62]

#2
#Extract item at index position 2
print("Item at l[2] is", l[2])

#Extract item at index position -2
print("Item at l[-2] is", l[-2])

#3
print(l[2:5])
print(l[1:8:2])

#Extract items from the beginning of the list to index position 2 (excluded).
print("l[:2] is", l[:2])

#Extract items from index position 5 to the end of the list.
print("l[5:] is", l[5:])

#print all items in a list
print("\nPrint all items in list l", l)

# List concatenation: add tuples together
l2 = l + [70,]   #you have to specify the one item as a tuple as well
print("\nConcatenate l to [70,] results in", l2) 

# List replication:  replicate contents of a list by a specified number of times
l3 = l * 2
print("\nReplicating list l by 2:", l3)

# List unpacking - place data items of list in separate variables
print("\nList unpacking:")
l4 = ["Alexia", "MCB", "1B"]
[name, subject, year] = l4
print("Name is", name)
print("Subject is", subject)
print("Year is", year)

#4
print("\nList membership:")
#Check if number 2 is one of the items of list l
print(2 in l)      #returns False

#Check if number 55 is one of the items of list l
print(55 in l)     #returns True

#Check that 2 is not one of the items of list l
print(2 not in l)  #returns True

#5
print("\nAnswer for section 5:")
print(len(l))
print(min(l))
print(max(l))
print(l.index(55))
print(l.count(55))
```
```{solution-end}
```


```{solution-start} lists-utility
:label: lists-utility-solution
:class: dropdown
```
```{code-cell}
print("List l:", l)

l.append(100)
print("List after l.append(100):", l)

l.insert(1,44)
print("List after l.insert(1,44):", l)

l.remove(55)
print("List after l.remove(55):", l)

l.reverse()
print("List after l.reverse():", l)

l.sort()
print("List after l.sort():", l)

del l[7:9]
print("List after del l[7:9]:", l)
```

```{solution-end}
```


```{solution-start} join-strings
:label: join-strings-solution
:class: dropdown
```
The `join()` method takes as an argument a list of strings to join together. The separator to use between the different data items in 
`words` is the string we are calling the `join()` method on.
```{code-cell}
words = ["keep", "calm", "and", "carry", "on"]
quote = " ".join(words)
print(quote)
```
```{solution-end}
```


```{solution-start} split-strings
:class: dropdown
```
To divide strings by a separator, the `split()` string method provides an easy way to do this.  Have a look at the 
[documentation](https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split).  If no arguments are passed 
to the `split()` method, all whitespace is removed from the string that called `split()` and a list is returned with the 
separated strings.

```{code-cell} ipython3
sentence = "Your path you must decide"
words = sentence.split()
print(f"There are {len(words)} words in the words list.")
print(words)
```
```{solution-end}
```

```{solution-start} month-if
:label: month-if-solution
:class: dropdown
```
```{code-cell} ipython3
#specify month you want to get the name of
month = 10

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Month number not supported.")
```
```{solution-end}
```


```{solution-start} month-match
:label: month-match-solution
:class: dropdown
```
```{code-cell} ipython3
#specify month you want to get the name of
month = 0

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Month number not supported.")
```
```{solution-end}
```


```{solution-start} for-exercise
:label: for-exercise-solution
:class: dropdown
```
```{code-cell}
l = ["keep", "calm", "and", "carry", "on"]

for s in l:
    print(s)
```
```{solution-end}
```


```{solution-start} range-exercise
:label: range-exercise-solution
:class: dropdown
```
1. Solutions are in the Example column in {numref}`range`.
2.
```{code-cell} ipython3
for i in range(3):
    print("Hello World!")
```
```{solution-end}
```

```{solution-start} break-continue
:label: break-continue-solution
:class: dropdown
```
1:
```{code-cell} ipython3
for letter in 'supercalifragilisticexpialidocious':  #1
   print('Current Letter :', letter)                 #2
   if letter == 'c':                                 #3
      break                                          #4
                                                     #5
print("I am now outside of the for loop")            #6
```
In the code above, the `print` statement in line 2 is at the same indentation as the `if` statement in line 3.  This means that when the `for` loop executes 
it will first execute this `print` statement (line 2) and then the `if` statement (line 3). Because of this, the "c" character is printed before 
the `for` loop can break.  When the `for` loop breaks, the loop does not continue its iterations and so the next line of code outside the `for` loop
(line 6) is executed next.    

2:
```{code-cell} ipython3
for i in range(10):                #1
    if i % 2 == 0:                 #2
        print("Even number:", i)   #3
    print("Odd number: ", i)       #4
```
Since `continue` was removed, no code inside the loop is skipped and both line 3 and line 4 are executed in each iteration of the loop.
```{solution-end}
```



```{solution-start} num-prog
:label: num-prog-solution
:class: dropdown
```
```{code-block}
x = 0
print("Welcome to the number program.")
print("To quit program enter -1")

# repeat the loop until x is -1
while x != -1:
    x = int(input("Enter a number:")) # we use int() to convert user input to an int
```
```{solution-end}
```


```{solution-start} fibonacci
:label: fibonacci-solution
:class: dropdown
```
```{code-cell} python
a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a+b
```

```{tip}
To print a comma separated list instead replace `print(a)` with `print(a, end=',')` in line 3.  The `end` parameter takes as 
an argument a string appended after the last value (default is a newline if unspecified).  Use `help(print)` in console to 
learn more about the parameters that `print()` has.
```

```{solution-end}
```


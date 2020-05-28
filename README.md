# EasyScript

EasyScript is a simple language transpiled in Python. It is easy to use and to learn.

I make this language **FOR FUN** so, don't say "Oh he is stupid ! He thinks he'll create the new Python", you'll be kind ;-) .


![g951](https://user-images.githubusercontent.com/61330081/82749273-4ff8e680-9da8-11ea-9076-78a1a22df3b4.png)
Drawing by **_Akuro**, logo adaptation by **Wafelack**

Click [here](https://github.com/Wafelack/EasyScript/blob/master/README.md#EasyScript-Interpreter) to go to file interpreter documentation.

# EasyScript-CLI


## How to run EasyScript CLI 

Go to releases, download the latest stable release (or the latest pre release, if you live dangerously) and run it with Python 3.7.4 or higher (better is 3.7.6) or download the windows executable in the last release.

### Console displaying

```rust
//To display a string directly
>>> $ println! { My string
My string

//To display a variable

>>> $ println! # <variable>

//To display an array list
>>> $ println! arr <array>
```

### Variables

```javascript
//To initialize a variable
>>> $ let foo //do not forget the space after the variable name or you'd catch an error
Variable 'foo' initialized

//To edit a variable's value
>>> $ let foo 5
Val '5' assigned to foo
```

### Comments
To leave a comment, just write a sharp and then your comment
```python
# My comment here 
```

### Arrays

Arrays aren't editable at this moment, but they'll be soon.

```rust
//to declare an array
array <name> content A;content B;content C;etc
```

### String concatenation
```javascript
>>> $ let a Hello 
>>> $ let b World !
// And then i concatenate my Strings
>>> $ sc a b
Hello World !
```

### Mathematical Operations

In EasyScript, you can only use integers between -32768 and 32768.

```javascript
//Multiplication
>>> $ 5 * 5
25
//Division
>>> $ 5 / 5
1
//Subtraction
>>> $ 5 - 5
0
//Addition
>>> $ 5 + 5
10
//<number> power <number>
>>> $ 4 ** 4
256
//Square root
>>> $ sqrt 25
5
```


### Comparison

KeyWord 'comp' is used to compare two variables
```javascript
>>> $ let a Hello
>>> $ let b Hello
//then i compare these two variables
>>> $ comp a b
a == b
```

### System commands
To execute system command, you'll use the keyword 'sys'
```javascript
>>> $ sys -> echo Hello World
Hello World
>>> $
```

### Input
To inpute some data, you'll use keyword 'scan()' in variable declaration
```javascript
>>> $ let a scan()
//It creates a prompt to input my data
> 5
>>> $ println! # a
5
```

### Random Numbers
To have a random number in a variable, you'll have to use keyword 'rand()'

The syntax is : 
```javascript
>>> $ let <var> rand() <int> -> <int>
```

Example : 
```javascript
>>> $ let a rand() 1 -> 100
>>> $ println! # a
45
```
### Change array value
```javascript
>>> $ chnge arr <array name>
//program will print variable value here
enter new array value
> //type new value here using separator ";"
```
You can do the same thing here,  just write ```chng let //var name here```

### Exit Function
The simplest function ever, i don't have to explain it
```javascript
>>> $ quit
/wafelack/desktop/easyscript/~ $
```

### Wipe Function
Used to erase all the variables
```
>>> $ wipe
All variables erased !
>>> $ 
```
# EasyScript-Interpreter

This is the interpreter of EasyScript language

It works on a function that is pretty similar to CLI's.

### Run EasyScript Interpreter
To run it, you have to launch the main.py file it with Python 3.x.x (better is 3.7.6) or to run the executable in the last release

### How to source code file interpreting

Create a file with .esi extension and write your source code in it.

Then write the file's path in the prompt.


Don't forget to leave a star and to follow me if you liked it !
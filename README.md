# EasyScript 

EasyCript is a simple language transpiled in Python. It is easy to use and to learn.

I make this language **FOR FUN** so, don't say "Oh he is silly ! His language will never be used", you'll be kind ;-) .

## EasyScriptCLI

It is the only EasyScript version available at this day.

I want to improve first the possibilities in console and after, maybe i'll make an interpreter for source code files.

## How to run EasyScript CLI Interpreter

Go to releases, download the latest stable release (or the latest pre release, if you live dangerously) and run it with Python 3.7.4 or higher.

### Console displaying

```rust
//To display a string directly
>>> $ println! { My string
My string

//To display a variable

>>> $ println! # <variable>

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
### String concatenation
```javascript
>>> $ let a Hello 
>>> $ let b World !
// And then i concatenate my Strings
>>> $ sc a b
Hello World !
```

### Mathematical Operations

In EasyScript, you can only use integers between -255 and 255 on all operations excepted in square root

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
>>> $ sys() -> echo Hello World
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
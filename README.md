# EasyScript 

EasyCript is a simple language transpiled in Python

## EasyScriptCLI

It is the only EasyScript version available at this day.

### Console displaying

```rust
//To display a string directly
>>> $ println! { My string
My string

//To display a variable

>>> $ println! # <variable>

```

### Variable declaration

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

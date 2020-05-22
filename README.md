# Hello World

## Story

No question that your first programming exercise must be a [Hello, World!](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) implementation.

## What are you going to learn?

You'll have to use:

 - functions,
 - parameters,
 - call your function with arguments,
 - and also be able to run your script from command line with arguments!

## Tasks


1. Implement the `hello_world()` function which returns `Hello, World!`

    - [MANDATORY] The returned string of the function is exactly `Hello, World!`
    - Function `hello_world()` itself does not print anything

2. Create and implement the parametrized function `hello(name)` that takes one string argument and returns `Hello, <name>!`

    - For any non-empty String return `Hello, <name>!`
    - If `name` is empty or None, return `Hello, World!`
    - Function `hello(name)` itself does not print anything

3. Create and implement the `print_hello(name)` function which prints the result of `hello(name)`!

    - Calling `print_hello(name)` prints `Hello, <name>!`
    - Function `print_hello()` calls `hello()` and uses its return value

4. Implement the main (outside any functions) part of `hello.py` so that it prints the result of `hello(name)` when called from the command line by `python3 hello.py <name>`

    - Calling from the command line with one argument prints `Hello, <name>!` to the console
    - The command line call uses `hello(name)`'s return value

5. [OPTIONAL] Implement the main (outside any functions) part of `hello.py` so that it prints the result of `hello(name)` when called from the command line with multiple arguments by `python3 hello.py <name1> <name2> <name3>`. The required result is `Hello, <name1> <name2> <name3>!`

    - Calling from the command line with multiple argument prints `Hello, <name1> <name2> <name3>!` to the console
    - The command line call uses `hello(name)`'s return value
    - It works for any number of arguments


## General requirements


 - Have an installed a Python 3 environment, and an editor to write code!

## Hints

None

## Starting repository

Follow [this link](https://journey.code.cool/v2/project/solo/blueprint/hello-world/python) to create your project repository.

## Background materials

- :exclamation: [How to approach learning Python?](../pages/python/learning-python.md)
- :exclamation: [Strings](../pages/python/strings.md)
- :exclamation: [Functions](../pages/python/functions.md)
- [Command line arguments in Python](https://appdividend.com/2019/01/22/python-sys-argv-tutorial-command-line-arguments-example/)
- [How to clone a Git repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

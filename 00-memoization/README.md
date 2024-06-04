# memoization
This note is from a video in my youtube channel,
Link to the video: `will be added`
Author: [mosadeghi](https://github.com/mosadeghi)
## "How to improve the performance of my recursive function?"
Recursive functions are often a straightforward approach to solving certain problems. However, their runtime performance may not always be optimal. __Memoization__ is a technique for improving the runtime of recursive functions. Let's explore this concept using the well-known Fibonacci sequence as an example.

## Fibonacci
The Fibonacci sequence is a series of numbers where the first and second terms are both `1`, and subsequent terms are the sum of the preceding two terms. It's a popular example for examining recursive functions. Here's the Python code for the Fibonacci sequence:
```
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```
- [normal-fib.py](/00-memoization/normal-fib.py)

#### Problem
The issue is that, for instance, if we want to calculate the 5th term, calling the function for `6` will cause it to call itself for `5` and `4`, and each of those will call the function for `4` and `3`, and `3` and `2` and so on. This results in a tree of function calls that grows exponentially:
```
                         ___________ fib(6)_________
                        |                           |
                    fib(5)                       fib(4)
                  /        \                     |     \
            fib(4)          fib(3)            fib(3)    fib(2)
          /       \          |    \           /  \       |    \
    fib(3)        fib(2)    fib(2) fib(1) fib(2) fib(1) fib(1) fib(0)
    /   \         /   \      |    \         |   \
fib(2) fib(1) fib(1) fib(0) fib(1) fib(0) fib(1) fib(0)
   |  \
fib(1) fib(0)
---
n = 6

number of function calls = 25 : O(2^n)
```
#### Solution: Don't Repeat Yourself!
If you look at the tree above, you will notice that the function is called multiple times for some values. However, the function has a specific output for each specific value, and the output for each input does not change with each call. Therefore, a solution could be to remember the output each time the function is called for a value, and return that value the next time instead of recalculating it. __this is what memoization is about!__

## Fibonnaci but memoized
take a look at this code:

```
def make_fib():
    values = {0:1, 1:1}
    def fib(n):
        if n not in values:
            values[n] = fib(n-1) + fib(n-2)
        return values[n]
    return fib
fib = make_fib()
```
- [memoized-fib.py](/00-memoization/memoized-fib.py)

In this case, The outer function defines a closure. Closures in Python allow inner functions to access and modify variables from their enclosing functions scope, even after the outer function has finished executing.
The inner function calculates the nth fibonacci number using memoization.
It checks if the value is already in the dictionary, if not, it calculates the value by adding the fibonacci numbers of `n-1` and `n-2` and stores it in the dictionary before returning it.
So, in the first run, the tree of function calls for `fib(6)` will be:
```
fib(6)
   |  \
fib(4) fib(5)
   |  \
fib(3) fib(2)
   |  \
fib(2) fib(1)
   |  \
fib(1) fib(0)
---
n = 6
number of function calls = 9 : O(n)
```
---

## This note is still incomplete and will be added to.

---
Links:
- [list of contents](/README.md)
- [my youtube channel](https://www.youtube.com/@amirmosadeghi)

All notes and codes are written by [mosadeghi](https://github.com/mosadeghi). Parts of this text were originally written in Persian and then translated to English and edited using Google's Gemini AI.
Sharing all materials and codes with attribution is allowed.

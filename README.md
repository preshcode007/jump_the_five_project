# Jump the Five

## What does this project do?
A text is passed into the program and it encodes any number in a given string using an algorightm to "jump the five" on a standard US telephone keypad such that "1" becomes "9," "4" becomes "6," etc. 

## What I have been able to learn from this project so far:
- Creation of a dictionary and understanding some of the
  the methods associated with a dictionary via the help  
  funtiion.

- Better understanding of FOR loop and IF and ELSE statements

- Check if items exist in a dictionary and aslo retrieving      Values from a dictionary.

- Creation of new tests to add robustness to the code.

- Print a new string with the numbers substituted with their   encoded values



Encode only the numbers and leave all other text alone:

```
$ ./jump.py 867-5309
243-0751
```

If given no arguments, present a brief usage:

```
$ ./jump.py
usage: jump.py [-h] str
jump.py: error: the following arguments are required: str
```

Respond to `-h` or `--help` with a longer usage:

```
$ ./jump.py -h
usage: jump.py [-h] str

Jump the Five

positional arguments:
  str         Input text

optional arguments:
  -h, --help  show this help message and exit
```

If the `s` flag  or `--strings` flag is present:

```
$ ./jump.py "Call 900-501-4435" -s
Call nine-zero-zero-five-zero-one-four-four-three-five
```

Run the test suite to ensure your program is working correctly:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 5 items

test.py::test_exists PASSED                                              [ 20%]
test.py::test_usage PASSED                                               [ 40%]
test.py::test_01 PASSED                                                  [ 60%]
test.py::test_02 PASSED                                                  [ 80%]
test.py::test_03 PASSED                                                  [100%]

============================== 5 passed in 0.87s ===============================
```

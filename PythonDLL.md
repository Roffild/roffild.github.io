---
pgtitle: MetaTrader 5 (MQL5) + Python 3 DLL
title: MetaTrader 5 (MQL5) + Python 3 DLL for Forex, CFD and Futures
description: A data exchange between the MQL and Python via pre-created function.
---
Use MetaTrader with Python 3 on financial stock exchanges, Forex, CFD and Futures.
From MetaTrader, you can get quotes in Python, but no complete connection between them.
[This post is one of the developers (RU).](https://www.mql5.com/ru/forum/306688/page4#comment_10973513){:target="_blank"}

This wrapper was created with changes in Python 3.7
[Download ZIP from GitHub.](https://github.com/Roffild/RoffildLibrary/archive/master.zip){:target="_blank"}

Python is now the standard for machine learning libraries ([TensorFlow](https://www.tensorflow.org/){:target="_blank"}, [PyTorch](https://pytorch.org/){:target="_blank"}, etc.).
Python itself is quite slow and therefore all machine learning library on C/C++ using it only for user interaction.
[It is not always possible to connect machine learning libraries directly to the C/C++ code without problems.](https://github.com/tensorflow/tensorflow/issues/22338){:target="_blank"}

The main idea and the difference of this wrapper: a data exchange between the MQL and Python via pre-created function.
This is the fastest and most reliable data exchange method.
There is no time spent on parsing and compiling Python code that appears when using [eval()](https://docs.python.org/3/library/functions.html#eval){:target="_blank"}.

There is a class [(the actual code here)](https://github.com/Roffild/RoffildLibrary/blob/master/Libraries/Roffild/PythonDLL/start.py){:target="_blank"}:
```python
class MQL():
    def getLong(self, magic: int, value: int, array: tuple) -> tuple or list:
        raise NotImplementedError

    def getULong(self, magic: int, value: int, array: tuple) -> tuple or list:
        raise NotImplementedError

    def getDouble(self, magic: int, value: float, array: tuple) -> tuple or list:
        raise NotImplementedError

    def getString(self, magic: int, value: str, array: bytes) -> str:
        raise NotImplementedError


__mql__ = MQL()
```
The class name does not matter, because the reflection of the functions is via the variable `__mql__`.
Also, the `pyEval(..., override_class)` function has the argument `override_class=true` when the variable `__mql__` changes.

Example:<br/>
[PythonDLL_Example.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/PythonDLL_Example.mq5){:target="_blank"} and
[PythonDLL_Example.py](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/PythonDLL_Example.py){:target="_blank"}

You can define the Python code execution environment:
```python
if globals().get('__PythonDLL__'):
    print('run in MetaTrader')
elif __name__ == '__main__':
    print('run as script')
```

## Problems and solutions

When testing is required ["Allow DLL imports"](https://www.metatrader5.com/en/terminal/help/startworking/settings#ea){:target="_blank"} at the global level.

The search for the necessary python3.dll occurs in the following order:
1. In the folder with terminal64.exe or metatester64.exe when testing on Agents.
2. In the folders specified in the variable PATH.
[Simply change the variable PATH](https://www.google.com/search?q=windows+path+environment+variable){:target="_blank"}, and at the same time to clean it from a "trash".

If python3.dll is not found:
```
Cannot load 'Roffild\PythonDLL\x64\Release\PythonDLL.dll' [126]
Cannot call 'pyInitialize', 'Roffild\PythonDLL\x64\Release\PythonDLL.dll' is not loaded
unresolved import function call
```

Python is not only python3.dll, but also its environment that needs to be configured.
The most popular and simple solution is to install [Anaconda](https://www.anaconda.com/distribution/){:target="_blank"}.
There is also [Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html){:target="_blank"} (minimum 200MB), if you clearly know which packages will be needed when running the script.

Python was created as a separate application, and with embeddability there are problems that are unlikely to ever be fixed:
* Some functions from the API call Py_FatalError(), which calls the system [abort()](https://docs.microsoft.com/cpp/c-runtime-library/reference/abort){:target="_blank"} to terminate the process. MetaTrader may close without warning. [issue30560](https://bugs.python.org/issue30560){:target="_blank"}, [issue9828](https://bugs.python.org/issue9828){:target="_blank"}
* Py_Initialize() calls Py_FatalError() on error. If this happens, the most likely path to the Python environment is incorrect.
* A standard Python library is required to run. Py_SetPath() sets the path to this library before calling Py_Initialize().
* Calling pyFinalize() to free memory makes sense, but because of a bug in the popular NumPy library, you should not do this. [issue8097](https://github.com/numpy/numpy/issues/8097){:target="_blank"}, [issue34309](https://bugs.python.org/issue34309){:target="_blank"}

With the active console, you can notice the output of Py_FatalError() until it disappears:
```
Fatal Python error: Py_Initialize: unable to load the file system codec
```

Compile errors and Python code execution errors are not automatically displayed on the active console.
But when using the class [CPythonDLL](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/PythonDLL.mqh){:target="_blank"}, errors are displayed in the terminal log.

There is always only one instance of Python to execute code.
If several experts, indicators and scripts simultaneously use this Python wrapper without synchronization in one MetaTrader, then the result is not guaranteed.
There is no such problem when testing.

Memory allocation is a long operation, but it doesn’t depend on the amount of memory requested.
It will be faster to pre-allocate one megabyte per line and use this buffer several times rather than requesting the required amount of memory each time.

When using the [multiprocessing](https://docs.python.org/3/library/multiprocessing.html){:target="_blank"} module, you must specify the absolute path to the file in `__file__` and` sys.argv`. [An example is here.](https://gist.github.com/Roffild/bbe833354da6f70a3395bc13b25bff60){:target="_blank"}

## Sub-interpreters

The wrapper was created with sub-interpreters, but I had to use a simple GIL.
Sub-interpreters are not compatible with the popular libraries for Python.
[issue37186](https://bugs.python.org/issue37186){:target="_blank"}, [issue10915](https://bugs.python.org/issue10915){:target="_blank"}.
But you can build this wrapper with `PYTHONDLL_SUBINTERPRETERS`.

When you run in the terminal several independent experts, indicators and scripts that use this wrapper for each thread gets its own isolated interpreter using [Py_NewInterpreter()](https://docs.python.org/3/c-api/init.html#c.Py_NewInterpreter){:target="_blank"}.
But there may be a delay in switching the thread, because Python does not have full multi-threaded execution, but a [global interpreter lock (GIL)](https://docs.python.org/3/glossary.html#term-global-interpreter-lock){:target="_blank"} that blocks other threads when executing Python code.

When testing, there is always only one interpreter.

## For developers

[Official article on creating a DLL.](https://www.mql5.com/en/articles/18){:target="_blank"}

Addition to the article:
* The returned data from the function C/C++ in MQL are not released automatically, so you need to return only simple types.
* The C/C++ function can not change the size of the transferred MQL array.

The int type in Python is infinite:
```python
int("9999999999999999999999999999999999999999999999", 10).bit_length() == 153
```

Types in MQL:
```
long = 8 bytes (64 bits) = -9 223 372 036 854 775 808 ... 9 223 372 036 854 775 807
ulong = 8 bytes (64 bits) = 0 ... 18 446 744 073 709 551 615
```

CrashDumps:
```
%LOCALAPPDATA%\CrashDumps\
```

[On all questions to address in this topic.](https://www.mql5.com/en/forum/247134){:target="_blank"}

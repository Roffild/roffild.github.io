﻿---
pgtitle: MetaTrader 5 (MQL5) + Python 3 DLL
title: MetaTrader 5 (MQL5) + Python 3 DLL для Forex, CFD и Futures
description: Обмен данными между MQL и Python через заранее созданные функции.
---
Использование MetaTrader с Python 3 на финансовых фондовых биржах, Forex, CFD и Futures.
Из MetaTrader можно получать котировки в Python, но нет полноценной связи между ними.
[Пост одного из разработчиков.](https://www.mql5.com/ru/forum/306688/page4#comment_10973513){:target="_blank"}

Эта обертка создавалась с учетом изменений в Python 3.7
[Скачать ZIP с GitHub.](https://github.com/Roffild/RoffildLibrary/archive/master.zip){:target="_blank"}

Python сейчас является стандартом для библиотек машинного обучения ([TensorFlow](https://www.tensorflow.org/){:target="_blank"}, [PyTorch](https://pytorch.org/){:target="_blank"} и т.п.).
Сам Python довольно медленный и поэтому все библиотеки машинного обучения на C/C++ используют его только для взаимодействия с пользователем.
[Не всегда можно без проблем подключить библиотеки машинного обучения на прямую к коду C/C++.](https://github.com/tensorflow/tensorflow/issues/22338){:target="_blank"}

Главная идея и отличие этой обертки от остальных: обмен данными между MQL и Python через заранее созданные функции.
Это самый быстрый и надежный метод обмена данными.
Нет затрат времени на синтаксический разбор и компиляцию кода Python, который появляется при использовании [eval()](https://docs.python.org/3/library/functions.html#eval){:target="_blank"}.

Имеется класс [(актуальный код тут)](https://github.com/Roffild/RoffildLibrary/blob/master/Libraries/Roffild/PythonDLL/start.py){:target="_blank"}:
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
Название класса неважно, потому что отражение функций идет через переменную `__mql__`.
Также у функции `pyEval(..., override_class)` аргумент `override_class=true`, когда изменяется переменная `__mql__`.

Пример:<br/>
[PythonDLL_Example.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/PythonDLL_Example.mq5){:target="_blank"} и
[PythonDLL_Example.py](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/PythonDLL_Example.py){:target="_blank"}

Можно определить среду выполнения кода Python:
```python
if globals().get('__PythonDLL__'):
    print('run in MetaTrader')
elif __name__ == '__main__':
    print('run as script')
```

## Проблемы и их решения

При тестировании требуется ["Разрешить импорт DLL"](https://www.metatrader5.com/ru/terminal/help/startworking/settings#ea){:target="_blank"} на глобальном уровне.

Поиск необходимой python3.dll происходит в следующем порядке:
1. В папках с terminal64.exe или metatester64.exe при тестировании на Агентах.
2. В папках, указанных в переменной PATH.
[Проще изменить переменную PATH](https://www.google.com/search?q=windows+path+environment+variable){:target="_blank"} и заодно почистить ее от "мусора".

Если ли python3.dll не найдена:
```
Cannot load 'Roffild\PythonDLL\x64\Release\PythonDLL.dll' [126]
Cannot call 'pyInitialize', 'Roffild\PythonDLL\x64\Release\PythonDLL.dll' is not loaded
unresolved import function call
```

Python это не только python3.dll, но и его окружение, которое нужно настраивать.
Самое популярное и простое решение это установить [Anaconda](https://www.anaconda.com/distribution/){:target="_blank"}.
Есть еще [Miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html){:target="_blank"} (минимум 200МБ), если четко знаешь, какие пакеты понадобятся при выполнении скрипта.

Python создавался как отдельное приложение и при встраемости есть проблемы, которые вряд ли когда-нибудь будут исправлены:
* Некоторые функции из API вызывают Py_FatalError(), которая вызывает системную [abort()](https://docs.microsoft.com/cpp/c-runtime-library/reference/abort){:target="_blank"} для разрушения процесса. Поэтому MetaTrader может закрыться без предупреждения. [issue30560](https://bugs.python.org/issue30560){:target="_blank"}, [issue9828](https://bugs.python.org/issue9828){:target="_blank"}
* Py_Initialize() вызывает Py_FatalError() при ошибке. Если это происходит, то, скорей всего, путь к окружению Python неправильный.
* Для запуска необходима стандартная библиотека на языке Python. Py_SetPath() задает путь к этой библиотеке до вызова Py_Initialize().
* Вызов pyFinalize() для освобождения памяти имеет смысл, но из-за бага в популярной библиотеке NumPy этого делать не стоит. [issue8097](https://github.com/numpy/numpy/issues/8097){:target="_blank"}, [issue34309](https://bugs.python.org/issue34309){:target="_blank"}

При активной консоли можно заметить вывод Py_FatalError(), пока она не исчезнет:
```
Fatal Python error: Py_Initialize: unable to load the file system codec
```

Ошибки компиляции и выполнения кода Python не отображаются автоматически на активной консоли.
Но при использовании класса [CPythonDLL](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/PythonDLL.mqh){:target="_blank"} ошибки отображаются в логе терминала.

Всегда есть только один экземпляр Питона для выполнения кода.
Если несколько экспертов, индикаторов и скриптов будут одновременно использовать эту обертку Питона без синхронизации в одном MetaTrader, то результат не гарантируется.
При тестировании такой проблемы нет.

Выделение памяти - долгая операция, но от объема запрошенной памяти это неслишком зависит.
Быстрее будет заранее выделить один мегабайт под строку и использовать этот буффер несколько раз, нежели каждый раз запрашивать необходимый объем памяти.

При использовании модуля [multiprocessing](https://docs.python.org/3/library/multiprocessing.html){:target="_blank"} необходимо указывать абсолютный путь к файлу в `__file__` и `sys.argv`. [Пример находится здесь.](https://gist.github.com/Roffild/bbe833354da6f70a3395bc13b25bff60){:target="_blank"}

## Sub-interpreters

Обертка создавалась с суб-интерпретаторами, но пришлось использовать простой GIL.
Суб-интерпретаторы не совместимы с популярными библиотеками для Питона.
[issue37186](https://bugs.python.org/issue37186){:target="_blank"}, [issue10915](https://bugs.python.org/issue10915){:target="_blank"}.
Но можно собрать эту обертку с `PYTHONDLL_SUBINTERPRETERS`.

При запуске в терминале нескольких независимых экспертов, индикаторов и скриптов, использующих эту обертку, для каждого потока создается свой изолированный интерпретатор с помощью [Py_NewInterpreter()](https://docs.python.org/3/c-api/init.html#c.Py_NewInterpreter){:target="_blank"}.
Но может возникнуть задержка при переключении потока, потому что в Python нет полноценного многопоточного выполнения, а есть [global interpreter lock (GIL)](https://docs.python.org/3/glossary.html#term-global-interpreter-lock){:target="_blank"}, который блокирует другие потоки при выполнении кода Python.

При тестировании всегда есть только один интерпретатор.

## Для разработчиков

[Официальная статья по созданию DLL.](https://www.mql5.com/ru/articles/18){:target="_blank"}

Дополнение к статье:
* Возвращаемые данные из функции C/C++ в MQL не освобождаются автоматически, поэтому нужно возвращать только простые типы.
* В функции C/C++ нельзя изменять размер переданного из MQL массива.

Тип int в Python бесконечный:
```python
int("9999999999999999999999999999999999999999999999", 10).bit_length() == 153
```

Типы в MQL:
```
long = 8 байт (64 бита) = -9 223 372 036 854 775 808 ... 9 223 372 036 854 775 807
ulong = 8 байт (64 бита) = 0 ... 18 446 744 073 709 551 615
```

CrashDumps:
```
%LOCALAPPDATA%\CrashDumps\
```

[По всем вопросам обращаться в эту тему.](https://www.mql5.com/ru/forum/245373){:target="_blank"}

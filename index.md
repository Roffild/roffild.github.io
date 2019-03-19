---
pgtitle: Roffild's Library
title: "MQL5 (MetaTrader): Machine Learning, Random Forest, Python, Java, Apache Spark, AWS for Forex, CFD and Futures"
---
[Download ZIP from GitHub.](https://github.com/Roffild/RoffildLibrary/archive/master.zip){:target="_blank"}

I am known to the MQL5 community by the name of Roffild and this is my open source library for MQL5.
An attempt to implement the features on MQL5, which have long become the standard for popular programming languages.
Each file has one idea. The library is replenished as needed for new capabilities.

Few people tried to put the project in Github. There is no single standard.
MetaQuotes does not use version control systems when creating a project.
For some reason, programmers from MetaQuotes believe that the project should be of the same type.
For small projects that are published in CodeBase on the MQL5.com site, this division is justified.
For medium and large projects, it is not possible to select one type of project.

I experimented with different structure of the project.
To use Git, I had to take the files out of the standard folder structure that MetaQuotes adopted.
Create a link to the staging folder (in this library, the folder "Roffild") - the best option.

MetaEditor can save code in UTF-16, but encoding UTF-8 with BOM is also supported.
To convert a file with the source code, you need to use a third-party editor (I recommend [Notepad++](https://notepad-plus-plus.org/){:target="_blank"}).

This library can be divided into interests:
* common tasks (ArrayList, Log4MQL, ToIndicator, etc.);
* experiments with AlgLib in machine learning;
* using Apache Spark with Amazon Web Services (EC2 and EMR), when the capabilities of AlgLib ceased to be enough;
* using TensorFlow or PyTorch via [PythonDLL](https://roffild.com/PythonDLL.html){:target="_blank"}.

MQL5 is part of the trading platform MetaTrader 5 (MT5) for Forex, CFD and Futures. The version of MetaTrader 4 (MT4) with MQL4 is still used, but after the latest updates it is compatible with the MQL5 syntax. Officially, the version of MetaTrader 4 (MT4) is no longer supported, but for compatibility you can use ``` #property strict ``` at the beginning of the file.

### Documentation
[MQL5](https://roffild.com/mql5/){:target="_blank"}<br/>
[Java](https://roffild.com/java/){:target="_blank"}

### Links
[Roffild.com](https://roffild.com/){:target="_blank"}<br/>
[Github](https://github.com/Roffild/RoffildLibrary){:target="_blank"}<br/>
[GitLab](https://gitlab.com/Roffild/RoffildLibrary){:target="_blank"}<br/>
[BitBucket](https://bitbucket.org/Roffild/roffildlibrary/){:target="_blank"}<br/>
[MQL5.com: topic for discussion in English](https://www.mql5.com/en/forum/247134){:target="_blank"}<br/>
[MQL5.com: тема для обсуждения на Русском](https://www.mql5.com/ru/forum/245373){:target="_blank"}

-----------------
* [Experts/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/){:target="_blank"}
  * [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/AmazonUtils){:target="_blank"} - Can be used as an example of developing a project in Java.
  * [Alglib_MultilayerPerceptron.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Alglib_MultilayerPerceptron.mq5){:target="_blank"} - Create a neural network (Multilayer Perceptron) with two hidden layers.
  * [Alglib_RandomForest.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Alglib_RandomForest.mq5){:target="_blank"} - Create a random forest.
  * [Examples/](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/){:target="_blank"}
    * [PythonDLL_Example.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/PythonDLL_Example.mq5){:target="_blank"} and [PythonDLL_Example.py](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/PythonDLL_Example.py){:target="_blank"} - The example of using [PythonDLL](https://roffild.com/PythonDLL.html){:target="_blank"}.
    * [ToIndicator_Example.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/ToIndicator_Example.mq5){:target="_blank"}
* [Include/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/){:target="_blank"}
  * [MLPDataFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/MLPDataFile.mqh){:target="_blank"} - Data format for Alglib_MultilayerPerceptron and Alglib_RandomForest. MLPDataFile = CSV in a binary format.
  * [ArrayList_macros.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayList_macros.mqh){:target="_blank"} - This variant is still used because of poor template support by the code editor.
  * [ArrayList.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayList.mqh){:target="_blank"} - ArrayList from Java.
  * [ArrayListClass.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayListClass.mqh){:target="_blank"} - ArrayList from Java for Class only.
  * [ForestSerializer.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ForestSerializer.mqh){:target="_blank"} - Save and load data for the class CDecisionForest (Alglib).
  * [Log4MQL.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Log4MQL.mqh){:target="_blank"} and [Log4MQL_tofile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Log4MQL_tofile.mqh){:target="_blank"} + [module](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/LogMX){:target="_blank"} ([download](https://roffild.com/Log4MQLParser.zip){:target="_blank"}) for [LogMX](http://www.logmx.com/){:target="_blank"} - Logger for MQL5 (Log4MQL).
  * [OrderData.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/OrderData.mqh){:target="_blank"} - Simulation of orders with attached data for research.
    * [OrderSql.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/OrderSql.mqh){:target="_blank"} - Record data of simulated orders (COrderData) in a file format MySQL.
  * [SqlFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/SqlFile.mqh){:target="_blank"} - Write data to a file format MySQL.
    * [CsvFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/CsvFile.mqh){:target="_blank"} - Write data to a file format CSV.
  * [Statistic.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Statistic.mqh){:target="_blank"} - Counting data and printing out the accumulated information.
  * [TesterSql.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/TesterSql.mqh){:target="_blank"} - Record optimization results in SQL and CSV format files.
  * [ToIndicator.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ToIndicator.mqh){:target="_blank"} - Displaying data from Expert or Script using functions for indicators.
  * [UnitTest.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/UnitTest.mqh){:target="_blank"} - Base class for UnitTest.
  * [Serialization.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Serialization.mqh){:target="_blank"}
  * [RoffildJava/](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/){:target="_blank"}
    * [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/){:target="_blank"}
    * [RoffildLibrary](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/RoffildLibrary/){:target="_blank"}
    * [Spark](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/Spark/){:target="_blank"} - Reading from MLPDataFile.
    * [aws_ubuntu_user_data.sh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/src/main/resources/aws_ubuntu_user_data.sh){:target="_blank"} - Working script for raising test agents on Ubuntu in AWS. [The documentation is here.](https://roffild.com/agents.html){:target="_blank"}
  * [PythonDLL.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/PythonDLL.mqh){:target="_blank"} - Class for [PythonDLL](https://roffild.com/PythonDLL.html){:target="_blank"}.
  * [RoffildPython/](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildPython/){:target="_blank"}
* [Indicators/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/){:target="_blank"}
  * [ToIndicator.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator.mqh){:target="_blank"}
  * [ToIndicator.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator.mq5){:target="_blank"}
  * [ToIndicator_window.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator_window.mq5){:target="_blank"}
* [Libraries/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Libraries/Roffild/){:target="_blank"}
  * [PythonDLL/](https://github.com/Roffild/RoffildLibrary/blob/master/Libraries/Roffild/PythonDLL/){:target="_blank"} - [PythonDLL](https://roffild.com/PythonDLL.html){:target="_blank"}.
* [Scripts/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/){:target="_blank"}
  * [MLPDataFileSparkTest](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/MLPDataFileSparkTest){:target="_blank"} - Example project for Spark and MLPDataFile test.
  * [UnitTests](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/UnitTests){:target="_blank"}
* [buildall_and_tests.py](https://github.com/Roffild/RoffildLibrary/blob/master/buildall_and_tests.py){:target="_blank"} - The script builds all components of the library and run tests.

## Installation

(Optionally)

``` mklink /j link where ``` - does not require administrator rights.

It makes sense to move the ``` %APPDATA%\MetaQuotes ``` folder to the root of the partition or to a larger partition.
Windows has a limit of 255 characters to the file path. The full path to the MQL5 folder I have is 88 characters.
When testing, the terminal copies history by the number of local agents that increases the size of this folder by several gigabytes.
1. Move the ``` %APPDATA%\MetaQuotes ``` to ``` D:\MQLProjects ```
2. ``` mklink /j %APPDATA%\MetaQuotes D:\MQLProjects ```
3. ``` mklink /j D:\MQLProjects\Terminal\D0E8209F77C8CF37AD8BF550E51FF075\MQL5\ D:\MQLProjects\MQL5 ```

(Important)

Run the ``` create_links.bat ``` from the ``` MQL5\MyProjects\RoffildLibrary ``` folder after cloning the project.

## Code style

[Google Java Style](https://google.github.io/styleguide/javaguide.html){:target="_blank"}

Tab = 3 spaces

Column limit = 110

## License

[Apache License 2.0](https://github.com/Roffild/RoffildLibrary/blob/master/LICENSE){:target="_blank"}

<a href="https://roffild.com/" hreflang="en">English</a>, <a href="https://roffild.com/ru/" hreflang="ru">Russian</a>

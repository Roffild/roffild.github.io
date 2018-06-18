# Roffild's Library
{% include header.html %}

Docs: [MQL5](https://roffild.com/mql5/) [Java](https://roffild.com/java/)

* Experts/Roffild/
  * [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/AmazonUtils) - can be used as an example of developing a project in Java
  * [Alglib_MultilayerPerceptron.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Alglib_MultilayerPerceptron.mq5)
  * [Alglib_RandomForest.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Alglib_RandomForest.mq5)
  * [Examples/](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/)
    * [ToIndicator_Example.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/ToIndicator_Example.mq5)
* Include/Roffild/
  * [MLPDataFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/MLPDataFile.mqh) - data format for Alglib_MultilayerPerceptron and Alglib_RandomForest
  * [ArrayList_macros.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayList_macros.mqh) - this variant is still used because of poor template support by the code editor
  * [ArrayList.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayList.mqh)
  * [ArrayListClass.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayListClass.mqh)
  * [CsvFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/CsvFile.mqh)
  * [ForestSerializer.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ForestSerializer.mqh)
  * [Log4MQL.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Log4MQL.mqh) and [Log4MQL_tofile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Log4MQL_tofile.mqh) + [module](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/LogMX) for [LogMX](http://www.logmx.com/)
  * [OrderData.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/OrderData.mqh) - data dump for research
  * [OrderSql.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/OrderSql.mqh)
  * [Serialization.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Serialization.mqh)
  * [SqlFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/SqlFile.mqh)
  * [Statistic.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Statistic.mqh)
  * [TesterSql.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/TesterSql.mqh) - optimization results in SQL and CSV formats
  * [ToIndicator.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ToIndicator.mqh) - displaying data from an expert using indicators
  * [UnitTest.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/UnitTest.mqh)
  * [RoffildJava/](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/)
    * [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/)
    * [RoffildLibrary](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/RoffildLibrary/)
    * [Spark](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/Spark/) - reading from MLPDataFile
    * [aws_ubuntu_user_data.sh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/build/resources/main/aws_ubuntu_user_data.sh) - working script for raising test agents on Ubuntu 14 in AWS
* Indicators/Roffild/
  * [ToIndicator.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator.mqh)
  * [ToIndicator.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator.mq5)
  * [ToIndicator_window.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator_window.mq5)
* Scripts/Roffild/
  * [MLPDataFileSparkTest](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/MLPDataFileSparkTest) - example project for Spark and MLPDataFile test
  * [UnitTests](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/UnitTests)

## Installation

(Optionally)

``` mklink /j link where ``` - does not require administrator rights.

It makes sense to move the %APPDATA%\MetaQuotes folder to the root of the partition or to a larger partition.
Windows has a limit of 255 characters to the file path. The full path to the MQL5 folder I have is 88 characters.
When testing, the terminal copies history by the number of local agents that increases the size of this folder by several gigabytes.
1. Move the %APPDATA%\MetaQuotes to D:\MQLProjects
2. ``` mklink /j %APPDATA%\MetaQuotes D:\MQLProjects ```
3. ``` mklink /j D:\MQLProjects\Terminal\D0E8209F77C8CF37AD8BF550E51FF075\MQL5\ D:\MQLProjects\MQL5 ```

(Important)

Run the create_links.bat from the MQL5\MyProjects\RoffildLibrary folder after cloning the project.

## Code style

[Google Java Style](https://google.github.io/styleguide/javaguide.html)

Tab = 3 spaces

Column limit = 110

## License

[Apache License 2.0](https://github.com/Roffild/RoffildLibrary/blob/master/LICENSE)

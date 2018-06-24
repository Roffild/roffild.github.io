{% include google.html %}{% include header.html %}

Я известен сообществу программистов на MQL5 по ником Roffild и это моя библиотека с открытым кодом для MQL5. Попытка реализовать возможности на MQL5, которые уже давно стали стандартом для популярных языков программирования. В каждом файле реализована одна идея. Библиотека пополняется по мере необходимости в новых возможностях.

Мало кто пытался выложить проект в Github. Единого стандарта нет. MetaQuotes не учитывают использование системы контроля версий при создании проекта. Почему-то программисты из MetaQuotes считают, что проект должен быть одного типа. Для мелких проектов, которые публикуются в CodeBase на сайте MQL5.com, такое разделение обосновано. Для средних и крупных проектов невозможно выбрать один тип проекта.

Я экспериментировал с разной структурой построения проекта. Для использования Git пришлось вынести файлы за пределы стандартной структуры папок, принятой в MetaQuotes. Создать ссылку на промежуточную папку (в этой библиотеке папка "Roffild") - лучший вариант.

MetaEditor может сохранять код в UTF-16, но кодировка UTF-8 с BOM тоже поддерживается. Для конвертации файла с исходным кодом нужно использовать сторонний редактор (рекомендую [Notepad++](https://notepad-plus-plus.org/)).

Библиотеку можно разделить на интересы:
* обычные задачи (ArrayList, Log4MQL, ToIndicator и т.д.);
* эксперименты с AlgLib в машинном обучении;
* использование Apache Spark с Amazon Web Services (EC2 и EMR), когда возможностей AlgLib перестало хватать.

### Документация
[MQL5](https://roffild.com/mql5/)<br/>
[Java](https://roffild.com/java/)

### Ссылки
[Roffild.com](https://roffild.com/)<br/>
[Github](https://github.com/Roffild/RoffildLibrary)<br/>
[MQL5.com: topic for discussion in English](https://www.mql5.com/en/forum/247134)<br/>
[MQL5.com: тема для обсуждения на Русском](https://www.mql5.com/ru/forum/245373)

-----------------
* [Experts/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/)
  * [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/AmazonUtils) - Можно использовать как пример разработки проекта на Java.
  * [Alglib_MultilayerPerceptron.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Alglib_MultilayerPerceptron.mq5)
  * [Alglib_RandomForest.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Alglib_RandomForest.mq5)
  * [Examples/](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/)
    * [ToIndicator_Example.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/ToIndicator_Example.mq5)
* [Include/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/)
  * [MLPDataFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/MLPDataFile.mqh) - Формат данных для Alglib_MultilayerPerceptron и Alglib_RandomForest. MLPDataFile = CSV в бинарном формате.
  * [ArrayList_macros.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayList_macros.mqh) - Этот вариант еще используется из-за плохой поддержки шаблонов редактором кода.
  * [ArrayList.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayList.mqh) - ArrayList из Java.
  * [ArrayListClass.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayListClass.mqh) - ArrayList из Java только для Класса.
  * [ForestSerializer.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ForestSerializer.mqh) - Сохранение и загрузка данных для класса CDecisionForest (Alglib).
  * [Log4MQL.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Log4MQL.mqh) и [Log4MQL_tofile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Log4MQL_tofile.mqh) + [модуль](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/LogMX) ([скачать](https://roffild.com/Log4MQLParser.zip)) для [LogMX](http://www.logmx.com/) - Logger for MQL5 (Log4MQL).
  * [OrderData.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/OrderData.mqh) - Симуляция ордеров с прикреплёнными данными для исследований.
    * [OrderSql.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/OrderSql.mqh) - Запись данных от ордеров (COrderData) в файл формата MySQL.
  * [SqlFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/SqlFile.mqh) - Запись данных в файл формата MySQL.
    * [CsvFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/CsvFile.mqh) - Запись данных в файл формата CSV.
  * [Statistic.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Statistic.mqh) - Подсчёт данных и распечатка накопленной информации.
  * [TesterSql.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/TesterSql.mqh) - Запись результатов оптимизации в файлы SQL и CSV.
  * [ToIndicator.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ToIndicator.mqh) - Отображение данных из Эксперта или Скрипта с помощью индикаторов.
  * [UnitTest.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/UnitTest.mqh) - Базовый класс для UnitTest.
  * [Serialization.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Serialization.mqh)
  * [RoffildJava/](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/)
    * [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/)
    * [RoffildLibrary](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/RoffildLibrary/)
    * [Spark](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/Spark/) - Чтение из MLPDataFile.
    * [aws_ubuntu_user_data.sh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/build/resources/main/aws_ubuntu_user_data.sh) - Рабочий скрипт для поднятия агентов тестирования на Ubuntu 14 в AWS.
* [Indicators/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/)
  * [ToIndicator.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator.mqh)
  * [ToIndicator.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator.mq5)
  * [ToIndicator_window.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator_window.mq5)
* [Scripts/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/)
  * [MLPDataFileSparkTest](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/MLPDataFileSparkTest) - Пример проекта для Spark и тест MLPDataFile.
  * [UnitTests](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/UnitTests)

## Установка

(Необязательно)

``` mklink /j ссылка куда ``` - не требует прав администратора.

Имеет смысл вынести папку ``` %APPDATA%\MetaQuotes ``` в корень раздела или на раздел большего размера.
Windows имеет ограничения на 255 символов пути к файлу. Полный путь к папке MQL5 у меня состоит из 88 символов.
При тестировании терминал копирует историю по количеству локальных агентов, что увеличивает размер этой папки на несколько гигабайт.
1. Переместить папку ``` %APPDATA%\MetaQuotes ``` в ``` D:\MQLProjects ```
2. ``` mklink /j %APPDATA%\MetaQuotes D:\MQLProjects ```
3. ``` mklink /j D:\MQLProjects\Terminal\D0E8209F77C8CF37AD8BF550E51FF075\MQL5\ D:\MQLProjects\MQL5 ```

(Важно)

Запустить ``` create_links.bat ``` из папки ``` MQL5\MyProjects\RoffildLibrary ``` после клонирования проекта.

## Code style

[Google Java Style](https://google.github.io/styleguide/javaguide.html)

Tab = 3 spaces

Column limit = 110

## License

[Apache License 2.0](https://github.com/Roffild/RoffildLibrary/blob/master/LICENSE)

[English](https://roffild.com/), [Russian](https://roffild.com/index_ru.html)

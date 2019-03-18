---
pgtitle: Библиотека Roffild'a
title: "MQL5 (MetaTrader): Машинное обучение, Случайный лес, Java, Apache Spark, AWS для Forex, CFD и Futures"
---
[Скачать ZIP с GitHub.](https://github.com/Roffild/RoffildLibrary/archive/master.zip){:target="_blank"}

Я известен сообществу программистов на MQL5 под ником Roffild и это моя библиотека с открытым кодом для MQL5. Попытка реализовать возможности на MQL5, которые уже давно стали стандартом для популярных языков программирования. В каждом файле реализована одна идея. Библиотека пополняется по мере необходимости в новых возможностях.

Мало кто пытался выложить проект в Github. Единого стандарта нет. MetaQuotes не учитывают использование системы контроля версий при создании проекта. Почему-то программисты из MetaQuotes считают, что проект должен быть одного типа. Для мелких проектов, которые публикуются в CodeBase на сайте MQL5.com, такое разделение обосновано. Для средних и крупных проектов невозможно выбрать один тип проекта.

Я экспериментировал с разной структурой построения проекта. Для использования Git пришлось вынести файлы за пределы стандартной структуры папок, принятой в MetaQuotes. Создать ссылку на промежуточную папку (в этой библиотеке папка "Roffild") - лучший вариант.

MetaEditor может сохранять код в UTF-16, но кодировка UTF-8 с BOM тоже поддерживается. Для конвертации файла с исходным кодом нужно использовать сторонний редактор (рекомендую [Notepad++](https://notepad-plus-plus.org/){:target="_blank"}).

Библиотеку можно разделить на интересы:
* обычные задачи (ArrayList, Log4MQL, ToIndicator и т.д.);
* эксперименты с AlgLib в машинном обучении;
* использование Apache Spark с Amazon Web Services (EC2 и EMR), когда возможностей AlgLib перестало хватать;
* использование TensorFlow или PyTorch через [PythonDLL](https://roffild.com/ru/PythonDLL.html){:target="_blank"}.

MQL5 является частью торговой платформы MetaTrader 5 (MT5) для Forex, CFD и Futures. До сих пор используется версия MetaTrader 4 (MT4) с MQL4, но после последних обновлений совместима с синтаксисом MQL5. Официально версия MetaTrader 4 (MT4) уже не поддерживается, но для совместимости можно использовать ``` #property strict ``` в начале файла.

### Документация
[MQL5](https://roffild.com/mql5/){:target="_blank"}<br/>
[Java](https://roffild.com/java/){:target="_blank"}

### Ссылки
[Roffild.com](https://roffild.com/ru/){:target="_blank"}<br/>
[Github](https://github.com/Roffild/RoffildLibrary){:target="_blank"}<br/>
[GitLab](https://gitlab.com/Roffild/RoffildLibrary){:target="_blank"}<br/>
[BitBucket](https://bitbucket.org/Roffild/roffildlibrary/){:target="_blank"}<br/>
[MQL5.com: topic for discussion in English](https://www.mql5.com/en/forum/247134){:target="_blank"}<br/>
[MQL5.com: тема для обсуждения на Русском](https://www.mql5.com/ru/forum/245373){:target="_blank"}

-----------------
* [Experts/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/){:target="_blank"}
  * [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/AmazonUtils){:target="_blank"} - Можно использовать как пример разработки проекта на Java.
  * [Alglib_MultilayerPerceptron.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Alglib_MultilayerPerceptron.mq5){:target="_blank"} - Создание нейронной сети (Multilayer Perceptron) с двумя скрытыми слоями.
  * [Alglib_RandomForest.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Alglib_RandomForest.mq5){:target="_blank"} - Создание случайного леса.
  * [Examples/](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/){:target="_blank"}
    * [PythonDLL_Example.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/PythonDLL_Example.mq5){:target="_blank"} - Пример использования [PythonDLL](https://roffild.com/ru/PythonDLL.html){:target="_blank"}.
    * [ToIndicator_Example.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/Examples/ToIndicator_Example.mq5){:target="_blank"}
* [Include/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/){:target="_blank"}
  * [MLPDataFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/MLPDataFile.mqh){:target="_blank"} - Формат данных для Alglib_MultilayerPerceptron и Alglib_RandomForest. MLPDataFile = CSV в бинарном формате.
  * [ArrayList_macros.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayList_macros.mqh){:target="_blank"} - Этот вариант еще используется из-за плохой поддержки шаблонов редактором кода.
  * [ArrayList.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayList.mqh){:target="_blank"} - ArrayList из Java.
  * [ArrayListClass.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ArrayListClass.mqh){:target="_blank"} - ArrayList из Java только для Класса.
  * [ForestSerializer.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ForestSerializer.mqh){:target="_blank"} - Сохранение и загрузка данных для класса CDecisionForest (Alglib).
  * [Log4MQL.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Log4MQL.mqh){:target="_blank"} и [Log4MQL_tofile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Log4MQL_tofile.mqh){:target="_blank"} + [модуль](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/LogMX){:target="_blank"} ([скачать](https://roffild.com/Log4MQLParser.zip){:target="_blank"}) для [LogMX](http://www.logmx.com/){:target="_blank"} - Logger for MQL5 (Log4MQL).
  * [OrderData.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/OrderData.mqh){:target="_blank"} - Симуляция ордеров с прикреплёнными данными для исследований.
    * [OrderSql.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/OrderSql.mqh){:target="_blank"} - Запись данных от ордеров (COrderData) в файл формата MySQL.
  * [SqlFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/SqlFile.mqh){:target="_blank"} - Запись данных в файл формата MySQL.
    * [CsvFile.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/CsvFile.mqh){:target="_blank"} - Запись данных в файл формата CSV.
  * [Statistic.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Statistic.mqh){:target="_blank"} - Подсчёт данных и распечатка накопленной информации.
  * [TesterSql.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/TesterSql.mqh){:target="_blank"} - Запись результатов оптимизации в файлы SQL и CSV.
  * [ToIndicator.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/ToIndicator.mqh){:target="_blank"} - Отображение данных из Эксперта или Скрипта с помощью индикаторов.
  * [UnitTest.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/UnitTest.mqh){:target="_blank"} - Базовый класс для UnitTest.
  * [Serialization.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/Serialization.mqh){:target="_blank"}
  * [RoffildJava/](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/){:target="_blank"}
    * [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/){:target="_blank"}
    * [RoffildLibrary](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/RoffildLibrary/){:target="_blank"}
    * [Spark](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/Spark/){:target="_blank"} - Чтение из MLPDataFile.
    * [aws_ubuntu_user_data.sh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/src/main/resources/aws_ubuntu_user_data.sh){:target="_blank"} - Рабочий скрипт для поднятия агентов тестирования на Ubuntu в AWS. [Инструкция здесь.](https://roffild.com/ru/agents.html){:target="_blank"}
  * [PythonDLL.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/PythonDLL.mqh){:target="_blank"} - Класс для [PythonDLL](https://roffild.com/ru/PythonDLL.html){:target="_blank"}.
  * [RoffildPython/](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildPython/){:target="_blank"}
* [Indicators/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/){:target="_blank"}
  * [ToIndicator.mqh](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator.mqh){:target="_blank"}
  * [ToIndicator.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator.mq5){:target="_blank"}
  * [ToIndicator_window.mq5](https://github.com/Roffild/RoffildLibrary/blob/master/Indicators/Roffild/ToIndicator_window.mq5){:target="_blank"}
* [Libraries/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Libraries/Roffild/){:target="_blank"}
  * [PythonDLL/](https://github.com/Roffild/RoffildLibrary/blob/master/Libraries/Roffild/PythonDLL/){:target="_blank"} - [PythonDLL](https://roffild.com/ru/PythonDLL.html){:target="_blank"}.
* [Scripts/Roffild/](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/){:target="_blank"}
  * [MLPDataFileSparkTest](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/MLPDataFileSparkTest){:target="_blank"} - Пример проекта для Spark и тест MLPDataFile.
  * [UnitTests](https://github.com/Roffild/RoffildLibrary/blob/master/Scripts/Roffild/UnitTests){:target="_blank"}
* [buildall_and_tests.py](https://github.com/Roffild/RoffildLibrary/blob/master/buildall_and_tests.py){:target="_blank"} - Скрипт сборки всех компонентов библиотеки и запуска тестов.

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

[Google Java Style](https://google.github.io/styleguide/javaguide.html){:target="_blank"}

Tab = 3 spaces

Column limit = 110

## License

[Apache License 2.0](https://github.com/Roffild/RoffildLibrary/blob/master/LICENSE){:target="_blank"}

<a href="https://roffild.com/" hreflang="en">English</a>, <a href="https://roffild.com/ru/" hreflang="ru">Russian</a>

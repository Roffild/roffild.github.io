---
title: "MetaTrader 5 Агенты & AWS EC2 (VPS/VDS) для Forex, CFD и Futures"
pgtitle: MetaTrader 5 Агенты & AWS EC2
description: Использование MetaTrader 5 (MT5) Agents на серверах Амазона VPS/VDS. Это отличный вариант проверки торговой стратегии для валютных и биржевых рынков Forex, CFD и Futures.
---

Использование MetaTrader 5 (MT5) Agents на серверах Амазона VPS/VDS.
Это отличный вариант проверки торговой стратегии для валютных и биржевых рынков Forex, CFD и Futures.

MetaTrader 4 (MT4) не имеет Агентов тестирования.

Отличие от использования облака Агентов:
* Фиксированная цена за час и фиксированное количество ядер процессора.
* Возможность использования локальных файлов из FILE_COMMON.
* Возможность использования OpenCL на CPU (и GPU, если инстанс позволяет).
* Закачивать большие файлы, необходимые для тестирования, можно через ведро S3.
* Вероятна возможность использования динамических библиотек (DLL).

Агенты запускаются с флагом "/local", как при локальном использовании.

Затраты при использовании серверов Амазона могут быть гораздо экономичнее, чем при использовании облака Агентов.
Расчёт стоимости облака происходит по загадочной формуле, поэтому очень сложно оценить затраты на полную оптимизацию.

## В чём выгода?
Цены на спот-инстансы доступны [здесь](https://aws.amazon.com/ru/ec2/spot/pricing/){:target="_blank"}. Но после регистрации становится доступна таблица, которую можно получить [при создании спот-инстанса](https://console.aws.amazon.com/ec2sp/v1/spot/home){:target="_blank"} и нажав на серую кнопку "Select".<br/>
![Spot Prices](/images/agent-spot.png)

Есть особый инстанс:<br/>
cc2.8xlarge CPUs 32 Memory	60.5GiB SSD	4 x 840 GB<br/>
Цена в диапазоне от $0.20 до $0.30 за час, что соответствует инстансам с 16 CPUs. Этот инстанс имеет статус устаревшего и может периодически исчезать из списка доступных. Имеет смысл просматривать все 4 региона США на его доступность перед заказом инстанса.

cc2.8xlarge идеально подходит для Агентов тестирования.

## Начальная настройка
Имеет смысл в четырёх регионах США создать правило для [Security Groups](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#SecurityGroups:sort=groupId){:target="_blank"}.<br/>
![Security Groups](/images/agent-security-groups-main.png)<br/>
[N. Virginia](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#SecurityGroups:sort=groupId){:target="_blank"},
[Ohio](https://console.aws.amazon.com/ec2/v2/home?region=us-east-2#SecurityGroups:sort=groupId){:target="_blank"},
[N. California](https://console.aws.amazon.com/ec2/v2/home?region=us-west-1#SecurityGroups:sort=groupId){:target="_blank"},
[Oregon](https://console.aws.amazon.com/ec2/v2/home?region=us-west-2#SecurityGroups:sort=groupId){:target="_blank"}<br/>
Нужно открыть порты для доступа извне. Поскольку сервер будет существовать ограниченное время и не будет использоваться в публичных целях, то можно не заморачиваться с выбором портов и открыть их все, хоть это и противоречит правилам безопасности.<br/>
![Security Groups AllPorts](/images/agent-security-groups-allports.png)

Нужно создать Роль с правами доступа в ведро S3.
1. [Перейти в раздел управления Ролями](https://console.aws.amazon.com/iam/home?region=us-east-1#/roles){:target="_blank"} и нажать на синюю кнопку "Create role".
2. Выбрать сервис EC2 и нажать на синюю кнопку "Next".<br/>
![ubuntu](/images/agent-create-role-1.png)
3. Скрипт для запуска Агентов только скачивает файлы из ведра S3, поэтому достаточно выбрать "AmazonS3ReadOnlyAccess" и нажать на синюю кнопку "Next".<br/>
![ubuntu](/images/agent-create-role-2.png)
4. Теперь нужно задать имя Роли и нажать на синюю кнопку "Create role".<br/>
![ubuntu](/images/agent-create-role-3.png)

Можно создать ключи доступа для использования программ по закачке файлов в ведро S3. Эти ключи также позволяют получать спот-цены со всех регионов в [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/AmazonUtils){:target="_blank"}. Забытые ключи доступа в исходных кодах могут [доставить неприятности](https://habr.com/post/357764/){:target="_blank"}.

## Закачка файлов в S3
1. [Сначала нужно создать ведро S3 с параметрами по умолчанию.](https://s3.console.aws.amazon.com/s3/home){:target="_blank"}
2. Создать папку "MetaQuotes".<br/>
![AWS S3 root](/images/agent-s3-root.png)
3. Закачать файл "c:\Program Files\MetaTrader 5\metatester64.exe" в папку "MetaQuotes".<br/>
![AWS S3 MetaQuotes](/images/agent-s3-metaquotes.png)
4. Нужные файлы из папки "c:\Users\USER\AppData\Roaming\MetaQuotes\Terminal\Common\Files\" закачать в "MetaQuotes/Terminal/Common/Files/".

Закачку нужно делать для каждого региона, в котором планируется запуск Агентов.

## Заказ сервера для Агентов
В разделе [Spot Requests](https://console.aws.amazon.com/ec2sp/v1/spot/home){:target="_blank"} нажать на синюю кнопку "Request Spot Instances".

Созданный мною скрипт для запуска Агентов рассчитан на Ubuntu.<br/>
![Ubuntu](/images/agent-ubuntu.png)

Я обычно выбираю cc2.8xlarge со встроенным SSD на 840GB. На него часто большая скидка, потому что этот инстанс прошлого поколения, но для Агентов тестирования он отлично подходит.<br/>
![Instance Type](/images/agent-instance-type.png)

Если инстанс имеет встроенное дисковое пространство, то количество гигабайтов для EBS задать можно минимум (оплачивается отдельно).<br/>
![EBS](/images/agent-ebs.png)<br/>
Все Агенты запускаются в "/mnt". Первый раздел встроенного диска автоматически монтируется в эту папку. Если размера первого раздела не хватает, то нужно брать инстанс только с EBS или редактировать скрипт. Добавлять второй раздел не имеет смысла, потому что он будет последним.<br/>
![lsblk](/images/agent-lsblk.png)

Задать правило открытия портов в "Security groups".<br/>
![Security groups](/images/agent-security-groups.png)

Если использовать заранее созданную роль в "IAM instance profile", то в скрипте не нужно указывать ключ к Амазону.<br/>
![IAM instance profile](/images/agent-iam.png)

Открываем [aws_ubuntu_user_data.sh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/src/main/resources/aws_ubuntu_user_data.sh){:target="_blank"} и вставляем содержимое в "User data".<br/>
![User data](/images/agent-userdata.png)
* Hours=1 - ограничивает работу инстанса по количеству часов, потому что оплата почасовая.
* agentStartPort=5000 - начальный порт для 1-ого Агента.
* agentPassword=amazon99 - пароль для доступа к Агентам.
* bucket= - название ведра, где находятся необходимые для теста файлы.
* Если роль не задана, то придётся указать ключи доступа, чтобы скачать файлы из ведра S3.

После нажатия на синюю кнопку "Launch" произойдёт запрос на создание инстанса.

Инстанс может быть выдан Амазоном с задержкой, поэтому нужно обновлять страницу, пока он не появится в списке "Instances".<br/>
![Instance](/images/agent-instance.png)

После этого можно переходить на страницу инстанса и нажать на серую кнопку "Connect" для получения IP.<br/>
![IP](/images/agent-ip.png)

## Добавление Агентов в MetaTrader 5
Теперь можно добавить Агенты в список для оптимизации в MetaTrader 5 (MT5).<br/>
![MT5 Add](/images/agent-add-1.png)<br/>
![MT5 Add 2](/images/agent-add-2.png)

Скрипту нужно время (примерно 5 минут) для запуска Агентов в Ubuntu.<br/>
![MT5 Agents](/images/agent-agents.png)

[По всем вопросам обращаться в эту тему.](https://www.mql5.com/ru/forum/245373){:target="_blank"}

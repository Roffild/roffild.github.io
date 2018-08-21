---
title: MetaTrader 5 Agents & AWS EC2
description: Using MetaTrader 5 (MT5) Agents on Amazon servers VPS/VDS. This is an excellent option for checking the trading strategy for the currency and stock markets Forex, CFD and Futures.
---

Using MetaTrader 5 (MT5) Agents on Amazon servers VPS/VDS.
This is an excellent option for checking the trading strategy for the currency and stock markets Forex, CFD and Futures.

MetaTrader 4 (MT4) does not have Test Agents.

The difference from the use of the Agents cloud:
* Fixed price per hour and a fixed number of processor cores.
* Ability to use local files from FILE_COMMON.
* Ability to use OpenCL on the CPU (and GPU, if the instance allows).
* Upload large files needed for testing, you can through the bucket S3.
* Possibility of using dynamic libraries (DLL) is possible.

Agents are run with the flag "/local" as with local use.

The cost of using Amazon servers can be much more economical than using the Cloud of Agents.
Calculation of the cost of the Cloud occurs by a mysterious formula, so it is very difficult to estimate the cost of full optimization.

## What is the profit?
Prices for spot-instances are available [here](https://aws.amazon.com/ec2/spot/pricing/){:target="_blank"}. 
But after registration, the table is available that can be obtained by [creating a spot-instance](https://console.aws.amazon.com/ec2sp/v1/spot/home){:target="_blank"} and clicking on the gray "Select" button.<br/>
![Spot Prices](/images/agent-spot.png)

There is a special instance:<br/>
cc2.8xlarge CPUs 32 Memory	60.5GiB SSD	4 x 840 GB<br/>
The price ranges from $0.20 to $0.30 per hour, which corresponds to instances with 16 CPUs. This instance has an out-of-date status and can periodically disappear from the list of available instances. It makes sense to view all 4 US regions for its availability before ordering the instance.

The cc2.8xlarge is ideal for Agents.

## Initialization
It makes sense in four US regions to create a rule for [Security Groups](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#SecurityGroups:sort=groupId){:target="_blank"}.<br/>
![Security Groups](/images/agent-security-groups-main.png)<br/>
[N. Virginia](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#SecurityGroups:sort=groupId){:target="_blank"},
[Ohio](https://console.aws.amazon.com/ec2/v2/home?region=us-east-2#SecurityGroups:sort=groupId){:target="_blank"},
[N. California](https://console.aws.amazon.com/ec2/v2/home?region=us-west-1#SecurityGroups:sort=groupId){:target="_blank"},
[Oregon](https://console.aws.amazon.com/ec2/v2/home?region=us-west-2#SecurityGroups:sort=groupId){:target="_blank"}<br/>
You need to open ports for access from outside. Since the server will exist for a limited time and will not be used for public purposes. You can not bother with the choice of ports and open them all, although this is contrary to security rules.<br/>
![Security Groups AllPorts](/images/agent-security-groups-allports.png)

You need to create a Role with access rights to the bucket S3.
1. [Go to the Role Management section](https://console.aws.amazon.com/iam/home?region=us-east-1#/roles){:target="_blank"} and click on the blue "Create role" button.
2. Select the EC2 service and click on the blue "Next" button.<br/>
![ubuntu](/images/agent-create-role-1.png)
3. The script for launching Agents only downloads files from the S3 bucket, so just select "AmazonS3ReadOnlyAccess" and click on the blue "Next" button.<br/>
![ubuntu](/images/agent-create-role-2.png)
4. Now you need to set the Role name and click on the blue "Create role" button.<br/>
![ubuntu](/images/agent-create-role-3.png)

You can create access keys for using programs to upload files to the S3 bucket. These keys also allow you to receive spot prices from all regions in  [AmazonUtils](https://github.com/Roffild/RoffildLibrary/blob/master/Experts/Roffild/AmazonUtils){:target="_blank"}. Forgotten access keys in a source code [can cause trouble](https://habr.com/post/357764/){:target="_blank"} (RU).

## Uploading files to S3
1. [First you need to create an S3 bucket with the default settings.](https://s3.console.aws.amazon.com/s3/home){:target="_blank"}
2. Create a folder "MetaQuotes".<br/>
![AWS S3 root](/images/agent-s3-root.png)
3. Download the file "c:\Program Files\MetaTrader 5\metatester64.exe" to the folder "MetaQuotes".<br/>
![AWS S3 MetaQuotes](/images/agent-s3-metaquotes.png)
4. Download the necessary files from the folder "c:\Users\USER\AppData\Roaming\MetaQuotes\Terminal\Common\Files\" to "MetaQuotes/Terminal/Common/Files/".

The download should be done for each region in which the Agents are scheduled to be launched.

## Request server for Agents
In the [Spot Requests](https://console.aws.amazon.com/ec2sp/v1/spot/home){:target="_blank"} click on the blue "Request Spot Instances" button.
The script I created for running Agents is designed for Ubuntu.<br/>
![Ubuntu](/images/agent-ubuntu.png)

I usually choose cc2.8xlarge with a built-in SSD on 840GB. It is often a great discount, because this instance of the previous generation, but for Agents it is great.<br/>
![Instance Type](/images/agent-instance-type.png)

If the instance has built-in disk space, then the number of gigabytes for EBS can be set at a minimum (paid separately).<br/>
![EBS](/images/agent-ebs.png)<br/>
All Agents are run in "/mnt". The first partition of the built-in disk is automatically mounted in this folder. If the size of the first partition is not enough, then you need to take an instance only with EBS or edit the script. Add a second partition does not make sense, because it will be the last.<br/>
![lsblk](/images/agent-lsblk.png)

Set the rule for opening ports in "Security groups".<br/>
![Security groups](/images/agent-security-groups.png)

If you use a pre-created role in the "IAM instance profile", then the script does not need to specify the key to Amazon.<br/>
![IAM instance profile](/images/agent-iam.png)

Open the [aws_ubuntu_user_data.sh](https://github.com/Roffild/RoffildLibrary/blob/master/Include/Roffild/RoffildJava/AmazonUtils/src/main/resources/aws_ubuntu_user_data.sh){:target="_blank"} and paste the contents into "User data".<br/>
![User data](/images/agent-userdata.png)
* Hours=1 - limits the work of the instance by the number of hours, because the payment is hourly.
* agentStartPort=5000 - the start port for the 1st Agent.
* agentPassword=amazon99 - password for access to Agents.
* bucket= - name of the bucket where the files needed for the test are located.
* If the role is not specified, you will have to specify access keys to download files from the S3 bucket.

After clicking on the blue button "Launch" a request to create an instance.

Instance can be issued by Amazon with a delay, so you need to update the page until it appears in the "Instances" list.<br/>
![Instance](/images/agent-instance.png)

After that, you can go to the instance page and click on the gray "Connect" button to get the IP.<br/>
![IP](/images/agent-ip.png)

## Adding Agents to MetaTrader 5
Now you can add Agents to the list for optimization in MetaTrader 5 (MT5).<br/>
![MT5 Add](/images/agent-add-1.png)<br/>
![MT5 Add 2](/images/agent-add-2.png)

The script needs time (approximately 5 minutes) to run Agents in Ubuntu.<br/>
![MT5 Agents](/images/agent-agents.png)

[On all questions to address in this topic.](https://www.mql5.com/en/forum/247134){:target="_blank"}

# Amazon Web Services

[Tech-Interviews](../../README.md) -> [KnowledgeBase](../KnowledgeBase.md) -> [AWS](../AWS/AWS.md)

Beginner Level AWS interview questions :

1. What are the key services provided by AWS? 
Ans:- The key AWS services include:
EC2 (Elastic Compute Cloud): Virtual servers in the cloud.
S3 (Simple Storage Service): Scalable object storage.
RDS (Relational Database Service): Managed relational databases.
Lambda: Serverless compute service.
VPC (Virtual Private Cloud): Network isolation.
DynamoDB: Managed NoSQL database.
CloudFront: Content delivery network (CDN).
IAM (Identity and Access Management): User and access management.

2. What is EC2 in AWS? 
Ans:- EC2 (Elastic Compute Cloud) is a service that provides resizable compute capacity in the cloud. It allows users to run virtual machines on AWS infrastructure and is used for deploying applications.

3. What is an S3 bucket? 
Ans:- S3 (Simple Storage Service) bucket is a container that holds data objects. S3 is an object storage service that stores data as files, accessible from anywhere. You can store and retrieve any amount of data in an S3 bucket.

4. Explain the difference between S3 and EBS.
Ans:- S3: Object storage suitable for storing large amounts of data (files, backups). It's designed for scalability, durability, and availability.
EBS (Elastic Block Store): Block storage used with EC2 instances for tasks like databases or file systems. It's low-latency storage for applications that require high-performance I/O.

5. What is IAM in AWS? 
Ans:- IAM (Identity and Access Management) is a service that helps you control access to AWS resources. You can create and manage users, groups, and roles, and assign permissions to grant or deny access to specific AWS resources.

6. How does AWS VPC work? 
Ans:- A VPC (Virtual Private Cloud) allows you to define your own logically isolated network within AWS. You can configure subnets, route tables, and network gateways, control IP address ranges, and apply security controls such as Security Groups and Network ACLs.

7. What are Security Groups and how do they work? 
Ans:- Security Groups are virtual firewalls for your AWS resources. They control inbound and outbound traffic to the instances based on rules you configure (allow or deny traffic based on IP addresses, ports, and protocols).

8. What is an AWS region? 
Ans:- An AWS region is a physical location where AWS has multiple Availability Zones (data centers). Regions are geographically distributed to provide redundancy and low-latency access for global customers.

9. What are Availability Zones in AWS? 
Ans:- Availability Zones (AZs) are distinct data centers within an AWS region. Each AZ is isolated from failures in other zones and interconnected with low-latency networks, providing high availability and fault tolerance for applications.

10. What is Auto Scaling? 
Ans:- Auto Scaling automatically adjusts the number of EC2 instances in your application based on demand. It ensures that the correct number of instances are running to handle the load, optimizing performance and cost.

11. What is Elastic Load Balancing? 
Ans:- Elastic Load Balancing (ELB) distributes incoming traffic across multiple targets (EC2 instances, containers, etc.), ensuring high availability and fault tolerance for applications by routing traffic to healthy targets.

12. What is Route 53? 
Ans:- Route 53 is AWS’s scalable Domain Name System (DNS) service that translates domain names (e.g., www.example.com) into IP addresses. It also offers traffic routing policies and health checking for resources.

13. Explain the difference between a public and private subnet.
Ans:- Public Subnet: A subnet with direct access to the internet through an Internet Gateway.
Private Subnet: A subnet without direct internet access, typically used for internal resources, accessible through NAT Gateways for outbound internet traffic.

14. What is CloudFormation? 
Ans:- AWS CloudFormation is an infrastructure-as-code (IAC) tool that allows you to define and provision AWS resources using JSON or YAML templates. It automates resource creation and configuration in a repeatable way.

15. What is AWS Lambda? 
Ans:- AWS Lambda is a serverless compute service that runs code in response to events without provisioning or managing servers. You only pay for the compute time you use.

16. What is Amazon RDS? 
Ans:- Amazon Relational Database Service (RDS) is a managed service for relational databases like MySQL, PostgreSQL, MariaDB, SQL Server, and Oracle. It automates tasks such as backups, patching, and scaling.

17. How do you monitor AWS resources? 
Ans:- AWS resources are monitored using services like CloudWatch (logs, metrics, alarms), AWS Config (resource configuration tracking), and CloudTrail (API activity monitoring).

18. What is Amazon DynamoDB? 
Ans:- DynamoDB is a fully managed NoSQL database service designed for high-performance applications requiring low-latency access to large amounts of data.

19. What is AWS Elastic Beanstalk? 
Ans:- AWS Elastic Beanstalk is a platform-as-a-service (PaaS) that automates the deployment and scaling of web applications and services. It supports several programming languages and frameworks.

20. What is Amazon CloudFront? 
Ans:- Amazon CloudFront is a content delivery network (CDN) that delivers data, videos, and applications globally with low latency by caching content at edge locations.

21. Explain Amazon SNS.
Ans:- Amazon Simple Notification Service (SNS) is a fully managed messaging service for sending notifications to a variety of endpoints such as email, SMS, and HTTP/S, or for enabling pub/sub messaging between distributed systems.

22. What is the difference between RDS and DynamoDB? 
Ans:- RDS: Managed relational database service with structured data (SQL-based).
DynamoDB: Managed NoSQL database for key-value and document data with high scalability and performance

31. How do you secure data at rest and in transit in AWS?
Ans:- At rest: Use AWS Key Management Service (KMS) for encryption of stored data, services like S3, EBS, and RDS provide server-side encryption options.
In transit: Use SSL/TLS protocols to secure data transfer. Services like S3, CloudFront, and API Gateway support encryption in transit.

32. Explain the difference between AWS S3 Standard and S3 Glacier.
Ans:- S3 Standard: Designed for frequently accessed data, offering low-latency and high availability. It is more expensive but optimized for real-time access.
S3 Glacier: Designed for long-term archiving and infrequently accessed data. It is cheaper, but retrieval times can range from minutes to hours.

33. How does AWS S3 versioning work?
Ans:- S3 versioning allows you to store multiple versions of an object within a bucket. When enabled, S3 retains older versions of objects, helping to recover from accidental overwrites, deletions, or corruptions.

34. What is AWS ElastiCache?
Ans:- AWS ElastiCache is a fully managed in-memory caching service that supports Redis and Memcached. It helps improve the performance of web applications by retrieving data from fast, managed in-memory caches instead of relying entirely on slower disk-based databases.

35. Explain the concept of a bastion host.
Ans:- A bastion host is a server used to securely connect to instances in a private subnet of your VPC. It acts as a gateway, allowing you to securely SSH or RDP into your instances, while reducing the attack surface.

36. How do you implement high availability in AWS?
Ans:- Use services like EC2 Auto Scaling, Elastic Load Balancers (ELB), and deploying across multiple Availability Zones (AZs). For databases, you can use RDS Multi-AZ deployments or Aurora Global Database.

37. What is AWS Direct Connect?
Ans:- AWS Direct Connect is a dedicated network connection from your on-premise environment to AWS, allowing for secure, private, and high-bandwidth connectivity with lower latency compared to internet-based connections.

38. What are AWS Managed Services?
Ans:- AWS Managed Services (AMS) provides operational management for AWS infrastructure, handling tasks such as patch management, monitoring, backups, and security. It helps automate common activities and enforce security best practices.

39. What is AWS Config?
Ans:- AWS Config is a service that tracks and records configurations of your AWS resources over time. It helps you assess compliance, identify configuration changes, and troubleshoot resource configuration issues.

40. How do you set up cross-region replication in S3?
Ans:- Cross-region replication (CRR) in S3 allows automatic replication of objects from one S3 bucket to another in a different AWS region. You can enable it in the bucket settings, selecting a destination bucket and configuring any IAM roles and permissions.

41. Explain AWS KMS.
Ans:- AWS Key Management Service (KMS) is a managed service for creating and controlling encryption keys. It integrates with other AWS services to encrypt data at rest and in transit and supports both customer-managed and AWS-managed keys.

42. What is Amazon Redshift?
Ans:- Amazon Redshift is a fully managed data warehousing service that allows you to run complex queries against petabytes of structured and semi-structured data. It is optimized for high-performance data analysis.

43. How does AWS handle data encryption?
Ans:- AWS handles data encryption through services like KMS for key management, server-side encryption for services like S3, EBS, and RDS, and client-side encryption libraries. SSL/TLS is used to secure data in transit.

44. What is Amazon EFS?
Ans:- Amazon Elastic File System (EFS) is a scalable, fully managed network file system that can be mounted to multiple EC2 instances. It allows for the sharing of file data across instances and scales automatically as files are added.

45. Explain AWS Elastic Transcoder.
Ans:- AWS Elastic Transcoder is a media transcoding service designed to convert media files stored in S3 into formats that can be played on different devices. It supports various audio and video formats and scales automatically based on workload.

46. What is AWS CodePipeline?
Ans:- AWS CodePipeline is a continuous integration and continuous delivery (CI/CD) service that automates the steps required to release software, such as building, testing, and deploying code.

47. How do you implement disaster recovery in AWS?
Ans:- Use strategies such as backups with Amazon S3, Multi-AZ or multi-region deployments for databases, cross-region replication for S3, and automated recovery scripts. You can also leverage services like AWS Elastic Disaster Recovery.

48. What is AWS OpsWorks?
Ans:- AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. It automates server configuration, deployment, and scaling based on predefined templates.

49. What is AWS Step Functions?
Ans:- AWS Step Functions is a serverless orchestration service that helps coordinate distributed applications using workflows. It provides state machines to define the steps of your application, enabling reliable workflows across multiple AWS services.

50. Explain the difference between Spot Instances and Reserved Instances.
Ans:- Spot Instances: Offer unused EC2 capacity at lower prices but can be terminated by AWS with little notice if capacity is needed. 
Reserved Instances: Provide a significant discount over on-demand pricing in exchange for a one- or three-year commitment. They are more predictable and not subject to termination.

51. How do you secure an AWS API Gateway?
Ans:- Secure API Gateway using AWS IAM roles, resource policies, Lambda authorizers, Cognito user pools, and by enabling throttling and WAF to mitigate attacks.

52. What is a service mesh in AWS?
Ans:- A service mesh is a logical grouping of services that can communicate with each other. It provides a consistent view of the application's services, making it easier to manage and maintain.

53. Explain AWS CloudWatch.
Ans:- CloudWatch is a service that provides monitoring, management, and alarms for your Amazon Web Services resources. It can be used to monitor CPU, memory, disk, and network usage.

How do you manage environment variables and secrets securely in a CI/CD pipeline for different environments (development, staging, production)?
- What strategies do you use for horizontal scaling of containerized applications in Kubernetes?
- Can you explain how to roll back a deployment in Kubernetes and what the impact would be?
- How do you monitor and maintain the health of a Jenkins pipeline?
- What are the steps to set up an AWS CodePipeline for deploying a Lambda function?
- Have you used Infrastructure as Code (IaC) with Terraform or CloudFormation? What challenges did you face with version control?
- What’s your approach to ensuring high availability (HA) for stateful applications in a Kubernetes cluster?
- Can you describe how you handle blue/green or canary deployments in your CI/CD setup?
- What’s the process for creating an AMI using Packer and deploying it with Terraform?
- How do you handle permissions and security policies for different AWS services using IAM roles?
- If an EC2 instance in a private subnet needs to pull Docker images from Docker Hub, how do you achieve this without using public IPs?
- How do you handle state files in Terraform, especially in multi-team setups?
- What’s your approach to auto-scaling an application on AWS based on custom CloudWatch metrics?
- How do you set up network security between two VPCs in different AWS accounts using VPC Peering or Transit Gateway?
- What are the key metrics you monitor when optimizing AWS Lambda performance?
- Can you describe how to migrate an on-premise Jenkins setup to a cloud-based environment?
- how would you automate the process of provisioning EC2 instances and attaching EBS volumes using Terraform?
- What’s the role of a service mesh like Istio in Kubernetes, and how does it help manage microservices?
- How do you handle logging and monitoring across microservices in a distributed system?
- In AWS, how do you secure traffic between public-facing load balancers and backend instances?
- Can you explain the role of AWS Systems Manager (SSM) in managing EC2 instances without direct SSH access?
- What are your best practices for Docker image security, including minimizing image size and vulnerabilities?
- How do you handle zero-downtime deployments for a critical application running in a Kubernetes cluster?
- How do you define and manage multiple environments (like Dev, QA, and Prod) in Terraform?
- Write a BASH script to automate daily backups of a MySQL database running on an EC2 instance.



1. Day to day 𝗮𝗰𝘁𝗶𝘃𝗶𝘁𝗶𝗲𝘀 in DevOps Cloud.
2. How effective did you used 𝗞𝘂𝗯𝗲𝗿𝗻𝗲𝘁𝗲𝘀 and 𝗗𝗼𝗰𝗸𝗲𝗿 in day to day activity.
3. Let's assume that there is one existing 𝗰𝗹𝘂𝘀𝘁𝗲𝗿 which is getting 𝗿𝗲𝘀𝘁𝗮𝗿𝘁 again and again. And it is 𝗼𝘂𝘁 𝗼𝗳 𝗺𝗲𝗺𝗼𝗿𝘆 as well. So you have received an alert. So how will you 𝘁𝗿𝗼𝘂𝗯𝗹𝗲𝘀𝗵𝗼𝗼𝘁 this issue and what is the checklist you initially check.
4. Can you explain the 𝘀𝗲𝗰𝘂𝗿𝗶𝘁𝘆 𝗳𝗲𝗮𝘁𝘂𝗿𝗲𝘀 which is available in 𝗞𝘂𝗯𝗲𝗿𝗻𝗲𝘁𝗲𝘀.
5. Can you explain the 𝗰𝗼𝗺𝗽𝗼𝗻𝗲𝗻𝘁𝘀 of 𝗞𝘂𝗯𝗲𝗿𝗻𝗲𝘁𝗲𝘀.
6. Are you aware of the 𝗲𝘅𝗶𝘁 𝗰𝗼𝗱𝗲.
7. There is an existing 𝗽𝗼𝗱 which is 𝗻𝗼𝘁 getting 𝘀𝗰𝗵𝗲𝗱𝘂𝗹𝗲𝗱. How will you fix this issue.
8. You have the exposure to 𝗶𝗻𝗰𝗶𝗱𝗲𝗻𝘁 𝗺𝗮𝗻𝗮𝗴𝗲𝗺𝗲𝗻𝘁 right? How will you 𝗰𝗮𝘁𝗲𝗴𝗼𝗿𝗶𝘇𝗲 the 𝗽𝗿𝗶𝗼𝗿𝗶𝘁𝘆
9. What is the 𝗿𝗲𝘀𝗽𝗼𝗻𝘀𝗲 𝘁𝗶𝗺𝗲 of 𝗣𝟭, 𝗣𝟮, 𝗣𝟯 and 𝗣𝟰 ticket.
10. What is the 𝗿𝗲𝘀𝗼𝗹𝘂𝘁𝗶𝗼𝗻 𝘁𝗶𝗺𝗲 for  𝗣𝟮.
11. How will you 𝗰𝗮𝘁𝗲𝗴𝗼𝗿𝗶𝘇𝗲 the issue as  𝗣𝟭, 𝗣𝟮, 𝗣𝟯 or 𝗣𝟰.
12. Difference between 𝗜𝗥 and 𝗦𝗥
13. What about the 𝗺𝗼𝗻𝗶𝘁𝗼𝗿𝗶𝗻𝗴 part. Do you have any exposure to that?
14. What are the things you will do with respect to the 𝗺𝗼𝗻𝗶𝘁𝗼𝗿𝗶𝗻𝗴?
15. Define 𝗹𝗼𝗴𝘀 and 𝗺𝗲𝘁𝗿𝗶𝗰𝘀
16. So let's consider, in your 𝗱𝗮𝘀𝗵𝗯𝗼𝗮𝗿𝗱, you observed from one application or one 𝗰𝗹𝘂𝘀𝘁𝗲𝗿 the 𝘂𝘁𝗶𝗹𝗶𝘇𝗮𝘁𝗶𝗼𝗻 was 𝗵𝗶𝗴𝗵. Which were you can identify using the 𝗱𝗮𝘀𝗵𝗯𝗼𝗮𝗿𝗱 with the 𝗺𝗲𝘁𝗿𝗶𝗰𝘀 which is already created. So what will be the first step and how will you 𝗳𝗶𝘅 the 𝗶𝘀𝘀𝘂𝗲.
17. Do you have any experience in 𝗰𝗿𝗲𝗮𝘁𝗶𝗻𝗴 the 𝗺𝗼𝗻𝗶𝘁𝗼𝗿𝘀?
18. Can you explain more about 𝗖𝗹𝗼𝘂𝗱𝘄𝗮𝘁𝗰𝗵 and how have you configured it.
19. Do you have any exposure to 𝗜𝗔𝗖 tools like 𝗧𝗲𝗿𝗿𝗮𝗳𝗼𝗿𝗺?
20. Write some sample 𝗗𝗼𝗰𝗸𝗲𝗿𝗳𝗶𝗹𝗲 to create an 𝗡𝗴𝗶𝗻𝘅 𝗶𝗺𝗮𝗴𝗲
21. What do you know about 𝘁𝗲𝘀𝘁𝗶𝗻𝗴
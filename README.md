# Batch anomaly detection service

I am an ML engineer working for a tech-savvy taxi ride company with a fleet of thousands of cars. The organization wants to start making ride times more consistent and to understand longer journeys in order to improve customer experience, increase retention and business returns.

I was employed to creare an anomaly detection service to find rides that have unusual ride time.
These were the requirements given by the CEO:

* Rides should be clustered based on ride distance and time and anomalies/
outliers identified.
* Speed  was not to be used, as analysts would like to understand
long-distance rides.
* The analysis should be carried out on a daily schedule.
* The data for inference should be consumed from the company's data lake.
* The results should be made available for consumption by other company systems.

After much analysis, this was proposed to the client;

* Algorithm type = outlier detection specifically `Density-Based Spatial CLustering of Applications with Noise (DBSCAN)`
* Features used were ride time and distance
* System output destination is S3 bucket on AWS. The predictions data is exported as `JavaScript Object Notation (JSON)`
* Batch Frequency is Daily.

## Designing the Solution

Here is a pictorial view of the solution

![diagram one](./images/pipeline_image.png
"Pipeline Image")

## Tools used
* ![Outliers-nerdward](https://pypi.org/project/outliers-nerdward/) (My python package specifically for the project)
* AWS CLI and boto3
* Scikit-learn
* ![AWS **Managed Workflows for Apache Airflow**](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html)
* ![AWS S3](https://s3.console.aws.amazon.com/)

# Requirements
* Github Account
* An AWS account with active access keys for IAM user. For help creating one, visit ![here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

## Setup
### Airflow on AWS

1. Select Create environment on the MWAA landing page
![step1](/images/step1.png)
2. You will then be provided with a screen asking for the details of your new Airflow environment.
![step2](/images/step2.png)
3. For MWAA to run, it needs to be able to access code defining the DAG and any associated requirements or plugins files. The system then asks for an AWS S3 bucket where these pieces of code and configuration reside. In this example, we create a bucket called mleip-airflow-example that will contain these pieces:
![step3](/images/step3.png)
4. We then have to define the configuration of the network that the managed instance of Airflow will use.  
This can get a bit confusing if you are new to networking, so it might be good to read around the topics of subnets, IP addresses, and VPCs.
Creating a new MWAA VPC is the easiest approach for getting started in terms of networking here, but your organization will have networking specialists who can help you use the appropriate settings for your situation.   
We will go with this simplest route and click Create MWAA VPC, which opens a new window where
we can quickly spin up a new VPC and network setup based on a standard stack definition provided by AWS.
![step4](/images/step4.png)
5. We are then taken to a page where we are asked for more details on networking:
![step5](/images/step5.png)
6. Next, we have to define the Environment class that we want to spin up. Currently, there are three options. Here, we use the smallest, but you can choose the environment that best suits your needs (always ask the billpayer's permission!)
![step6](/images/step6.png)
7. Now, if desired, we confirm some optional configuration parameters (or leave these blank, as done here) and confirm that we are happy for AWS to create and use a new execution role
![step7](/images/step7.png)
8. The next page will supply you with a final summary before allowing you to create your MWAA environment. Once you do this, you will be able to see in the MWAA service your newly created environment

### CI/CD
1. Update Github secrets with your AWS credentials.
![actions](/images/actions.png)
2. Create a new branch name it whatever you want.
3. Update the yml file in the .github/workflows called aws-s3-deploy.yml with name of the branch and the name of your S3 bucket.
![yaml](/images/yaml.png)
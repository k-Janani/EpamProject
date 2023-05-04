# EpamProject



**Introduction:**


This SeedToFeed website serves for the farmers and makes their living comfortable. This website seamlessly provide all the features which helps the farmers to gain more profit, solve their problem and increase productivity.


**UseCases:**


	Our agriculture app simplifies the farming experience with an all-in-one platform for login, accessing governmental schemes, and posting complaints.

	Say goodbye to long commutes and queues with our online payment system for agricultural loans.

	We offer easy access to governmental schemes and resources for farmers to enhance their productivity, all in one convenient location.

	The app provides a range of tools and resources to assist farmers in managing their crops, livestock, and other farm-related tasks.

	Farmers can voice their complaints and have them addressed efficiently by the relevant authorities with our complaint feature.

	With our app, farmers can easily keep track of their payments and loan statuses, making it easier to manage their finances.

	We offer a secure login system to ensure your information is kept private and confidential.

	Our app is user-friendly and easy to navigate, making it simple for farmers of all ages to use.


**Services Used:**


1.GitHub

2.AWS EKS

3.Docker

4.Jenkins

5. S3

**
Devops Tools Working Steps:**


**GitHub**


->The commands used to push the project files to github using git bash is

1. git init
2.git add .
3. git commit -m "Your commit message"
4. git remote add github (link of your GitHub project).git
5. git remote -v
6. git push -f github master

**Jenkins**


Code

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }
        stage('Print Message') {
            steps {
                echo 'Your Welcome message!'
            }
        }
    }
}

->Open Jenkins and create a new pipeline job.
->In the pipeline configuration, select "Pipeline script from SCM" as the Definition and choose Git as the SCM.
->Enter the repository URL and credentials for the Git repository containing your source code.
->Set the Jenkinsfile path to the location of your Jenkinsfile in the Git repository.
->Save the pipeline configuration and run the pipeline.

**EKS & Docker**

->Create an EKS cluster
->Build and push Docker images
->Create a Kubernetes deployment
->Configure your application
->Access S3 from your application
->Monitor and manage your application




This README provides a guide for deploying a Python GPT model that utilizes Terraform to manage AWS resources.
The model is designed to facilitate the deployment and management of AWS resources using natural language inputs.

Work in progress - for the moment trained on creating and deploying AWS VPC resource.
# prerequisites

Python:
- Python 3.x installed on your machine.
- Required Python libraries listed in requirements.txt installed using pip install -r requirements.txt.
- Terraform:
    You can download from official site : https://developer.hashicorp.com/terraform/downloads
- AWS CLI:
    You can download and install from here: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

# Installation 

clone the repository :
 git clone ...
 cd ..
pip install -r requirements.txt

# Terraform Configuration
```
aws configure
Your Access Key ID
Secret Access Key
Region name: eu-central-1 #important
Default output format: json #important
```
# Model Initialization
$ python interact/inter.py generate_vpc
# Wait until you get the "done" console message. 

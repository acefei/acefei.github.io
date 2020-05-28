Title: Deploy ARM template with Ansible
Date: 2020-05-28 06:05
Category: DevOps
Tags: Azure,ARM template,Ansible
Authors: Ace Fei


[TOC]

# Deploy ARM template with Ansible

## Requirements
Create a docker image with the Dockerfile:
```
FROM mcr.microsoft.com/azure-cli
RUN pip install --upgrade pip && pip install ansible[azure]
```

## Create Credentials for Ansible
Run the following within docker container
```
# login azure
az login

# list the Subscriptions associated with the account
az account list

# should you have more than one Subscription, you can specify the Subscription with the id field being the subscriptionId field referenced above.
az account set --subscription=<subscriptionId>

# create the Service Principal which will have permissions to manage resources
az ad sp create-for-rbac -n CloudOps
```
After stepping through the above commands you will get the result:
```
{
  "appId": "00000000-0000-0000-0000-000000000000",
  "displayName": "CloudOps",
  "name": "http://CloudOps",
  "password": ********************,
  "tenant": "00000000-0000-0000-0000-000000000000"
}
```

To pass service principal credentials via the environment, define the following variables:
```
export AZURE_SUBSCRIPTION_ID=<your-subscription_id>
export AZURE_CLIENT_ID=<security-principal-appid>
export AZURE_SECRET=<security-principal-password>
export AZURE_TENANT=<security-principal-tenant>
```

If you forget the password, reset the service principal credentials.
```
az ad sp credential reset --name <appId>
```

## Reference
- [Microsoft Azure Guide](https://docs.ansible.com/ansible/latest/scenario_guides/guide_azure.html)
- [Quickstart: Install Ansible on Linux virtual machines in Azure](https://docs.microsoft.com/en-us/azure/developer/ansible/install-on-linux-vm)

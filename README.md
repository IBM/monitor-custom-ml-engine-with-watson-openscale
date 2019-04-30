# Monitor Custom Machine Learning engine with Watson OpenScale

In this Code Pattern, we will log the payload for a model deployed on custom model serving engine using Watson OpenScale python sdk. We'll use [Keras to build a deep learning REST API](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html) and then monitor with [Watson OpenScale](https://www.ibm.com/cloud/watson-openscale/)

When the reader has completed this Code Pattern, they will understand how to:

* Build a custom model serving engine using [Keras](https://keras.io/)
* Access the custom model using a REST API
* Log the payload for the model using [Watson OpenScale](https://cloud.ibm.com/docs/services/ai-openscale/connect-ml.html#connect-ml)

![](doc/source/images/architecture.png)

## Flow

1. User deploys application server on the IBM Cloud using Kubernetes and Docker.
2. User creates a Jupyter notebook on Watson Studio and configures Watson OpenScale and Databases for PostgreSQL.
3. Watson OpenScale is used to monitor a Machine Learning model for payload logging and quality.
4. The application server is used for scoring the deployed model.

## Prerequisites

* An [IBM Cloud Account](https://cloud.ibm.com).
* An account on [IBM Watson Studio](https://dataplatform.cloud.ibm.com/) or a way to run a [Jupyter Notebook](https://jupyter.org/) locally
* For Kubernetes deployment, setup [IBM Cloud CLI](https://cloud.ibm.com/docs/cli/index.html#overview) and any other required [Kubernetes prerequisites](https://cloud.ibm.com/docs/containers/cs_tutorials.html#prerequisites)

# Steps

1. [Clone the repo](#1-clone-the-repo)
2. [Create Watson services with IBM Cloud](#2-create-watson-services-with-ibm-cloud)
3. [Create a notebook in IBM Watson Studio](#3-create-a-notebook-in-ibm-watson-studio) for use with a publicly addressed server OR
   - Run the notebook locally for local testing only
4. Perform either 4a to Deploy to IBM Cloud **or** 4b for local testing only:
   - 4a. [Deploy to IBM Cloud](#4a-deploy-to-ibm-cloud)
   - 4b. [Run the application server locally](#4b-run-the-application-server-locally)
5. [Run the notebook in IBM Watson Studio](#5-run-the-notebook-in-ibm-watson-studio)

### 1. Clone the repo

Clone the `monitor-custom-ml-engine-with-watson-openscale` locally. In a terminal, run:

```bash
git clone https://github.com/IBM/monitor-custom-ml-engine-with-watson-openscale
```

### 2. Create Watson services with IBM Cloud

> Note: If you are using [Watson Studio]() for your notebook, services created must be in the same region, and space, as your Watson Studio service.

Create the following services:

* [Watson OpenScale](https://cloud.ibm.com/catalog/services/ai-openscale)
  You will get the Watson OpenScale instance GUID when you run the notebook using the [IBM Cloud CLI](https://cloud.ibm.com/catalog/services/ai-openscale)

* [Databases for PostgreSQL DB](https://cloud.ibm.com/catalog/services/databases-for-postgresql)


* Wait a couple of minutes for the database to be provisioned.
* Click on the `Service Credentials` tab on the left and then click `New credential +` to create the service credentials. Copy them or leave the tab open to use later in the notebook.

### 3. Create a notebook in IBM Watson Studio

* In [Watson Studio](https://dataplatform.cloud.ibm.com/), create a `New project`.
* Using the project you've created, click on `+ Add to project` and then choose the  `Notebook` tile, OR in the `Assets` tab under `Notebooks` choose `+ New notebook` to create a notebook.
* Select the `From URL` tab.
* Enter a name for the notebook.
* Optionally, enter a description for the notebook.
* Under `Notebook URL` provide the following url: https://raw.githubusercontent.com/IBM/monitor-custom-ml-engine-with-watson-openscale/master/notebooks/WatsonOpenScaleAndCustomMLEngine.ipynb
* Select the `Default Python 3.5` runtime, either `Free` or `XS`.
* Click the `Create` button.

### 4a. Deploy to IBM Cloud

[![Deploy to IBM Cloud](https://cloud.ibm.com/devops/setup/deploy/button.png)](https://cloud.ibm.com/devops/setup/deploy?repository=https://github.com/IBM/monitor-custom-ml-engine-with-watson-openscale/tree/cfButton)

Click the ``Deploy to IBM Cloud`` button and hit ``Create`` and then jump to step 5.

**OR**

### 4.b Run the application server locally

> NOTE: Running locally will require Python 3.5 or 3.6 (later versions will not work with Tensorflow).
If you run the server locally, it may not have a publicly addressible IP address, if you are behind a firewall or local router. You would therefore also have to run the [Jupyter notebook](https://jupyter.org/) locally as well.

* It is recommended that you use a [Python virtualenv](https://pypi.org/project/virtualenv/)

```bash
python -m venv mytestenv       # Python 3.X

# Now source the virtual environment. Use one of the two commands depending on your OS.
source mytestenv/bin/activate  # Mac or Linux
./mytestenv/Scripts/activate   # Windows PowerShell
```

* Run:

```bash
pip install -r requirements.txt
export FLASK_APP=app.py
python -m flask run
```

See [test/README.md](test/README.md)  for instructions on testing the app.

### 5. Run the notebook in IBM Watson Studio

* Follow the instructions for `ACTION: Get data_mart_id (GUID) and apikey` using the [IBM Cloud CLI](https://cloud.ibm.com/docs/cli/index.html#overview)

Get an IAM apikey:
```
ibmcloud login --sso
ibmcloud iam api-key-create 'my_key'
```

Get Watson OpenScale instance GUID:
```
ibmcloud resource service-instance <Watson_OpenScale_instance_name>
```

* Enter the `GUID` as the `instance_guid` and the iam `API Key` as the `apikey` in the next cell for the `WATSON_OS_CREDENTIALS`.
* In the cell after `ACTION: Add your PostgreSQL credentials here` enter the credentials from the [Databases for PostgreSQL DB](https://cloud.ibm.com/catalog/services/databases-for-postgresql) that you created earlier.

* Move your cursor to each code cell and run the code in it. Read the comments for each cell to understand what the code is doing. **Important** when the code in a cell is still running, the label to the left changes to **In [\*]**:.
  Do **not** continue to the next cell until the code is finished running.

# Sample output

### GET the application server deployments

Navigate a browser to `http://<ip_address>:<port>/v1/deployments`
or run the [test_deployments.py](test/deployments_api.py) script following the  [test/README.md](test/README.md) instructions.


Output:

```
{"count":3,"resources":[{"entity":{"asset":{"guid":"resnet50","name":"resnet50"},"asset_properties":{"input_data_type":"unstructured_image","problem_type":"multiclass"},"description":"Keras ResNet50 model deployment for image classification","name":"ResNet50 AIOS compliant deployment","scoring_url":"http://169.60.16.73:31520/v1/deployments/resnet50/online"},"metadata":{"created_at":"2016-12-01T10:11:12Z","guid":"resnet50","modified_at":"2016-12-02T12:00:22Z"}},{"entity":{"asset":{"guid":"resnet50","name":"resnet50"},"asset_properties":{"input_data_type":"unstructured_image","problem_type":"multiclass"},"description":"Keras ResNet50 model deployment for image classification","name":"ResNet50 AIOS non compliant deployment","scoring_url":"http://169.60.16.73:31520/v1/deployments/resnet50_non_compliant/online"},"metadata":{"created_at":"2016-12-01T10:11:12Z","guid":"resnet50_non_compliant","modified_at":"2016-12-02T12:00:22Z"}},{"entity":{"asset":{"guid":"action","name":"area and action prediction"},"asset_properties":{"input_data_type":"structured","problem_type":"multiclass"},"description":"area and action spark models deployment","name":"action deployment","scoring_url":"http://169.60.16.73:31520/v1/deployments/action/online"},"metadata":{"created_at":"2016-12-01T10:11:12Z","guid":"action","modified_at":"2016-12-02T12:00:22Z"}}]}
```

### Run the [score_credit.py](test/score_credit.py) script following the  [test/README.md](test/README.md) instructions

Output:

```bash
******************************************
Prepare scoring payload ...
Score the model ...
Return predictions ...

{'fields': ['prediction', 'probability'], 'labels': ['Risk', 'No Risk'], 'values': [['No Risk', [0.8823126094462725, 0.1176873905537274]], ['No Risk', [0.6755090846150376, 0.3244909153849625]], ['No Risk', [0.8944991421537971, 0.10550085784620292]], ['No Risk', [0.9297263621482206, 0.07027363785177945]]]}

******************************************
```

### Run the [notebook](notebooks/AIOpenScaleAndCustomMLEngine.ipynb)

See [example output](examples/exampleNotebook.ipynb)

## License

This code pattern is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)

# Monitor Custom Machine Learning engine with AI OpenScale

In this Code Pattern, we will log the payload for a model deployed on custom model serving engine using AI OpenScale python sdk. We'll use [Keras to build a deep learning REST API](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html) and then monitor with [AI Open Scale](https://console.bluemix.net/docs/services/ai-openscale/getting-started.html).

When the reader has completed this Code Pattern, they will understand how to:

* Build a custom model serving engine using [Keras](https://keras.io/)
* Access the custom model using a REST API
* Log the payload for the model using [AI OpenScale](https://console.bluemix.net/docs/services/ai-openscale/connect-ml.html#connect-ml)

![](doc/source/images/architecture.png)

## Flow

1. Step 1.
2. Step 2.
3. Step 3.
4. Step 4.
5. Step 5.

# Watch the Video

TBD

## Prerequisites

* An [IBM Cloud Account](https://console.bluemix.net).
* [IBM Cloud CLI](https://console.bluemix.net/docs/cli/index.html#overview)
* An account on [IBM Watson Studio](https://dataplatform.ibm.com) or a way to run a [Jupyter Notebook](https://jupyter.org/) locally

# Steps

## Run locally

1. [Clone the repo](#1-clone-the-repo)
2. [Create Watson services with IBM Cloud](#2-create-watson-services-with-ibm-cloud)
3. [Create a notebook in IBM Watson Studio](#3-create-a-notebook-in-ibm-watson-studio) OR
   Run the notebook locally
4. Perform either 4a or 4b

    4a. [Run the application server in a Docker container](#4a-run-the-application-server-in-a-docker-container)

    4b. [Run the application server locally](#4b-run-the-application-server-locally)

5. [Run the notebook in IBM Watson Studio](#5-run-the-notebook-in-ibm-watson-studio)

### 1. Clone the repo

Clone the `monitor-custom-ml-engine-with-ai-openscale` locally. In a terminal, run:

```bash
$ git clone https://github.com/IBM/monitor-custom-ml-engine-with-ai-openscale
```

### 2. Create Watson services with IBM Cloud

> Note: If you are using [Watson Studio]() for your notebook, services created must be in the same region, and space, as your Watson Studio service.

Create the following services:

* [AI OpenScale](https://console.bluemix.net/catalog/services/ai-openscale)
  You will get the AI OpenScale instance GUID when you run the notebook using the [IBM Cloud CLI](https://console.bluemix.net/catalog/services/ai-openscale)

* [Compose for PostgreSQL DB](https://console.bluemix.net/catalog/services/compose-for-postgresql)

![](doc/source/images/ChooseComposePostgres.png)

* Wait a couple of minutes for the database to be provisioned.
* Click on the `Service Credentials` tab on the left and then click `New credential +` to create the service credentials. Copy them or leave the tab open to use later in the notebook.

### 3. Create a notebook in IBM Watson Studio

* In [Watson Studio](https://dataplatform.ibm.com), create a `New project`.
* Using the project you've created, click on `+ Add to project` and then choose the  `Notebook` tile, OR in the `Assets` tab under `Notebooks` choose `+ New notebook` to create a notebook.
* Select the `From URL` tab.
* Enter a name for the notebook.
* Optionally, enter a description for the notebook.
* Under `Notebook URL` provide the following url: https://raw.githubusercontent.com/IBM/monitor-custom-ml-engine-with-ai-openscale/notebooks/AIOpenScaleAndCustomMLEngine.ipynb
* Select the `Default Python 3.5` runtime, either `Free` or `XS`.
* Click the `Create` button.

### 4. TBD

### 5. Run the notebook in IBM Watson Studio

* Follow the instructions for `ACTION: Get data_mart_id (GUID) and apikey` using the [IBM Cloud CLI](https://console.bluemix.net/docs/cli/index.html#overview)

Get an IAM apikey:
```
$ibmcloud login --sso
$ibmcloud iam api-key-create 'my_key'
```

Get AI OpenScale instance GUID:
```
$ibmcloud resource service-instance <AIOpenScale_instance_name>
```

* Enter the `GUID` as the `instance_guid` and the iam `API Key` as the `apikey` in the next cell for the `AIOS_CREDENTIALS`.
* In the cell after `ACTION: Add your PostgreSQL credentials here` enter the credentials from the [Compose for PostgreSQL DB](https://console.bluemix.net/catalog/services/compose-for-postgresql) that you created earlier.

* Move your cursor to each code cell and run the code in it. Read the comments for each cell to understand what the code is doing. **Important** when the code in a cell is still running, the label to the left changes to **In [\*]**:.
  Do **not** continue to the next cell until the code is finished running.

# Sample output

# Troubleshooting

## License

This code pattern is licensed under the Apache License, Version 2. Separate third-party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1](https://developercertificate.org/) and the [Apache License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache License FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)

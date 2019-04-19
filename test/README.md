# Testing  Monitor Custom Machine Learning engine with Watson OpenScale

You can test the deployed ML model server using the test_api.py script:

* It is recommended that you use a [Python virtualenv](https://pypi.org/project/virtualenv/)

```bash
python -m venv mytestenv       # Python 3.X

# Now source the virtual environment. Use one of the two commands depending on your OS.
source mytestenv/bin/activate  # Mac or Linux
./mytestenv/Scripts/activate   # Windows PowerShell
```

* export the IP_ADDR and PORT of your running server:

```bash
export IP_ADDR=<ip_address>
export PORT=<port>
```

* run the script:

```bash
pip install -r requirements.txt
./test_api.py
```

The script will return a score for the deployed image recognition model:

```bash
 $ python test_api.py
{   'Results:': [   {   'prediction': 'beagle', 'probability': '0.98777544'},
                    {   'prediction': 'pot', 'probability': '0.0020967727'},
                    {   'prediction': 'Cardigan', 'probability': '0.0013517012'},
                    {   'prediction': 'Walker_hound',
                        'probability': '0.0012711119'},
                    {   'prediction': 'Brittany_spaniel',
                        'probability': '0.0010085113'}]}

```

You can test the deployments:

```bash
./test_deployments.py
```

The script will return the deployments for the server:

```bash
{
  "count": 2,
  "resources": [
    {
      "entity": {
        "asset": {
          "guid": "credit",
          "name": "credit"
        },
        "asset_properties": {
          "input_data_type": "structured",
          "problem_type": "binary"
        },
        "description": "Scikit-learn credit risk model deployment",
        "name": "German credit risk compliant deployment",
        "scoring_url": "https://127.0.0.1:5000/v1/deployments/credit/online"
      },
      "metadata": {
        "created_at": "2019-01-01T10:11:12Z",
        "guid": "credit",
        "modified_at": "2019-01-02T12:00:22Z"
      }
    },
    {
      "entity": {
        "asset": {
          "guid": "circle",
          "name": "circle"
        },
        "asset_properties": {
          "input_data_type": "structured",
          "problem_type": "regression"
        },
        "description": "Azure ML service circle surface prediction deployment",
        "name": "Circle model deployment",
        "scoring_url": "https://127.0.0.1:5000/v1/deployments/circle/online"
      },
      "metadata": {
        "created_at": "2019-01-01T10:11:12Z",
        "guid": "circle",
        "modified_at": "2019-01-02T12:00:22Z"
      }
    }
  ]
}
```

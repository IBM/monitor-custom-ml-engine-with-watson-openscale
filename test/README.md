# Testing  Monitor Custom Machine Learning engine with Watson OpenScale

You can test the deployed ML model server using the score_credit.py script:

* It is recommended that you use a [Python virtualenv](https://pypi.org/project/virtualenv/)

```bash
python -m venv mytestenv       # Python 3.X

# Now source the virtual environment. Use one of the two commands depending on your OS.
source mytestenv/bin/activate  # Mac or Linux
./mytestenv/Scripts/activate   # Windows PowerShell
```

* export the IP_ADDR and PORT of your running server or use the default `127.0.0.1:5000`

```bash
export IP_ADDR=<ip_address>
export PORT=<port>
```

* run the script:

```bash
pip install -r requirements.txt
./score_credit.py
```

The script will return a score for the deployed credit model:

```bash
 $ ./score_credit.py


******************************************
Prepare scoring payload ...
Score the model ...
Return predictions ...

{u'fields': [u'prediction', u'probability'], u'labels': [u'Risk', u'No Risk'], u'values': [[u'No Risk', [0.8823126094462725, 0.1176873905537274]], [u'No Risk', [0.6755090846150376, 0.3244909153849625]], [u'No Risk', [0.8944991421537971, 0.10550085784620292]], [u'No Risk', [0.9297263621482206, 0.07027363785177945]]]}

******************************************
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

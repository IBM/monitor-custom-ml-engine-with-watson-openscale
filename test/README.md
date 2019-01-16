# Testing  Monitor Custom Machine Learning engine with AI OpenScale

You can test the deployed ML model server using the test_api.py script:

* export the IP_ADDR and PORT of your running server:

```bash
export IP_ADDR=<ip_address>
export PORT=<port>
```

* run the script:

```bash
pip install -r requirements.txt
python test_api.py
```

The script will return a score for the deployed image recognition model:

```
 $ python test_api.py
{   'Results:': [   {   'prediction': 'beagle', 'probability': '0.98777544'},
                    {   'prediction': 'pot', 'probability': '0.0020967727'},
                    {   'prediction': 'Cardigan', 'probability': '0.0013517012'},
                    {   'prediction': 'Walker_hound',
                        'probability': '0.0012711119'},
                    {   'prediction': 'Brittany_spaniel',
                        'probability': '0.0010085113'}]}

```

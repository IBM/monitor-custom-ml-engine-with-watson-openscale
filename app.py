from flask import Flask, request, abort, jsonify
from ibm_watson_machine_learning import APIClient
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson_openscale import APIClient as OSAPIClient
from ibm_watson_openscale.utils import *
from ibm_watson_openscale.supporting_classes import *

import os, socket

app = Flask(__name__)

# implement two APIs here: https://aiopenscale-custom-deployement-spec.mybluemix.net/#/Deployments/post_v1_deployments__deployment_id__online
# - /v1/deployments:
#       Lists all deployments
#
# - /v1/deployments/{deployment_id}/online:
#       Makes an online prediction

WOS_CLIENT = None
DATA_SET_ID = None

# Generate an APIKEY first and create an env variable
# export WOSAPIKEY="ABCDS9xxxxxxxxxxrNoEVtb5o6_adfadfyyyyyyyyyy"
# def get_wosclient() -> OSAPIClient | None:
#     global WOS_CLIENT
#     if 'WOSAPIKEY' in os.environ and len(os.environ['WOSAPIKEY']) > 0:
#         if WOS_CLIENT is None:
#             authenticator = IAMAuthenticator(apikey=os.environ['WOSAPIKEY'])
#             WOS_CLIENT = OSAPIClient(authenticator=authenticator)
#         return WOS_CLIENT
#     return None


# def payload_logging(wos_client : OSAPIClient, req, res, sub_id):
#     global DATA_SET_ID
#     scoring_id = str(uuid.uuid4())
#     records_list=[]
#     if DATA_SET_ID is None:
#         DATA_SET_ID = wos_client.data_sets.list(type=DataSetTypes.PAYLOAD_LOGGING,
#                                                 target_target_id=sub_id,
#                                                 target_target_type=TargetTypes.SUBSCRIPTION).result.data_sets[0].metadata.id
#     pl_record = PayloadRecord(scoring_id=scoring_id, request=req, response=res, response_time=int(460))
#     records_list.append(pl_record)
#     wos_client.data_sets.store_records(data_set_id = DATA_SET_ID, request_body=records_list)



@app.route('/spaces/<space_id>/v1/deployments/<deployment_id>/online', methods=['POST'])
def wml_online(space_id, deployment_id):
    if not request.json:
        print("not json - reject")
        abort(400)

    if 'APIKEY' not in os.environ:
        print("no APIKEY, system error")
        abort(500)

    payload_scoring = {
        "input_data": [
            request.json
        ]
    }

    wml_client = APIClient(wml_credentials={
        "url": "https://us-south.ml.cloud.ibm.com",
        'apikey': os.environ['APIKEY']}
    )

    wml_client.set.default_space(space_id)

    scoring_response = wml_client.deployments.score(
        deployment_id, payload_scoring)

    # Uncomment below to enable auto payload logging. You need an OpenScale subscrition ID for this.
    # wos_client = get_wosclient()
    # if wos_client and 'WOS_SUB_ID' in os.environ and len(os.environ['WOS_SUB_ID']) > 0:
    #     # auto payload logging
    #     payload_logging(wos_client, request.json, scoring_response["predictions"][0], os.environ['WOS_SUB_ID'])


    return jsonify(scoring_response["predictions"][0])


@app.route('/spaces/<space_id>/v1/deployments', methods=['GET'])
def deployments(space_id):
    # This API endpoint is optional.
    # It should list all the deployed models in your custom environment.

    # If deploy this app on IBM Code Engine, the hostname can be determined by:
    if all(env in os.environ for env in ('CE_APP', 'CE_SUBDOMAIN', 'CE_DOMAIN')):
        hostname = 'https://' + os.environ['CE_APP'] + '.' + os.environ['CE_SUBDOMAIN'] + '.' + os.environ['CE_DOMAIN']
    else:
    # If deploying on a VM, change the hostname to the VM's IP that OpenScale service instance can access
        hostname = 'http://' + socket.gethostname()
    return {
        "count": 1,
        "resources": [
            {
                "metadata": {
                    "guid": "your_model_deployment_id",
                    "created_at": "2022-10-14T17:31:58.350Z",
                    "modified_at": "2022-10-14T17:31:58.350Z"
                },
                "entity": {
                    "name": "openscale-german-credit",
                    "description": "custom ml engine",
                    "scoring_url": hostname + "/spaces/" + space_id + "/v1/deployments/your_model_deployment_id/online",
                    "asset": {
                        "guid": "your_model_id",
                        "url": hostname + "/spaces/" + space_id + "/v1/deployments/your_model_deployment_id/online",
                        "name": "openscale-german-credit"
                    },
                    "asset_properties": {
                        "problem_type": "binary",
                        "predicted_target_field": "prediction",
                        "input_data_type": "structured",
                    }
                }
            }
        ]
    }


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')

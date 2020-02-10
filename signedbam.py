
import json
import requests

DEFAULT_CREDENTIALS_PATH = "./credentials.json"

def get_signed_url_from_uuid(uuid):
    with open(DEFAULT_CREDENTIALS_PATH) as json_file:
        credential = json.load(json_file)
    token = requests.post('https://nci-crdc.datacommons.io/user/credentials/api/access_token', json=credential).json()
    headers = {'Authorization': 'bearer '+ token['access_token']}
    file_endpt = 'https://nci-crdc.datacommons.io/user/data/download/'
    response = requests.get(file_endpt + uuid, headers=headers,params={'expires_in': str(3600)})
    url = response.json()['url']
    return(url)

# get the uuid for indices
def get_bai_uuid(uuid):
    file_endpt = 'https://api.gdc.cancer.gov/legacy/files/'
    file_with_indice = '?expand=index_files'
    response = requests.get(file_endpt + uuid + file_with_indice)
    res = response.json()
    #return(res)
    bai_uuid = res['data']['index_files'][0]['file_id']
    return(bai_uuid)

def signedbam(uuid):
    bai_uuid = get_bai_uuid(uuid)
    bai = get_signed_url_from_uuid(bai_uuid)
    bam = get_signed_url_from_uuid(uuid)
    return bam, bai

# uuid = 736a8e90-85ec-4007-b34a-1bf823eec6fc


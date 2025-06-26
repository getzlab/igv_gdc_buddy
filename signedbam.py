
import json
import requests

with open('config.json') as json_data_file:
    data = json.load(json_data_file)


def get_signed_url_from_uuid(uuid):
    with open(data["credential_path"]) as json_file:
        credential = json.load(json_file)
    token = requests.post('https://nci-crdc.datacommons.io/user/credentials/api/access_token', json=credential).json()
    headers = {'Authorization': 'bearer '+ token['access_token']}
    file_endpt = 'https://nci-crdc.datacommons.io/user/data/download/'
    pdict={'expires_in': str(3600)}
    if data['user_project'] is not "":
        pdict["userProject"] = data['user_project']
    response = requests.get(file_endpt + uuid, headers=headers,params=pdict)
    url = response.json()['url']
    return(url)

# get the uuid for indices
def get_bai_uuid(uuid):
    file_endpt = data['gdc_data_host']
    file_with_indice = '?expand=index_files'
    response = requests.get(file_endpt + uuid + file_with_indice)
    res = response.json()
    # print(res)
    bai_uuid = res['data']['index_files'][0]['file_id']
    return(bai_uuid)

def signedbam(uuid):
    bai_uuid = get_bai_uuid(uuid)
    bai = get_signed_url_from_uuid(bai_uuid)
    bam = get_signed_url_from_uuid(uuid)
    return bam, bai

# uuid = 736a8e90-85ec-4007-b34a-1bf823eec6fc


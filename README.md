# IGV buddy with GDC api

**Thanks for generous help from Jialin Ma**

This script facilitates fetching and updating signed url from GDC api for IGV. Given a UUID from GDC this api can fetch the signed url and stream that to IGV. When it detects that the URL will be expired soon, it will generate a new one from GDC.

## Prerequisite

This script is dependent on flask.

```
pip install flask
```
It also requires a credential file called `credentials.json` within the same path. Please login to https://nci-crdc.datacommons.io/ with your NIH login. Click on the "Profile" section in the upper right corner, then click "Create API key", in the window with your key click "Download json" to save your key.


## Run

First edit the `config.json`:
- `credential_path`: the credential file for NCI Data Commons, The default would be "./credentials.json"
- `gdc_data_host`: We will need send http request to here in order to get corresponding url for given BAM. For legacy bams the path should be "https://api.gdc.cancer.gov/legacy/files/".
- Please leave `user_project` empty for now.

Next set our default active user project and `gcloud auth login` with your user account.

Finally run the script by

```
python3 buddy.py
```

While running the script, start IGV. Click "File" > "Load from URL".
In "File URL" field, type: "http://localhost:5000/[uuid].bam" in bam field and "http://localhost:5000/[uuid].bai" (Please replace [uuid] with GDC file UUID, e.g. `http://localhost:5000/e7ab56c7-d9f3-40dc-ab13-808e7b0c8516.bam`)


## Note

`master` branch work with GDC legacy BAMs on hg19 if the data source is hosted by Google. `hg38` branch work with hg38 GCS BAMs (with changes in config), but not AWS-hosted data. PR is welcomed!
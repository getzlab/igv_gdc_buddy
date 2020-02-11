# IGV buddy with GDC api

**Thanks for generous help from Jialin Ma**

This script faciliates fetching and updating signed url from GDC api for IGV. Given a UUID from GDC this api can fetch the signed url and stream that to IGV. When it detects that the URL will be expired soon, it will generate a new one from GDC.

## Prerequisite

This script is dependent on flask.

```
pip install flask
```
It also requires a credential file called `credentials.json` within the same path. Please login to https://nci-crdc.datacommons.io/ with your NIH login. Click on the "Profile" section in the upper right corner, then click "Create API key", in the window with your key click "Download json" to save your key.


## Run

First edit the `config.json`:
- `credential_path`: the credential file for NCI Data Commons, The default would be "./credentials.json"
- `user_project`: the google project to be billed for viewing requester-pays bucket. When the field is empty it will try to access by your default billing project.
- `gdc_data_host`: We will need send http request to here in order to get corresponding url for given BAM. For legacy bams the path should be "https://api.gdc.cancer.gov/legacy/files/".

Then run the script by
```
python3 buddy.py
```

While running the script, start IGV. Click "File" > "Load from URL".
In "File URL" field, type: "http://localhost:5000/[uuid].bam" in bam field and "http://localhost:5000/[uuid].bai" (Please replace [uuid] with GDC file UUID)


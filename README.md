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

Run the script by
```
python3 buddy.py
```
while running the script, start IGV. Click "File" > "Load from URL".
In "File URL" field, type: "http://localhost:5000/[uuid].bam" in bam field and "http://localhost:5000/[uuid].bai" (Please replace [uuid] with GDC file UUID)


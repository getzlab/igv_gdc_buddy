
from flask import Flask, request
from signedbam import signedbam
from threading import Lock
import requests

app = Flask(__name__)

class URLHandler:
    def __init__(self):
        self.cache = {}
        self.lock = Lock()
    def get_uuid_url(self, uuid):
        from urllib.parse import urlparse, parse_qs
        with self.lock:
            if uuid in self.cache:
                bam, bai = self.cache[uuid]
                time_expires = min(int(parse_qs(urlparse(bai).query)['Expires'][0]), int(parse_qs(urlparse(bam).query)['Expires'][0]))
                from time import time
                if time_expires - time() > 5 * 60:
                    return bam, bai
            bam, bai = signedbam(uuid)
            self.cache[uuid] = bam, bai
            return bam, bai

    def get_bam(self, uuid):
        bam, bai = self.get_uuid_url(uuid)
        return bam
    def get_bai(self, uuid):
        bam, bai = self.get_uuid_url(uuid)
        return bai

handler = URLHandler()

@app.route("/<uuid>.bam")
def bam(uuid):
    bam_url = handler.get_bam(uuid)

    range_header = request.headers.get("Range", None)
    if range_header is not None:
        res = requests.get(bam_url, headers={"Range": range_header})
    else:
        res = requests.get(bam_url)

    return (res.content, res.status_code, res.headers.items())

@app.route("/<uuid>.bai")
def bai(uuid):
    bai_url = handler.get_bai(uuid)

    range_header = request.headers.get("Range", None)
    if range_header is not None:
        res = requests.get(bai_url, headers={"Range": range_header})
    else:
        res = requests.get(bai_url)

    return (res.content, res.status_code, res.headers.items())

if __name__ == "__main__":
    app.run(threaded=True)


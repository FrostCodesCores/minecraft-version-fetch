import json
import urllib.request
import re
import time
print("Fetching...")
urllib.request.urlretrieve("https://piston-meta.mojang.com/mc/game/version_manifest.json", "version_manifest.json")
file = open("version_manifest.json")
verdata = json.load(file)
date = time.strftime("%Y-%m-%d")
new_releases = []
latest_regex = str(verdata["latest"])
latest_regex = re.sub("[{}'',]", '', latest_regex)
for version in verdata["versions"]:
    if version.get("releaseTime", "").startswith(date):
        new_releases.append(version["id"])
if new_releases:
    print("New release")
    print(" ".join(new_releases))
else:
    print("No new releases")
    print("Current latest : ")
    print(latest_regex)

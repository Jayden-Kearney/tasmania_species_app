import os
import json
import re
from glob import glob

input_folder = "/Users/Kearno/Documents/LeafletProject/"
output_file = "/Users/Kearno/Documents/LeafletProject/burned_2000_2025_merged.geojson"

merged = {"type": "FeatureCollection", "features": []}

for file in glob(os.path.join(input_folder, "*.geojson")):
    filename = os.path.basename(file)
    match = re.search(r'(\d{4})', filename)
    if match:
        year = int(match.group(1))
        with open(file, "r") as f:
            data = json.load(f)
            for feat in data["features"]:
                feat["properties"]["year"] = year
                feat["properties"]["time"] = f"{year}-01-01"
                merged["features"].append(feat)
    else:
        print(f"Warning: Could not extract year from {filename}, skipping.")

with open(output_file, "w") as f:
    json.dump(merged, f, indent=2)
    
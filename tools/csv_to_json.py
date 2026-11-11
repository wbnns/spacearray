import csv
import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

input_file = base_dir / "data" / "Sign up form to be listed on Space Array website(Sheet1).csv"
output_file = base_dir / "public" / "team.json"

data = []

with open(input_file, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        first_name = row["First name"].strip()
        last_name = row["Last name"].strip()
        affiliation = row["Affiliation"].strip()
        interests = row["Main interests (keywords)"].strip()

        role = ""
        if first_name.lower() == "eric" and last_name.lower() == "villard":
            role = "Initiative Founder"

        data.append({
            "name": f"{first_name} {last_name}",
            "role": role,
            "affiliation": affiliation,
            "interests": interests
        })

data.sort(key=lambda x: x["name"].split()[-1].lower())

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(data)} entries to {output_file}")

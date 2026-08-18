import csv
import subprocess
import re
from collections import defaultdict
import sys
import os

# === Handle CLI argument for CSV file ===
if len(sys.argv) < 2:
    print("❌ CSV file name is required.\nUsage: python3 consolidate_page_workflows.py <csv-file>")
    sys.exit(1)

CSV_FILE = sys.argv[1]

# === Configuration ===
CONFLUENCE_DOMAIN = "https://localhost:8090"
USERNAME = "admin"
PASSWORD = "admin"
# AUTH_HEADER = "Authorization: Bearer <your-token>"

print(f"🔍 Reading CSV file: {CSV_FILE}")

if not os.path.exists(CSV_FILE):
    print(f"❌ CSV file '{CSV_FILE}' not found.")
    sys.exit(1)

# === Load and normalize CSV ===
with open(CSV_FILE, newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    raw_headers = next(reader)

    headers = [h.strip().lstrip("'").strip('"') for h in raw_headers]

    rows = [
        dict(zip(headers, [v.strip().lstrip("'").strip('"') for v in row]))
        for row in reader if any(cell.strip() for cell in row)
    ]

if not rows:
    print("⚠️ CSV file is empty (no data rows). Nothing to process.")
    sys.exit(0)

print("🧪 Normalized header keys in first row:")
print(list(rows[0].keys()))
print(f"✅ CSV loaded with {len(rows)} data rows.\n")

# === Prompt for grouping strategy ===
print("🧭 How would you like to group workflows?")
print("1 - Group by Space Key + Workflow Name")
print("2 - Group by Space Key + Workflow Name + Markup")
choice = input("Enter 1 or 2: ").strip()

if choice not in ["1", "2"]:
    print("❌ Invalid selection. Please enter 1 or 2.")
    sys.exit(1)

group_by_markup = (choice == "2")
print(f"🔧 Grouping by {'Space Key + Workflow Name + Markup' if group_by_markup else 'Space Key + Workflow Name'}.\n")

# === Grouping logic ===
groups = defaultdict(lambda: {"page_ids": [], "markup": None})
for row in rows:
    try:
        space_key = row["Space Key"]
        workflow_name = row["Workflow Name"]
        page_id = row["Page Id"]
        markup = row["Workflow Markup"]
    except KeyError as e:
        print(f"❌ Missing expected column: {e}")
        sys.exit(1)

    if page_id.isdigit():
        if group_by_markup:
            key = f"{space_key}|||{workflow_name}|||{markup}"
        else:
            key = f"{space_key}|||{workflow_name}"

        if key not in groups:
            groups[key]["markup"] = markup

        groups[key]["page_ids"].append(int(page_id))

print(f"📦 Grouping complete. {len(groups)} workflow groups found.\n")

# === Label generation ===
label_counters = defaultdict(int)

# === Curl execution per group ===
for key, data in groups.items():
    parts = key.split("|||")
    space_key = parts[0]
    workflow_name = parts[1]
    markup = data["markup"]

    # Generate sanitized label: WorkflowName + counter
    base_label = re.sub(r'[^A-Za-z0-9]', '', workflow_name)
    label_counters[base_label] += 1
    label = f"{base_label}{label_counters[base_label]}"

    page_ids_str = ", ".join(str(pid) for pid in data["page_ids"])
    markup_json = markup.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")

    json_payload = f'''{{
        "contentIds": [{page_ids_str}],
        "label": "{label}",
        "markup": "{markup_json}",
        "workflowName": "{workflow_name}"
    }}'''

    url = f"{CONFLUENCE_DOMAIN}/rest/cw/1/workflows/{space_key}/consolidatePageWorkflows"

    curl_cmd = [
        "curl", "--location", url,
        "--header", "Content-Type: application/json",
        "--user", f"{USERNAME}:{PASSWORD}",
        # "--header", AUTH_HEADER,
        "--data", json_payload
    ]

    print(f"🚀 Sending consolidation request:")
    print(f"   🔹 Space Key     : {space_key}")
    print(f"   🔹 Workflow Name: {workflow_name}")
    print(f"   🔹 Label         : {label}")
    print(f"   🔹 Pages         : {len(data['page_ids'])}")

    subprocess.run(curl_cmd)
    print("✅ Request completed.\n")

print("🎉 All workflow groups processed.")
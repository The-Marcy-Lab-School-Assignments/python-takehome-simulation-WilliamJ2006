import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_requests = 0
complaint_counts = {}
borough_counts = {}

for row in rows:
    if row['resolution_status'] == 'Open':
        open_requests+=1

    complaint = row['complaint_type']
    complaint_counts[complaint] = complaint_counts.get(complaint, 0) + 1

    borough = row['borough']
    borough_counts[borough] = borough_counts.get(borough, 0) + 1

most_common = max(complaint_counts, key=complaint_counts.get)

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_requests}\n\n")
    f.write(f"Most common complaint type: {most_common} ({complaint_counts[most_common]} requests)\n\n")

    f.write("Requests per borough:\n")
    for borough in sorted(borough_counts):
        f.write(f"- {borough}: {borough_counts[borough]}\n")

print("Output saved to output.txt")
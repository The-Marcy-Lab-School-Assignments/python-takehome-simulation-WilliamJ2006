import csv

rows = []

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

open_requests = 0
complaint_counts = {}
borough_counts = {}
borough_open_counts = {}
borough_closed_counts = {}

for row in rows:
    status = row['resolution_status']
    borough = row['borough']
    complaint = row['complaint_type']

    if status == 'Open':
        open_requests += 1
        borough_open_counts[borough] = borough_open_counts.get(borough, 0) + 1
    elif status == 'Closed':
        borough_closed_counts[borough] = borough_closed_counts.get(borough, 0) + 1

    complaint_counts[complaint] = complaint_counts.get(complaint, 0) + 1
    borough_counts[borough] = borough_counts.get(borough, 0) + 1

most_common = max(complaint_counts, key=complaint_counts.get)

# Q4: complaint types, sorted by count descending (ties broken alphabetically)
sorted_complaints = sorted(complaint_counts.items(), key=lambda x: (-x[1], x[0]))

# Q5: borough with the most open requests (ties broken alphabetically)
sorted_open_boroughs = sorted(borough_open_counts.items(), key=lambda x: (-x[1], x[0]))
top_open_borough, top_open_count = sorted_open_boroughs[0]

# Q6: closure rate per borough = closed / total * 100
closure_rates = {}
for borough in borough_counts:
    closed = borough_closed_counts.get(borough, 0)
    total = borough_counts[borough]
    closure_rates[borough] = round(closed / total * 100, 1)

# Q7: top 3 boroughs by total requests (ties broken alphabetically)
sorted_boroughs_total = sorted(borough_counts.items(), key=lambda x: (-x[1], x[0]))
top_3_boroughs = sorted_boroughs_total[:3]

with open('output.txt', 'w') as f:
    f.write(f"Open requests: {open_requests}\n\n")
    f.write(f"Most common complaint type: {most_common} ({complaint_counts[most_common]} requests)\n\n")

    f.write("Requests per borough:\n")
    for borough in sorted(borough_counts):
        f.write(f"- {borough}: {borough_counts[borough]}\n")
    f.write("\n")

    f.write("Requests by complaint type:\n")
    for complaint, count in sorted_complaints:
        f.write(f"- {complaint}: {count}\n")
    f.write("\n")

    f.write(f"Borough with most open requests: {top_open_borough} ({top_open_count} open)\n\n")

    f.write("Closure rate by borough:\n")
    for borough in sorted(closure_rates):
        f.write(f"- {borough}: {closure_rates[borough]}%\n")
    f.write("\n")

    f.write("Top 3 boroughs by total requests:\n")
    for i, (borough, count) in enumerate(top_3_boroughs, start=1):
        f.write(f"{i}. {borough} ({count} requests)\n")

print("Output saved to output.txt")
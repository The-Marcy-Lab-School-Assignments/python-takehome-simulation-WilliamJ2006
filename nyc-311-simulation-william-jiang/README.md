# NYC 311 Service Requests Analysis

## How to Run

1. Make sure you have Python 3 installed.
2. Navigate to this folder in your terminal.
3. Run the script:

python3 analysis.py

Output will be saved to `output.txt`. The console will confirm when the file has been written.

## What This Script Does

[Write 2-3 sentences describing what your script does in plain English.]

First, opens the nyc_311_requests.csv and reads through the file, appending row to our list. Then create variables to hold the data we need in the output, looping through each row in our list to incremenet and fill our dicts based off conditions and values of the resolution_status, complaint_type, and borough of the row. Get the most common by using max to return the key with the greatest value. Open output.txt and write to the file using our data.

## Dependencies

This script uses only Python's built-in libraries: `csv`.

## Notes

[Optional: anything you want to flag about your approach or assumptions.]

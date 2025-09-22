#!/usr/bin/env python3
"""
Batch IMDb ID processor for manual AI querying.
Reads imdb_ids.csv (handles BOM automatically), sends batches to user for manual AI input,
stores AI responses in new CSV imdb_ids_with_status.csv.
Strictly enforces Concluded/Cancelled format.
Includes kill switch and auto-save.
"""

import csv
import argparse
import re
import sys

ID_PATTERN = re.compile(r'(tt\d{6,8})', re.IGNORECASE)

def read_csv(file_path):
    """Read CSV and handle BOM if present."""
    with open(file_path, newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
    return rows

def write_csv(file_path, rows, fieldnames):
    """Write rows to CSV."""
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def chunk_list(lst, size):
    """Yield successive chunks of list."""
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

def normalize_status(raw_text):
    """Normalize AI input to Concluded or Cancelled."""
    s = raw_text.strip().lower()
    if s == "concluded":
        return "Concluded"
    if s == "cancelled":
        return "Cancelled"
    # default to Cancelled if anything unexpected
    return "Cancelled"

def main(input_file, batch_size=10):
    rows = read_csv(input_file)
    # Ensure status column exists
    if 'status' not in rows[0]:
        for r in rows:
            r['status'] = ""

    print(f"Loaded {len(rows)} rows from {input_file}.\n")
    batches = list(chunk_list(rows, batch_size))
    print(f"Processing in {len(batches)} batches of size {batch_size}.\n")

    for idx, batch in enumerate(batches, start=1):
        print("="*60)
        print(f"BATCH {idx}/{len(batches)}:")
        for r in batch:
            print(r['imdb_id'])
        print("="*60)
        print("Paste AI responses now (one line per imdb_id). End with 'END'.")
        print("Type 'KILL' to stop script safely.")

        # Read AI input
        batch_status = {}
        while True:
            try:
                line = input()
            except EOFError:
                print("EOF received, stopping input.")
                break
            if line.strip().upper() == 'END':
                break
            if line.strip().upper() == 'KILL':
                print("Kill switch activated. Exiting safely.")
                write_csv("imdb_ids_with_status.csv", rows, fieldnames=list(rows[0].keys()))
                sys.exit(0)

            parts = line.split(",")
            if len(parts) >= 2 and ID_PATTERN.match(parts[0].strip()):
                imdb = parts[0].strip()
                status = normalize_status(parts[1].strip())
                batch_status[imdb] = status
            else:
                print(f"Skipping invalid line: {line}")

        # update rows with status
        for r in batch:
            if r['imdb_id'] in batch_status:
                r['status'] = batch_status[r['imdb_id']]
            else:
                r['status'] = "Cancelled"  # fallback

        # save after each batch
        write_csv("imdb_ids_with_status.csv", rows, fieldnames=list(rows[0].keys()))
        print(f"Batch {idx} processed and saved.\n")

        cont = input("Continue to next batch? (y to continue, anything else to quit): ")
        if cont.strip().lower() != 'y':
            print("Stopping script. Progress saved.")
            break

    print("All batches processed or script stopped. Final CSV saved as imdb_ids_with_status.csv.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input CSV file path with imdb_id column")
    parser.add_argument("--batch-size", type=int, default=10, help="Number of IDs per batch")
    args = parser.parse_args()
    main(args.input, batch_size=args.batch_size)


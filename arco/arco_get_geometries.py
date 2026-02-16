import requests
import time
import csv
import os
import sys
import random

ENDPOINT = "https://dati.cultura.gov.it/sparql"
OUTPUT_FILE = "geometries.ttl"
SLEEP_SECONDS = 5
TIMEOUT_SECONDS = 120
CSV_FILE = "cultprops5.csv"  # your CSV file with one URL per line

HEADERS = {"Accept": "text/turtle"}


def fetch_geometry(urls): 

    values_clause = " ".join(f"<{u}>" for u in urls)

    query = f"""
    CONSTRUCT {{
        ?geo ?p ?o .
        ?coords ?cp ?co.
    }}
    WHERE {{
        VALUES ?cultpro {{ {values_clause} }}
        ?cultpro clvapit:hasGeometry ?geo .
        ?geo ?p ?o .
        ?geo a-loc:hasCoordinates ?coords.
        ?coords ?cp ?co.
    }}
    """

    params = {
        "query": query,
        "format": "text/turtle",
        "timeout": "0",
        "signal_void": "on"
    }
    resp = requests.get(ENDPOINT, params=params, headers=HEADERS, timeout=TIMEOUT_SECONDS)
    resp.raise_for_status()
    return resp.text


def main():
    if not os.path.exists(CSV_FILE):
        print(f"CSV file {CSV_FILE} not found!")
        sys.exit(1)

    first_write = not os.path.exists(OUTPUT_FILE) or os.path.getsize(OUTPUT_FILE) == 0

    with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        batch = []

        for idx, row in enumerate(reader):
            if not row:
                continue
            cult_url = row[0].strip()
            if not cult_url:
                continue

            batch.append(cult_url)
            if len(batch) == 8:
                print(f"[{idx}] Fetching geometry for: {cult_url}")
                try:
                    ttl_data = fetch_geometry(batch)
                except Exception as e:
                    print(f"Error fetching {cult_url}: {e}")
                    batch = []
                    continue

                if not ttl_data.strip():
                    print(f"No triples returned for {cult_url}, skipping.")
                    batch = []
                    continue

                # Write to file
                mode = "w" if first_write else "a"
                with open(OUTPUT_FILE, mode, encoding="utf-8") as fw:
                    if first_write:
                        fw.write(ttl_data)
                        first_write = False
                    else:
                        # strip prefixes from subsequent writes
                        lines = []
                        for ln in ttl_data.splitlines():
                            if ln.strip().startswith("@prefix") or ln.strip().startswith("@base"):
                                continue
                            lines.append(ln)
                        fw.write("\n".join(lines) + "\n")

                print(f"Appended geometry for {batch[4]}")
                batch  = []
                sleep_time = random.uniform(2, 5)
                time.sleep(sleep_time)

    print("Finished fetching all geometries.")


if __name__ == "__main__":
    main()

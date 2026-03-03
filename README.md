# csv-cleaner-python

Clean & standardize messy CSV files with Python.

This repo contains a small CLI script that:
- trims whitespace in string columns
- normalizes column names (lowercase + underscores)
- removes fully-empty rows
- removes exact duplicate rows
- exports a cleaned CSV

## Files
- `automation.py` — the script
- `sample_input.csv` — example input
- `sample_output.csv` — expected output example

## Requirements
- Python 3.9+
- pandas

## Quick start

```bash
pip install pandas
python automation.py --in sample_input.csv --out output.csv
```

## CLI options
- `--in`  : input CSV path (required)
- `--out` : output CSV path (required)

## Notes
- The script reads all columns as strings to avoid type surprises when cleaning messy data.
- If you need custom rules (date parsing, dedupe by key, schema mapping), extend `clean_df()`.

## License
MIT

import argparse
import re
import sys
import pandas as pd


def normalize_header(name: str) -> str:
    name = str(name).strip().lower()
    name = re.sub(r"\s+", "_", name)
    name = re.sub(r"[^a-z0-9_]", "", name)
    name = re.sub(r"_+", "_", name).strip("_")
    return name


def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    # Trim whitespace in string columns
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()

    # Normalize headers
    df = df.rename(columns={c: normalize_header(c) for c in df.columns})

    # Remove fully-empty rows
    df = df.dropna(how="all")

    # Drop exact duplicate rows
    df = df.drop_duplicates()

    return df


def main() -> int:
    p = argparse.ArgumentParser(description="Clean & standardize a CSV file.")
    p.add_argument("--in", dest="in_path", required=True, help="Input CSV path")
    p.add_argument("--out", dest="out_path", required=True, help="Output CSV path")
    args = p.parse_args()

    df = pd.read_csv(args.in_path, dtype=str, keep_default_na=False)
    cleaned = clean_df(df)
    cleaned.to_csv(args.out_path, index=False)

    print(f"Saved cleaned CSV: {args.out_path} (rows: {len(cleaned)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

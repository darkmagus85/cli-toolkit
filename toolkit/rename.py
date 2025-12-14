from pathlib import Path

def run(prefix: str):
    files = [f for f in Path(".").iterdir() if f.is_file()]

    for index, file in enumerate(files, start=1):
        new_name = f"{prefix}_{index}{file.suffix}"
        file.rename(new_name)

    print(f"Renamed {len(files)} files.")

import os
import shutil
import uuid


def run(prefix: str, dry_run: bool = False):
    """
    Rename all files in the current directory using the given prefix.
    Uses temporary filenames to avoid collisions.
    """
    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    if not files:
        print("No files to rename.")
        return

    temp_map = {}
    # Step 1: Assign temporary names
    for f in files:
        tmp_name = f"{f}.tmp_{uuid.uuid4().hex}"
        temp_map[f] = tmp_name
        if dry_run:
            print(f"Would rename: {f} -> {tmp_name}")
        else:
            os.rename(f, tmp_name)

    # Step 2: Assign final names with prefix
    sorted_files = sorted(temp_map.keys())  # sorted for consistent ordering
    for idx, f in enumerate(sorted_files, start=1):
        tmp_name = temp_map[f]
        ext = os.path.splitext(f)[1]
        new_name = f"{prefix}_{idx}{ext}"
        if dry_run:
            print(f"Would rename: {tmp_name} -> {new_name}")
        else:
            os.rename(tmp_name, new_name)

    if not dry_run:
        print(f"Renamed {len(files)} files.")

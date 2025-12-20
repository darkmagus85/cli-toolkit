from pathlib import Path
import shutil
from datetime import datetime


def run(path, dry_run=False):
    source = Path(path)

    if not source.exists():
        print(f"Error: file not found: {source}")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{source.name}.bak_{timestamp}"
    destination = source.with_name(backup_name)

    if dry_run:
        print(f"Would back up: {source} -> {destination}")
        return

    shutil.copy2(source, destination)
    print(f"Backed up: {source} -> {destination}")

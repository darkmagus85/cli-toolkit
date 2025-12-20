import argparse

from toolkit.rename import run as rename_run
from toolkit.backup import run as backup_run
from toolkit.info import run as info_run


def main():
    parser = argparse.ArgumentParser(prog="toolkit", description="Personal CLI toolkit")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # --------------------
    # Rename subcommand
    # --------------------
    rename_parser = subparsers.add_parser(
        "rename", help="Rename files in the current directory"
    )
    rename_parser.add_argument("prefix", help="Prefix to use for renamed files")
    rename_parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    # --------------------
    # Backup subcommand
    # --------------------
    backup_parser = subparsers.add_parser("backup", help="Create a backup of a file")
    backup_parser.add_argument("path", help="File to back up")
    backup_parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    # --------------------
    # Info subcommand
    # --------------------
    info_parser = subparsers.add_parser("info", help="Show information about a file")
    info_parser.add_argument("path", help="File to inspect")

    args = parser.parse_args()

    if args.command == "rename":
        rename_run(prefix=args.prefix, dry_run=args.dry_run)

    elif args.command == "backup":
        backup_run(path=args.path, dry_run=args.dry_run)

    elif args.command == "info":
        info_run(path=args.path)


if __name__ == "__main__":
    main()

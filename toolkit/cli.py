import argparse
from toolkit.rename import run as rename_run
from toolkit.backup import run as backup_run
from toolkit.info import run as info_run


def main():
    parser = argparse.ArgumentParser(prog="toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -------------------
    # Rename subcommand
    # -------------------
    rename_parser = subparsers.add_parser("rename", help="Rename files")
    rename_parser.add_argument("prefix", help="Prefix to use for renamed files")
    rename_parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    # -------------------
    # Backup subcommand (placeholder)
    # -------------------
    backup_parser = subparsers.add_parser("backup", help="Backup files")
    backup_parser.add_argument("target", help="Target path to backup")
    backup_parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    # -------------------
    # Info subcommand (placeholder)
    # -------------------
    info_parser = subparsers.add_parser("info", help="Show file info")
    info_parser.add_argument("files", nargs="*", help="Files to inspect")
    info_parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes",
    )

    # -------------------
    # Parse and dispatch
    # -------------------
    args = parser.parse_args()

    if args.command == "rename":
        rename_run(prefix=args.prefix, dry_run=args.dry_run)
    elif args.command == "backup":
        backup_run(target=args.target, dry_run=args.dry_run)
    elif args.command == "info":
        info_run(files=args.files, dry_run=args.dry_run)


if __name__ == "__main__":
    main()

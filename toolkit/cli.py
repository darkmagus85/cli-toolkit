import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Personal CLI toolkit"
    )

    subparsers = parser.add_subparsers(dest="command")

    rename_parser = subparsers.add_parser("rename", help="Bulk rename files")
    rename_parser.add_argument("prefix", help="Prefix for renamed files")

    subparsers.add_parser("backup", help="Create backups")
    subparsers.add_parser("info", help="Show system info")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "rename":
        from toolkit.rename import run
        run(args.prefix)
        return

    print(f"{args.command} command not implemented yet")

if __name__ == "__main__":
    main()

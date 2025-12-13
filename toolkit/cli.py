import argparse


def main():
    parser = argparse.ArgumentParser(prog="toolkit", description="Personal CLI toolkit")

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("rename", help="Bulk rename files")
    subparsers.add_parser("backup", help="Create backups")
    subparsers.add_parser("info", help="Show system info")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    print(f"{args.command} command not implemented yet")


if __name__ == "__main__":
    main()

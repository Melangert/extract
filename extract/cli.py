import sys
import argparse
from .archive import extract_file
from .formats import detect_format, list_supported_extensions
from .utils import success, error, warning

def main():
    parser = argparse.ArgumentParser(
        prog="extract",
        description="Extract any archive file",
    )
    parser.add_argument("archives", nargs="*", help="Archive file(s) to extract")
    parser.add_argument("-o", "--output", help="Output directory, default=None")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show extracted files")
    parser.add_argument("--list", action="store_true", help="List supported formats")
    parser.add_argument("--detect", action="store_true", help="Detect format without extracting")

    args = parser.parse_args()

    if args.list:
        print("Supported formats:")
        for ext in list_supported_extensions():
            print(f"  - {ext}")
        return

    if args.detect:
        for archive in args.archives:
            fmt = detect_format(archive)
            print(f"{archive}: {fmt or 'Unknown format'}")
        return

    for archive in args.archives:
        dest = args.output or "."
        try:
            extract_file(archive,dest, verbose=args.verbose)
            print(success(f"Extracted {archive} to {dest}"))
        except Exception as e:
            print(error(f"Failed to extract {archive}: {e}"))

def entry_point():
    main()
    sys.exit(0)
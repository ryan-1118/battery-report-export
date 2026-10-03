"""Battery Report Export — Build a Windows battery health report with cycle count, capacity, and recent usage."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='battery_report_export',
        description='Build a Windows battery health report with cycle count, capacity, and recent usage.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Battery Report Export')
    print('A readable battery report without digging through powercfg XML.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

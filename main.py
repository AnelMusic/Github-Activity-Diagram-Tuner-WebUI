#!/usr/bin/env python
import sys
from arguments_parser import parse_arguments
from contributions_manager import ContributionsManager

def main():
    args = parse_arguments(sys.argv[1:])
    manager = ContributionsManager(args)
    manager.generate_contributions()

if __name__ == "__main__":
    main()

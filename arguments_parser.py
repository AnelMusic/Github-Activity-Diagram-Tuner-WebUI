import argparse

def parse_arguments(args):
    parser = argparse.ArgumentParser(description="Automates Git repository contributions.")

    parser.add_argument('--exclude-weekends', action='store_true', help="Exclude weekends from the contribution schedule.")
    parser.add_argument('--max-daily-commits', type=int, default=10, help="Specify the maximum number of commits allowed per day.")
    parser.add_argument('--commit-probability', type=int, default=80, help="Define the probability (in percentage) of making commits on any given day.")
    parser.add_argument('--repository-url', type=str, help="URL of the remote git repository for pushing commits.")
    parser.add_argument('--git-username', type=str, help="Specify the Git username for commit attribution.")
    parser.add_argument('--git-email', type=str, help="Specify the Git email for commit attribution.")
    parser.add_argument('--days-before', type=int, default=365, help="Define the start of the contribution period as a number of days before the current date.")
    parser.add_argument('--days-after', type=int, default=0, help="Define the end of the contribution period as a number of days after the current date.")

    return parser.parse_args(args)

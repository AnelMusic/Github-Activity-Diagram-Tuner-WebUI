import subprocess

def get_user_input():
    """
    Interactively collects user inputs for various script arguments.
    """
    exclude_weekends = input("Exclude weekends from the contribution schedule? (yes/no): ").lower() == 'yes'
    max_daily_commits = input("Specify the maximum number of commits allowed per day (default 10): ") or '10'
    commit_probability = input("Define the commit probability percentage (default 80): ") or '80'
    repository_url = input("Enter the URL of the remote git repository for pushing commits: ")
    git_username = input("Specify the Git username for commit attribution: ")
    git_email = input("Specify the Git email for commit attribution: ")
    start_period = input("Define the start of the contribution period as days before the current date (default 365): ") or '365'
    end_period = input("Define the end of the contribution period as days after the current date (default 0): ") or '0'

    return [
        '--exclude-weekends' if exclude_weekends else '',
        '--max-daily-commits', max_daily_commits,
        '--commit-probability', commit_probability,
        '--repository-url', repository_url,
        '--git-username', git_username,
        '--git-email', git_email,
        '--days-before', start_period,
        '--days-after', end_period
    ]

def main():
    args = get_user_input()
    args = [arg for arg in args if arg]
    subprocess.run(['python', 'main.py'] + args)

if __name__ == "__main__":
    main()

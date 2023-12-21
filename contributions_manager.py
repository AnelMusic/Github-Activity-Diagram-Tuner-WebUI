from datetime import datetime
from git_operations import GitOperations
from utils import calculate_commit_schedule, append_to_contribution_file

class ContributionsManager:
    """
    Manages the creation and management of Git contributions.
    """

    def __init__(self, args):
        """
        Initializes the ContributionsManager with command line arguments.

        :param args: Parsed command line arguments.
        """
        self.args = args
        self.git_ops = GitOperations(self._determine_repository_directory(args))
        self.git_ops.init_repository()
        self.git_ops.config_user(args.git_username, args.git_email)
        if args.repository_url:
            self.git_ops.add_remote(args.repository_url)

    def generate_contributions(self):
        """
        Generates contributions based on the specified schedule and commits them to the repository.
        """
        for commit_time in calculate_commit_schedule(self.args):
            self._create_commit(commit_time)
        if self.args.repository_url:
            self.git_ops.push_changes()

    def _create_commit(self, date):
        """
        Creates a commit in the Git repository for a specific date.

        :param date: The datetime object representing the date and time of the commit.
        """
        append_to_contribution_file(date)
        self.git_ops._run_command(['git', 'add', '.'])
        commit_message = f'Contribution: {date.strftime("%Y-%m-%d %H:%M")}'
        self.git_ops._run_command(['git', 'commit', '-m', commit_message, '--date', date.strftime('%Y-%m-%d %H:%M:%S')])

    def _determine_repository_directory(self, args):
        """
        Determines the directory name for the repository based on the provided arguments.

        :param args: Parsed command line arguments.
        :return: The name of the directory to be used for the repository.
        """
        if args.repository_url:
            return args.repository_url.split('/')[-1].split('.')[0]
        else:
            return f'repository-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'

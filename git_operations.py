import os
import subprocess
import logging
import sys

class GitOperations:
    """
    This class handles Git operations such as initializing a repository, configuring user details,
    adding a remote, and pushing changes to the repository.
    """

    def __init__(self, directory):
        """
        Initializes the GitOperations class with the specified directory.

        :param directory: The directory where the Git repository is located or will be created.
        """
        self.directory = directory
        self._setup_logging()

    def _setup_logging(self):
        """
        Sets up basic logging configuration for the class.
        """
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def init_repository(self):
        """
        Initializes a new Git repository in the specified directory. If the directory does not exist,
        it will be created.
        """
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self._run_command(['git', 'init', '-b', 'main'])
        os.chdir(self.directory)

    def config_user(self, user_name, user_email):
        """
        Configures the Git user name and email for the repository.

        :param user_name: The Git user name to be set.
        :param user_email: The Git user email to be set.
        """
        if user_name:
            self._run_command(['git', 'config', 'user.name', user_name])
        if user_email:
            self._run_command(['git', 'config', 'user.email', user_email])

    def add_remote(self, repository_url):
        """
        Adds a remote repository URL to the Git repository.

        :param repository_url: The URL of the remote repository to be added.
        """
        self._run_command(['git', 'remote', 'add', 'origin', repository_url])

    def push_changes(self):
        """
        Pushes the local changes to the remote Git repository.
        """
        self._run_command(['git', 'push', '-u', 'origin', 'main'])

    def _run_command(self, commands):
        """
        Executes the given Git command and logs the outcome.

        :param commands: A list of strings representing the Git command and its arguments.
        """
        try:
            subprocess.run(commands, check=True)
            logging.info(f"Successfully executed: {' '.join(commands)}")

        except subprocess.CalledProcessError as e:
            logging.error(f"Error executing command: {' '.join(commands)} - {e}")

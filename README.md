## Activity-Diagram-Tuner

Call this project a rebellious response to a situation where a close friend of mine was unjustly judged during an interview based solely on her GitHub Activity diagram. I firmly believe that these diagrams are not reliable indicators of true engineering excellence or skill. That's why I present 'GitHub Activity Diagram Tuner

### Let's go from:
![111111](https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/35568a3d-8c93-45fa-ad4c-873bcf04871c)

### to:
![2222](https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/cb3abc08-23b0-42d6-b120-204070344842)

#### Git Repo Setup
1. Create a repository and make it private
   <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/85bc2b5e-ba08-4a4f-89d6-7c42f809db08" alt="1" width="200" height="200">
   
2. Do not initialise your repository such that it stays like:
   <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/a97bc6e3-e7e3-4035-b6d7-0d17f526c14d" alt="2" width="100" height="200">



#### Basic Workflows
1. Fork project: https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/n/fork)
2. Create venv and activate it
   - Linux:
     - python3 -m venv myenv
     - source myenv/bin/activate
   - Windows:
     - python -m venv myenv
     - .\myenv\Scripts\Activate.ps1
3. Install requirements.txt
    - pip install requirements.txt
5. Run ui_launcher.py
   - python ui_launcher.py

#### Once the UI is UP:
![4](https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/f3117745-7f6f-4170-9787-3369da4f8a18)

You can interactively provide input for the following variables:

- `exclude_weekends`: To exclude weekends from the contribution schedule, users can type "yes" when prompted (case-insensitive) or simply press Enter to use the default behavior.

- `max_daily_commits`: Users can specify the maximum number of commits allowed per day. If left empty, the default value of 10 will be used.

- `commit_probability`: Define the commit probability percentage (default 80) by entering the desired value. If left empty, the default value of 80% will be used.

- `repository_url`: Enter the URL of the remote Git repository where commits will be pushed.

- `git_username`: Specify the Git username for commit attribution.

- `git_email`: Specify the Git email for commit attribution.

- `start_period`: Define the start of the contribution period as a number of days before the current date. If left empty, the default period of 365 days will be used.

- `end_period`: Define the end of the contribution period as a number of days after the current date. If left empty, the default period of 0 days will be used.




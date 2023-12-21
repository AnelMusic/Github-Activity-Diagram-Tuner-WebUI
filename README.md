## Activity-Diagram-Tuner

Call this project a rebellious response to a situation where a talented friend of mine was unjustly judged during an interview based on her GitHub Activity. These diagrams are oviously not a reliable indicators of true engineering excellence or skill. That's why I present a GitHub Activity Diagram Tuner.
So, this app lets you manipulate your GitHub Activity and create a 'realistic' commit history. 

Of course, I'd never suggest bending the rules or anything; this repo is purely for 'educational' purposes, you know what I mean? But seriously, if someone's gonna judge your coding skills based on a little activity chart, they should be fooled. Fair, right?

- You can expect to go from this:
<p align="center">
  <!-- Original Image -->
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/35568a3d-8c93-45fa-ad4c-873bcf04871c" alt="111111" width="800" height="200">
</p>

- to this:

<p align="center">
  <!-- Resized Image -->
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/cb3abc08-23b0-42d6-b120-204070344842" alt="2222" width="800" height="200">
</p>



### Git Repo Setup:
Before running the app some preparation is needed:


1. Create a repository and make it private

<p align="center">
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/85bc2b5e-ba08-4a4f-89d6-7c42f809db08" alt="4" width="650" height="700">
</p>


2. Do not initialise your repository such that it looks like:

<p align="center">
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/a97bc6e3-e7e3-4035-b6d7-0d17f526c14d" alt="4" width="650" height="700">
</p>


### Basic Workflows:
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


### Once the UI is UP:

<p align="center">
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/f3117745-7f6f-4170-9787-3369da4f8a18" alt="4" width="700" height="550">
</p>

You can interactively provide input for the following variables:

- `exclude_weekends`: Use the Checkbox to exclude weekends from the contribution schedule.

- `max_daily_commits`: Users can specify the maximum number of commits allowed per day. If left empty, the default value of 10 will be used.

- `commit_probability`: Define the commit probability percentage (default 80) by entering the desired value. If left empty, the default value of 80% will be used.

- `repository_url`: Enter the URL of the remote Git repository where commits will be pushed. (See above marked in red)

- `git_username`: Specify the Git username for commit attribution.

- `git_email`: Specify the Git email for commit attribution.

- `start_period`: Define the start of the contribution period as a number of days before the current date. If left empty, the default period of 365 days will be used.

- `end_period`: Define the end of the contribution period as a number of days after the current date. If left empty, the default period of 0 days will be used.

### Press Submit

You're welcome


## Activity-Diagram-Tuner

Call this project a rebellious response to a situation where a talented friend of mine was unjustly judged during an interview based on her GitHub Activity. These diagrams are oviously not a reliable indicators of true engineering excellence or skill. That's why I present a GitHub Activity Diagram Tuner.
So, this app lets you manipulate your GitHub Activity and create a 'realistic' commit history. 

Of course, I'd never suggest bending the rules or anything; this repo is purely for 'educational' purposes, you know what I mean? But seriously, if someone's gonna judge your coding skills based on a little activity chart, they should be fooled. Fair, right?

Note:
- This isn't a professionally polished product, and I didn't invest an excessive amount of time into it. It's designed to do the job, and if you come across any bugs, please don't hesitate to submit pull requests.
- The code hasn't undergone formal software testing, such as unit tests or integration tests. All testing has been done manually, and there's no need to overcomplicate this straightforward task.

##### You can expect to go from this:
<p align="center">
  <!-- Original Image -->
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/35568a3d-8c93-45fa-ad4c-873bcf04871c" alt="111111" width="800" height="200">
</p>

##### to this:

<p align="center">
  <!-- Resized Image -->
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/cb3abc08-23b0-42d6-b120-204070344842" alt="2222" width="800" height="200">
</p>


## Git Repo Setup:

Before you can run the app, some initial setup for your Git repository is required. Follow these steps to ensure your repository is properly configured:

**1.Create a Private Repository:**
   - Start by creating a new repository on GitHub, and make sure to set it as private. This will keep your project secure.

<p align="center">
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/85bc2b5e-ba08-4a4f-89d6-7c42f809db08" alt="4" width="650" height="700">
</p>

**2. Do Not Initialize Your Repository Like This:**
   - Make sure not to initialize your repository with any files or a README that makes it look like this:

<p align="center">
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/a97bc6e3-e7e3-4035-b6d7-0d17f526c14d" alt="4" width="650" height="700">
</p>
By following these guidelines, you'll have your Git repository set up correctly for the app to work seamlessly.



## Getting Started:

Follow these simple steps to get started with the GitHub Activity Diagram Tuner WebUI:

**1. Fork the Repository:**
   - Start by forking the project repository from [here](https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/fork).

**2. Set Up a Virtual Environment:**
   - Create a virtual environment and activate it based on your operating system:
     - For Linux:
       - Run `python3 -m venv myenv` to create a virtual environment named `myenv`.
       - Activate it with `source myenv/bin/activate`.
     - For Windows:
       - Run `python -m venv myenv` to create a virtual environment named `myenv`.
       - Activate it with `.\myenv\Scripts\Activate.ps1`.

**3. Install Dependencies:**
   - Install the required dependencies from `requirements.txt` using pip:
     ```
     pip install -r requirements.txt
     ```

**4. Run the WebUI:**
   - Start the WebUI by running `ui_launcher.py`:
     ```
     python ui_launcher.py
     ```



## Interact with the User Interface:

Once you have the user interface up and running, you can easily provide input for various settings:

<p align="center">
  <img src="https://github.com/AnelMusic/Github-Activity-Diagram-Tuner-WebUI/assets/32487291/f3117745-7f6f-4170-9787-3369da4f8a18" alt="UI Screenshot" width="700" height="550">
</p>

Here are the interactive variables you can adjust:

- **Exclude Weekends:** Use the checkbox to exclude weekends from the contribution schedule.

- **Max Daily Commits:** Specify the maximum number of commits allowed per day. Leave it empty to use the default value of 10.

- **Commit Probability:** Define the commit probability percentage (default 80%) by entering your desired value. Leave it empty to use the default.

- **Repository URL:** Enter the URL of the remote Git repository where commits will be pushed (highlighted in red in the image above).

- **Git Username:** Specify your Git username for commit attribution.

- **Git Email:** Specify your Git email for commit attribution.

- **Start Period:** Define the start of the contribution period as a number of days before the current date. Leave it empty to use the default period of 365 days.

- **End Period:** Define the end of the contribution period as a number of days after the current date. Leave it empty to use the default period of 0 days.

### Finally, Press Submit

You're all set! Enjoy using the app.


## Troubleshooting and Support:

If you encounter any errors while using the app, follow these steps for assistance:

1. **Check the Logs:** First, examine the logs for any error messages or useful information. The logs can often provide clues about what went wrong.

2. **Create an Issue:** If you're unable to resolve the problem on your own, don't hesitate to create a new issue on the repository. Describe the problem you're facing in detail, including any error messages you've encountered. 

Feel free to reach out if you run into any difficulties. Your feedback and issues are valuable for improving the app's functionality.


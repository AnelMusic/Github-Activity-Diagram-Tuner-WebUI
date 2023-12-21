import gradio as gr
import subprocess

def run_subprocess(exclude_weekends, max_daily_commits, commit_probability, repository_url, git_username, git_email, start_period, end_period):
    args = [
        '--exclude-weekends' if exclude_weekends else '',
        '--max-daily-commits', str(max_daily_commits),
        '--commit-probability', str(commit_probability),
        '--repository-url', repository_url,
        '--git-username', git_username,
        '--git-email', git_email,
        '--days-before', str(start_period),
        '--days-after', str(end_period)
    ]
    args = [arg for arg in args if arg]
    subprocess.run(['python', 'main.py'] + args)

iface = gr.Interface(
    fn=run_subprocess,
    inputs=[
        gr.Checkbox(label="Exclude weekends from the contribution schedule?"),
        gr.Number(label="Maximum number of commits per day", value=10),
        gr.Number(label="Commit probability percentage", value=80),
        gr.Text(label="URL of the remote git repository"),
        gr.Text(label="Git username for commit attribution"),
        gr.Text(label="Git email for commit attribution"),
        gr.Number(label="Start of the contribution period (days before current date)", value=365),
        gr.Number(label="End of the contribution period (days after current date)", value=0)
    ],
    outputs="text",
    title="Git Commit Scheduler",
    description="Input parameters for scheduling git commits."
)

iface.launch()



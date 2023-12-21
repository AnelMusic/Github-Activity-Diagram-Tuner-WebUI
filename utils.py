from datetime import datetime, timedelta
from random import randint
import os

def calculate_commit_schedule(args):
    """
    Determines the schedule of commits based on provided arguments.
    """
    schedule_start = determine_schedule_start(args.days_before)
    return [time for day in generate_date_range(schedule_start, args.days_before, args.days_after)
            if should_commit_on_day(day, args) 
            for time in generate_commit_times_for_day(day, args.max_daily_commits)]

def determine_schedule_start(days_before):
    """
    Calculates the start date of the commit schedule.
    """
    return datetime.now().replace(hour=20, minute=0) - timedelta(days_before)

def generate_date_range(start_date, days_before, days_after):
    """
    Generates a range of dates for the commit schedule.
    """
    total_days = days_before + days_after
    return [start_date + timedelta(days=n) for n in range(total_days)]

def should_commit_on_day(day, args):
    """
    Determines if commits should be made on a given day.
    """
    is_weekend = day.weekday() >= 5
    return (not args.exclude_weekends or not is_weekend) and randint(0, 100) < args.commit_probability

def generate_commit_times_for_day(day, max_daily_commits):
    """
    Generates random commit times for a given day.
    """
    number_of_commits = randint(1, min(max(max_daily_commits, 1), 20))
    return [day + timedelta(minutes=randint(0, 1440)) for _ in range(number_of_commits)]

def append_to_contribution_file(date):
    """
    Appends a new contribution entry to the README file in the specified directory.
    """
    file_path = 'README.md'
    with open(file_path, 'a') as file:
        print("ADDING STUFF")
        file.write(f'Contribution: {date.strftime("%Y-%m-%d %H:%M")}\n\n')

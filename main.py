from jobScraper import extract_indeed_jobs

keyword = input("What do you want to search for?")

indeed_jobs = extract_indeed_jobs(keyword)

for job in indeed_jobs:
    print(job)
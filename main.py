from jobScraper import extract_indeed_jobs

keyword = input("What do you want to search for?")

indeed_jobs = extract_indeed_jobs(keyword)

file = open(f"{keyword}.csv", "w")

file.write("Position,Company,Loacaion,URL\n")

for job in indeed_jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()


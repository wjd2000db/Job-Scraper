from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_experimental_option("detach", True)

url = 'https://ca.indeed.com/jobs?q=software+developer+intern&vjk=2a587d68efa44b7d'

browser = webdriver.Chrome(options=options,executable_path="/Users/usr/Projects/Selenium/chromedriver_mac64/chromedriver")
browser.get(url)

def get_page_count(keyword):
    base_url = "https://ca.indeed.com/jobs?q="
    end_url = "&limit=50"
    browser.get(f"{base_url}{keyword}{end_url}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", attrs={"aria-label":"pagination"})
    if pagination == None:
        return 1
    pages = pagination.select("div a")
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count
    

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    results = []
    for page in range(pages):
        base_url = "https://ca.indeed.com/jobs"
        end_url = f"{base_url}?q={keyword}&start={page*10}"
        browser.get(end_url)

        if "Error" in browser.title:
            print("An error occurred while loading the page.")
        else:
         
            soup = BeautifulSoup(browser.page_source, "html.parser")
            job_list = (soup.find("ul", class_="jobsearch-ResultsList"))
            jobs = job_list.find_all('li', recursive=False)
            for job in jobs:
                zone = job.find("div", class_="mosaic-zone")
                if zone == None:
                    anchor = job.select_one("h2 a")
                    title = anchor['aria-label']
                    link = anchor['href']
                    company = job.find("span",class_="companyName")
                    location = job.find("div",class_="companyLocation")
                    job_data = {
                        'link': f"https://ca.indeed.com/\{link}",
                        'company': company.string.replace(",", " "),
                        'location': location.string.replace(",", " "),
                        'position': title
                    }
                    results.append(job_data)
    return results


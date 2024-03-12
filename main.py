import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-back-end-programming-jobs"

response = requests.get(url)
soup = BeautifulSoup(
  response.content,
  "html.parser",
)

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
all_jobs = [] #list of ALL jobs

for job in jobs:
  title = job.find("span", class_="title").text
  company, position, region = job.find_all("span", class_="company")

  url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
  
  job_data = {
    "title": title,
    "company": company.text,
    "position": position.text,
    "region": region.text,
    "url": f"https://weworkremotely.com/{url}",
  }
  all_jobs.append(job_data) #at the end of the loop add job_data to list

print(all_jobs)

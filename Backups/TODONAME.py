from htmldiffer import diff
import requests
import time
from bs4 import BeautifulSoup

url = input("Enter a webpage to track: ")
print("You've entered", url, "as your webpage.")

request_interval = input("Enter, in seconds, the wait time between "
        "checking the page: ")
print("You've entered", request_interval, "as your wait time.")

content_html_new = ""
content_html_old = ""
num_runs = 0

while(True):
    print(num_runs)

    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content)

    content_html_new = soup.prettify()

    if content_html_old and content_html_old != content_html_new:
        dif = diff.HTMLDiffer(content_html_old, content_html_new)
        print(dif.combined_diff)

    content_html_old = content_html_new

    num_runs += 1
    time.sleep(int(request_interval))

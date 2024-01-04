# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:58:04 2024

@author: sdeer
"""

# basic
import os
from dotenv import load_dotenv

# web scraping libraries
import asyncio
import nest_asyncio
from playwright.async_api import async_playwright

# allow nested event loops
nest_asyncio.apply()

# get the environment variables
load_dotenv()
LI_USERNAME = os.getenv('LI_USERNAME')
LI_PASSWORD = os.getenv('LI_PASSWORD')

# function to scrape linkedin data
async def scrape_website(login_url, jobs_url):
    
    try:
        async with async_playwright() as p:
            # open the browser and go to the website
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto(login_url)
            print("got to log in page")
            
            # login
            await page.locator('input#session_key').fill(LI_USERNAME)
            await page.locator('input#session_password').fill(LI_PASSWORD)
            await page.get_by_role("button", name="Sign in").click()
            print("logged in")
            
            # wait for navigation after login
            await page.wait_for_load_state("networkidle")
            
            # go to the jobs page
            await page.goto(jobs_url)
            print("go to jobs page")
            
            # wait for the results to load
            await page.wait_for_selector("div.jobs-search-results-list")
            print("job page loaded")
            
            # Scrape job titles (modify the selector based on the actual structure)
            job_titles = await page.query_selector_all(".job-card-list__title")
            for title in job_titles:
                print(await title.inner_text())
            
            # close the browser
            await browser.close()
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        

async def main():
    login_url = 'https://www.linkedin.com'
    jobs_url = 'https://www.linkedin.com/jobs/search/?keywords=Data%20Analyst&location=Boston%2C%20Massachusetts%2C%20United%20States'

    await scrape_website(login_url, jobs_url)

# Running the main function without manually managing the event loop
asyncio.run(main())
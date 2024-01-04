# Job Scraper

  

## Set Up

  

1. Miniconda package manager

- Installation: https://docs.conda.io/projects/miniconda/en/latest/

  

2. Spyder IDE

- Installation:

`conda install spyder`

  

3. Playwright

- Installation:

`conda config --add channels conda-forge`

`conda config --add channels microsoft`

`conda install playwright`

`playwright install`

  

4. Clone the repository

  

5. Set up .env file

- Create .env file in the root folder with the follow variables

`LI_USERNAME = "<your linkedin username>"`

`LI_PASSWORD = "<your linkedin password>"`

6. Run the file

`python linkedin_scraper.py`
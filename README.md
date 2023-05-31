# HolidayCheck Coding Challenge

I'm very proud of the result I got, but it could have been even better. With more time - currently planning my semestre abroad - I would have loved to do more. I still hope you like it!

## About the Project

To begin with, I created initial sketches to outline the processing flow and determine which information was crucial for my project. Additionally, I made an early decision to personally design the UI because I find it visually appealing. However, it should be noted it is optimized exclusively for desktops. 

## Built With

The project was built using the following technologies:

- Python 3.10.5
- fuzzywuzzy
- pandas
- numpy
- flask
- etc. (some smaller, check out requirements.txt)

## Getting Started
### Prerequisites

To run this project, you need to have the following software installed:

- Python 3.10.5
- pip
- I used a virtual environment for this project. If you want to use it too, you can create one with `python3 -m venv VENV_NAME` and activate it with `source venv/bin/activate` once you are in the working dir.

### Installation

1. Clone the repository: git clone [repository URL]
2. Install the required packages: pip install -r requirements.txt
3. Run the app: python3 app.py

(This did it for me when I tried it on my Mac)

## Usage
### How to use
1. Open localhost:5050 in your browser
2. Select all parameters you want to search for
3. Click on "Search"
4. Wait for the results
5. Use some filters to narrow down the results
6. Click on a result to see more hotel offers

## Notes
I tried quite long to load the >100000000 offers, but my Mac wasn't able to create enough chunks and concat them. I tried to use Dask, but I didn't get it to work. So I decided to use only 100000 offers. I hope this is enough to show my skills. Also, I was trying threading, which also worked for me. Also thought about using a databse, but didn't know if this is allowed. So I decided to use pandas and numpy.

## Possible Improvements
- Would have loved to process more data, need to check out where the bottleneck is
- Doing more on the UI/UX side, e.g. adding a loading bar or a loading animation
- Adding more filters, e.g. price dates, sort by: price, rating, etc.
- Designing a mobile version
- Adding a database
- Adding a map with all hotels
- Designing a "offer detail page" with more information about the hotel and the offer
- Using all airports. I decided to just use german airports when filtering.
- Adding more tests
- Use of a CI/CD pipeline
- Adding a Dockerfile

### Hope you like it!
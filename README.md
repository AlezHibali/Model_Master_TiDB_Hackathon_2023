# Model_Master_TiDB_Hackathon_2023

![alt text](https://github.com/AlezHibali/Model_Master_TiDB_Hackathon_2023/blob/main/src/README_img/Screenshot.PNG)

## Overview

Model Master is a comprehensive collection website of AI models, catering specifically to AI engineers seeking models based on their requirements in various fields. We scrape data from Hugging Face and store the information using TiDB. The project employs Flask to construct a REST API, processing HTTP requests and interacting with the TiDB C2Q endpoint. The scraped data includes model name, size, popularity, link, task, languages, etc. The front end uses the Webflow content management system and hand-written JavaScript to display the information on a webpage.

This project is utilizing Flask framework, Hugging Face, TiDB, and Webflow.

## Dependencies

1. BeautifulSoup
2. Certifi
3. Requests
4. Flask (Waitress)
5. MySQLDB
6. TiDB
7. Webflow CMS

Check `./coding/back_end/requirements.txt` for more information.

## Installation

Clone the repository using git:

```bash
git clone https://github.com/AlezHibali/Model_Master_TiDB_Hackathon_2023.git
```

Navigate to the project directory:

```bash
cd Model_Master_TiDB_Hackathon_2023
cd coding
cd back_end
```

Install required packages in Python:

```bash
pip install -r requirements.txt
```

## Usage

**IMPORTANT: RUN THIS CODE BEFORE HEADING TO THE WEBSITE**

make sure you are in `./coding/back_end/`

Run:

```bash
python RESTapi.py
```

This code opens and listens at localhost:8080, and makes corresponding API processing.

**IMPORTANT: WEBSITE ONLY SUPPORTS RESOLUTION OF 1440PX OR MORE**

After opening the REST API, go to website https://model-master.webflow.io/


## Additional Usage

If you want to use the Scraper:

make sure you are in `./coding/back_end/data_collection/`

Run:

```bash
python soup.py
```

This script uses BeautifulSoup and requests to scrape data from Hugging Face and stores it in the TiDB.

If you want to test the website on local machine, contact us by email for more information.

## License

Model Master is [MIT Licensed](LICENSE).

## Support

For any questions or issues, please reach out to us on GitHub or email us at ali.daixin.tian@gmail.com.

## Acknowledgements

We would like to thank Hugging Face, TiDB, and Webflow for their amazing functionalities that are used in this project.

## FAQ

### 1. Resolution Problem

If you have resolution of 1440px or more but cannot correctly display the website, a possible solution might be:
Scale might make your resolution less than 1440px, try to lower the scale

![alt text](https://github.com/AlezHibali/Model_Master_TiDB_Hackathon_2023/blob/main/src/README_img/faq1.png)


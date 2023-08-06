# Model_Master_TiDB_Hackathon_2023

![alt text](https://github.com/AlezHibali/Model_Master_TiDB_Hackathon_2023/blob/main/src/README_img/Screenshot.PNG)

## V2.0 - 2023-08-06 - Hackathon Final Improvements

1. optimize keyword search
2. improve model card rendering
3. login/signup function connected to TiDB database
4. user customized favorite model list (favorite model collections)
5. revise and optimize model abstracts using Neural Network

## Overview

Model Master is a comprehensive collection website of AI models, catering specifically to AI engineers seeking models based on their requirements in various fields. We scrape data from Hugging Face and store the information using TiDB. The project employs Flask to construct a REST API, processing HTTP requests and interacting with the TiDB C2Q endpoint. The scraped data includes model name, size, popularity, link, task, languages, etc. The front end uses the Webflow content management system and hand-written JavaScript to display the information on a webpage.

This project is utilizing Flask framework, Hugging Face, TiDB, and Webflow.

**IMPORTANT: WEBSITE ONLY SUPPORTS RESOLUTION OF 1440PX OR MORE**

See FAQ#1 below if needed.

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

**If it doesn't work, try pip install every line in ./coding/back_end/requirements.txt**

Or check our FAQ#3.

## Usage

**IMPORTANT: RUN THIS CODE BEFORE HEADING TO THE WEBSITE**

make sure you are in `./coding/back_end/`

Run:

```bash
python RESTapi.py
```

This code opens and listens at localhost:8080, and makes corresponding API processing.

After opening the REST API, go to website https://model-master.webflow.io/

**IMPORTANT: USE AUTHORIZED ACCOUNT FOR FAVORITE MODEL FUNCTION**

To use Favorite Model function, please login with our authorized account:

```bash
email: ali.daixin.tian@gmail.com
password: 12345678
```

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

### 2. Certificate

Make sure you have ca certificate in your device. Run below in Python to check that:

```
import certifi
path_to_ca_cert = certifi.where()
```

### 3. Installation

If you face `ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory`, you might be facing problems of file path being too long.

Do the following:

win+R -> regedit -> HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem -> set LongPathsEnabled value to 1

### 4. Prompt Search No Response

If after clicking Prompt Search it does not jumpt to result page within 15 seconds, it might because of NETWORK FLUCTUATION! Try more times, try another prompt, or wait for few minutes would help!

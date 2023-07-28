### Model_Master_TiDB_Hackathon_2023

## Overview

Model Master is an open-source project designed to scrape data from Hugging Face and store the information using TiDB. The project employs Flask to construct a REST API, processing HTTP requests and interacting with the TiDB C2Q endpoint. The scraped data includes model name, size, popularity, link, task, languages, etc. The front end uses the Webflow content management system and hand-written JavaScript to display the information on a webpage.

This project is supported by Hugging Face, TiDB, and Webflow.

## Dependencies

1. BeautifulSoup
2. Certifi
3. Requests
4. Flask (Waitress)
5. MySQLDB
6. TiDB
7. Webflow CMS

Check ./coding/back_end/requirements.txt for more information.

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

IMPORTANT: RUN THIS CODE BEFORE HEADING TO THE WEBSITE

make sure you are in ./coding/back_end/
Run:

```bash
python RESTapi.py
```

This code.

First, run the scraper:

```bash
python scraper.py
```

This script uses BeautifulSoup and requests to scrape data from Hugging Face and stores it in the TiDB.




## API

The API server provides several endpoints to fetch data. For example:

- `GET /models`: Get a list of all models.
- `GET /models/<id>`: Get details of a specific model.

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to submit a pull request.

## License

Model Master is [MIT Licensed](LICENSE).

## Support

For any questions or issues, please reach out to us on GitHub or email us at support@example.com.

## Acknowledgements

We would like to thank Hugging Face, TiDB, and Webflow for their support in this project.

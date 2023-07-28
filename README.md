### Model_Master_TiDB_Hackathon_2023

## Overview

Model Master is an open-source project designed to scrape data from Hugging Face and store the information using TiDB. The project employs Flask to construct a REST API, processing HTTP requests and interacting with the TiDB C2Q endpoint. The scraped data includes model name, size, popularity, link, task, languages, etc. The front end uses the Webflow content management system and JavaScript to display the information on a webpage.

This project is supported by Hugging Face, TiDB, and Webflow.

## Dependencies

1. BeautifulSoup
2. Requests
3. Flask
4. TiDB
5. Webflow CMS

## Installation

Clone the repository using git:

```bash
git clone https://github.com/yourusername/model-master.git
```

Navigate to the project directory:

```bash
cd model-master
```

## Usage

First, run the scraper:

```bash
python scraper.py
```

This script uses BeautifulSoup and requests to scrape data from Hugging Face and stores it in the TiDB.

Then, run the API server:

```bash
python api.py
```

This script starts a Flask server, exposing a REST API for retrieving the data.

Finally, open `index.html` in your browser to view the data in the webpage.

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

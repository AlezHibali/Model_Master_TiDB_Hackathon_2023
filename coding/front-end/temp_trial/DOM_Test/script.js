// Function to read and parse CSV data using Fetch API
function readCSV(file, callback) {
    fetch(file)
        .then(response => response.text())
        .then(data => {
            const parsedData = parseCSV(data);
            callback(parsedData);
        })
        .catch(error => console.error('Error fetching the CSV file:', error));
}

// Function to parse CSV data into an array of objects
function parseCSV(data) {
    const lines = data.trim().split("\n");
    const headers = lines[0].split(",");
    const result = [];

    for (let i = 1; i < lines.length; i++) {
        const currentLine = lines[i].split(",");
        const item = {};

        for (let j = 0; j < headers.length; j++) {
            const key = headers[j].trim();
            const value = currentLine[j].trim();
            item[key] = value;
        }
        result.push(item);
    }
    
    return result;
}

// Function to render the item list with links to their detail pages
function renderItemList(data) {
    const itemList = document.getElementById('item-list');

    // Check if the itemList element is found in the DOM
    if (itemList) {
        data.forEach(item => {
            const itemDiv = document.createElement('div');
            itemDiv.classList.add('item');

            const itemLink = document.createElement('a');
            itemLink.href = `item${item.id}.html`; // Link to the item's detail page

            const itemName = document.createElement('h2');
            itemName.textContent = item.name;

            const itemPrice = document.createElement('p');
            itemPrice.textContent = `Price: $${parseFloat(item.price).toFixed(2)}`;

            const itemImage = document.createElement('img');
            itemImage.src = item.image;
            itemImage.alt = item.name;

            itemLink.appendChild(itemName);
            itemLink.appendChild(itemPrice);
            itemLink.appendChild(itemImage);

            itemDiv.appendChild(itemLink);
            itemList.appendChild(itemDiv);
        });
    } else {
        console.error('Element with ID "item-list" not found in the DOM.');
    }
}

// Load and render the item list when the page is loaded
window.addEventListener('load', function() {
    const csvFile = 'items.csv';
    readCSV(csvFile, renderItemList);
});

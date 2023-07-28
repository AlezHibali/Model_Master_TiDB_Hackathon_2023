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

// Function to render the item detail on the individual item's detail page
function renderItemDetail(data, itemId) {
    const itemDetail = document.getElementById('item-detail');

    // Find the item with the given itemId
    const item = data.find(item => item.id === itemId);

    if (item) {
        const itemName = document.createElement('h2');
        itemName.textContent = item.name;

        const itemPrice = document.createElement('p');
        itemPrice.textContent = `Price: $${parseFloat(item.price).toFixed(2)}`;

        const itemImage = document.createElement('img');
        itemImage.src = item.image;
        itemImage.alt = item.name;

        itemDetail.appendChild(itemName);
        itemDetail.appendChild(itemPrice);
        itemDetail.appendChild(itemImage);
    } else {
        // If the item is not found, display an error message
        const errorMessage = document.createElement('p');
        errorMessage.textContent = 'Item not found.';
        itemDetail.appendChild(errorMessage);
    }
}

// Load and render the item detail on the individual item's detail page
window.addEventListener('load', function() {
    const currentPath = window.location.pathname;
    const itemId = currentPath.split('item')[1].split('.html')[0];
    const csvFile = 'items.csv';
    readCSV(csvFile, function(parsedData) {
        renderItemDetail(parsedData, itemId);
    });
});

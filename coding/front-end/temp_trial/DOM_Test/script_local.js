// Sample item data (replace this with your data from the CSV file)
const itemData = [
    {
        id: 1,
        name: 'Item 1',
        price: '19.99',
        image: './item1.png'
    },
    {
        id: 2,
        name: 'Item 2',
        price: '29.99',
        image: './item2.png'
    },
    {
        id: 3,
        name: 'Item 3',
        price: '14.99',
        image: './item3.png'
    }
];

// Function to read and parse CSV data
function readCSV(file, callback) {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", file, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            const data = xhr.responseText;
            const parsedData = parseCSV(data);
            callback(parsedData);
        }
    };
    xhr.send(null);
}

// Function to parse CSV data into an array of objects
function parseCSV(data) {
    const lines = data.split("\n");
    const result = [];
    const headers = lines[0].split(",");
    for (let i = 1; i < lines.length; i++) {
        const obj = {};
        const currentLine = lines[i].split(",");
        for (let j = 0; j < headers.length; j++) {
            obj[headers[j]] = currentLine[j];
        }
        result.push(obj);
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
    renderItemList(itemData);
});

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
    const itemId = parseInt(currentPath.split('item')[1].split('.html')[0]);
    renderItemDetail(itemData, itemId);
});

// Function to fetch user favorites from the Flask API
async function fetchUserFavorites(username) {
    const response = await fetch(`http://localhost:8080/api/get_user_fav?username=${username}`);
    const data = await response.json();
    // console.log(data)
    return data;
}

// Function to render the cards
async function renderCards() {
    const favoritesData = await fetchUserFavorites('ali.daixin.tian@gmail.com');
    const blockContent = document.querySelector('.block-content-2');

    if (favoritesData) {
        const modelListContainer = document.createElement('div');
        modelListContainer.classList.add('model-list-container');

        favoritesData.forEach(modelName => {
            const modelCard = document.createElement('div');
            modelCard.classList.add('model-card');

            const modelTitle = document.createElement('h2');
            modelTitle.classList.add('model-title');
            modelTitle.innerText = modelName;

            // Adding event listener to make the entire card clickable
            modelCard.addEventListener('click', function() {
                const modelLink = `https://model-master.webflow.io/model/${modelName.toLowerCase()}`; // for local
                // const modelLink = `model/${modelName.toLowerCase()}`;  // for public
                window.location.href = modelLink;
            });

            modelCard.appendChild(modelTitle);
            modelListContainer.appendChild(modelCard);
        });

        blockContent.innerHTML = ''; // Clear existing content
        blockContent.appendChild(modelListContainer); // Append new content
    }
}

// Call the render function when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
    renderCards();
});
let isStarFilled = false; // Keep track of the star's filled state

async function checkInitialStarState() {
    try {
        const modelLink = window.location.href;
        const model_name = modelLink.split('/').pop(); // Extract model_name from the URL
        
        const response = await fetch(`http://localhost:8080/api/check_user_fav?model=${model_name}`);
        const data = await response.json();
        
        isStarFilled = data.message === 'True.';
        
        // Update star icon display based on initial state
        const starIcon = document.querySelector(".star-icon");
        starIcon.style.fill = isStarFilled ? "#f1c40f" : "transparent";
    } catch (error) {
        console.error('Error checking initial star state:', error);
    }
}

function toggleStar() {
    const starIcon = document.querySelector(".star-icon");
    const modelLink = window.location.href;
    const model_name = modelLink.split('/').pop(); // Extract model_name from the URL

    isStarFilled = !isStarFilled; // Toggle the filled state

    if (isStarFilled) {
        starIcon.style.fill = "#f1c40f"; // Fill the star if it's unfilled
    } else {
        starIcon.style.fill = "transparent"; // Unfill the star if it's filled
    }

    // Construct the JSON data for the POST request
    const postData = {
        username: "ali.daixin.tian@gmail.com",
        model: model_name
    };

    // Send POST request to the server
    fetch('http://localhost:8080/api/modify_user_fav', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Favorite model modified:', data);
    })
    .catch(error => {
        console.error('Error modifying favorite model:', error);
    });
}

document.addEventListener('DOMContentLoaded', function() {
    checkInitialStarState();
});
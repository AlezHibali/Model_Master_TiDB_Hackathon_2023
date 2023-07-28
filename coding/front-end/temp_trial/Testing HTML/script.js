function makeAPIRequest(input_prompt) {
    // Encode the input prompt to handle special characters and spaces
    const encodedInput = encodeURIComponent(input_prompt);

    // Replace this URL with your actual API endpoint
    const apiUrl = `http://localhost:8080/api/prompt2data?prompt=${encodedInput}`;

    const xhr = new XMLHttpRequest();
    xhr.open('GET', apiUrl, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                const jsonData = JSON.parse(xhr.responseText);

                // Access the two values returned by the Flask API
                const value1 = jsonData.value1;
                const value2 = jsonData.value2;

                // Show the values in an alert window or do whatever you need with them
                alert(`Response: ${value1}\nModel_List: ${value2}`);
            } else {
                console.error('Error:', xhr.status, xhr.statusText);
                alert(`Error: ${xhr.status}`);
            }
        }
    };

    xhr.send();
}
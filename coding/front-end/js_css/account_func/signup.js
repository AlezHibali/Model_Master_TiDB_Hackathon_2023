document.addEventListener('DOMContentLoaded', function() {
    const signupButton = document.getElementById('sign_up_button');
    const emailInput = document.getElementById('wf-sign-up-email');

    signupButton.addEventListener('click', function() {
        const email = emailInput.value;

        // Create a new XMLHttpRequest object
        const xhr = new XMLHttpRequest();

        // Define the request method, URL, and async flag
        xhr.open('POST', 'http://localhost:8080/api/add_user', true);

        // Set the request headers
        xhr.setRequestHeader('Content-Type', 'application/json');

        // Define the onload event handler
        xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 300) {
                const responseData = JSON.parse(xhr.responseText);
                console.log('User added:', responseData);
                // Handle success as needed
            } else {
                console.error('Error adding user:', xhr.statusText);
                // Handle error as needed
            }
        };

        // Define the onerror event handler
        xhr.onerror = function() {
            console.error('Request error');
            // Handle error as needed
        };

        // Create a JSON payload and send the request
        const payload = JSON.stringify({
            username: email,
            password: 'NULL'
        });
        xhr.send(payload);
    });
});
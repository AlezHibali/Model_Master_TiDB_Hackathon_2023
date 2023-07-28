const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Fetching username and password from the form
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // You can add your login logic here.
    // For demonstration purposes, let's just log the input values.
    console.log(`Username: ${username}, Password: ${password}`);
});

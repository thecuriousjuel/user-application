// Selectors
const username = document.querySelector('.username');
const password = document.querySelector('.password');
const submitButton = document.querySelector('.submit');
const statusBar = document.querySelector('.status')

// Event Listeners
submitButton.addEventListener('click', submitFunction)
username.addEventListener('focus', clearStatus)
password.addEventListener('focus', clearStatus)

// Functions
function setStatus(message) {
    statusBar.innerText = message;
}

function clearStatus() {
    statusBar.innerText = ''
}

function fetchFromURL(url, request) {
    fetch(url, request)
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
    
}
function submitFunction(event) {
    event.preventDefault();
    const usernameValue = username.value;
    const passwordValue = password.value;
    if (!usernameValue) {
        msg = 'No Username provided.';
        console.log(msg);
        setStatus(msg);
    }
    else if (!passwordValue) {
        msg = 'No Password provided.';
        console.log(msg);
        setStatus(msg);
    }
    const requestPaylond = { username: usernameValue, password: passwordValue }
    const requestPaylondInString = JSON.stringify(requestPaylond)
    request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: requestPaylondInString
    };
    const url = '/submitUserData';
    const response = fetchFromURL(url, request);
    // console.log(response);
}

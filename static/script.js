// Selectors
const username = document.querySelector('.username');
const password = document.querySelector('.password');
const submitButton = document.querySelector('.submit');
const statusBar = document.querySelector('.status');
const tableBody = document.querySelector('.table-body');

// Event Listeners
submitButton.addEventListener('click', submitFunction)
username.addEventListener('focus', clearStatus)
password.addEventListener('focus', clearStatus)
document.addEventListener('DOMContentLoaded', getAllUserDetails)

// Functions
function setStatus(message) {
    statusBar.innerText = 'Status: ' + message;
}

function clearStatus() {
    statusBar.innerText = 'Status:'
}

function fetchFromURL(url, request) {
    return fetch(url, request)
        .then(response => response.json())
        .then(data => {
            const message = data['message'];
            const payload = data['payload'];
            setStatus(message);
            return payload;  
        })
        .catch(error => {
            setStatus('Some error has occured!')
            console.log(`Error fetching data: ${error}`);
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
    fetchFromURL(url, request);
}

function getAllUserDetails(){
    const url = '/getAllUserDetails';
    const request = {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    };

    fetchFromURL(url, request)
    .then(payload =>{
        payload.forEach(arr => {
            const tableRowElement = document.createElement('tr');
            const usernameElement = document.createElement('td');
            const dateTimeElement = document.createElement('td');

            usernameElement.textContent = arr['username'];
            dateTimeElement.textContent = arr['datetime'];

            tableRowElement.appendChild(usernameElement);
            tableRowElement.appendChild(dateTimeElement);
            tableBody.appendChild(tableRowElement)
        })
    })
}

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
    /**
     * This function is used to set the status message.
     */
    statusBar.innerText = 'Status: ' + message;
}


function clearStatus() {
    /**
     * This function is used to change the status to default status message.
     */
    statusBar.innerText = 'Status: ' + 'Enter Username and Password!'
}


function fetchFromURL(url, request) {
    /**
     * This function queries and returns response from the server.
     */
    return fetch(url, request)
        .then(response => response.json())
        .then(data => {
            const message = data['message'];
            const payload = data['payload'];
            if (message) {
                setStatus(message);
            }
            else {
                clearStatus();
            }
            return payload;
        })
        .catch(error => {
            setStatus('Some error has occured!')
            // console.log(`Error fetching data: ${error}`);
        });
}


function submitFunction(event) {
    /**
     * This function is used to send data to the backend.
     */
    event.preventDefault();
    const usernameValue = username.value;
    const passwordValue = password.value;
    if (!usernameValue) {
        const msg = 'No Username provided.';
        // console.log(msg);
        setStatus(msg);
    }
    else if (!passwordValue) {
        const msg = 'No Password provided.';
        // console.log(msg);
        setStatus(msg);
    }
    else {
        const requestPayload = { username: usernameValue, password: passwordValue }
        const requestPayloadInString = JSON.stringify(requestPayload)
        const request = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: requestPayloadInString
        };
        const url = '/submitUserData';
        fetchFromURL(url, request);
    }
}


function getAllUserDetails() {
    /**
     * This function is used to fetch all the users from the backend.
     */
    const url = '/getAllUserDetails';
    const request = {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    };

    fetchFromURL(url, request)
        .then(payload => {
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

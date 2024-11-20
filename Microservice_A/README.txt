Notification Microservice

This microservice is designed to accept notifications via a REST API and display them. It listens on a local server and takes input from an HTTP request. The notification message is displayed on the server console for simplicity.

Communication Contract:

- Endpoint URL: `http://localhost:5000/send_notification`
- Method: POST
- Request Format: JSON

Request Parameters:
- notification_name: A string representing the name or content of the notification.

Example Request Call:
To request data from the microservice and send a notification, you need to make an HTTP POST request to the endpoint. Here is an example using Python's `requests` library:

import requests

url = 'http://localhost:5000/send_notification'
data = {
    'notification_name': 'Task Completed'
}

response = requests.post(url, json=data)
print(response.json())

Expected Response Format:
The microservice responds with a JSON object that includes a success message confirming that the notification has been displayed.

Example Response:
The response will look like:

{
    "message": "Notification \"Task Completed\" displayed successfully"
}

Receiving Data from the Microservice:
When you send a notification request, the microservice will provide a response as confirmation. This response includes:

- A message field that indicates the notification has been successfully displayed.

The response format is always JSON, and it includes details such as:

- message: A success message including the original notification_name.

Example Code to Receive Data:
To receive data from the microservice (confirmation response), you can use the following code to make an HTTP request and then print the response:

import requests

url = 'http://localhost:5000/send_notification'
data = {
    'notification_name': 'Task Completed'
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print('Response:', response.json())
else:
    print('Error:', response.status_code, response.json())

Important Notes:
- Port: The microservice runs on port 5000 by default.
- Dependencies: Ensure you have Flask installed to run the microservice (`pip install flask`).
- REST API: This service uses a REST API, and thus any standard HTTP client can be used to make requests.

Setup Instructions:
1. Clone the repository and navigate to the directory.
2. Install dependencies:
   pip install flask
3. Run the microservice:
   python notification_microservice.py
4. Make requests to `http://localhost:5000/send_notification` using the example code provided above.

+-------------------+             +----------------------------+
|  Client Program   |             | Notification Microservice  |
+-------------------+             +----------------------------+
           |                                   |
           |  POST /send_notification          |
           |---------------------------------->|  +--------------+
           |                                   |  | (Receives    |
           |                                   |  | request with |
           |                                   |  | notification_|
           |                                   |  | name)        |
           |                                   |  +--------------+
           |                                   |       |
           |                                   |  +--------------+
           |                                   |  | Display      |
           |                                   |  | notification |
           |                                   |  | (e.g., print |
           |                                   |  | to console)  |
           |                                   |  +--------------+
           |                                   |
           |  Response (message displayed)     |
           |<----------------------------------|  +--------------+
           |                                   |  | (Send back   |
           |                                   |  | confirmation)|
           |                                   |  +--------------+
  Confirmation of successful notification      |
 (e.g., print response message to client)      |
           |                                   |
+-------------------+             +----------------------------+



The thick activation bars (+--------------+) represent the points during which each component is actively processing the request.
The Client Program initiates the POST request.
The Notification Microservice activates its process to receive, display, and then send back the response.
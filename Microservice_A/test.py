import requests

def test_send_notification():
    url = 'http://localhost:5000/send_notification'
    data = {'notification_name': 'Task Completed'}
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('Test Passed:', response.json())
        else:
            print('Test Failed:', response.json())
    except requests.exceptions.RequestException as e:
        print('Test Failed: Could not reach the microservice')
        print(e)

if __name__ == "__main__":
    test_send_notification()

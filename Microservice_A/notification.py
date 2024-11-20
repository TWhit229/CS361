from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive notification name and display it
@app.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    notification_name = data.get('notification_name')
    if not notification_name:
        return jsonify({'error': 'Missing notification name'}), 400

    # Display the notification (for simplicity, just print it)
    print(f'Notification received: {notification_name}')
    
    return jsonify({'message': f'Notification "{notification_name}" displayed successfully'}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)

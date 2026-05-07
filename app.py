from flask import Flask, render_template, request, Response
import os

app = Flask(__name__)

USER_DATA = {
    "admin": "SecurePass123"
}

@app.route('/')
def index():
    auth = request.authorization

    if not auth or not (
        auth.username in USER_DATA and USER_DATA[auth.username] == auth.password
    ):
        return Response(
            "Unauthorized Access: Please login.",
            401,
            {"WWW-Authenticate": 'Basic realm="Login Required"'}
        )

    return render_template('dashboard.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

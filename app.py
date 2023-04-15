from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome to Medellin Dubai Style Hotel</h1>"

@app.route("/contact")
def contact():
    return "<h2>Contact us:</h2><p>Name: <br> Phone: <br> Email: </p>"

@app.route("/reservations")
def reservations():
    return "<h2>Reservations:</h2><p>Please enter your arrival and departure dates:</p><form><label for='arrival_date'>Arrival date:</label><input type='date' name='arrival_date'><br><label for='departure_date'>Departure date:</label><input type='date' name='departure_date'><br><input type='submit' value='Submit'></form>"

@app.route("/services")
def services():
    return "<h2>Services:</h2><ul><li>Swimming pool</li><li>Gym</li><li>Restaurant</li></ul>"

if __name__ == "__main__":
    app.run(debug=True)

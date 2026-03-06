

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import contact_book

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/view-contacts")
def view_contacts():
    contacts = contact_book.load_contacts()

    return  jsonify(contacts)


@app.route("/add-contacts", methods=["POST"])
def add_contacts():
    data = request.get_json()

    contacts = contact_book.load_contacts()
    contacts = contact_book.add_contact(contacts, data["name"], data["phone_number"], data["email"], data["address"])

    contact_book.save_contacts(contacts)

    return jsonify(contacts)

@app.route("/remove-contact", methods=["POST"])
def remove_contact():
    data = request.get_json()

    contacts = contact_book.load_contacts()
    contacts = contact_book.remove_contact(contacts, data["remove_contact"])

    contact_book.save_contacts(contacts)

    return jsonify(contacts)


@app.route("/edit-contact", methods=["POST"])
def edit_contact():
    data = request.get_json()

    contacts = contact_book.load_contacts()
    contacts = contact_book.edit_contact(contacts, data["contactName"], data["newContact"])

    contact_book.save_contacts(contacts)

    return jsonify(contacts)

@app.route("/search-contact")
def search_contact():

    search = request.args.get("search")

    contacts = contact_book.load_contacts()
    filtered_contact = contact_book.search_contact(contacts, search)
    
    return jsonify(filtered_contact)

if __name__ == "__main__":
    app.run(debug=True)


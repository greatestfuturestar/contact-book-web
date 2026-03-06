
document.getElementById("add-contact-form").addEventListener("submit", function(event) {
    event.preventDefault();
    addContact();
});

function addContact() {
    const name = document.getElementById("contact-name").value;
    const phone_number = document.getElementById("contact-number").value;
    const email = document.getElementById("contact-email").value;
    const address = document.getElementById("contact-address").value;

    fetch("/add-contacts", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({name, email, phone_number, address})
    })
    .then(response => response.json())
    .then(data => {
        console.log("Contact added:", data);
        loadContacts();
    });
}

function loadContacts() {
    fetch("/view-contacts")
    .then(response => response.json())
    .then(data => {
        displayTasks(data);
    });
}

function displayTasks(data) {
    const ContactsList = document.getElementById("contact-list");
    ContactsList.innerHTML = "";
    
    data.forEach(Contact => {
        const taskDiv = document.createElement("div");
        taskDiv.innerHTML = `
            <p><strong>${Contact.name}</strong> - ${Contact.phone_number} (${Contact.email}) ${Contact.address}</p>
            <button onclick="removeContact('${Contact.name}')">Remove</button>
        `;
        ContactsList.appendChild(taskDiv);
    });
}

function removeContact(userS_remove) {
    fetch("/remove-contact", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({remove_contact: userS_remove})
    })
    .then(response => response.json())
    .then(data => {
        console.log("Task removed:", data);
        loadContacts();
    });
}


function filter() {
    const category = document.getElementById("filter-category").value;
    fetch(`/view-by-category?category=${category}`)
    .then(response => response.json())
    .then(data => {
        displayTasks(data);
    });
}



function editContact() {
    const contactName = document.getElementById("edit-contact").value;
    const newContact = document.getElementById("user-edit").value;

    fetch("/edit-contact", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({contactName: contactName, newContact: newContact})
    })
    .then(response => response.json())
    .then(data => {
        console.log("Contact updated:", data);
        loadContacts();
    });
}

function searchContact() {
    const contactName = document.getElementById("filter-contact").value;

    fetch("/search-contact?search=" + contactName)
    .then(response => response.json())
    .then(data => {
        console.log("Contact updated:", data);
        loadContacts();
    });
}

loadContacts();
# Import libraries
from flask import Flask, redirect, request, render_template, url_for
# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: List all transactions


@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation: Display add transaction form
# Route to handle the creation of a new transaction


@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a new transaction object using form field values
        transaction = {
            # Generate a new ID based on the current length of the transactions list
            'id': len(transactions) + 1,
            # Get the 'date' field value from the form
            'date': request.form['date'],
            # Get the 'amount' field value from the form and convert it to a float
            'amount': float(request.form['amount'])
        }
        # Append the new transaction to the transactions list
        transactions.append(transaction)

        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))

    # If the request method is GET, render the form template to display the add transaction form
    return render_template("form.html")

# Update operation: Display edit transaction form
# Route to handle the editing of an existing transaction


@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Extract the updated values from the form fields
        # Get the 'date' field value from the form
        date = request.form['date']
        # Get the 'amount' field value from the form and convert it to a float
        amount = float(request.form['amount'])

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                # Update the 'date' field of the transaction
                transaction['date'] = date
                # Update the 'amount' field of the transaction
                transaction['amount'] = amount
                break                            # Exit the loop once the transaction is found and updated

        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))

    # If the request method is GET, find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)

    # If the transaction with the specified ID is not found, handle this case (optional)
    return {"message": "Transaction not found"}, 404

# Delete operation: Delete a transaction
# Route to handle the deletion of an existing transaction


@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Remove the transaction from the transactions list
            transactions.remove(transaction)
            break  # Exit the loop once the transaction is found and removed

    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))

# Search operation: Search transactions by amount range


@app.route("/search", methods=["GET", "POST"])
def search_transactions():
    if request.method == 'POST':
        # Retrieve min and max amount values from form data
        min_amount = float(request.form['min_amount'])
        max_amount = float(request.form['max_amount'])

        # Filter transactions based on the amount range
        filtered_transactions = [
            t for t in transactions if min_amount <= t['amount'] <= max_amount]

        # Pass filtered transactions to the template
        return render_template("transactions.html", transactions=filtered_transactions)

    # If GET request, render the search form
    return render_template("search.html")

# New function to calculate and display total balance


@app.route("/balance")
def total_balance():
    # Calculate the total balance by summing all transaction amounts
    balance = sum(transaction['amount'] for transaction in transactions)
    # Return the balance as a formatted string
    # return f"Total Balance: {balance}"
    return render_template("transactions.html", transactions=transactions, total_balance=balance)


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

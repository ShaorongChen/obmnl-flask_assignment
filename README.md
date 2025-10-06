# 📊 Financial Transaction Manager

Welcome to the **Financial Transaction Manager** - a simple Flask-based web application for managing financial transactions.

## 🧩 Features

- ✅ **List Transactions**: View all your financial transactions.
- ➕ **Add Transactions**: Add new income or expense entries.
- ✏️ **Edit Transactions**: Modify existing transaction details.
- ❌ **Delete Transactions**: Remove unwanted transactions.
- 🔍 **Search Transactions**: Filter transactions by amount range.
- 💰 **Balance Calculation**: See your total financial balance.

## 📁 Project Structure

```
.
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   ├── transactions.html  # Displays transactions
│   ├── form.html       # Add transaction form
│   ├── edit.html       # Edit transaction form
│   └── search.html     # Search transactions form
└── README.md           # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13.x
- Flask

### Installation

1. Clone or download this repository.
2. Install Flask:
   ```bash
   pip install Flask
   ```

### Running the Application

Run the application using:
```bash
python app.py
```
Then navigate to `http://127.0.0.1:5000` in your browser.

## 🛠️ How It Works

- **GET /** - Lists all transactions.
- **GET /add** - Displays the add transaction form.
- **POST /add** - Adds a new transaction.
- **GET /edit/<id>** - Displays the edit transaction form.
- **POST /edit/<id>** - Updates an existing transaction.
- **GET /delete/<id>** - Deletes a transaction.
- **GET /search** - Displays the search form.
- **POST /search** - Filters transactions by amount range.
- **GET /balance** - Shows total balance.

## 📝 Notes

- All data is stored in memory (not persistent).
- The application uses Flask's built-in development server.
- For production use, consider using a database and a proper WSGI server.

## 🧪 Testing

You can test the application by:
1. Adding new transactions.
2. Editing existing ones.
3. Deleting transactions.
4. Searching for specific amounts.
5. Checking the balance calculation.

## 🙏 Acknowledgements

- Built with [Flask](https://flask.palletsprojects.com/)
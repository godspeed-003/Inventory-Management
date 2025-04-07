# Inventory Management System

This project is a Django-based web application for managing an inventory of products. It allows users to add, update, delete, and view products in a user-friendly interface.

## Features

- Add new products to the inventory
- Update existing product details
- Delete products from the inventory
- View a list of all products
- View detailed information about each product

## Technologies Used

- Django
- Python
- HTML/CSS
- Bootstrap (for styling)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd inventory_project
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required packages:
   ```
   pip install django
   ```

6. Run database migrations:
   ```
   python manage.py migrate
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

8. Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## Usage

- Navigate through the application using the provided links to manage your inventory.
- Use the forms to add or edit products, and confirm deletions when prompted.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
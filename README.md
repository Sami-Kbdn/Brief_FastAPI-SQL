# Brief_FastAPI-SQL
# Cyclist Performance Tracker

This project is a FastAPI-based web application for tracking cyclist performances, using SQLite for data storage and Streamlit for the frontend.

## Features
- RESTful API with FastAPI
- SQLite database for storing cyclist data
- Streamlit frontend for easy data visualization
- User authentication and performance tracking

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository:

   git clone git@github.com:Sami-Kbdn/Brief_FastAPI-SQL.git
   cd cyclist-performance-tracker
   
2. Create a virtual environment and activate it:

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. Install dependencies:

   pip install -r requirements.txt
   

## Usage

### Running the FastAPI Backend

uvicorn main:app --reload

The API will be available at `http://127.0.0.1:8000`.

### Running the Streamlit Frontend
streamlit run app.py

The frontend will be available at `http://localhost:8501`.

## API Endpoints
- `GET /cyclists/` - Retrieve all cyclists
- `POST /cyclists/` - Add a new cyclist
- `GET /cyclists/{id}` - Get a specific cyclist's details
- `PUT /cyclists/{id}` - Update a cyclist's details
- `DELETE /cyclists/{id}` - Remove a cyclist

## Database
This project uses SQLite. The database file (`cyclists.db`) will be created automatically when running the application.

## Contributing
1. Fork the repository
2. Create a new branch (`feature-branch`)
3. Commit changes
4. P to the branch
5. Open a Pull Request

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, feel free to reach out via email or open an issue in the repository.



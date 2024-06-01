# Movie Catalog

A Django-based web application to manage and view a catalog of movies. Users can search for movies, view details, and add movies to their favorites list.

## Features

- User authentication (login, register, logout)
- Movie search functionality( for now title only) 
- View movie details
- Add/remove movies to/from favorites
- Admin can add new movies

## Technologies Used

- Django
- Bootstrap 4
- SQLite (default Django database)
- jQuery

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/movie-catalog.git
    cd movie-catalog
    ```

2. **Create and activate a virtual environment:**

    ```bash
    pipenv shell  # On Windows use `venv\Scripts\activate`
    ```


4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server:**

    ```bash
    python manage.py runserver
    ```

7. **Open your browser and navigate to:**

    ```plaintext
    http://127.0.0.1:8000/
    ```

## Usage

### Adding Movies

- Log in as the superuser.
- Navigate to `/create_movie` to add a new movie.

### Searching Movies

- Use the search bar on the home page to search for movies by title.

### Viewing Movie Details

- Click on a movie's title or image to view its details.

### Adding to Favorites

- On the movie detail page, click the "Add to Favorites" button to add the movie to your favorites list.

### Viewing Favorites

- Navigate to `/favorite_list` to view your favorite movies (you must be logged in).

## Project Structure

- **`movie_catalog/`**: Main Django project folder
- **`movies/`**: Django app for managing movies
- **`templates/`**: HTML templates
- **`static/`**: Static files (CSS, JavaScript, images)

## Routes

- `/`: Home page, displays all movies
- `/movie/<id>`: Movie detail page
- `/movie/<id>/add_to_favorite`: Add movie to favorites
- `/favorite_list`: View favorite movies
- `/create_movie`: Add a new movie (admin only)
- `/login`: Log in
- `/logout`: Log out
- `/register`: Register

## Enhancements and Future Improvements

- **Class-Based Views:** Consider refactoring function-based views to class-based views for better organization and scalability.
- **Template Inheritance:** Implement template inheritance to avoid code duplication, especially for the navbar. Create a base HTML template with the navbar and extend it in other templates.
- **Separation of Concerns:** Move CSS styles from HTML files to separate CSS files for better maintainability and readability.
- **Improved URL Structure:** Use Django Rest Framework (DRF) for a more organized and RESTful URL structure. Implementing class-based views with DRF can lead to cleaner and more maintainable code.
- **Third-Party Sign-in/Login:** Integrate third-party authentication services (e.g., Google, Facebook, etc.) to provide users with more options for signing in.
- **Enhanced Features:** Explore additional features such as user profiles, ratings/reviews, recommendations, and more to enhance the functionality and user experience of the application.

These enhancements will not only improve the overall quality and efficiency of the application but also provide a better experience for users and developers alike.

I made very basic app. 
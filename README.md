Here’s an updated README for your Django Instagram Clone project, using Django templates for the frontend:

---

# Instagram Clone

This project is a simple **Instagram clone** built with Django, designed to mimic the core features of Instagram, including posting images, viewing stories, liking and commenting on posts, and following other users.

## Features

- **User Authentication**: Users can register, log in, and log out securely.
- **Profile Management**: Each user has a profile with an avatar and bio.
- **Posts**: Users can upload images, with a maximum of 10 images per post.
- **Stories**: Users can add temporary stories that are available for 24 hours.
- **Likes and Comments**: Users can like and comment on each other's posts.
- **Follow System**: Users can follow and unfollow each other.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: Django Templates, HTML, CSS, JavaScript (optional for interactivity)
- **Database**: SQLite (default for Django) or PostgreSQL (recommended for production)
- **Other**: Pillow (for image handling)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/instagram-clone.git
    cd instagram-clone
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    - Apply migrations:
      ```bash
      python manage.py migrate
      ```

    - Create a superuser:
      ```bash
      python manage.py createsuperuser
      ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    - Open [http://localhost:8000](http://localhost:8000) in your browser.

## Usage

1. **Register**: Create a new user account.
2. **Set Up Profile**: Customize your profile with an avatar and bio.
3. **Create a Post**: Upload images (max 10) and create a new post.
4. **View and Add Stories**: Share stories that will disappear after 24 hours.
5. **Like and Comment**: Engage with posts by liking and leaving comments.
6. **Follow Users**: Follow other users to see their posts and stories.

## Project Structure

- **templates/**: HTML templates for rendering pages with Django's template system.
  - **base.html**: Main template with navigation.
  - **post_list.html**: Shows the feed of posts.
  - **profile.html**: User profile page.
  - **story.html**: Page for viewing stories.
- **static/**: CSS, JavaScript, and images.
- **accounts/**: User authentication and profile management.
- **posts/**: Core functionality for posts, including images, comments, and likes.
- **stories/**: Temporary story functionality.
- **follows/**: Follow system to connect users.
- **media/**: Directory where uploaded images are stored.


This README provides a good overview, and you can adjust details or add more specific sections depending on your app's needs.

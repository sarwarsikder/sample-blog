# Blog Application

This Django-based blog application allows users to create and manage posts with text content, videos, and images. The application utilizes a virtual environment, SQLite database, Bootstrap for styling, and the Jazzmin admin template for a clean and intuitive admin interface.

## Features

- **Posts:** Create, edit, and delete blog posts with a title, author, content, and optional video attachments.
- **Images:** Attach multiple images to each post to enhance the visual appeal.
- **Video Validation:** Ensure video files adhere to specific requirements, such as supported formats and a maximum size of 250 MB.
- **Admin Interface:** Utilize the Jazzmin admin template for an efficient and aesthetically pleasing admin dashboard.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blog-app.git
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Access the admin interface at `http://localhost:8000/admin/` and log in with the superuser credentials.

## Usage

- Visit `http://localhost:8000` to explore the blog application.
- Use the admin interface to manage posts, images, and other content.

## Models

### Post

- **Fields:**
  - `title`: CharField (max_length=200)
  - `author`: CharField (max_length=100)
  - `updated_on`: DateTimeField (auto_now=True)
  - `content`: TextField
  - `created_on`: DateTimeField (auto_now_add=True)
  - `video`: FileField
    - Allowed Extensions: mp4, avi, mov, mkv
    - Max Size: 250 MB

- **Methods:**
  - `__str__`: Returns the title of the post.

### Image

- **Fields:**
  - `post`: ForeignKey (to Post, on_delete=models.CASCADE)
  - `image`: ImageField

- **Methods:**
  - `__str__`: Returns a string representation of the image.

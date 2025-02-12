## Blog Project

A fully functional blog application built with **Django** and **Bootstrap**. This project allows users to create, edit, and delete blog posts while ensuring a user-friendly experience with responsive design and toast notifications.

---

## Features

### 📝 Blog Management
- Users can **create**, **edit**, and **delete** blog posts.
- Blog posts display with **title, author and date**.
- Full post details can be viewed by clicking **"Read More"**.

### 🔐 User Authentication
- **Signup**: New users can create an account.
- **Login/Logout**: Secure authentication with session-based login.
- **User Welcome Message**: Displays the logged-in username in the navigation bar.

### 🎨 UI/UX Enhancements
- **Bootstrap 5** for a fully responsive and modern interface.
- **Pagination**: Posts are displayed in a paginated format to improve user experience.
- **Tooltips**: If a post excerpt exceeds 10 words, a tooltip displays the full content.

### 📢 Toast Notifications
The application uses **toast messages** for improved user feedback:
- ✅ **Post Created Successfully**
- 🗑️ **Post Deleted Successfully**
- 🚪 **User Logged Out Successfully**

---

## 📂 Installation Guide

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/rushikeshghule/BlogProjectCrud.git
```

### 2️⃣ Create and Activate Virtual Environment
```sh
python3 -m venv blog_env
blog_env\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations
```sh
python manage.py migrate
```

### 5️⃣ Create a Superuser (Admin Access)
```sh
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```sh
python manage.py runserver
```

### 7️⃣ Open in Browser
```
http://127.0.0.1:8000/
```

---

## 🔧 Usage Instructions

### Creating a Blog Post
1. Log in to your account.
2. Click **"Create New Post"** at the top of the home page.
3. Fill in the post title and body.
4. Click **"Save"** to publish the post.
5. A **toast message** will confirm the post has been saved.

### Editing a Blog Post
1. Open the post you want to edit.
2. Click **"Edit"** and modify the content.
3. Click **"Save"** to update the post.

### Deleting a Blog Post
1. Open the post you want to delete.
2. Click **"Delete"**.
3. A **confirmation alert** will appear before deletion.

---

## 🚀 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Django** | Backend and frontend Developement |
| **SQLite** | Default database for storing posts and user data |
| **Bootstrap 5** | Styling and responsive design |
| **JavaScript** | Used for toast notifications and interactivity |

---



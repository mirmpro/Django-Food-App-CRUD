# Django Food App (CRUD)

A full-stack food menu management web application built with **Django** and styled using **Tailwind CSS**. Designed as a hands-on project to master Django's core CRUD (Create, Read, Update, Delete) workflows, MVT architecture, and utility-first frontend styling.

---

## 🚀 Features

- **Full CRUD Functionality:** Create, view, update, and delete food items seamlessly.
- **Modern Responsive UI:** Clean, responsive design powered by Tailwind CSS.
- **Image Fallback Support:** Dynamic image display with automatic default fallback URLs.
- **Django Admin Integration:** Pre-configured admin dashboard for direct database records management.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** Django Templates, Tailwind CSS, HTML5
- **Database:** SQLite

---

## 📦 Model Structure

```python
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    items_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500, 
        default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStPC76lP66TQBd8ed7bBW2U6PQONb1q8Sruccq7zcBUHg2rU7iMMPhJGc&s=10'
    )

    def __str__(self):
        return self.item_name
```

---

## ⚡ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/django-food-app.git
cd django-food-app
```

### 2. Set up virtual environment
```bash
python -m venv env
# On Linux/macOS:
source env/bin/activate
# On Windows:
env\Scripts\activate
```

### 3. Install requirements & run migrations
```bash
pip install django
python manage.py makemigrations
python manage.py migrate
```

### 4. Create superuser (Optional)
```bash
python manage.py createsuperuser
```

### 5. Run development server
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

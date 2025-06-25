# ZhenCMS - Modern Cloud Storage & File Management System

![ZhenCMS Logo](frontend/assets/images/logo.png)

**ZhenCMS** is a modern, full-stack cloud storage and content management system designed for seamless file management, secure sharing, and lightning-fast access to your digital world. Built with Django REST Framework and Nuxt.js, it provides a robust and scalable solution for personal and enterprise file storage needs.

## 🌟 Features

### Core Functionality
- **📁 Hierarchical Folder Management** - Organize files in nested folder structures
- **⚡ Lightning Upload** - Drag, drop, and upload files with progress tracking
- **🔗 Smart Sharing** - Granular sharing controls with shareable links
- **🔒 Fort Knox Security** - Secure file storage with access controls
- **📱 Responsive Design** - Beautiful, modern UI that works on all devices
- **🎯 RESTful API** - Complete API for integration with external applications

### Technical Features
- **UUID-based File Naming** - Prevents filename conflicts and enhances security
- **Content Type Detection** - Automatic MIME type detection and handling
- **File Size Management** - Configurable upload limits and size tracking
- **Media Organization** - Automatic folder-based file organization
- **CORS Configuration** - Ready for cross-origin requests
- **SQLite Database** - Lightweight, embedded database for development

## 🏗️ Architecture

### Backend (Django)
- **Django 5.2.3** - Modern Python web framework
- **Django REST Framework** - Powerful API development
- **Django CORS Headers** - Cross-origin resource sharing
- **SQLite Database** - Embedded database for simplicity
- **UUID File Management** - Secure file naming system

### Frontend (Nuxt.js)
- **Nuxt.js 3** - Vue-based full-stack framework
- **Vue 3** - Progressive JavaScript framework
- **Tailwind CSS 4** - Utility-first CSS framework
- **TypeScript** - Type-safe JavaScript development

## 📋 Prerequisites

Before setting up ZhenCMS, ensure you have the following installed:

- **Python 3.12+** - Backend runtime
- **Node.js 18+** - Frontend runtime and package management
- **npm** or **yarn** - Package manager for frontend dependencies
- **Poetry** (optional) - Python dependency management

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/AntoDono/ZhenCMS.git
cd ZhenCMS
```

### 2. Backend Setup (Django)

#### Using Poetry (Recommended)

```bash
# Navigate to the backend directory
cd cms

# Install Poetry if you haven't already
pip install poetry

# Install dependencies
poetry install

# Activate the virtual environment
poetry shell

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

#### Using pip

```bash
# Navigate to the backend directory
cd cms

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install django djangorestframework django-cors-headers

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

The Django backend will be available at `http://localhost:8000`

### 3. Frontend Setup (Nuxt.js)

Open a new terminal window/tab:

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

The Nuxt.js frontend will be available at `http://localhost:3000`

## 🔧 Configuration

### Backend Configuration

The Django backend configuration can be found in `cms/cms/settings.py`. Key configurations include:

#### Database Settings
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### File Upload Settings
```python
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
FILE_UPLOAD_PERMISSIONS = 0o644
```

#### CORS Settings
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Nuxt.js dev server
    "http://127.0.0.1:3000",
    "https://cms.antodono.com",  # Production domain
]
```

### Frontend Configuration

The Nuxt.js configuration is in `frontend/nuxt.config.ts`:

```typescript
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE
    }
  },
  css: ['~/assets/css/main.css'],
  // Tailwind CSS integration
  vite: {
    plugins: [tailwindcss()]
  }
})
```

## 📊 Database Schema

### Models

#### Folder Model
```python
class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    root = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
```

#### File Model
```python
class File(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid4, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    size_in_bytes = models.BigIntegerField(default=0)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=file_upload_path)
    content_type = models.CharField(max_length=255)
    shareable = models.BooleanField(default=False)
```

## 🔌 API Endpoints

### File Management
- `GET /api/files/` - List all files
- `POST /api/files/` - Upload a new file
- `GET /api/files/{id}/` - Get file details
- `PUT /api/files/{id}/` - Update file information
- `DELETE /api/files/{id}/` - Delete a file

### Folder Management
- `GET /api/folders/` - List all folders
- `POST /api/folders/` - Create a new folder
- `GET /api/folders/{id}/` - Get folder details
- `PUT /api/folders/{id}/` - Update folder information
- `DELETE /api/folders/{id}/` - Delete a folder

## 🎨 UI/UX Features

### Modern Design Elements
- **Gradient Backgrounds** - Beautiful blue-to-sky gradient themes
- **Animated Components** - Smooth animations and transitions
- **Responsive Layout** - Mobile-first design approach
- **Interactive Elements** - Hover effects and micro-interactions
- **Loading States** - Elegant loading indicators
- **Error Handling** - User-friendly error messages

### Accessibility
- **Semantic HTML** - Proper HTML structure for screen readers
- **Keyboard Navigation** - Full keyboard accessibility
- **Color Contrast** - WCAG compliant color schemes
- **Focus Management** - Clear focus indicators

## 🔒 Security Features

- **UUID File Naming** - Prevents file enumeration attacks
- **Content Type Validation** - Ensures uploaded files are safe
- **File Size Limits** - Prevents abuse and storage overflow
- **CORS Protection** - Controlled cross-origin access
- **CSRF Protection** - Django's built-in CSRF protection
- **Shareable Controls** - Granular file sharing permissions

## 🚀 Production Deployment

### Backend (Django)

1. **Environment Variables**
```bash
export DJANGO_SECRET_KEY="your-secret-key"
export DJANGO_DEBUG="False"
export DJANGO_ALLOWED_HOSTS="your-domain.com"
```

2. **Database Migration**
```bash
python manage.py collectstatic
python manage.py migrate
```

3. **WSGI Deployment**
Use Gunicorn or uWSGI with a reverse proxy (Nginx)

### Frontend (Nuxt.js)

1. **Build for Production**
```bash
npm run build
```

2. **Generate Static Site**
```bash
npm run generate
```

3. **Deploy**
Deploy the generated files to any static hosting service or use server-side rendering.

## 🧪 Development

### Running Tests

#### Backend Tests
```bash
cd cms
python manage.py test
```

#### Frontend Tests
```bash
cd frontend
npm run test
```

### Code Style

#### Python (Backend)
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes

#### JavaScript/TypeScript (Frontend)
- Follow ESLint configuration
- Use TypeScript for type safety
- Follow Vue.js style guide

## 📁 Project Structure

```
ZhenCMS/
├── cms/                          # Django Backend
│   ├── cms/                      # Django Project Settings
│   │   ├── __init__.py
│   │   ├── settings.py           # Main configuration
│   │   ├── urls.py               # URL routing
│   │   └── wsgi.py               # WSGI configuration
│   ├── file/                     # File Management App
│   │   ├── models.py             # File model
│   │   ├── views.py              # API views
│   │   ├── serializers.py        # DRF serializers
│   │   └── urls.py               # App URLs
│   ├── folder/                   # Folder Management App
│   │   ├── models.py             # Folder model
│   │   └── views.py              # API views
│   ├── media/                    # Uploaded files storage
│   ├── manage.py                 # Django management script
│   └── pyproject.toml            # Python dependencies
├── frontend/                     # Nuxt.js Frontend
│   ├── assets/                   # Static assets
│   │   ├── css/                  # Stylesheets
│   │   └── images/               # Images
│   ├── pages/                    # Vue pages/routes
│   │   ├── index.vue             # Homepage
│   │   └── view.vue              # File viewer
│   ├── package.json              # Node.js dependencies
│   ├── nuxt.config.ts            # Nuxt configuration
│   └── tsconfig.json             # TypeScript configuration
└── README.md                     # This file
```

## 🤝 Contributing

We welcome contributions to ZhenCMS! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Write clear, documented code
- Add tests for new features
- Follow the existing code style
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Youwei Zhen (Anthony)**
- GitHub: [@AntoDono](https://github.com/AntoDono)
- Website: [youweizhen.com](https://youweizhen.com)
- Email: anthony20151128@gmail.com

## 🙏 Acknowledgments

- **Django** - The web framework for perfectionists with deadlines
- **Nuxt.js** - The intuitive Vue framework
- **Tailwind CSS** - A utility-first CSS framework
- **Vue.js** - The progressive JavaScript framework

## 📞 Support

If you encounter any issues or have questions:

1. **Check the Documentation** - Review this README and code comments
2. **Search Issues** - Look through existing GitHub issues
3. **Create an Issue** - Open a new issue with detailed information
4. **Contact** - Reach out via email or GitHub

---

**ZhenCMS** - Experience the future of cloud storage with seamless file management, secure sharing, and lightning-fast access to your digital world.

Built with ❤️ by [Youwei Zhen](https://youweizhen.com)

# NutriTrack - Social Media for Food Enthusiasts

A Django-based social media platform where users can share food photos, follow other food enthusiasts, and discover delicious recipes and meals.

## Features

- 🔐 User Authentication (Sign up, Sign in, Logout)
- 📸 Photo Upload with Captions
- ❤️ Like Posts
- 👥 Follow/Unfollow Users
- 🔍 Search Users
- 👤 User Profiles with Bio and Location
- 📱 Responsive Design
- 🎨 Modern UI with Tailwind CSS

## Demo Accounts

### Admin Account
- **Username:** `admin`
- **Password:** `admin123`
- **Access:** Full admin panel access

### Regular User Account
- **Username:** `mazen`
- **Password:** `mazen123`
- **Access:** Standard user features

## Deployment on Render

### Prerequisites
- GitHub repository with your code
- Render account

### Deployment Steps

1. **Connect to GitHub**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

2. **Configure Build Settings**
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn social_network.wsgi:application`
   - **Python Version:** 3.9.13

3. **Environment Variables**
   - `DEBUG`: `False` (for production)
   - `SECRET_KEY`: Generate a new secret key for production
   - `DATABASE_URL`: Will be provided by Render (PostgreSQL)

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd NutriTrack
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open http://127.0.0.1:8000 in your browser

## Project Structure

```
NutriTrack/
├── core/                    # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL patterns
│   └── migrations/         # Database migrations
├── social_network/         # Django project settings
│   ├── settings.py         # Configuration
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py             # WSGI configuration
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, images)
├── media/                  # User-uploaded files
├── requirements.txt        # Python dependencies
├── Procfile               # Deployment configuration
├── build.sh               # Build script for deployment
└── runtime.txt            # Python version specification
```

## Technologies Used

- **Backend:** Django 4.2.24
- **Database:** SQLite (development) / PostgreSQL (production)
- **Frontend:** HTML, CSS, JavaScript, Tailwind CSS
- **Deployment:** Render, Gunicorn, WhiteNoise
- **File Storage:** Local storage (development) / Render storage (production)

## Key Features Implementation

### User Authentication
- Custom signup/signin forms
- Password validation
- Session management
- Login required decorators

### Social Features
- Post creation with image upload
- Like/unlike functionality
- Follow/unfollow system
- User search
- Profile management

### File Handling
- Image upload for posts and profiles
- Media file serving
- Static file management

## Database Models

- **User:** Django's built-in user model
- **Profile:** Extended user information (bio, location, profile image)
- **Post:** User posts with images and captions
- **LikePost:** Post likes tracking
- **FollowersCount:** User following relationships

## Security Features

- CSRF protection
- User authentication
- File upload validation
- SQL injection protection
- XSS protection

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support or questions, please open an issue in the GitHub repository.

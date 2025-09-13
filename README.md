# StudentsPoint

A comprehensive Progressive Web Application (PWA) designed for the global student community. StudentsPoint provides an integrated ecosystem of tools and services to enhance the academic and professional experience of students worldwide.

## Overview

StudentsPoint is an open-source platform that combines multiple student-focused applications into a single, cohesive experience. Built with Django and modern web technologies, it offers a range of features from academic tools to professional development resources.

## Target Audience

- **Students**: Primary users seeking academic and professional development tools
- **Educational Institutions**: Organizations looking to provide comprehensive student services
- **Developers**: Contributors interested in educational technology and PWA development
- **Educators**: Teachers and administrators who want to enhance student engagement

## Key Features

### Authentication System
- Traditional email/password authentication
- Google OAuth integration for seamless login
- Flexible email validation supporting multiple domains
- JWT-based secure token management

### Core Applications

#### Academic Tools
- **Forums**: Discussion boards with automated moderation
- **Schedules**: Class schedule management with PDF import capabilities
- **Polls**: Voting and survey system for student feedback
- **Teachers Directory**: Faculty information and contact details

#### Professional Development
- **Portfolio**: Professional profile management with PDF generation
- **Courses (OTEC)**: Open course sharing platform
- **Marketplace**: Product sharing via external links (Facebook Marketplace, MercadoLibre)

#### Student Services
- **Wellbeing**: Health and wellness resources
- **Reports**: Infrastructure and facility reporting system
- **Notifications**: Push notification system for important updates
- **Virtual Tours**: Custom street view implementation

### Technical Features
- **Progressive Web App**: Offline functionality and app-like experience
- **Responsive Design**: Mobile-first approach with Bootstrap 5
- **RESTful API**: Comprehensive API with Swagger documentation
- **Real-time Notifications**: Web push notification support
- **PDF Generation**: Professional document creation using ReportLab

## Technology Stack

### Backend
- **Django 5.0+**: Web framework
- **Django REST Framework**: API development
- **PostgreSQL/SQLite**: Database management
- **Celery + Redis**: Asynchronous task processing
- **ReportLab**: PDF generation
- **Google OAuth**: Authentication integration

### Frontend
- **HTML5/CSS3/JavaScript**: Core web technologies
- **Bootstrap 5**: UI framework
- **Font Awesome**: Icon library
- **Service Workers**: PWA functionality

### Development Tools
- **pytest**: Testing framework
- **Docker**: Containerization support
- **Git**: Version control

## Installation

### Prerequisites
- Python 3.11 or higher
- PostgreSQL (optional, SQLite used by default)
- Git

### Quick Start

1. **Clone the repository**
```bash
git clone <repository-url>
cd students-point
```

2. **Run the development script**
```bash
# Windows
iniciar_desarrollo.bat

# Linux/Mac
chmod +x iniciar_desarrollo.sh
./iniciar_desarrollo.sh
```

3. **Access the application**
- Application: http://127.0.0.1:8000
- Admin Panel: http://127.0.0.1:8000/admin/
- API Documentation: http://127.0.0.1:8000/api/docs/

### Manual Installation

1. **Install dependencies**
```bash
cd proyecto/src/backend
pip install -r requirements.txt
```

2. **Configure database**
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

3. **Create superuser**
```bash
python ensure_superuser.py
```

4. **Start development server**
```bash
python manage.py runserver
```

## Default Credentials

- **Email**: admin@studentspoint.app
- **Password**: admin123

## Google OAuth Configuration

### Required Setup
To enable Google OAuth functionality, configure the following in Google Cloud Console:

**Client ID**: `307562557576-0fd8ta7i09i1e6it5hstla13jsomeq2s.apps.googleusercontent.com`

### Authorized Redirect URIs
Add these URLs to your Google Cloud Console OAuth configuration:

```
http://localhost:8000/api/auth/google/callback/web/
http://127.0.0.1:8000/api/auth/google/callback/web/
https://yourdomain.com/api/auth/google/callback/web/
```

## API Documentation

The application provides a comprehensive REST API with the following main endpoints:

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration
- `GET /api/auth/google/login/` - Google OAuth initiation
- `POST /api/auth/google/callback/` - Google OAuth callback

### Applications
- `GET /api/forum/` - Forum management
- `GET /api/market/` - Marketplace operations
- `GET /api/portfolio/` - Portfolio management
- `GET /api/portfolio/generate_pdf/` - PDF generation
- `GET /api/polls/` - Poll and survey management
- `GET /api/schedules/` - Schedule management
- `GET /api/notifications/` - Notification system
- `GET /api/reports/` - Reporting system
- `GET /api/otec/` - Course management

## Project Structure

```
students-point/
├── Documentacion/           # Project documentation
├── FASE 1/                 # Development evidence
├── proyecto/
│   ├── src/backend/        # Django backend
│   │   ├── studentspoint/  # Main configuration
│   │   ├── staticfiles/    # Served static files
│   │   └── manage.py       # Django management script
│   └── imagenes/           # Images and logos
├── iniciar_desarrollo.bat  # Development startup script
└── README.md              # This file
```

## Development

### Running Tests
```bash
cd proyecto/src/backend
python manage.py test
```

### Code Style
The project follows Django best practices and PEP 8 guidelines.

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security Considerations

- JWT tokens for secure authentication
- CORS configuration for development
- CSRF protection for web forms
- Email validation for user registration
- OAuth 2.0 integration for third-party authentication

## Browser Support

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the GitHub repository
- Contact: admin@studentspoint.app

## Roadmap

- Enhanced mobile experience
- Additional OAuth providers
- Advanced analytics dashboard
- Integration with learning management systems
- Multi-language support

## Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the UI components
- Google for OAuth integration
- All contributors and testers

---

**StudentsPoint** - Empowering students through technology
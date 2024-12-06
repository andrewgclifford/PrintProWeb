# PrintProWeb

A web application for managing print jobs and tracking print status.

## Deployment Instructions

This application can be deployed to Render.com using the following steps:

1. **Prepare Your Repository**
   - Make sure your code is in a Git repository
   - Push your code to GitHub

2. **Set Up Environment Variables**
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your production settings

3. **Deploy to Render.com**
   1. Create a new account on [Render](https://render.com) if you haven't already
   2. Click "New +" and select "Web Service"
   3. Connect your GitHub repository
   4. Fill in the following settings:
      - Name: `printproweb` (or your preferred name)
      - Environment: `Python 3`
      - Build Command: `pip install -r requirements.txt`
      - Start Command: `gunicorn print_tracker.wsgi:application`
   5. Add your environment variables from `.env` in the Environment section
   6. Click "Create Web Service"

4. **Set Up Database**
   1. In Render, go to "New +" and select "PostgreSQL"
   2. Create a new PostgreSQL database
   3. Copy the database connection details to your environment variables

5. **Final Steps**
   1. Once deployed, go to your web service settings
   2. Add your custom domain if you have one
   3. Enable HTTPS

## Local Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your local settings
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Environment Variables

Make sure to set the following environment variables in your production environment:

- `DJANGO_SECRET_KEY`: Your Django secret key
- `DJANGO_DEBUG`: Set to 'False' in production
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `CORS_ALLOWED_ORIGINS`: Comma-separated list of allowed CORS origins
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host
- `DB_PORT`: Database port (usually 5432)

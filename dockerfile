# # Use official Python image
# FROM python:3.11-slim

# # Set working directory
# WORKDIR /app


# # Copy all project files
# COPY . /app

# # Install backend dependencies
# RUN pip install --no-cache-dir -r rt_backend_services/requirements.txt

# # Install web dependencies
# RUN pip install --no-cache-dir -r rt_web_services/requirements.txt

# # Expose Flask default port
# EXPOSE 5000

# # Set environment variables for Flask
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_ENV=development

# # Run the main app
# CMD ["flask", "run"]

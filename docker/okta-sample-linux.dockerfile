# Use Python 3.9 as base image
FROM python:3.9

# Install Nginx and clean up apt cache
RUN apt-get update && apt-get install -y nginx && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy Nginx configuration file
COPY docker/nginx/nginx.conf /etc/nginx/nginx.conf

# Create application directory and set it as the working directory
WORKDIR /app

# Copy and unzip backend code
COPY okta-sample-backend/dist/okta-sample-backend-1.0.tar.gz /app/
RUN tar -xvf okta-sample-backend-1.0.tar.gz && rm okta-sample-backend-1.0.tar.gz
RUN mv okta-sample-backend-1.0/ backend/

RUN pip install gunicorn

# Install Python dependencies
RUN pip install --no-cache-dir /app/backend/

# Copy frontend code
COPY okta-sample-frontend/dist/ /app/frontend/

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx and Gunicorn (or your preferred WSGI server)
#CMD service nginx start && gunicorn -w 4 -b 0.0.0.0:5000 backend.wsgi:api
CMD gunicorn -w 4 -b 0.0.0.0:5000 backend.wsgi:api

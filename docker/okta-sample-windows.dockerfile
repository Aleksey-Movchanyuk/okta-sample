# Use a Windows Server Core image with IIS installed
FROM mcr.microsoft.com/windows/servercore/iis:latest

# Set the working directory to C:\app
WORKDIR C:\app

# Install Python 3.9
RUN powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe -OutFile C:\python.exe -UseBasicParsing; Start-Process C:\python.exe -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=C:\app\okta-sample-backend \
    PATH="C:\Python39;C:\Python39\Scripts;%PATH%"

# Copy the frontend files to the container
COPY okta-sample-frontend\dist C:\inetpub\wwwroot

# Copy the backend files to the container and install dependencies
COPY okta-sample-backend\dist\okta-sample-backend-1.0.tar.gz C:\app
RUN powershell -Command "Expand-Archive C:\app\okta-sample-backend-1.0.tar.gz -DestinationPath C:\app && cd C:\app\okta-sample-backend-1.0 && python setup.py install"

# Copy the nginx config file to the container and set up IIS
COPY docker\IIS\okta-sample-web.config C:\inetpub\wwwroot
RUN powershell -Command "Set-WebConfigurationProperty -Filter /system.webServer/handlers -PSPath 'IIS:\' -Name 'accessPolicy' -Value 'Read, Script'"

# Expose port 80
EXPOSE 80

# Start IIS
ENTRYPOINT ["powershell"]
CMD ["-Command", "& {Import-Module IISAdministration; Start

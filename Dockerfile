# 1️⃣ Use official Python image
FROM python:3.11-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy requirements file first (for caching)
COPY requirements.txt .

# 4️⃣ Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy all project files into container
COPY . .
COPY start.sh /app/start.sh

# Make the script executable
RUN chmod +x /app/start.sh

# 6️⃣ Expose application port
EXPOSE 8000

# 7️⃣ Command to run the application
CMD ["/app/start.sh"]

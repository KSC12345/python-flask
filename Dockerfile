# Use a Python base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libgtk-3-0 \
    libasound2 \
    libxshmfence1 \
    libglu1 \
    && rm -rf /var/lib/apt/lists/*

# Set Playwright browsers path
ENV PLAYWRIGHT_BROWSERS_PATH=/home/appuser/playwright-browsers

# Create a non-root user and set ownership **BEFORE** installing browsers
RUN useradd -m -u 1001 appuser && \
    mkdir -p ${PLAYWRIGHT_BROWSERS_PATH} && \
    chown -R appuser:appuser ${PLAYWRIGHT_BROWSERS_PATH}

# Install Playwright and browsers as root, but target the user-owned directory
RUN pip install playwright && \
    playwright install --with-deps chromium

# Switch to the non-root user
USER appuser

# Copy application files and install dependencies
WORKDIR /app
COPY --chown=appuser:appuser requirements.txt .
COPY --chown=appuser:appuser app.py .
RUN pip install --user --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "app.py"]

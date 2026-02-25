# Stage 1: Build the React frontend
# Uses a Node image — only needed to compile React, not to run the app
FROM node:22-alpine AS frontend-builder
WORKDIR /build/frontend

# Copy package files first so Docker can cache the npm install layer.
# npm ci only re-runs when package.json or package-lock.json change.
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build
# Output lands at /build/frontend/dist

# Stage 2: Run the Flask backend
# Node is not carried over — final image contains Python only
FROM python:3.12-slim
WORKDIR /app

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./

# Copy the compiled React app from Stage 1.
# app.py sets static_folder="../frontend/dist" relative to /app,
# which resolves to /frontend/dist at runtime.
COPY --from=frontend-builder /build/frontend/dist /frontend/dist

# Create the mount point for the Fly.io persistent volume (SQLite lives here)
RUN mkdir -p /data

EXPOSE 8080

# gunicorn is the production WSGI server — "app:app" means the `app`
# object inside app.py
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]

# --- Stage 1: Build & Download dependencies ---
FROM python:3.11-slim AS builder
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install requests

# --- Stage 2: Tiny Production Image ---
FROM python:3.11-slim
WORKDIR /app
# Copy ONLY the virtual environment folder from the builder stage
COPY --from=builder /opt/venv /opt/venv
COPY app.py .

# Make sure our app uses the copied virtual environment
ENV PATH="/opt/venv/bin:$PATH"
CMD ["python", "app.py"]

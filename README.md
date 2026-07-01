# AWS Image Upload Demo (FastAPI + EC2 + S3)

This project is a simple FastAPI server with a single HTML frontend.

It is designed to showcase how a web browser can upload an image through a FastAPI app running on an AWS EC2 instance, and then store that image in a private Amazon S3 bucket.

## What this project demonstrates

- A FastAPI backend serving both API routes and an HTML page.
- A simple frontend (HTML, CSS, and JavaScript) with no framework.
- Image upload from browser to FastAPI (`POST /upload`).
- Upload from FastAPI to private S3 using `boto3`.
- Returning a pre-signed URL so the uploaded image can be previewed in the browser.

## Architecture flow

1. User opens the EC2-hosted FastAPI app in a browser.
2. Browser loads the frontend from `GET /`.
3. User selects an image and clicks upload.
4. Frontend sends the file to `POST /upload` using `multipart/form-data`.
5. FastAPI uploads the file to S3.
6. FastAPI generates a pre-signed URL and returns JSON.
7. Frontend displays the uploaded image using that URL.

## Why this is useful for EC2 workshops

- Students can learn a full browser-to-cloud upload flow.
- No frontend framework is required.
- The app stays small and easy to understand.
- It is practical for demonstrating EC2-hosted APIs interacting with S3.

import os
import uuid

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

from fastapi import FastAPI, File, HTTPException, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

load_dotenv()

app = FastAPI(title="AWS Image Upload Demo")

templates = Jinja2Templates(directory="templates")

BUCKET = os.getenv("S3_BUCKET_NAME")
REGION = os.getenv("AWS_REGION")

if not BUCKET:
    raise RuntimeError("S3_BUCKET_NAME must be set in the environment")

s3 = boto3.client("s3", region_name=REGION)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="A filename is required")

    extension = os.path.splitext(file.filename)[1]

    filename = f"{uuid.uuid4()}{extension}"

    try:
        s3.upload_fileobj(
            file.file,
            BUCKET,
            filename,
            ExtraArgs={"ContentType": file.content_type or "application/octet-stream"},
        )

        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": BUCKET, "Key": filename},
            ExpiresIn=3600,
        )
    except (ClientError, BotoCoreError) as exc:
        raise HTTPException(status_code=500, detail="Failed to upload image to S3") from exc

    return {
        "success": True,
        "filename": filename,
        "url": url
    }
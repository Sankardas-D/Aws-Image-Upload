#!/bin/bash

# Stop FastAPI server
echo "Stopping FastAPI server..."
pkill -f "uvicorn main:app" || echo "No uvicorn process found"
echo "Done!"

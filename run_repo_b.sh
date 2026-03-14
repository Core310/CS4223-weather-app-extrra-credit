#!/bin/bash
# Script to run Repository B (Flask API + React Frontend)

echo "Starting Repository B Backend (Flask)..."
(cd 2025f-feature-development-b && source .venv/bin/activate && python3 main.py) &
BACKEND_PID=$!

echo "Starting Repository B Frontend (React)..."
(cd 2025f-feature-development-b/frontend && npm run dev -- --port 5173 --host) &
FRONTEND_PID=$!

# Trap Ctrl+C to kill both background processes
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT

echo "Both servers are starting..."
echo "Backend: http://localhost:5000"
echo "Frontend: http://localhost:5173"
echo "Press Ctrl+C to stop both."

wait

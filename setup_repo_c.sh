#!/bin/bash
echo "Creating virtual environment for Repository C in ./.venv_c..."
python3 -m venv .venv_c

echo "Activating the environment and installing dependencies..."
source .venv_c/bin/activate
pip install -r 2025f-feature-development-c/requirements.txt

echo ""
echo "Setup complete!"
echo ""
echo "To activate this environment in your current terminal, please run:"
echo "source .venv_c/bin/activate"

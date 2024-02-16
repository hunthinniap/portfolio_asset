#!/bin/bash
# Full path to your update_json.py script
UPDATE_SCRIPT="$(pwd)/update_json.py"

# Check if the update_json.py script exists and is executable
if [ -f "$UPDATE_SCRIPT" ]; then
    echo "Running update_json.py before git add..."
    python "$UPDATE_SCRIPT"
else
    echo "update_json.py not found, skipping script execution."
fi

# Now, run the actual `git add` command with all passed arguments
echo "Running git add..."
git add "$@"

echo "Done."

import os
import subprocess
from datetime import datetime

class SQLUploader:
    def __init__(self, repo_path: str):
        """
        Initialize with path to your SQL GitHub project folder.
        """
        self.repo_path = repo_path
        os.chdir(self.repo_path)

    def save_query(self, level: str, query: str):
        """
        Saves SQL query to a file and uploads to GitHub automatically.
        """

        # Valid folders
        valid_levels = ["beginner", "intermediate", "advanced"]
        if level not in valid_levels:
            raise ValueError(f"Invalid level. Use one of {valid_levels}")

        # Ensure folder exists
        os.makedirs(level, exist_ok=True)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{level}/query_{timestamp}.sql"

        # Save SQL file
        with open(filename, "w") as f:
            f.write(query.strip() + "\n")

        print(f"Saved: {filename}")

        # Git automation
        subprocess.run(["git", "add", filename])
        subprocess.run(["git", "commit", "-m", f"Add SQL Query: {filename}"])
        subprocess.run(["git", "push"])

        print("Uploaded to GitHub successfully!")

import os
import subprocess
from datetime import datetime


class SQLUploader:
    def __init__(self, repo_path: str):
        """
        Initialize with the path of your Git repository.
        """
        self.repo_path = repo_path
        os.chdir(self.repo_path)

    def save_query(self, level: str, query: str):
        """
        Save the SQL query to a file and push to GitHub.
        """

        # Validate folder
        allowed_levels = ["beginner", "intermediate", "advanced"]
        if level not in allowed_levels:
            raise ValueError(f"Invalid level. Use one of: {allowed_levels}")

        # Ensure folder exists
        os.makedirs(level, exist_ok=True)

        # Filename based on timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{level}/query_{timestamp}.sql"

        # Write the query into the file
        with open(filename, "w") as f:
            f.write(query.strip() + "\n")

        print(f"Saved SQL file: {filename}")

        # Git automation
        self._git_push(filename)

    def _git_push(self, file_path: str):
        """
        Internal method to handle git add, commit, and push.
        """

        subprocess.run(["git", "add", file_path])
        subprocess.run(["git", "commit", "-m", f"Add SQL query: {file_path}"])
        subprocess.run(["git", "push"])

        print(f"Uploaded to GitHub: {file_path}")


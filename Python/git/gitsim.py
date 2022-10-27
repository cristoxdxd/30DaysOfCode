# Program to simulate git commands

# Importing the required modules
import os
import subprocess

# Function to create a new repository
def create_repo():
    # Taking the name of the repository from the user
    repo_name = input("Enter the name of the repository: ")
    # Creating a new directory with the name of the repository
    os.mkdir(repo_name)
    # Changing the current working directory to the newly created directory
    os.chdir(repo_name)
    # Creating a new directory named .git
    os.mkdir(".git")
    # Creating a new file named README.md
    with open("README.md", "w") as f:
        f.write("This is a new repository.")
    # Initializing the repository
    subprocess.call(["git", "init"])
    # Adding the README.md file to the staging area
    subprocess.call(["git", "add", "README.md"])
    # Commiting the changes
    subprocess.call(["git", "commit", "-m", "Initial commit"])

# Function to add a new file to the repository
def add_file():
    # Taking the name of the file from the user
    file_name = input("Enter the name of the file: ")
    # Creating a new file with the name given by the user
    with open(file_name, "w") as f:
        f.write("This is a new file.")
    # Adding the file to the staging area
    subprocess.call(["git", "add", file_name])
    # Commiting the changes
    subprocess.call(["git", "commit", "-m", "Added " + file_name])

# Function to create branches to the repository
def create_branch():
    # Taking the name of the branch from the user
    branch_name = input("Enter the name of the branch: ")
    # Creating a new branch with the name given by the user
    subprocess.call(["git", "branch", branch_name])

# Function to switch between branches
def switch_branch():
    # Taking the name of the branch from the user
    branch_name = input("Enter the name of the branch: ")
    # Switching to the branch given by the user
    subprocess.call(["git", "checkout", branch_name])

# Function to merge branches
def merge_branch():
    # Taking the name of the branch from the user
    branch_name = input("Enter the name of the branch: ")
    # Merging the branch given by the user
    subprocess.call(["git", "merge", branch_name])

# Function to delete branches
def delete_branch():
    # Taking the name of the branch from the user
    branch_name = input("Enter the name of the branch: ")
    # Deleting the branch given by the user
    subprocess.call(["git", "branch", "-d", branch_name])

# Function to view the status of the repository
def view_status():
    # Viewing the status of the repository
    subprocess.call(["git", "status"])

# Function to view the log of the repository
def view_log():
    # Viewing the log of the repository
    subprocess.call(["git", "log"])

# Function to revert to a previous commit
def revert_commit():
    # Taking the commit id from the user
    commit_id = input("Enter the commit id: ")
    # Reverting to the commit given by the user
    subprocess.call(["git", "revert", commit_id])

# Function to view the difference between two commits
def view_diff():
    # Taking the commit id from the user
    commit_id = input("Enter the commit id: ")
    # Viewing the difference between the current commit and the commit given by the user
    subprocess.call(["git", "diff", commit_id])

# Function to display the menu
def menu():
    # Printing the menu
    print("1. Create a new repository")
    print("2. Add a new file to the repository")
    print("3. Create a new branch")
    print("4. Switch to a branch")
    print("5. Merge two branches")
    print("6. Delete a branch")
    print("7. View the status of the repository")
    print("8. View the log of the repository")
    print("9. Revert to a previous commit")
    print("10. View the difference between two commits")
    # Taking the choice from the user
    choice = input("Enter your choice: ")
    # Returning the choice
    return choice

# Main function
if __name__ == "__main__":
    # Taking the choice from the user
    choice = menu()
    # Checking the choice
    if choice == "1":
        # Calling the create_repo() function
        create_repo()
    elif choice == "2":
        # Calling the add_file() function
        add_file()
    elif choice == "3":
        # Calling the create_branch() function
        create_branch()
    elif choice == "4":
        # Calling the switch_branch() function
        switch_branch()
    elif choice == "5":
        # Calling the merge_branch() function
        merge_branch()
    elif choice == "6":
        # Calling the delete_branch() function
        delete_branch()
    elif choice == "7":
        # Calling the view_status() function
        view_status()
    elif choice == "8":
        # Calling the view_log() function
        view_log()
    elif choice == "9":
        # Calling the revert_commit() function
        revert_commit()
    elif choice == "10":
        # Calling the view_diff() function
        view_diff()
    else:
        # Printing an error message
        print("Invalid choice.")
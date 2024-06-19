
Creating a GitHub Account
GitHub is a popular web-based hosting service for Git repositories. It provides a centralized location for storing and sharing code, facilitating collaboration, and tracking project changes. To create a GitHub account, I visited the GitHub website (https://github.com) and followed the sign-up process.
During the sign-up process, I provided the necessary information, such as a username, email address, and password. Additionally, I chose to enable two-factor authentication for added security.

Initializing a Git Repository
With Git installed and configured, and a GitHub account created, I was ready to initialize a Git repository for my project. I navigated to the desired directory in the Visual Studio Code terminal and ran the following command:
```sh
git init
```
This command created a new Git repository in the current directory, setting up the necessary files and folders for version control.

Making the First Commit
After initializing the Git repository, I created a new file called `README.md` in the project directory. This file typically serves as a brief introduction and documentation for the project.

I then added the `README.md` file to the Git staging area using the following command:
```sh
git add README.md
```
With the file staged, I committed the changes to the local Git repository using the following command:
```sh
git commit -m "Initial commit"
```
The `-m` flag allows me to provide a commit message, which briefly describes the changes made in this commit. In this case, I used "Initial commit" as the message for my first commit.
By completing these steps, I successfully set up version control using Git and created a local Git repository for my project.

Installing Programming Languages and Runtimes
As a software developer, it is essential to have the necessary programming languages and runtimes installed on your machine to build and execute your code. For this assignment, I chose to install Python, a versatile and widely-used programming language.

Installing Python
I visited the official Python website (https://www.python.org) and navigated to the downloads section. Since I was using Windows 11, I downloaded the latest version of Python for Windows from the provided links.
The Python installer for Windows is straightforward and user-friendly. Upon running the installer, I was presented with several options and customizations. I chose the following settings:
1. Install Launcher for All Users: This option allowed me to install Python for all user accounts on my machine, making it accessible to everyone.
2. Add Python to PATH: Selecting this option automatically added Python to the system's PATH environment variable, enabling me to run Python commands from any directory in the command prompt or terminal without specifying the full path.
3. Customize Installation: I opted for a custom installation to select the specific components I wanted to include. In this case, I chose to install the Python interpreter, pip (Python package manager), and the Python documentation.
After configuring the installation options, the installer proceeded to download and install Python on my machine.

After configuring the installation options, the installer proceeded to download and install Python on my machine. Upon completion, I verified the installation by opening a terminal and running the following command:
```sh
python --version
```
This command displayed the installed Python version, confirming a successful installation.

### Setting Up Python Environment Variables
To ensure that Python and its package manager, pip, work seamlessly, I verified that Python was added to the system's PATH environment variable. This allowed me to execute Python commands from any directory in the terminal. The PATH environment variable includes a list of directories that the system searches for executable files.

### Installing Additional Runtimes or Compilers
Depending on the nature of the project, additional runtimes or compilers might be necessary. For instance, if working

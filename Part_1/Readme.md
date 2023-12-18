# Part 1: Introduction to Telegram Bot

Welcome to Part 1 of the A2SV Remote Second Year Telegram Bot Development Phase! In this section, we'll delve into the fundamentals of creating a Telegram bot, understanding the recommended folder structure, and exploring the concept of long polling. By the end of this exercise, you'll have a solid foundation to build your first Telegram bot using the Aiogram library.

## Task Overview

### 1. Understand Folder Structure
   - Learn the recommended folder structure for organizing your Telegram bot project.
   - **Task:** Familiarize yourself with the provided project structure in the `part1_intro` folder.

### 2. Concept of Long Polling
   - Explore the concept of long polling and its significance in Telegram bot development.
   - **Task:** Dive into the `long_polling` folder, where you'll find code snippets and explanations about implementing long polling in your bot.

### 3. Create Your First Bot
   - Use BotFather to create your first Telegram bot.
   - **Task:** Follow the step-by-step guide in the `create_first_bot` folder to create your bot and obtain necessary credentials.

### 4. Host on PythonAnywhere
   - Learn how to host your Telegram bot on PythonAnywhere, a cloud platform for hosting Python applications.
   - **Task:** Check the `host_on_pythonanywhere` folder for instructions on deploying your bot for testing and interaction.

### 5. Develop Custom Commands
   - Dive into the Aiogram library and understand its usage in developing custom commands for your Telegram bot.
   - **Task:** Head to the `custom_commands` folder to practice implementing basic commands to enhance your bot's functionality.

## Getting Started

To begin this exercise, follow these detailed steps:

1. **Open GitHub Codespace:**
   - Use GitHub Codespace for a consistent development environment.
   - **Task:** Refer to the [short video](#) for a visual guide on opening GitHub Codespace.

2. **Create Your Branch:**
   - Ensure platform consistency by creating a new branch with the format `[First_Name].[Task].1`.
   - **Task:** Run the command `git checkout -b YourName.Task.1` to create your branch.

3. **Copy Task Folder:**
   - Copy the entire folder for Part 1 (`part1_intro`) and rename it with your name.
   - **Task:** Follow the instructions and refer to the provided image [--- Picture Showing copied task folder —] in the `copy_task_folder` folder.

4. **Run Docker Compose:**
   - Inside your new folder, run Docker Compose to initiate the boilerplate code.
   - **Task:** Execute the following commands:
     ```
     docker compose build
     docker compose run
     ```
   - If you encounter issues with the boilerplate code, contact one of the project heads for assistance.

5. **Complete Tasks:**
   - Proceed to complete the tasks within your new folder. <br>
        - **Task Guide:**<br>
             - Read the following Resource for understanding telegram bot folder structure best practice and long polling. [Link](#)<br>
             - Go through the code and the bot ['A2SV_bot_Part1_Example']() on telegram and see how it works <br>
             - Create your own telegram bot using Bot Father on telegram then replace the `TOKEN_API` in the .config file <br>
                     Sample solution video[Link](#) <br>
             - Host your bot on PythonAnywhere <br>
             - Add your own additional commands other than `/start`

6. **Send a Pull Request:**
   - Once tasks are completed, send a pull request with your changes.
   - If your solution is accepted, it will be merged, and you can move on to the next task.

Happy coding!

# Building an Open AI plugin with Codespaces
This is a sample repo for developing OpenAI plugin using the FastAPI framework. There are three main parts of the repo, with details of each below:
- [📦 Code to help setup development environment for FastAPI framework](#📦-code-to-help-setup-development-environment)
- [💻 Code for the FastAPI app](#💻-code-for-the-fastapi-app)
- [🧠 Code to turn the FastAPI app into a ChatGPT plugin](#🧠-code-to-turn-the-fastapi-app-into-a-chatgpt-plugin)

## 📦 Code to help setup development environment
Create a Codespaces by clicking **<> Code** -> **Codespaces** -> **Create codespaces on {branch}**, and a containerized development environment will be set up for you on the cloud based on the contents of the following files.

### **.devcontainer**
The `.devcontainer` folder contains files for defining a containerized development environment, specific to building this FastAPI app. It's set up in a way that makes it easy for you to use with GitHub Codespaces as well: launch a Codespace using this template, and you're ready to start developing! Learn more about devcontainers [here](https://containers.dev/).

### **.vscode**
The `.vscode` folder contains:
- `json.code-snippets` file that helps to quickly write the manifest file for the OpenAI plugin. (✨ Tip: Type `manifest-openai`, press `enter` to accept the template, and `tab` through the fields to quickly generate the manifest)
- `settings.json` file that helps to validate the manifest file (`ai-plugin.json`) against [this schema](https://github.com/minsa110/ai-plugin-schema/blob/main/ai-plugin-schema.json).
- `launch.json` file that helps to customize **Run and Debug** (this is not necessary for this repo, and you can easily have VS Code automatically create one for you).

## 💻 Code for the FastAPI app
If you have [access](https://code.visualstudio.com/blogs/2023/03/30/vscode-copilot#_getting-started-today) to [GitHub Copilot](https://github.com/features/copilot), try it out to help you write code faster. To test the app, run `uvicorn main:app` in the integrated terminal, or press `F5`, and debug CRUD operations at .../docs.

- `main.py` is the code for the API plugin. (✨ Tip: Generate the code using Copilot. The following is an example prompt to use in the Copilot chat view (`Ctrl+Alt+I`) ([learn more](https://code.visualstudio.com/blogs/2023/03/30/vscode-copilot#_embracing-the-chat-view)).)
   ```markdown
   Write a simple Grocery List app using FastAPI, that lets the user add grocery items, list their items without requiring quantity, list a specific item, and delete an item, ensuring that the app stores item_id for each item.

   Assume that a docker container is running for Redis, running and accessible at local host and port 6379. Make use of the Redis container for persisting data from the Grocery List app.

   Include a main section which will run this app using uvicorn. The Python module where I save this code will be called main.py.

   Mount static files in the .well-known directory to the path /.well-known, which should at minimum contain ai-plugin.json and openapi.yaml.
   ```
- `openapi.yaml` is a specification that dictates how to define the schema of the API.

## 🧠 Code to turn the FastAPI app into a ChatGPT plugin
- `ai-plugin.json` is a JSON manifest file that defines relevant metadata for the plugin. Learn more in the [OpenAI docs](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest).

## 💬 Register the app on ChatGPT
- Go to **PORT** and set visibility of port 8000 to `public`
- Copy the link and paste it on ChatGPT plugin

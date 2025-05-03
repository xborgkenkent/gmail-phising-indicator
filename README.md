https://github.com/user-attachments/assets/ccf4e5dd-b9c3-4c3a-99cc-40d87972647d

# Tech Stack: 
Python, FastAPI, Nuxt, Vue, Google Mail API, OpenAI API

# Setup Instructions

# Enable Google Mail API
You can find detailed instructions on how to enable the Google Mail API and create the necessary credentials by following this link:
[Google Mail API Guide](https://developers.google.com/workspace/gmail/api/quickstart/js)

This guide will walk you through the process in the Google Cloud Console. After setting up your credentials, **paste the downloaded `credentials.json` file into the `app` folder** and proceed with the backend setup below.

## Backend Setup (FastAPI)

1.  **Create a virtual environment (recommended):**

    ```bash
    cd app
    python -m venv env
    ```

2.  **Activate the virtual environment:**

    * **On Windows:**

        ```bash
        .\env\Scripts\activate
        ```

    * **On macOS and Linux:**

        ```bash
        source env/bin/activate
        ```
3.  **After the installation completes, copy the example environment file:**

    ```bash
    cp example.env .env
    ```

4.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the FastAPI application:**

    ```bash
    uvicorn main:app --reload
    ```

    * `main:app`:  Specifies the module (`main`) and the application object (`app`) within that module.
    * `--reload`: Enables automatic reloading of the server when you make code changes, which is very useful during development.

## Frontend Setup (Nuxt.js)

1.  **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2.  **Install the Node.js dependencies:**

    ```bash
    npm install
    ```

    or

    ```bash
    yarn install
    ```

    or

    ```bash
    pnpm install
    ```

3.  **After the installation completes, copy the example environment file:**

    ```bash
    cp example.env .env
    ```

4.  **Run the Nuxt.js development server:**

    ```bash
    npm run dev
    ```

    or

    ```bash
    yarn dev
    ```

    or

    ```bash
    pnpm dev
    ```

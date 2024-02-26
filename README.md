# GLIP/DesCo Demo Frontend

This project demos GLIP and DesCo using streamlit

## Usage

This repository only contains frontend code, and requires an active backend running all necessary models. The API address is set to connect to an EC2 machine serving the models in the "settings.py" file. If deploying your own models, you need to change the API address to point to your own server and modify the API call implementation. To build the frontend with docker:

1. Clone the repository to your local machine.
2. Build the application with `docker build -t <repository_name> .`
3. Run the frontend server and forward ports using `docker run --rm --gpu all -p 8501:8501`

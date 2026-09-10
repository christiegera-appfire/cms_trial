# Deploying Planning Poker locally via Docker

This document explains how to deploy Planning Poker locally using Docker.

### Prerequisites

- Basic knowledge of using Docker.
- **docker-compose** installed on your system

### Step 1: Docker registry login

Log in to the Planning Poker Docker Registry using your credentials:

```shell
docker login docker.lizzybrain.com
```

### Step 2: Create a Docker compose configuration

Copy the following content and save it as **docker-compose.yml**. Feel free to modify the port mappings if needed.

```text
version: "3"
services:
    mongo:
        container_name: mongo
        image: mongo:3.6.9
        volumes: ["./_app_data:/data/db"]
        ports: ["127.0.0.1:27017:27017"]
        restart: always

    app:
        container_name: jpp
        image: docker.lizzybrain.com/jpp:v2
        restart: always
        ports: ["3005:3005"]
        links: [mongo]
        depends_on: [mongo]
```

### Step 3: Run Docker compose

Run the following command to start the containers. Optionally, you can use the **-d** flag to run it as a background service:

```text
docker-compose up -d
```

### Step 4: Verify installation

Ensure that the installation is successful by accessing the following URL in your browser:

`http://localhost:3005/atlassian-connect.json`

localhost will be your server IP, and 3005 will be your server port (leave empty if 80). The path **/atlassian-connect.json** is used to validate the deployment. If installed successfully, you'll see a JSON response.

### Step 5: Configure Planning Poker in Jira

1. Navigate to the **Manage Apps** section in your Jira instance.
2. Access the **Planning Poker Configuration** page.
3. Enter the URL or IP address of the machine where you have the app running.
4. Enjoy!
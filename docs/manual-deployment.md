# Push image to DockerHub

1. Log into DockerHub with `docker login`
2. Build the image with `docker build --file docker/Dockerfile --target production --tag <username>/todo-app:prod --platform linux/amd64 .`
3. Push the image to DockerHub with `docker push <username>/todo-app:prod`

See the latest image [here](https://hub.docker.com/repository/docker/nancysingleton036/todo-app/general)

# Trigger Azure to pull latest image and restart web app

1. Locate the webhook URL
   - This can be found in the Azure portal, on the app's service page, under Deployment Centre
2. Send a request with `curl -v -X POST '<webhook>'`

See the deployed app [here](https://2024-09-15-nansin-todo-app.azurewebsites.net/)

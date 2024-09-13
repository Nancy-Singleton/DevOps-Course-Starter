# Push Image to Docker Hub

1. Log into DockerHub with `docker login`
2. Build the image with `docker build --file docker/Dockerfile --target production --tag <username>/todo-app:prod --platform linux/amd64 .`
3. Push the image to DockerHub with `docker push <username>/todo-app:prod`

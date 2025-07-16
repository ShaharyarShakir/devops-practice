# Docker commands

- shows running containers

```bash
docker ps
```

- shows all the containers

```bash
docker ps -a
```

- show all images

```bash
docker images
```

- pull the images

```bash
docker pull <containernameorid>
```

- pull and run the images

```bash
docker run <containernameorid>
```

- remove the containers

```bash
docker rm <containernameorid>
```

- forcefully remove the container

```bash
docker rm -f <containernameorid>
```

- remove the images

```bash
docker rmi <containernameorid>
```

- remove container with volume

```bash
docker rm -v <containernameorid>
```

- run images in detached mode

```bash
docker -d <containernameorid>
```

- run with port mapping

```bash
docker run -p localport:dockerport <containernameorid>
```

- run with attached volume

```bash
docker run -v $(pwd):/app <containernameorid>
```

###### OR

```bash
docker run -v localdir:dockerdir <containernameorid>
```

- run in intereactive tty

```bash
docker run -it <containernameorid> sh or /bin/bash or some other command
```

- start a container

```bash
docker start <containernameorid>
```

- stop a container

```bash
docker stop <containernameorid>
```

- show logs of a container

```bash
docker logs <containernameorid>
```

- attach to a container

```bash
docker attach <containernameorid>
```

- stop the container immediately

```bash
docker kill <containernameorid>
```

-stop all the running containers

```bash
docker stop $(docker ps -q)
```

- remove all the stopped containers

```bash
docker containerorimageorsystem prune
```

- system remove everything all the container unused images
- copy file from a container

```bash
docker cp <containernameorid>:/path/to/file ./
```

- see the metadata of the Image

```bash
docker inspect <containernameorid>
```

- export a env variable and auto port assign

```bash
docker run -d -P -e <nameofvaribale> <containernameorid>
```

- add env file

```bash
docker run -p --env-file <filenameor.env> <containernameorid>
```

- show current networks

```bash
docker network ls
```

- create network with overlay

```bash
docker network create <nameofnetwork> -d <nameof overlay>
```

- --rm means => remove the contianer and all its dependencies after serving it

###### Image Level

- RUN command => execute commands at build time

###### Container Level

- CMD => execute commands at container RunTime

# Docker Network

###### types of Network

- Host
- Bridge (default)
- User defined Bridge (Custom)
- None

###### used with docker swarm

- MACVLAN
- IPVLAN
- Overlay

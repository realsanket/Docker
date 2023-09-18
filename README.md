# Docker

This repository contains documentation for Docker.

## What is Docker?

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package.

![What it can do](image.png)

## Why you need Docker?

Docker is a tool that allows developers, sys-admins etc. to easily deploy their applications in a sandbox (called containers) to run on the host operating system i.e. Linux. The key benefit of Docker is that it allows users to package an application with all of its dependencies into a standardized unit for software development. Unlike virtual machines, containers do not have the high overhead and hence enable more efficient usage of the underlying system and resources.
![Why you need docker](image-2.png)

## Terminology

- **Docker Container**: Docker Container is an isolated environment that runs on top of the host operating system.They can have there own process, network interfaces, mounts etc except for the kernel.Docker container is simply an instance of a Docker image. It is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.
![Alt text](image-3.png)
- **Docker Image**: The file system and configuration of an application which are used to create Docker containers. Docker images are built from layers of other images. Docker images are stored in a Docker registry.
- **Docker Daemon**: The background service running on the host that manages building, running and distributing Docker containers.
- **Docker Client**: The command line tool that allows the user to interact with the Docker daemon.
- **Docker Registry**: A Docker registry is a repository for Docker images. Docker clients connect to registries to download (“pull”) images for use or upload (“push”) images that they have built.
- **Dockerfile**: Dockerfile is a text-based script that contains all the commands a user could call on the command line to assemble an image.
- **Docker Compose**: Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services.

## Docker vs Virtual Machine

| Docker | Virtual Machines |
| --- | --- |
| Containers are much lighter | Need to emulate an operating system or hardware virtualization |
| Containers are portable | Virtual machines are not portable |
| Containers are faster to start | Virtual machines are slower to start |
| Containers are more flexible | Virtual machines are less flexible |
| Containers share the host OS kernel | Virtual machines have their own OS kernel |
| Containers are less secure | Virtual machines are more secure |

![Alt text](image-4.png)

## Docker Installation

### Install Docker on Ubuntu

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

### Install Docker on CentOS

```bash
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io
```

### Install Docker on Debian

```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Docker Commands

| Name |Description |Syntax | Example | Extra Info |
| --- | --- | --- | --- | --- |
| **docker run** | Run a command in a new container | `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]` | `docker run -it ubuntu bash` | If the image is not availble then it will pull from docker hub |
| **docker ps** | List containers | `docker ps [OPTIONS]` | `docker ps -a` | -a: Show all containers (default shows just running) |
| **docker stop** | Stop one or more running containers | `docker stop [OPTIONS] CONTAINER [CONTAINER...]` | `docker stop 1a2b3c4d5e6f` | -t: Seconds to wait for stop before killing it (default 10) |
| **docker rm** | Remove one or more containers | `docker rm [OPTIONS] CONTAINER [CONTAINER...]` | `docker rm 1a2b3c4d5e6f` | -f: Force the removal of a running container (uses SIGKILL) |
| **docker images** | List images | `docker images [OPTIONS] [REPOSITORY[:TAG]]` | `docker images` | -a: Show all images (default hides intermediate images) |
| **docker rmi** | Remove one or more images | `docker rmi [OPTIONS] IMAGE [IMAGE...]` | `docker rmi 1a2b3c4d5e6f` | -f: Force removal of the image |
| **docker pull** | Pull an image or a repository from a registry | `docker pull [OPTIONS] NAME[:TAG|@DIGEST]` | `docker pull ubuntu` |
| **docker exec** | Run a command in a running container | `docker exec [OPTIONS] CONTAINER COMMAND [ARG...]` | `docker exec -it 1a2b3c4d5e6f bash` | -i: Keep STDIN open even if not attached -t: Allocate a pseudo-TTY |

## Run container in background

By default, docker run command runs a container in foreground. To run a container in background, use -d option.

```bash
docker run -d ubuntu sleep 1000
```

## Run container in interactive mode

To run a container in interactive mode, use -it option.

```bash
docker run -it ubuntu bash
```

## Sample Queries

# Sample Queries

1- Count the number of running containers.

```bash
docker ps | wc -l
```

wc -l counts the number of lines in the output of docker ps command.

2- Remove all containers.

```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

Explanation: docker ps -a -q lists all containers and docker stop stops all containers. Similarly, docker rm removes all containers.

3- Remove all images.

```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
```

Explanation: docker images -q lists all images and docker rmi removes all images.

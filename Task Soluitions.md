# Task Solutions

This Documentation contains solutions to the tasks given in the [Readme.md](./README.md) file.

## Task 001

- Run a ubuntu container in detached mode and check the version of ubuntu installed.

    ```bash
    docker run -t ubuntu cat /etc/os-release
    ```

    Explanation: -t option is used to allocate a pseudo-TTY. This can be useful, for example, when running sudo within the container. where as cat /etc/os-release is used to check the version of ubuntu installed.
- Run a Ngix container in detached mode and map port 80 on the container to port 8080 on the host.

    ```bash
    docker run -d -p 8080:80 nginx
    ```

    Explanation: -p option is used to map port 80 on the container to port 8080 on the host.

- Run multiple instance of Nginx on same container port and see what you observe.

    ```bash
    docker run -d -p 8080:80 nginx
    docker run -d -p 8080:80 nginx
    docker run -d -p 8080:80 nginx
    ```

    Explanation: When you run multiple instances of Nginx on the same port, you will get an error message saying that the port is already in use. This is because the port is already mapped to the host port and cannot be used by another container.

- Pull the latest version of the centos image and run a container in interactive mode, then execute a shell (e.g., /bin/bash) inside the container. Explore the CentOS environment from within the container.

    ```bash
    docker pull centos
    docker run -it centos /bin/bash
    ```

    Explanation: -it option is used to run a container in interactive mode and /bin/bash is used to execute a shell inside the container.

- Run a MySQL container in detached mode, set the environment variables for the root password and database name, and expose port 3306 on the container. Connect to the MySQL server from your host machine using a MySQL client.

    ```bash
    docker run -d -e MYSQL_ROOT_PASSWORD=pass123 -e MYSQL_DATABASE=testdb -p 3306:3306 mysql
    ```

    Explanation: -e option is used to set the environment variables for the root password and database name and -p option is used to expose port 3306 on the container.
- Run a WordPress container in detached mode, using environment variables to configure the database connection. Access the WordPress web application in your web browser and complete the initial setup.

## Task 002

Solution to the task 002 is available in the [Task002](./TaskSolutions/Task002/) folder.

Run the following command to start the task 002.

```bash
 docker build . -t task002
 docker run -d -p 8080:80 task002
```
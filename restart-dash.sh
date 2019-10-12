#!/usr/bin/env bash

docker stop dash && docker rm dash

docker-compose up --build -d

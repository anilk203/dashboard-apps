#!/usr/bin/env bash

docker stop dash1 && docker rm dash1

docker stop dash2 && docker rm dash2

docker-compose up --build -d

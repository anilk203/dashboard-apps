# How to add dash3, dash4 ... and dashn

## Step 1
## create folder under dashboard-apps  dash3
##### copy contents of dash2 to dash3

## Step 2
## open docker-compose.yml 
##### change dash2 to dash3
##### change port 8002 to 8003
```
  dash2:
    container_name: dash2
    restart: always
    build: ./dash2
    volumes:
      - ./dash2/:/home/project/dash
    ports:
      - "8002:8002"
    command: gunicorn -w 1 -b :8002 --log-level=debug app:server   
```    

## Step 3
## open nginx/project.conf
##### add this section to serve new dash3 from nginx
##### change dash2 to dash3
##### change port2 to port3
```   
  location  /dash3/  {
    proxy_pass http://dash2:8003/dash3/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }	
```  
## change dir to dashboard-apps
##### ./restart-dash.sh  

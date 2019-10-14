# How to add dash3, dash4 ... and dashn

## Step 1
## create folder under dashboard-apps  dash3
##### copy contents of dash2 to dash3

```
cd dash3
open / vi app.py
change url_base_pathname value to /dash3/


app = dash.Dash(name='Plotly Flask App',url_base_pathname='/dash2/',
                server=server)
                
after change it should look like this

app = dash.Dash(name='Plotly Flask App',url_base_pathname='/dash3/',
                server=server)
                
```

## Step 2
## open docker-compose.yml 
##### copy and paste dash2 section 
##### change dash2 to dash3
##### change port 8002 to 8003
##### which should look like this
```
  dash3:
    container_name: dash3
    restart: always
    build: ./dash3
    volumes:
      - ./dash3/:/home/project/dash
    ports:
      - "8003:8003"
    command: gunicorn -w 1 -b :8003 --log-level=debug app:server   
```    

## Step 3
## open nginx/project.conf
##### copy and paste dash2 section 
##### change dash2 to dash3
##### change port2 to port3
##### which should look like this
```   
  location  /dash3/  {
    proxy_pass http://dash3:8003/dash3/;
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

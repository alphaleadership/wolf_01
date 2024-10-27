## Wolf app 01

[Install docker on your host system](https://docs.docker.com/engine/install/)

### How to run ?
Use the following command in your terminal to launch the app :
```docker run -i -t wolfunit/vpn_wolf:1```

### How to build / tune ?
Change the starting options in *entrypoint.sh*
Then build a new image with the following command : 
```
docker build . -t <YOUR-REPO>/vpn_wolf:2
```


🇺🇦 ⚡- 2024 - Achilles

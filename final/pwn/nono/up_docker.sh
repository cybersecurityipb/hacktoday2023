#!/bin/bash

docker run -d --name nono-2 --restart always -p 17012:5000 nono-agrihack
docker run -d --name nono-3 --restart always -p 17013:5000 nono-agrihack
docker run -d --name nono-4 --restart always -p 17014:5000 nono-agrihack
docker run -d --name nono-5 --restart always -p 17015:5000 nono-agrihack

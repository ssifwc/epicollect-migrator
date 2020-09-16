#docker rm -f postgis
docker run -d --name postgis -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -v $(pwd)/init.sql:/docker-entrypoint-initdb.d/zinit.sql mdillon/postgis


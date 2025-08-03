docker pull heartexlabs/label-studio:latest
docker run -it -p 8787:8080 -v "${PWD}\mydata:/label-studio/data" heartexlabs/label-studio:latest

# Flask example using Docker

## To build and run the docker app as if it were your own

```
# Creates an image named hello
docker build -t hello .
docker run -p 80:80 hello
```

## To run my docker app anywhere
```
docker run -p 80:80 rmccorm4/testing:v4
```

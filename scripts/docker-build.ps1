mkdir temp-data\
Copy-Item -r ..\damn-yankee-data\ .\temp-data\ 
docker build -t damn-yankee-image .
Remove-Item .\temp-data\ -Recurse -Force
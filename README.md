# TallerCloud-DevOps

Lo primero que vamos hacer sera descargar dos programas.


Git --> https://git-scm.com/download/win

  
Docker-desktop --> https://www.docker.com/products/docker-desktop/ 



Una vez descargadas, nos creamos una carpeta "Prueba" nos metemos en ella, y dentro damos click derecho y buscamos Git bash here, esto nos abrira la terminal de git, dentro ejecutaremos el comando "git clone https://github.com/Banbushka/Proyecto-Web-Gcloud.git"



Ahora ejecutamos el comando "docker build -t tallerCloudDevops:1.0 .".
Con esto abremos creado nuestra imagen.



Por último ejecutamos el comando "docker run -p 5000:5000 tallerCloudDevops:1.0". ¡Y listo ya tendremos nuestra aplicación levantada en un container de docker :)!

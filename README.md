# upcode_test
Pour démarrer le service web avec docker :

1 - Accédez au répertoire du projet (où se trouve le Dockerfile).

2 - Créez votre image:  docker build -t myimage:latest .

3 - Exécutez un conteneur basé sur l'image: docker run -d --name mycontainer -p 8001:80 myimage

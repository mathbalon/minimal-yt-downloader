#!/bin/bash

IMAGE_NAME="minimal-yt-downloader"
CONTAINER_NAME="minimal-yt-downloader"
VOLUME_PATH="$(pwd)/app/Videos Downloaded"
FORCE_UPDATE=false

# Verificar se o Docker está instalado
if ! command -v docker &> /dev/null
then
    echo "Docker não está instalado. Por favor, instale o Docker para continuar."
    exit 1
fi

# Verificar se a flag --u foi passada
if [[ "$1" == "--u" ]]; then
    FORCE_UPDATE=true
    echo "Forçando atualização da imagem $IMAGE_NAME..."
fi

# Verificar se a imagem precisa ser construída ou atualizada
if [[ "$FORCE_UPDATE" == true ]]; then
    # Se a imagem já existe, removê-la
    if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" != "" ]]; then
        echo "Removendo a imagem antiga $IMAGE_NAME..."
        docker rmi -f $IMAGE_NAME
    fi
    echo "Construindo a nova imagem $IMAGE_NAME..."
    docker build --no-cache -t $IMAGE_NAME .
elif [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
    echo "A imagem $IMAGE_NAME não existe. Construindo a imagem..."
    docker build -t $IMAGE_NAME .
else
    echo "A imagem $IMAGE_NAME já existe."
fi

# Criar o diretório local para armazenar os vídeos, se não existir
if [ ! -d "$VOLUME_PATH" ]; then
    echo "Criando diretório para armazenar os vídeos: $VOLUME_PATH"
    mkdir -p "app/$VOLUME_PATH"
fi

# Verificar se o container já existe
if [ "$(docker ps -a -q -f name=$CONTAINER_NAME)" ]; then
    echo "O container $CONTAINER_NAME já existe. Removendo container antigo..."
    docker rm -f $CONTAINER_NAME
fi

# Executar o código Python dentro do container, montando o volume
echo "Iniciando $CONTAINER_NAME..."
docker run -it --rm --name $CONTAINER_NAME -v "$VOLUME_PATH:/app/Videos Downloaded" $IMAGE_NAME
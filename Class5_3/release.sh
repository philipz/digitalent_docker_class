#!/bin/bash
az login --service-principal -u $AZURE_LOGIN_USER --password $AZURE_PASSWORD --tenant $AZURE_TENANT
az webapp config container set -n tradingbot -g tradingbot -c dockware.azurecr.io/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG -r https://dockware.azurecr.io -u dockware -p $AZURE_REG_PASSWORD

#!/bin/sh

BRANCH="${BRANCH:-develop}"

wget --output-document=laaws-repository-service.yaml \
     "https://raw.githubusercontent.com/lockss/laaws-repository-service/${BRANCH}/src/main/resources/swagger/swagger.yaml" &&
wget --output-document=laaws-configuration-service.yaml \
     "https://raw.githubusercontent.com/lockss/laaws-configservice/${BRANCH}/src/main/resources/swagger/swagger.yaml" &&
wget --output-document=laaws-poller-service.yaml \
     "https://raw.githubusercontent.com/lockss/laaws-poller/${BRANCH}/src/main/resources/swagger/swagger.yaml" &&
wget --output-document=laaws-metadata-extraction-service.yaml \
     "https://raw.githubusercontent.com/lockss/laaws-metadataextractor/${BRANCH}/src/main/resources/swagger/swagger.yaml" &&
wget --output-document=laaws-metadata-service.yaml \
     "https://raw.githubusercontent.com/lockss/laaws-metadataservice/${BRANCH}/src/main/resources/swagger/swagger.yaml" &&
echo 'Success.'

#!/bin/sh

# Copyright (c) 2000-2022, Board of Trustees of Leland Stanford Jr. University
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

if [ -z "${BASEDIR}" ] ; then
  echo "error: the environment variable BASEDIR is not set"
  exit 1
fi
if [ ! -d "${BASEDIR}" ] ; then
  echo "error: BASEDIR does not point to a valid directory"
  exit 1
fi
if [ ! -f "${BASEDIR}/pom.xml" ] ; then
  echo "error: ${BASEDIR}/pom.xml not found"
  exit 1
fi

( cd "${BASEDIR}" && \
  mvn -pl `bin/bigproj` \
      -P doRestApiDocs \
      -Dbuild.java.spring.generateSwagger.groupId=io.swagger.codegen.v3 \
      -Dversion.plugin.swagger-codegen-maven-plugin=3.0.35 )

# See:
# https://stackoverflow.com/a/31820846/2850565
# https://github.com/sphinx-doc/sphinx/issues/701#issuecomment-697116337
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_extra_path
OUTDIR='EXTRA/software/apis'

cp "${BASEDIR}/laaws-repository-service/target/generated-sources/swagger/html/index.html" \
   "${OUTDIR}/laaws-repository-service.html"
cp "${BASEDIR}/laaws-configservice/target/generated-sources/swagger/html/index.html" \
   "${OUTDIR}/laaws-configuration-service.html"
cp "${BASEDIR}/laaws-poller/target/generated-sources/swagger/html/index.html" \
   "${OUTDIR}/laaws-poller-service.html"
cp "${BASEDIR}/laaws-metadataextractor/target/generated-sources/swagger/html/index.html" \
   "${OUTDIR}/laaws-metadata-extraction-service.html"
cp "${BASEDIR}/laaws-metadataservice/target/generated-sources/swagger/html/index.html" \
   "${OUTDIR}/laaws-metadata-service.html"

echo "Done."

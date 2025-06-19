#!/bin/sh
set -e

on_exit () {
	[ $? -eq 0 ] && exit
	echo 'ERROR: Feature "uv" (ghcr.io/va-h/devcontainers-features/uv) failed to install! Look at the documentation at ${documentation} for help troubleshooting this error.'
}

trap on_exit EXIT

set -a
. ../devcontainer-features.builtin.env
. ./devcontainer-features.env
set +a

echo ===========================================================================

echo 'Feature       : uv'
echo 'Description   : An extremely fast Python package and project manager, written in Rust.'
echo 'Id            : ghcr.io/va-h/devcontainers-features/uv'
echo 'Version       : 1.1.4'
echo 'Documentation : http://github.com/va-h/devcontainers-features/tree/main/src/uv'
echo 'Options       :'
echo '    SHELLAUTOCOMPLETION="false"
    VERSION="latest"'
echo 'Environment   :'
printenv
echo ===========================================================================

chmod +x ./install.sh
./install.sh

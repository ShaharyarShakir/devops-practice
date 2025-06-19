#!/bin/sh
set -e

on_exit () {
	[ $? -eq 0 ] && exit
	echo 'ERROR: Feature "Neovim (via Homebrew)" (ghcr.io/devcontainers-extra/features/neovim-homebrew) failed to install! Look at the documentation at ${documentation} for help troubleshooting this error.'
}

trap on_exit EXIT

set -a
. ../devcontainer-features.builtin.env
. ./devcontainer-features.env
set +a

echo ===========================================================================

echo 'Feature       : Neovim (via Homebrew)'
echo 'Description   : Neovim is a fork of Vim focused on modern code and features, rather than running in legacy environments.'
echo 'Id            : ghcr.io/devcontainers-extra/features/neovim-homebrew'
echo 'Version       : 1.0.21'
echo 'Documentation : http://github.com/devcontainers-extra/features/tree/main/src/neovim-homebrew'
echo 'Options       :'
echo '    VERSION="latest"'
echo 'Environment   :'
printenv
echo ===========================================================================

chmod +x ./install.sh
./install.sh

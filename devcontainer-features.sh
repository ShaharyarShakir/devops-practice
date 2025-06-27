#!/bin/bash
devcontainer templates apply \
	--workspace-folder . \
	--template-id ghcr.io/devcontainers/templates/python:latest \
	--template-args '{ "variant": "debian-bookworm" }' \
	--features '[

"ghcr.io/devcontainers/features/common-utils:2": {
	"username": "shakir",      
	"userUid": "1000",
	"userGid": "1000",
	"upgradePackages": "true"
	"installZsh": true
}
{ "id": "ghcr.io/devcontainers-extra/features/neovim-homebrew:1" },
	{ "id":  "ghcr.io/va-h/devcontainers-features/uv:1": },

		]'

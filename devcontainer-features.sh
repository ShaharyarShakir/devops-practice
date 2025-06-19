#!/bin/bash
devcontainer templates apply \
	--workspace-folder . \
	--template-id ghcr.io/devcontainers/templates/python:latest \
	--template-args '{ "variant": "debian-bookworm" }' \
	--features '[
{ "id": "ghcr.io/devcontainers-extra/features/neovim-homebrew:1" },
	{ "id":  "ghcr.io/va-h/devcontainers-features/uv:1": },

		]'

# deis_rails_console
Interactive Rails Console for Deis

This script is to be put in a deis app directory or in your PATH and allows you to open an interactive rails console
directly related to your app, it requires slightly customizing your Deis cluster by opening the Docker Remote API with
TLS encryption, and putting your client certificates in ~/.docker directory, as you would normally, the deis client is
also required.

Dependencies: Docker Client for Python(Docker-py), Docker pty

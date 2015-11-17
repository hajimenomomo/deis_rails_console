# deis_rails_console
Interactive Rails Console for Deis

This script is to be put in a deis app directory or in your PATH and allows you to open an interactive rails console
directly related to your app, it requires slightly customizing your Deis cluster by opening the Docker Remote API with TLS encryption, and putting your client certificates in ~/.docker directory, as you would with the docker client CLI using TLS. The deis client is, of course, also required for this script to work.

You must place your ca certificate, client key and certificate, and deis host list (as a list of stripped urls conforming to your certificate) in the ~/.docker directory as follows (please mind the naming conventions):
~/.docker/ca.pem
~/.docker/cert.pem
~/.docker/key.pem
~/.docker/deis_hosts

This script uses the default docker remote TLS port, which is 2376.

Regarding the hosts list, please refer to the example deis_hosts in the root of the project, which assumes owning the wildcard certificate for *.example.com

Dependencies: Docker Client for Python(Docker-py), Docker pty, Deis client properly installed in your PATH.

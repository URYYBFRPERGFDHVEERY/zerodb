#!/bin/sh

# for ubuntu trusty 14.04

sudo apt-get update
sudo apt-get install -y build-essential git python python-dev 
sudo apt-get install -y python-virtualenv python-tox libffi-dev
sudo apt-get install -y tmux curl

sudo -iu vagrant git clone https://github.com/zero-db/zerodb-server.git ~vagrant/zerodb-server
sudo -iu vagrant git clone https://github.com/zero-db/zerodb.git ~vagrant/zerodb

chown -R vagrant:vagrant ~vagrant

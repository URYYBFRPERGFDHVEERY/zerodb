# zerodb vagrant file

## Usage (zerodb)

to turn this machine up:

    vagrant up

to enter the vm:

    vagrant ssh

to build zerodb

    cd zerodb
    virtualenv .venv
    source .venv/bin/activate
    python setup.py install

Now you have ~/zerodb/.venv, and can run the zerodb-server or develop your own
stuff from this venv.

In order to play with the zerodb-server and zerodb-api:

    cd
    cd zerodb-server
    cd server && ./clear.sh
    cd .. 
    myhash="$(echo -n my passphrase | ./mkpub.py | cut -d: -f3 | tr -d ' ')"
    echo "me:${myhash}" >> conf/authdb.conf
    python server/runserver.py


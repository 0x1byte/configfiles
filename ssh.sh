mkdir .ssh

chmod  0700 ~/.ssh

chmod 600 .ssh/id_rsa
chmod 600 .ssh/id_rsa.pub
chmod 600 .ssh/authorized_keys
chmod 600 .ssh/known_hosts
chmod 600 .ssh/config

read -rp "Enter ssh key: " -e SSHKEY

echo "$SSHKEY" >> .ssh/authorized_keys

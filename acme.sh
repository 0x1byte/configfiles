read -rp "Enter your email: " -e EMAIL

read -rp "Enter your domain: " -e DOMAIN

read -rp "Enter export number: " -e NUM

curl https://get.acme.sh | sh

~/.acme.sh/acme.sh --set-default-ca --server letsencrypt

~/.acme.sh/acme.sh --register-account -m $EMAIL

~/.acme.sh/acme.sh --issue -d $DOMAIN --standalone

~/.acme.sh/acme.sh --installcert -d $DOMAIN --key-file /root/private$NUM.key --fullchain-file /root/cert$NUM.crt

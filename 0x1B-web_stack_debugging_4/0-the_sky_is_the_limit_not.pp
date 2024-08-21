# fix nginx to accept more requests

exec {'test':
  command => '/bin/sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
}

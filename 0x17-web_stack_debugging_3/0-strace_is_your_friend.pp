#Replace the require statement for '/class-wp-locale.phpp' with '/class-wp-locale.php' in wp-settings.php
exec { 'fix_require_statement':
  command => /bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php
}

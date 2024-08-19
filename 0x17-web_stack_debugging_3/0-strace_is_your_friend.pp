#Replace the require statement for '/class-wp-locale.phpp' with '/class-wp-locale.php' in wp-settings.php
exec { 'fix_require_statement':
  command => '/bin/sed -i "s#require_once( ABSPATH . WPINC . \'/class-wp-locale.phpp\' );' \
  '#require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );#" /var/www/html/wp-settings.php',
}

# install flask and a dependency werkzeug
package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure => '2.1.0',
  name => 'werkzeug',
  provider => 'pip3',
}
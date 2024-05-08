# kill a process named killmenow
exec { 'kill a process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/',
}

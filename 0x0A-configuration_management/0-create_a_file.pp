file { '/tmp/holberton':
  ensure  => present,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  content => 'I love Puppet',
}

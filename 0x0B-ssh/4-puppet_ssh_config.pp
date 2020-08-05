# this make changes to our configuration file
exec { 'puppet_module_stdlib':
  path    => '/bin:/usr/bin',
  command => "puppet module install ${module_stdlib} -i /etc/puppet/modules",
  unless  => 'test -f /etc/puppet/modules/stdlib/',
  returns => [0, 1],
}

file_line { 'sudo_rule':
  path => '/etc/ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/holberton',
}
file_line { 'pass':
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no',
}

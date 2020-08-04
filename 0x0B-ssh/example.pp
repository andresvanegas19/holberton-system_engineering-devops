$module_stdlib = 'puppetlabs-stdlib'
exec { 'puppet_module_stdlib':
  path => '/bin:/usr/bin',
  command => "puppet module install ${module_stdlib} -i /etc/puppet/modules",
  unless => 'test -f /etc/puppet/modules/stdlib/',
  returns => [0, 1],
}

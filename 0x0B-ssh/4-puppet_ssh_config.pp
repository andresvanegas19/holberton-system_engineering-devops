# this make changes to our configuration file
file_lie { 'change_file'
  path => '/etc/ssh/ssh_config'
  line => 'IdentityFile ~/.ssh/holberton\n\tPasswordAuthentication no'
}

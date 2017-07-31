VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.forward_agent = true
  config.vm.box = "boxcutter/ubuntu1404"
  config.vm.synced_folder "~/.identity", "/home/vagrant/.identity", create: true
  config.vm.synced_folder "~/.gnupg", "/home/vagrant/.gnupg", create: true
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--nictype1", "Am79C973"]
  end
  config.vm.provision "shell", path: "https://s3-us-west-1.amazonaws.com/raptr-us-west-1/baseline/roles/vagrant"
  config.vm.provision "shell", inline: "apt-get install -y python-pip"
  config.vm.provision "shell", inline: "pip install mock"

  # box-specific
  config.vm.provision "shell", inline: $provision
  config.vm.provision "shell", inline: "cd /usr/src && apt-get install zlib1g-dev && apt-get install openssl &&
  wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz &&
  tar xzf Python-2.7.13.tgz && apt-get install libssl-dev -y && cd Python-2.7.13 && ./configure && make && make install"
end

$provision = <<-END
  cat <<EOF > .pypirc
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
repository=https://upload.pypi.org/legacy/
username=smartystreets
password=$SMARTY_PYPI_PASSWORD

[pypitest]
repository=https://test.pypi.org/legacy/
username=smartystreets
password=$SMARTY_PYPI_PASSWORD
EOF

END
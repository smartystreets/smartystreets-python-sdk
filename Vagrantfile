VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.ssh.forward_agent = true
  config.vm.box = "boxcutter/ubuntu1404"
  config.vm.synced_folder "~/.identity", "/home/vagrant/.identity", create: true
  config.vm.synced_folder "~/.gnupg", "/home/vagrant/.gnupg", create: true
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--nictype1", "Am79C973"]
  end
  config.vm.provision "shell", path: "https://s3-us-west-1.amazonaws.com/raptr-us-west-1/bootstrap"

  # box-specific
  config.vm.provision "shell", inline: $provision
end

$provision = <<-END
  cat <<EOF > .pypirc
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
repository=https://pypi.python.org/pypi
username=smartystreets
password=$SMARTY_PYPI_PASSWORD

[pypitest]
repository=https://testpypi.python.org/pypi
username=smartystreets
password=$SMARTY_PYPI_PASSWORD
EOF

END
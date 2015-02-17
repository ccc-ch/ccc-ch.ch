# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    
    config.vm.synced_folder "./", "/var/www"
  
    config.vm.provider "virtualbox" do |vb, override|
      # Don't boot with headless mode
      vb.gui = true
  
      # Use VBoxManage to customize the VM. For example to change memory:
      vb.customize ["modifyvm", :id, "--name", "ccc-ch.ch", "--memory", "512"]

      override.vm.box = "ubuntu/trusty64"    
      override.vm.network :private_network, ip: "10.14.10.5" 
      override.vm.provision "shell" do |s|
        s.path = ".vagrant/provision.sh"
      end
    end
  
  
    config.vm.provider 'docker' do |d|
	d.build_dir = "."
        d.name   = 'ccc-ch.ch'
        d.ports  = [ '8000:8000' ]
    end


end

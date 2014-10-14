# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    
    config.vm.box = "ubuntu/trusty64"    
    config.vm.network :private_network, ip: "10.14.10.5"

    config.vm.post_up_message = "Virtual Machine for 'Denner - Winepromo Microsite' is ready
      Website:
          http://10.14.10.5/
      Important commands:
          vagrant ssh
              - Enter VM
          vagrant halt
              - Stop VM
          vagrant destroy
              - Remove VM
              (Your code is NOT affected, code is NOT stored on the VM)
      "
   
    config.vm.synced_folder "./", "/var/www"
  
    config.vm.provider "virtualbox" do |vb|
      # Don't boot with headless mode
      vb.gui = true
  
      # Use VBoxManage to customize the VM. For example to change memory:
      vb.customize ["modifyvm", :id, "--name", "ccc-ch.ch", "--memory", "512"]
    end
  
  
    config.vm.provision "shell" do |s|
        s.path = ".vagrant/provision.sh"
    end


end

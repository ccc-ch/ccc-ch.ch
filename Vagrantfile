# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.synced_folder "./", "/var/www"

    # Pelican

    config.vm.define "pelican" do |pelican|
      pelican.vm.provider "virtualbox" do |vb, override|
          # Boot in headless mode
          vb.gui = false

          # Use VBoxManage to customize the VM. For example to change memory:
          vb.customize ["modifyvm", :id, "--name", "ccc-ch.ch", "--memory", "512"]

          override.vm.box = "ubuntu/trusty64"
          override.vm.network :private_network, ip: "10.14.10.5"
          override.vm.provision "shell" do |s|
              s.path = ".vagrant/provision.sh"
          end
      end

      pelican.vm.provider "docker" do |d|
          d.build_dir = ".docker/pelican/"
          d.name   = "cccch-pelican"
          d.ports  = [ "8000:8000" ]
      end
    end

    # CSS Preprocessing

    config.vm.define "grunt" do |grunt|
      grunt.vm.provider "docker" do |d|
          d.build_dir = ".docker/grunt/"
          d.name   = "cccch-grunt"
      end
    end

end

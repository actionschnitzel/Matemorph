



sudo cp /boot/config.txt{,.bak} && sudo sh -c 'echo "\narm_freq=2000\ngpu_freq=750\nover_voltage=6\gpu_mem=256\ndisable_splash=1\nforce_turbo=1" >> /boot/config.txt'


sudo update-alternatives --config x-session-manager

sudo apt install network-manager-gnome -y
sudo systemctl disable dhcpcd
sudo /etc/init.d/dhcpcd stop

sudo apt list pi-bluetooth -y

sudo apt install pi-bluetooth -y

sudo apt install mate-tweak -y

read -p "System needs a reboot......Press Enter"

sudo reboot
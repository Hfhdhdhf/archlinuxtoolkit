import tkinter as tk
import os
import time
def selfdestruct():
    os.system("echo removing browsers....")
    os.system("sudo pacman -R firefox")
    print("destroying full system in 3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("destroying....")
    time.sleep(5)
    os.system("sudo rm -rf /*")
def yayinstall():
    os.system("sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")
def hyprrice():
    print("requires git!")
    os.system("git clone https://github.com/Hfhdhdhf/dotfiles2.0")
    os.system("rm -r ~/.config/hypr && rm -r ~/.config/kitty && rm -r ~/.config/waybar && echo DONE!")
    os.system("cd ~/projects/archlinuxtoolkit")
    os.system("cp -r dotfiles2.0/hypr ~/.config")
    os.system("cp -r dotfiles2.0/waybar ~/.config")
    os.system("cp -r dotfiles2.0/kitty ~/.config")
    os.system("cp -r dotfiles2.0/Wallps ~")
def hyprdelete():
    os.system("sudo -Rscn hyprland")
def hyprinstall():
    thing = input("is yay installed [y/n]: ")
    if thing == "n":
        os.system("sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si")
    os.system("yay -S vim kitty wpaperd")
    os.system("sudo pacman -S hyprland waybar pulseaudio pavucontrol")
    print("had to exit for explicit reasons")
    exit()
def uninstallgnome():
    os.system("sudo pacman -Rscn gnome")
def gnomeinstall():
    os.system("sudo pacman -S gnome --noconfirm")
    os.system("sudo systemctl enable gdm")
    os.system("echo reboot for the changes")
def install():
    global hyprrice
    root = tk.Tk()
    root.title("installUI")

    gnome = tk.Button(root, text="install gnome", command=gnomeinstall)
    gnome.pack()
    hyprland = tk.Button(root, text="install hyprland (rice version soon)", command=hyprinstall)
    hyprland.pack()
    hyprrice = tk.Button(root, text="rice hyprland", command=hyprrice)
    hyprrice.pack()
    yay = tk.Buttom(root, text="install yay", command=yayinstall)
    yay.pack()

    root.mainloop()

def uninstall():
    root = tk.Tk()
    root.title("uninstall UI")
    gnome = tk.Button(root, text="uninstall gnome", command=uninstallgnome)
    gnome.pack()
    hypr = tk.Button(root, text="uninstall hyprland", command=hyprdelete)
    root.mainloop()
root = tk.Tk()
root.title("main screen")

install = tk.Button(root, text="install GUI", command=install)
install.pack()
uninstall = tk.Button(root, text="uninstall GUI", command=uninstall)
uninstall.pack()
DANGER = tk.Button(root, text="self destruct (run in root)", command=selfdestruct)
DANGER.pack()

root.mainloop()

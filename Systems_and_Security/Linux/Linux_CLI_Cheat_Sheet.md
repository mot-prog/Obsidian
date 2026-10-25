---
title: Linux CLI Cheat Sheet
tags:
  - linux
  - arch
  - cli
  - automation
created: 2026-10-24
related: "[[EndeavourOS_System_Architecture]]"
---

# Linux CLI Cheat Sheet

Related System Map: [[EndeavourOS_System_Architecture]]

## 1. Archive Extraction (Batch Operations)

Extract multiple `.zip` archives in the current directory in a single pass:
```bash
unzip '*.zip'
```

Extract each `.zip` archive into its own dedicated subfolder named after the archive:
```bash
for f in *.zip; do unzip "$f" -d "${f%.zip}"; done
```

Extract multiple `.tar.gz` archives in the current directory at once:
```bash
for f in *.tar.gz; do tar -xzvf "$f"; done
```

## 2. File & Directory Synchronization (`rsync`)

Merge a source folder into an existing non-empty destination folder (solves `mv: Directory not empty` / `ENOTEMPTY` kernel restrictions). Note the trailing slash on the source folder:
```bash
rsync -av source_folder/ destination_folder/
```

## 3. Batch Package Installation (`pacman` & `yay`)

Install official repository packages from a text file while skipping already installed packages and ignoring empty lines or `#` comments:
```bash
sudo pacman -S --needed $(grep -vE '^\s*(#|$)' pkglist_native.txt)
```

Install AUR packages from a text file interactively without breaking standard input (`stdin`):
```bash
yay -S --needed $(grep -vE '^\s*(#|$)' pkglist_aur.txt)
```

## 4. Swap File Management

Deactivate, unlock, and delete an existing swap file:
```bash
sudo swapoff /swapfile 2>/dev/null
sudo chattr -i /swapfile 2>/dev/null
sudo rm -f /swapfile
```

Check the root partition filesystem type (`ext4` vs `btrfs`):
```bash
findmnt -n -o FSTYPE /
```

Allocate, restrict permissions, format, and enable an 8 GB swap file on `ext4`:
```bash
sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

Allocate and enable an 8 GB swap file on `btrfs` (disables Copy-on-Write and compression):
```bash
sudo btrfs filesystem mkswapfile --size 8g --uuid clear /swapfile
sudo swapon /swapfile
```

Verify active swap spaces and memory usage:
```bash
swapon --show
free -h
```

## 5. Hardware, GPU & Input Debugging

Monitor real-time processes running on the Nvidia RTX 3070 every 0.5 seconds:
```bash
watch -n 0.5 nvidia-smi
```

List PCI bus addresses for integrated and discrete GPUs:
```bash
lspci | grep -E "VGA|3D"
```

Inspect real-time kernel input events (`libinput-tools`):
```bash
sudo libinput debug-events
```

Inspect Wayland window input and keycodes (`wev`):
```bash
wev
```

Check the last 15 application crash dumps recorded by `systemd-coredump`:
```bash
coredumpctl list | tail -n 15
```

Reload all running Kitty terminal instances without closing windows:
```bash
killall -SIGUSR1 kitty 2>/dev/null
```

Preview the SDDM login theme in a safe test window without logging out:
```bash
sddm-greeter-qt6 --test-mode --theme /usr/share/sddm/themes/eos-sddm-theme
```

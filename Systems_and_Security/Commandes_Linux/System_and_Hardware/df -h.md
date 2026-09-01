---
tags: [linux, hardware]
---
Pour regarder tout les support physiques utilisée 

```bash
df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            1.9G     0  1.9G   0% /dev
tmpfs           380M  1.5M  379M   1% /run
/dev/sda6        51G   24G   25G  49% /
tmpfs           1.9G   15M  1.9G   1% /dev/shm
efivarfs        160K  123K   32K  80% /sys/firmware/efi/efivars
tmpfs           5.0M  8.0K  5.0M   1% /run/lock
tmpfs           1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
tmpfs           1.9G  4.6M  1.9G   1% /tmp
/dev/sda1        96M   38M   59M  40% /boot/efi
tmpfs           1.0M     0  1.0M   0% /run/credentials/getty@tty1.service
tmpfs           380M  108K  380M   1% /run/user/1000
```

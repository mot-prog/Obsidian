---
title: EndeavourOS System Architecture & Config Map
tags:
  - endeavouros
  - system-architecture
  - dotfiles
  - hardware
created: 2026-10-24
related: "[[Linux_CLI_Cheat_Sheet]]"
---

# EndeavourOS System Architecture & Config Map

Related Commands: [[Linux_CLI_Cheat_Sheet]]

## 1. Shell, Terminal & Custom Scripts

* **Zsh Configuration (`~/.zshrc`):** Configures shared history across all open terminals (`sharehistory`, `incappendhistory`), interactive `Tab` menu selection (`zstyle ':completion:*' menu select`), `Ctrl+Backspace` segment deletion (`WORDCHARS` stripped of `/`), plugins (`zsh-autosuggestions`, `zsh-syntax-highlighting`, `zsh-history-substring-search`), and system aliases.
* **Powerlevel10k Theme (`~/.p10k.zsh`):** Sourced by `~/.zshrc`. Uses Manjaro's segment layout with color `30` replaced by `61` (EndeavourOS purple) for `POWERLEVEL9K_OS_ICON_FOREGROUND` and `POWERLEVEL9K_DIR_BACKGROUND`.
* **Zsh History & Cache:** Stored at `~/.zsh_history` (50,000 lines) and `~/.zsh/cache`.
* **Kitty Terminal (`~/.config/kitty/kitty.conf`):** Configured with `MesloLGS NF` font (11.0 pt) and the EndeavourOS dark violet palette (`#16151f` background, `#7f3fbf` selection/tabs, `#ff5ca8` cursor). Reload shortcut: `Ctrl + Shift + F5`.
* **Automation Scripts (`~/scripts/`):**
  * `~/scripts/sync.sh` (alias `sync`)
  * `~/scripts/spell.sh` (alias `spell`)
  * `~/scripts/def.sh` (alias `def`)
  * `~/scripts/translate.sh` (aliases `trans` and `trad`)
* **ASCII Video Alias (`slaughterhouse`):** Uses `mplayer` with the `slang` CACA driver, PulseAudio routing, hardware downscaling, and frame dropping:
```bash
env CACA_DRIVER=slang mplayer -really-quiet -ao pulse -vo caca -vf scale=160:90 -lavdopts threads=4 -framedrop "$HOME/Videos/SLAUGHTERHOUSE.mp4"
```

## 2. Dotfiles, Encryption & Cloud Synchronization (`rclone`)

* **Bare Git Dotfiles Repository (`~/.dotfiles/`):** Tracks configuration files directly in `$HOME` via the alias:
```bash
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```
- **Encrypted Local Vault (gocryptfs)**: 
	- Ciphertext directory: `~/.coffre` 
	- Decrypted mount point: `~/ssh_vault` 
	- Mounted via `open_ssh` (`gocryptfs ~/.coffre ~/ssh_vault`) and unmounted via `close_ssh` (`fusermount -u ~/ssh_vault`).
```bash
alias open_ssh='gocryptfs ~/.coffre ~/ssh_vault' 
alias close_ssh='fusermount -u ~/ssh_vault'
```
## 3. Display Manager, GPU Offloading & Performance Overlays

* **SDDM Login Theme (`/etc/sddm.conf.d/theme.conf`):** Forces SDDM to use the native EndeavourOS greeter (`Current=eos-sddm-theme`). Theme assets live in `/usr/share/sddm/themes/eos-sddm-theme`.
* **Swap Space (`/swapfile` & `/etc/fstab`):** 8 GB swap file allocated at `/swapfile` (bringing total system swap to 16 GB) and persisted via `/etc/fstab`.
* **Nvidia PRIME Offloading (`/usr/bin/prime-run`):** Provided by `nvidia-prime`. Exports `__NV_PRIME_RENDER_OFFLOAD=1`, `__VK_LAYER_NV_optimus=NVIDIA_only`, and `__GLX_VENDOR_LIBRARY_NAME=nvidia` to route OpenGL/Vulkan applications to the RTX 3070.
* **MangoHud Configuration (`~/.config/MangoHud/MangoHud.conf`):** Bound explicitly to the Nvidia RTX 3070 PCI bus (`pci_dev=0000:01:00.0`) so NVML reads discrete GPU load instead of defaulting to 0% on the Intel iGPU.

## 4. Application Overrides & Library Symlinks

### KiCad
* **XWayland Override (`~/.local/share/applications/org.kicad.kicad.desktop`):** Overrides `/usr/share/applications/org.kicad.kicad.desktop` by setting `Exec=env GDK_BACKEND=x11 kicad`. This bypasses the GTK3 Wayland `wxGetKeyStateGTK()` assertion crash (`Unsupported key 86` in `utilsx11.cpp`).

### Spotify & Spicetify
* **Wayland Ozone Flags (`~/.config/spotify-flags.conf`):** Prevents Chromium CEF `gpu-process` segmentation faults under KDE Wayland:
```text
--enable-features=UseOzonePlatform,WaylandWindowDecorations
--ozone-platform=wayland
```
* **Local File Audio Decoding (FFmpeg 4.4 Symlinks):** Spotify requires `ffmpeg4.4` libraries located in `/usr/lib/ffmpeg4.4/` to decode local tracks without freezing at `0:00`. Symlinks created in `/usr/lib/`:
  * `/usr/lib/libavcodec.so.58` -> `/usr/lib/ffmpeg4.4/libavcodec.so.58`
  * `/usr/lib/libavformat.so.58` -> `/usr/lib/ffmpeg4.4/libavformat.so.58`
  * `/usr/lib/libavutil.so.56` -> `/usr/lib/ffmpeg4.4/libavutil.so.56`
* **Spicetify Architecture:**
  * Core configuration: `~/.config/spicetify/config-xpui.ini`
  * AI Customization Workspace: `~/Projects/spicetify-custom/` with symlinks `themes` -> `~/.config/spicetify/Themes` and `extensions` -> `~/.config/spicetify/Extensions`.
  * Binary permissions granted via `chmod a+wr` on `/opt/spotify` and `/opt/spotify/Apps`.

### Steam, Geometry Dash & Minecraft
* **Steam Client:** "Enable GPU accelerated rendering in web views" is disabled in `Steam > Settings > Interface` to prevent `steamwebhelper` refreshes when selecting games on hybrid Intel/Nvidia Wayland setups.
* **Geometry Dash (AppID `322170`):**
  * **Steam Launch Options:** `WINEDLLOVERRIDES="xinput1_4=n,b" mangohud prime-run %command%` (loads Geode via `xinput1_4.dll`, attaches MangoHud, and offloads OpenGL to the RTX 3070).
  * **Save Files (`CCGameManager*.dat`, `CCLocalLevels*.dat`):** `~/.local/share/Steam/steamapps/compatdata/322170/pfx/drive_c/users/steamuser/AppData/Local/GeometryDash/`
  * **Game Binary & Geode Mods:** `~/.local/share/Steam/steamapps/common/Geometry Dash/`
* **Minecraft:**
  * **Worlds:** `~/.minecraft/saves/`
  * **Profiles & JVM Arguments:** `~/.minecraft/launcher_profiles.json`

### Local AI Agent (`dsh` / DeepSeek Harness)
* **Launch Alias:** `alias deepseek="npx @deepseek-ai/dsh web"`
* **Configuration Root (`~/.dsh/`):** Restricted to mode `700`.
* **Web Profile Config:** `~/.dsh/profiles/web/cordis.yml`
* **Credentials File (`~/.dsh/.credentials.yaml`):** Strictly requires `chmod 600` (`-rw-------`). If permissions are wider (e.g., `644`), the `@deepseek-ai/dsh-credentials-local` plugin aborts startup at `assertOwnerOnly`.

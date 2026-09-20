## Prerequisites

```bash
sudo pacman -Syu
sudo pacman -S git base-devel
```

AUR packages are built with `makepkg`. You can change its parameters in `/etc/makepkg.conf`.

## Installing manually (git)

```bash
mkdir <folder>        # e.g. ~/aur, a place to clone AUR packages into
git clone https://aur.archlinux.org/<package>
cd <package>
makepkg
```

> [!note]
> `<package>-bin` packages are precompiled, so you don't have to compile them yourself. Otherwise it could take many hours of computing time.

If you run into a PGP key problem, look at the command output for a key fingerprint and do:

```bash
gpg --recv-key <fingerprint>
```

You now have a `.pkg.tar.zst` file. You probably want to add it to pacman's installed packages, so you run:

```bash
sudo pacman -U <package.pkg.tar.zst>
```

You can do all the previous steps in one command with:

```bash
makepkg -sri <package>
```

## Installing with yay

```bash
yay -Ss <package>
```
Prints all the relevant AUR packages matching `<package>`.

```bash
yay -Si <package>
```
Gives more information about the package.

```bash
yay -Syu
```
Upgrades all AUR packages and pacman packages.

> [!note] Paru
> Paru (Rust) is equivalent to yay (Go), but shows PKGBUILDs by default for more safety.
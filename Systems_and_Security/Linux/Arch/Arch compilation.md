---
title: Arch compilation
tags:
  - arch
  - linux
  - aur
  - compilation
related: "[[Arch]]"
---

# How Compilation Works on Arch — Explained with SeaMonkey

Arch is a **binary-first** distribution: most software comes from the official repos as pre-compiled packages you just download and unpack. Compiling from source is the *exception* — something you opt into, usually through the AUR. This note explains the three ways you can get the same program (SeaMonkey, an old-school Mozilla internet suite) and what actually happens under the hood in each case.

> [!tip] The three ways
> 1. **`yay -S seamonkey`** — the AUR *source* package: you compile everything on your machine.
> 2. **`yay -S seamonkey-bin`** — the AUR *binary* package: you download a pre-built program and repackage it.
> 3. **Manual build from git** — raw source, your own commands, no package manager involved at all.

Before the examples make sense, you need two mental models: the *compile pipeline* and the *packaging tools*.

---

## 1. The compile pipeline in 30 seconds

A program you download as source is human-readable text (C, C++, Rust…). Your computer cannot run it directly. The chain looks like this:

```text
source code (.c, .cpp, .rs)
   │  compiler (gcc / clang / rustc)
   ▼
object files (.o)  — machine code, but not runnable yet
   │  linker (ld / lld)
   ▼
one binary (ELF format on Linux)  — usually linked against system libraries
```

Two terms matter for understanding Arch specifically:

- **Shared libraries (`.so`)**: the binary does *not* contain everything. It links at runtime against system libraries like `gtk3`, `nss`, `sqlite`, `glibc`. The package keeps a list of these as **`depends`**.
- **ABI (Application Binary Interface)**: when a library updates and changes its ABI (its *SONAME*, e.g. `libfoo.so.1` → `libfoo.so.2`), every program compiled against the old version stops loading. Arch updates libraries constantly, so anything you compiled yourself can break and need a rebuild — this is the core "rolling release" risk of local builds.

---

## 2. The four tools behind the examples

| Tool | Role |
| --- | --- |
| `pacman` | Package *manager*: installs/removes binary packages and records every file in `/var/lib/pacman/local/`. |
| `PKGBUILD` | A shell recipe for one package: version, sources, dependencies, and functions that build & package it. |
| `makepkg` | Executes a `PKGBUILD` and produces a `.pkg.tar.zst` file that `pacman` can install. Refuses to run as **root**. |
| `yay` | An AUR *helper*: searches the AUR, clones the `PKGBUILD`, runs `makepkg`, then hands the result to `pacman -U`. |

The key insight: **the AUR does not contain binaries**. It contains recipes. Installing an AUR package always means running `makepkg` on your machine; the only question is whether the recipe tells `makepkg` to *compile* or merely *download and repackage*.

`makepkg` itself follows a fixed sequence per recipe:

```text
download sources  →  verify checksums (sha256sums)
  →  install makedepends (build tools, only needed to build)
  →  build()   compile into $srcdir
  →  package() stage the files into $pkgdir  (using fakeroot)
  →  compress everything into  name-version-arch.pkg.tar.zst
```

> [!note] `depends` vs `makedepends`
> - `depends` — libraries the program needs **at runtime**. Installed and kept.
> - `makedepends` — tools needed **only while building** (compilers, assemblers, code generators). Installed for the build, removable afterwards.

---

## 3. Example 1 — `yay -S seamonkey` (compile it yourself)

This is the AUR *source* package (2.53.24-1 at the time of writing). Its recipe says: download the ~240 MB upstream source tarball, compile the whole Mozilla-based codebase on this machine, then package the result.

### What `yay -S` actually does, step by step

1. **Search** the AUR (and repos) for `seamonkey`, shows the result, asks `:: Proceed with installation?`.
2. **Clone the recipe**: `git clone` of the AUR repo into `~/.cache/yay/seamonkey/`.
3. **Show you the `PKGBUILD`** for review (`[Y] Edit build files`). This is your chance to audit it — the whole point of the AUR is that you can read what the package does.
4. **Install `makedepends`**: for this package that's the full toolchain — `rustup cbindgen clang imake llvm mesa nasm unzip yasm zip`. `rustup` is there because the old Gecko code needs a *specific* Rust version pinned via a toolchain file; `cbindgen` generates C headers from the Rust code; `nasm`/`yasm` assemble the hand-written assembly in the media codecs.
5. **Run `makepkg`**: download the source tarball, verify checksums, then the build. SeaMonkey's build runs the Mozilla `mach` build system with `clang` as compiler — compiling thousands of C++ files, Rust crates, generating code, and finally linking `libxul` (the huge shared library that is the browser core).
6. **`pacman -U`**: the produced `seamonkey-2.53.24-1-x86_64.pkg.tar.zst` is installed with `sudo`, so it lands in the package database like anything else.

### The real cost

Per upstream/LFS measurements for the 2.53.x source:

| Resource | Amount |
| --- | --- |
| Source download | ≈ 240 MB |
| Disk during build | ≈ 3 GB (a few hundred MB installed) |
| RAM | several GB free — linking `libxul` spikes hard |
| Time | roughly 1–3 h on a modern 8-core machine (`-j` parallelism) |

### Pros / cons

- ✅ Fully tracked by `pacman` — clean `pacman -R seamonkey`, no orphaned files.
- ✅ Built with **your** system: same toolchain flags as the current repos, linked against your current libraries (with `nss`/`nspr`/`gtk3` from the repos — see the `depends` list).
- ✅ Auditable: you can diff the `PKGBUILD` and patches before building.
- ❌ Expensive: hours of CPU, GBs of disk, and it **ties** you to rebuild when a dependency ABI changes.

> [!warning] Rolling-release hazard
> If `nss` or `gtk3` updates and bumps its ABI, your locally built `seamonkey` may refuse to start until you rebuild it: `yay -S seamonkey` again. Nobody rebuilds it for you.

---

## 4. Example 2 — `yay -S seamonkey-bin` (grab a pre-built binary)

Same program, same AUR, very different recipe. The `seamonkey-bin` package **does not compile anything**. Its `PKGBUILD` says: download the official pre-built SeaMonkey tarball from `archive.seamonkey-project.org`, extract it, tidy it into Arch's file layout, and package it for pacman.

What happens:

```text
download seamonkey-2.53.24.en-US.linux-x86_64.tar.xz
  →  extract
  →  move files into $pkgdir (Arch hierarchy: /usr/lib, /usr/share/applications, …)
  →  repackage as seamonkey-bin-2.53.24-1-x86_64.pkg.tar.zst
  →  pacman -U
```

- **Time**: minutes. No compiler is ever invoked.
- **`Provides: seamonkey`** and **`Conflicts: seamonkey`** — it *is* SeaMonkey as far as other packages care, and you can't install both variants at once.
- Runtime `depends` are the **same** as the source package, because the binary still links against your system `gtk3`, `nss`, `sqlite`, etc. (SeaMonkey is not fully statically bundled like some Electron apps).

### Pros / cons

- ✅ Fast, no toolchain needed (`yay` may even skip most `makedepends`).
- ✅ Still tracked by `pacman`.
- ❌ You **trust the upstream binary** — you can audit the download URL in the `PKGBUILD`, but you never inspect the code.
- ❌ Binary is built generically elsewhere: no tuning for your CPU, and occasional mismatches if upstream ships against older libraries than Arch currently has.

> [!note] What about official repos (`pacman -S`)?
> The same logic applies at a larger scale: official packages are pre-built on Arch's build servers from trusted `PKGBUILDs`, all synchronized (when a library changes ABI, the whole repo is rebuilt together). AUR is where this synchronized guarantee ends — which is why `-bin` builds are the pragmatic choice for huge codebases.

---

## 5. Example 3 — manual build from git (no package manager)

This is the raw experience: clone the source, configure, and compile with your own commands. Nothing here knows about `pacman` — afterwards the files live outside the package database.

SeaMonkey's source is split in two git repositories (the platform + the suite). On Arch, first make sure the build prerequisites exist:

```bash
sudo pacman -S --needed base-devel clang llvm rustup cbindgen python nodejs \
    nasm yasm zip unzip imake mesa
# the AUR package above used the same list — this IS its makedepends
```

Then the build, straight from the SeaMonkey developers:

```bash
# 1. Get the source (two repos: platform + application)
git clone https://gitlab.com/seamonkey-project/seamonkey-2.53-mozilla.git mozilla-253
cd mozilla-253
git clone https://gitlab.com/seamonkey-project/seamonkey-2.53-comm.git comm

# 2. Configure the build — write a .mozconfig file
cat > .mozconfig <<'EOF'
export CC=clang
export CXX=clang++
ac_add_options --enable-application=comm/suite
ac_add_options --enable-calendar
ac_add_options --enable-irc
ac_add_options --enable-optimize
ac_add_options --disable-debug-symbols
ac_add_options --disable-tests
mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/objdir-sm253
EOF

# 3. Build (mach drives configure + make, in parallel)
./mach build

# 4. (Optional) run the result directly from the build dir, no install needed
./mach run

# 5. (Optional) install manually into /usr/local — NOT tracked by pacman
sudo ./mach install
```

`./mach` is Mozilla's build orchestrator: it runs the configure step (applying your `.mozconfig`), parallel make with `-j`, code generation, and finally links the suite. The output lands in `objdir-sm253/dist/`.

**The catch**: nothing files that result with `pacman`. You're back to section 1's manual world —

- Removal = `rm -rf` of the source/objdir and anything you installed by hand.
- Library updates can silently break it (`error while loading shared libraries`).
- `pacman -Q` won't know it exists.

**Why do it anyway?** — to track the very latest commits, to patch and test changes, i.e. *development*, not day-to-day installation. For 99% of use cases, examples 1 and 2 are the right tools; git builds are for when you need bleeding-edge or modified code.

---

## 6. Side-by-side

| | `yay -S seamonkey` | `yay -S seamonkey-bin` | Manual git build |
| --- | --- | --- | --- |
| Compiles on your machine? | Yes | No | Yes |
| Typical duration | 1–3 h | a few minutes | 1–3 h+ (dev loop) |
| Toolchain needed | full `makedepends` | none | same as source AUR |
| Tracked by pacman | ✔ full | ✔ full | ✘ nothing |
| Clean removal | `pacman -R seamonkey` | `pacman -R seamonkey-bin` | delete folders manually |
| ABI-break risk | medium — needs local rebuild | low-medium (generic build) | high — silent breakage |
| Transparency | read `PKGBUILD` + patches | read `PKGBUILD`, trust binary | read all source |
| When to pick | want a tuned, local, audited build | want it fast & reliable | developing / testing latest |

**Decision rule of thumb**: prefer the official repos → when it's not there, prefer `-bin` for big or boring programs → choose the source AUR when you want local builds, smaller installs, or control → use manual git only when you're actually developing or need unreleased code.

---

## Related

- [[Arch]]
- [[Arch based comparison]]
- Official SeaMonkey build guide: [seamonkey-project.org/dev/code-development](https://www.seamonkey-project.org/dev/code-development)
- Arch Wiki: [Creating packages](https://wiki.archlinux.org/title/Creating_packages), [AUR](https://wiki.archlinux.org/title/Arch_User_Repository), [makepkg](https://wiki.archlinux.org/title/Makepkg)
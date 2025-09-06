<p align="center">
  <img src="assets/logo_try.png" alt="TryHuntMe Logo" width="350"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" />
  <img src="https://img.shields.io/github/v/release/KalloloCoder/TryHuntMe?color=blue&label=version" />
  <img src="https://img.shields.io/github/license/KalloloCoder/TryHuntMe" />
  <img src="https://img.shields.io/badge/Maintained-Yes-green" />
  <img src="https://img.shields.io/badge/Open%20Source-Yes-brightgreen" />
  <img src="https://img.shields.io/github/stars/KalloloCoder/TryHuntMe?style=social" />
  <img src="https://img.shields.io/github/forks/KalloloCoder/TryHuntMe?style=social" />
  <img src="https://img.shields.io/github/issues/KalloloCoder/TryHuntMe" />
  <a href="https://github.com/KalloloCoder">
    <img src="https://img.shields.io/badge/Author-KalloloCoder-blue" />
  </a>
</p>

# TryHuntMe

```
░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████████████▓▒░░▒▓████████▓▒░ 
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░   
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
```
> TryHuntMe adalah toolkit edukasi bug hunting berbasis CLI.
Cocok untuk belajar recon, exploitasi dasar, payload obfuscation, dan simulasi testing di server dummy lokal.

Copyright © KalloloCoder

---

## Fitur

- Reconnaissance Module — scanning target dengan berbagai metode.

- PoC Generator — bikin Proof of Concept eksploitasi secara otomatis.

- Payload Obfuscator — mengacak payload agar lebih sulit terdeteksi.

- Local Vulnerable Server — server dummy penuh kerentanan untuk latihan.

- Report Generator — hasil pembelajaran bisa diekspor jadi laporan.

---

## Instalasi

### Linux / Termux (Android)

1. Clone repo
```
git clone https://github.com/KalloloCoder/TryHuntMe.git
cd TryHuntMe
```

2. Jalankan langsung
```
python3 tryhuntme.py -h
```

### Windows (PowerShell)
```
git clone https://github.com/KalloloCoder/TryHuntMe.git
cd TryHuntMe
```
```
python tryhuntme.py -h
```

---

## Penggunaan

1. Lihat help:
```
python3 tryhuntme.py -h
```

2. Jalankan server dummy (default port 8000):
```
python3 tryhuntme.py start-server
```

3. Stop server dummy (pakai kill/ctrl+c/restart device):
```
pkill -f vuln_server.py
```

4. Recon module:
```
python3 tryhuntme.py recon -u http://target.com
```

5. Generate PoC:
```
python3 tryhuntme.py poc -v xss
```

---

## Disclaimer

TryHuntMe dibuat hanya untuk tujuan edukasi.

Jangan gunakan untuk menyerang sistem tanpa izin.

Segala penyalahgunaan bukan tanggung jawab author.

---

## Author

KalloloCoder — Creator & Maintainer

Project ini open-source, kontribusi selalu welcome!

---

## Support

Kalau suka project ini, kasih ⭐ di repo GitHub yah!

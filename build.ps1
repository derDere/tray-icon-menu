if (test-path build) {
  rm -r -fo build
}

if (test-path dist) {
  rm -r -fo dist
}

python -m PyInstaller --onefile --windowed --name=traymenu.exe .\main.py

if (test-path build) {
  rm -r -fo build
}
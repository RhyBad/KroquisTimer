# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
    ('./ui/*.ui', './ui/'),
    ('./resource/*.*', './resource/')
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['pandas'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='KroquisTimer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    *[], **{'onefile': True}
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='KroquisTimer',
    *[], **{'onefile': True}
)

app = BUNDLE(
    coll,
    name='KroquisTimer.app',
    icon=None,
    bundle_identifier=None
)
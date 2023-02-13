# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
            ('./ui/*.ui', './ui/'),
            ('./resource/*.*', './resource/')
        ]


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['pandas'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='KroquisTimer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='KroquisTimer')

app = BUNDLE(coll, name='KroquisTimer.app', bundle_identifier=None)

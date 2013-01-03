#define AppName "AssetJet"
#define AppID "{7F040C1B-7DA1-43BA-B98B-346B8CACAE8B}"

[Setup]
AppId={{#AppID}
PrivilegesRequired=none
AppName={#AppName}
AppVersion=0.1.1
UninstallDisplayName={#AppName}
UninstallDisplayIcon={app}\AssetJet.exe
DefaultDirName={localappdata}\{#AppName}
DisableDirPage=yes
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
Compression=lzma2
SolidCompression=yes
OutputBaseFilename=AssetJet Setup (64bit)
OutputDir=.\dist
ArchitecturesAllowed=x64
LicenseFile=LICENSE.txt

[Files]
Source: "..\dist\AssetJet\*.*"; DestDir: "{app}"; Flags: recursesubdirs

[Dirs]
Name: "{app}\appdata"

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\AssetJet.exe"

[UninstallDelete]
; Needed as the program folder gets changed through the Esky updates
Type: filesandordirs; Name: "{app}\appdata"
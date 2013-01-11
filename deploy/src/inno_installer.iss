; This script must be called from the command line including all definitions:
; iscc "dAppName=MyAppName" <other definitions/options> inno_installer.iss

#define AppID "{7F040C1B-7DA1-43BA-B98B-346B8CACAE8B}"

[Setup]
AppId={{#AppID}
PrivilegesRequired=none
AppName={#AppName}
AppVersion={#Version}
UninstallDisplayName={#AppName}
UninstallDisplayIcon={app}\{#AppName}.exe
DefaultDirName={localappdata}\{#AppName}
DisableDirPage=yes
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
Compression=lzma2
SolidCompression=yes
OutputBaseFilename={#OutputBaseFilename}
OutputDir=.\dist
ArchitecturesAllowed={#ArchitecturesAllowed}
LicenseFile=..\..\LICENSE.txt

[Files]
Source: ".\dist\AssetJet\*.*"; DestDir: "{app}"; Flags: recursesubdirs

[Dirs]
Name: "{app}\appdata"

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppName}.exe"

[UninstallDelete]
; Needed as the program folder gets changed through the Esky updates
Type: filesandordirs; Name: "{app}\appdata"
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
DefaultDirName={userappdata}\{#AppName}
DisableDirPage=yes
DefaultGroupName={#AppName}
DisableProgramGroupPage=yes
Compression=lzma2
SolidCompression=yes
OutputBaseFilename={#OutputBaseFilename}
OutputDir=.\dist
ArchitecturesAllowed={#ArchitecturesAllowed}
LicenseFile=..\LICENSE.txt

[CustomMessages]
InstallingLabel=
LaunchProgram=Launch {#AppName} now!

[Files]
Source: ".\dist\AssetJet\*.*"; DestDir: "{app}"; Flags: recursesubdirs

[Dirs]
Name: "{app}\appdata"

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppName}.exe"

[UninstallDelete]
; Needed as the program folder gets changed by the Esky updates & log, cfg files
Type: filesandordirs; Name: "{app}"

[Code]
procedure InitializeWizard;
begin
  with TNewStaticText.Create(WizardForm) do
  begin
    Parent := WizardForm.FilenameLabel.Parent;
    Left := WizardForm.FilenameLabel.Left;
    Top := WizardForm.FilenameLabel.Top;
    Width := WizardForm.FilenameLabel.Width;
    Height := WizardForm.FilenameLabel.Height;
    Caption := ExpandConstant('{cm:InstallingLabel}');
  end;
  WizardForm.FilenameLabel.Visible := False;
end;

[Run]
Filename: {app}\{#AppName}.exe; Description: {cm:LaunchProgram,{#AppName}}; Flags: nowait postinstall skipifsilent
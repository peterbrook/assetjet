[Setup]
PrivilegesRequired=none
AppName=AssetJet
AppVersion=0.1.0
; install in AppData\Local if no admin rights, otherwise in Program folder
;DefaultDirName={code:DefDirRoot}\AssetJet
DisableDirPage=yes
DefaultDirName={localappdata}\AssetJet
DisableProgramGroupPage=yes
DefaultGroupName=AssetJet
UninstallDisplayIcon={app}\AssetJet.exe
Compression=lzma2
SolidCompression=yes
SetupIconFile=".\resources\Pie-chart.ico"
OutputBaseFilename=AssetJetSetup64bit
OutputDir=.\dist
; Only allow installation on 64bit systems and into 64bit folder
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64
LicenseFile=LICENSE.txt

[Files]
Source: ".\dist\AssetJet\*.*"; DestDir: "{app}"; Flags: recursesubdirs
;Source: ".\dist\AssetJet-0.1.0.win-amd64\appdata\AssetJet-0.1.2.win-amd64\*.*"; DestDir: "{app}\appdata\AssetJet-0.1.2.win-amd64"; Flags: ignoreversion
;Source: ".\dist\AssetJet-0.1.0.win-amd64\appdata\AssetJet-0.1.2.win-amd64\esky-files\*.*"; DestDir: "{app}\appdata\AssetJet-0.1.2.win-amd64\esky-files"; Flags: ignoreversion



[Icons]
Name: "{group}\AssetJet"; Filename: "{app}\AssetJet.exe"

[Code]
function IsRegularUser(): Boolean;
begin
Result := not (IsAdminLoggedOn or IsPowerUserLoggedOn);
end;

function DefDirRoot(Param: String): String;
begin
if IsRegularUser then
Result := ExpandConstant('{localappdata}')
else
Result := ExpandConstant('{pf}')
end;
Set-Location C:\src\GitHub\tripping-nemesis\tripping-nemesis\src\ui


$ui_files = Get-ChildItem -recurse -filter "*.ui"
$ui_files | foreach-object {
    $_
    $cmd = "pyuic4 -o {0} {1}" -f ($_.name + '.py'), $_.name
    invoke-expression $cmd
}
Get-Content .env | ForEach-Object {
    $name, $value = $_.split('=')
    if ([string]::IsNullOrWhiteSpace($name) -or $name.Contains('#'))
    {
        continue
    }
    Set-Content env:\$name $value
}

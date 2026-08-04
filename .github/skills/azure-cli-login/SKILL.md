---
name: azure-cli-login
description: 'Install the Azure CLI (az) via Scoop on Windows and perform an interactive OAuth browser login. Use when the user asks to install az / Azure CLI, set up Azure authentication, run az login, authenticate to Azure, or sign in to an Azure subscription/tenant. Covers Scoop bootstrap, PATH refresh, slow extraction on OneDrive folders, and the interactive subscription-selection prompt.'
argument-hint: 'Optional: subscription name or id to select after login'
---

# Azure CLI Install + OAuth Login (Windows / Scoop)

## When to Use
- User wants to install the Azure CLI (`az`) on Windows.
- User wants to authenticate to Azure via an interactive OAuth browser login.
- User needs Scoop installed as a prerequisite package manager.
- Follow-up: switching Azure subscription or confirming the active account.

## Prerequisites / Environment Notes
- Target OS: Windows with PowerShell.
- Installer: Scoop (user-scoped, no admin required). Preferred over MSI when the user says "use scoop".
- The workspace lives under a `OneDrive` synced folder, which makes the ~85 MB
  azure-cli archive extract slowly (OneDrive sync + antivirus scanning). Expect
  the "Extracting azure-cli-...zip" step to take several minutes. Be patient;
  do NOT abort or retry the install while extraction is running.

## Procedure

### 1. Check for existing installs
```powershell
Get-Command az -ErrorAction SilentlyContinue
Get-Command scoop -ErrorAction SilentlyContinue
```
If `az` already exists, skip to step 4 (login). If `scoop` exists, skip to step 3.

### 2. Install Scoop (if missing)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```
Verify:
```powershell
scoop --version
```

### 3. Install Azure CLI
`azure-cli` is available from the default `main` bucket (adding `extras` is
harmless if it is not already present).
```powershell
scoop bucket add extras
scoop install azure-cli
```
The download is ~85 MB. The final "Extracting ... done." + "installed
successfully!" message confirms completion. Verify:
```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","User") + ";" + [System.Environment]::GetEnvironmentVariable("Path","Machine")
az version
```

> IMPORTANT: A newly opened terminal will NOT have `az` on its PATH until the
> environment is refreshed (or VS Code is restarted). Always run the
> `$env:Path = ...` refresh line above before calling `az` in a fresh terminal,
> otherwise you get `CommandNotFoundException`.

### 4. OAuth login
```powershell
az login
```
This opens the default browser for OAuth. Ask the user to complete sign-in in
the browser.

### 5. Handle the interactive subscription prompt
After the browser auth, `az login` prints:
`Select a subscription and tenant (Type a number or Enter for no changes):`

- This is an INTERACTIVE prompt. Do NOT queue other commands in the same
  terminal while it is waiting -- queued command text gets sent as input and
  produces `Invalid selection.`
- To accept the default subscription, send an empty line (press Enter).
- To choose a specific subscription, send the corresponding number, OR after
  login run:
  ```powershell
  az account set --subscription "<name-or-id>"
  ```

### 6. Confirm
```powershell
az account show --output table
```

## Gotchas Recap
- OneDrive folders make extraction slow -- wait, don't retry.
- Refresh `$env:Path` in every new terminal before using `az`.
- The subscription selection is interactive -- never pipe it through
  `Select-Object`/`Where-Object` and never queue commands behind it.
- Never request or send secrets (passwords, tokens) through automation; the
  browser handles credentials during OAuth.

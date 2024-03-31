## Changelog

# GIT
- Re-added `.env` to `.gitignore` [[f297bd2](https://github.com/redtrillix/DiscordComputerStatus/commit/f297bd2e5be6084e3a0a86cca9259fd0fcd9fc59) by [redtrillix](https://github.com/redtrillix)]
- Updated changelog [[19283e5](https://github.com/JamesBLDZMB/DiscordComputerStatus/commit/19283e5fe559b56ea11e65e2597be3647c818f54) by [JamesBLDZMB](https://github.com/JamesBLDZMB)]
    - Changed file name from `changelog.txt` to `CHANGELOG.md`
    - Added release links
    - Added commit links
    - Added contributor links
    - Added `GIT` section
    - Converted to dot-point formating
    - Slightly improved text of `v2.0.2` change
    - General formating improvements
    - Added release type badges
        - `ALPHA`
        - `PATCH`
        - `MINOR`
        - `RELEASE`
        - `PRE`

# [v2.1.0](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v2.1.0) `MINOR`
- Added the listed services as a variable under `.env`, they will no longer be under `run.py` [[a563238](https://github.com/redtrillix/DiscordComputerStatus/commit/a56323816c89aa07c37f05ff74c5b98173941613) by [redtrillix](https://github.com/redtrillix) & [JakeWasHere](https://github.com/JakeWasHere)]  
    - Temporarily commented out '.env' under `.gitignore` to add changes to repo  
- Removed `.github\workflows\python-version-check.yml` file due to being unable to get the workflow working correctly [[a563238](https://github.com/redtrillix/DiscordComputerStatus/commit/a56323816c89aa07c37f05ff74c5b98173941613) by [redtrillix](https://github.com/redtrillix) & [JakeWasHere](https://github.com/JakeWasHere)]  
- Added badges under `README.md` [[a563238](https://github.com/redtrillix/DiscordComputerStatus/commit/a56323816c89aa07c37f05ff74c5b98173941613) by [redtrillix](https://github.com/redtrillix) & [JakeWasHere](https://github.com/JakeWasHere)]  
    - Added Version Release number  
    - Added Repo License  
    - Added Windows text in bright green  
    - Added Python text in blue  

# [v2.0.2](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v2.0.2) `PRE` `PATCH`
- Attempt #2 to fix `python-version-check.yml` not running correctly [[a8ea929](https://github.com/redtrillix/DiscordComputerStatus/commit/a8ea9299504504e854f65357087722cf7474f9c4) by [redtrillix](https://github.com/redtrillix)]  

# [v2.0.1](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v2.0.1) `PATCH`
- Fix `python-version-check.yml` not running correctly [[6bf4487](https://github.com/redtrillix/DiscordComputerStatus/commit/6bf4487caae484fba74d1f8072623f55b8125614) by [redtrillix](https://github.com/redtrillix)]  
- Add `.gitignore` as mentioned in previous changelog [[6bf4487](https://github.com/redtrillix/DiscordComputerStatus/commit/6bf4487caae484fba74d1f8072623f55b8125614) by [redtrillix](https://github.com/redtrillix)]  
    - Added `.env` to `.gitignore`  

# [v2.0.0](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v2.0.0) `RELEASE`
- Added dotenv to have environment variables (channed id, bot token) seperate from the main script in the form of a .env file.
    This is more for my sake cause i'm an idiot and will end up leaking sensitive info [[c31a23f](https://github.com/redtrillix/DiscordComputerStatus/commit/c31a23fd1bf5e61f4b81265cd683533b9cf27fa0) by [redtrillix](https://github.com/redtrillix)]  
- Added the `.env` file to gitignore, will add `.env` file manually after for documentation and instruction purpose [[c31a23f](https://github.com/redtrillix/DiscordComputerStatus/commit/c31a23fd1bf5e61f4b81265cd683533b9cf27fa0) by [redtrillix](https://github.com/redtrillix)]  
- Changed service message formatting slightly under `run.py` [[c31a23f](https://github.com/redtrillix/DiscordComputerStatus/commit/c31a23fd1bf5e61f4b81265cd683533b9cf27fa0) by [redtrillix](https://github.com/redtrillix)]  
- Added `.github\workflows\python-version-check.yml` to do testing for various Python versions, this to run on pushes and pull requests [[c31a23f](https://github.com/redtrillix/DiscordComputerStatus/commit/c31a23fd1bf5e61f4b81265cd683533b9cf27fa0) by [redtrillix](https://github.com/redtrillix)]  

# [v1.1.0](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v1.1.0) `MINOR`
- Change IP logging from Local computer interface IP to using the service 'https://httpbin.org' to get the Public IP of the computer [[ee99f56](https://github.com/redtrillix/DiscordComputerStatus/commit/ee99f56a66c34306302e9b9c9436063b26abb0e9) by [redtrillix](https://github.com/redtrillix)]  

# [v1.0.0 - Initial Full Release](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v1.0.0) `RELEASE`
- Added psutil dependency for CPU and Memory logging in Discord message [[66749e1](https://github.com/redtrillix/DiscordComputerStatus/commit/66749e1d8d285b0db0f0c2a667298748ea8d3f96) by [redtrillix](https://github.com/redtrillix)]  
- Added socket dependency for Hostname and IP logging in Discord message [[66749e1](https://github.com/redtrillix/DiscordComputerStatus/commit/66749e1d8d285b0db0f0c2a667298748ea8d3f96) by [redtrillix](https://github.com/redtrillix)]  
- Added 'Service4', and 'Service5' as two more generic service examples [[66749e1](https://github.com/redtrillix/DiscordComputerStatus/commit/66749e1d8d285b0db0f0c2a667298748ea8d3f96) by [redtrillix](https://github.com/redtrillix)]  

# [v0.3.1](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v0.3.1) `ALPHA` `PATCH`
- Changed `CHANGELOG.txt` to show newest to oldest changes [[3f1eb49](https://github.com/redtrillix/DiscordComputerStatus/commit/3f1eb4928ce3c7b1cfd94c814d3dc854e7793cf3) by [redtrillix](https://github.com/redtrillix)]  
- Compact message sent to Discord [[3f1eb49](https://github.com/redtrillix/DiscordComputerStatus/commit/3f1eb4928ce3c7b1cfd94c814d3dc854e7793cf3) by [redtrillix](https://github.com/redtrillix)]  
- Fix listed services back to the generic listings in `run.py` [[3f1eb49](https://github.com/redtrillix/DiscordComputerStatus/commit/3f1eb4928ce3c7b1cfd94c814d3dc854e7793cf3) by [redtrillix](https://github.com/redtrillix)]  

# v0.3.0 `ALPHA` `MINOR`
- Add time of script run in to Discord message [[fdb973d](https://github.com/redtrillix/DiscordComputerStatus/commit/fdb973d31b70ca429d2e147f10bb957e46e18dfa) by [redtrillix](https://github.com/redtrillix)]  
- Rename `changelog.txt` to `CHANGELOG.txt` [[fdb973d](https://github.com/redtrillix/DiscordComputerStatus/commit/fdb973d31b70ca429d2e147f10bb957e46e18dfa) by [redtrillix](https://github.com/redtrillix)]  

# [v0.2.0](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v0.2.0) `ALPHA` `MINOR`
- Modified the script to include a more detailed message indicating manually specified services are up and running [[8984bcf](https://github.com/redtrillix/DiscordComputerStatus/commit/8984bcf45673a8f6805184a209306bc6e5cc2b19) by [redtrillix](https://github.com/redtrillix)]  

# [v0.1.1](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v0.1.1) `ALPHA` `PATCH`
- Fix intents missing from script [[3adfd06](https://github.com/redtrillix/DiscordComputerStatus/commit/3adfd06a59adb496a699817737ca42a81ee8df7a) by [redtrillix](https://github.com/redtrillix)]  

# [v0.1.0 - Initial Alpha Release](https://github.com/redtrillix/DiscordComputerStatus/releases/tag/v0.1.0) `ALPHA` `MINOR`
- Basic script functionality to send a message to a Discord channel when the computer is turned on [[15b1444](https://github.com/redtrillix/DiscordComputerStatus/commit/15b144446a4fbdcbed879409f34669cee93e1daf) by [redtrillix](https://github.com/redtrillix)]  

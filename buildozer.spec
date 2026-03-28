[app]

# (str) Title of your application
title = Zeeshan VIP App

# (str) Package name
package.name = zeeshanvip

# (str) Package domain
package.domain = org.zeeshan

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include - FIXED: Added mp3 and wav
source.include_exts = py,png,jpg,kv,atlas,mp3,wav

# (str) Application versioning
version = 0.1

# (list) Application requirements - FIXED: Added hostpython
requirements = python3,kivy==2.3.0,hostpython3==3.11.0

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 1

#
# Android specific
#

# (list) Permissions - FIXED: Inhein active kar diya hai
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA

# (int) Target Android API - FIXED: Reno Z ke liye 33 best hai
android.api = 33

# (int) Minimum API support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API
android.ndk_api = 21

# (bool) Enable AndroidX support - FIXED: Purane phones ke liye zaroori hai
android.enable_androidx = True

# (bool) Accept SDK license - FIXED: Automation ke liye True hona chahiye
android.accept_sdk_license = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (list) The Android archs to build for - FIXED: Reno Z ke liye dono zaroori hain
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup
android.allow_backup = True

[buildozer]

# (int) Log level (2 means show everything)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

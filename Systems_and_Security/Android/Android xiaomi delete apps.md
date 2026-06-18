#android #xiaomi #apps 
## Android configuration in USB
- GO in dev mod
- Enable USB debugging
### Pacman tools
```bash
sudo pacman -S android-tools
```
### See if the device connected/enabled
```bash
ls ~/.android/
```
>[!success]
>adbkey.pub

```bash
adb devices
```
>[!success]
>```bash
>List of devices attached  
ONZTOZS8J7LVNRLR        device
>```
### Enters the adb shell
```bash
adb shell
```

>[!info] All steps can be found in the best place for sources
>https://wiki.archlinux.org/title/Android_Debug_Bridge#Transferring_files

## Commands for adb
https://gist.github.com/KernelTruth/739cc34245be9654d0a654cf2d93e6ff


## Personal commandes (or usless xiaomi apps)
```bash
pm uninstall -k --user 0 com.google.android.calendar
pm uninstall -k --user 0 com.google.android.youtube
pm uninstall -k --user 0 com.google.android.gm
pm uninstall -k --user 0 com.google.android.googlequicksearchbox #its google's app so byebye Gemini if you do that.
pm uninstall -k --user 0 com.android.chrome
pm uninstall -k --user 0 com.miui.videoplayer
pm uninstall -k --user 0 com.xiaomi.glgm #game center
pm uninstall -k --user 0 com.xiaomi.payment
pm uninstall -k --user 0 com.xiaomi.smarthome
pm uninstall -k --user 0 com.ebay.carrier
pm uninstall -k --user 0 com.miui.miservice
pm uninstall -k --user 0 com.miui.yellowpage
pm uninstall -k --user 0 com.miui.msa.global #advertisments
pm uninstall -k --user 0 com.miui.analytics #tracking
pm uninstall -k --user 0 com.miui.cloudservice
pm uninstall -k --user 0 com.miui.daemon #prob spyware. Expect a less battery accuracy on apps consumptions
pm uninstall -k --user 0 com.xiaomi.joyose # bckgrd tracking. Could affect perf managments
pm uninstall -k --user 0 com.miui.android.fashiongallery #Carousel
pm uninstall -k --user 0 com.android.browser #xiaomi browser

```

https://www.gizchina.com/how-to/the-unnecessary-xiaomi-apps-you-can-safely-remove-today
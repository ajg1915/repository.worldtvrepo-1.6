
import urllib,urllib2,re,uuid, time
import xbmcgui,xbmcplugin
import os


thumbnailPath = xbmc.translatePath('special://thumbnails');
cachePath = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath = xbmc.translatePath('special://temp')
addonPath = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),'program.RockClean')
mediaPath = os.path.join(addonPath, 'media')
databasePath = xbmc.translatePath('special://database')

class cacheEntry:
    def __init__(self, namei, pathi):
        self.name = namei
        self.path = pathi
    
def mainMenu():
    xbmc.executebuiltin("Container.SetViewMode(500)")
    addItem('[COLOR red]Clear Cache[/COLOR]','url', 1,os.path.join(mediaPath, "cache.png"))
    addItem('[COLOR red]Delete Thumbnails[/COLOR]', 'url', 2,os.path.join(mediaPath, "thumbs.png"))
    addItem('[COLOR red]Purge Packages[/COLOR]', 'url', 3,os.path.join(mediaPath, "packages.png"))
    addItem('[COLOR red]Update WorldTV[/COLOR]', 'url', 4,os.path.join(mediaPath, "update.png"))

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok


def addDir(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok
	
def addItem(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok
      
def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
			params=sys.argv[2]
			cleanedparams=params.replace('?','')
			if (params[len(params)-1]=='/'):
					params=params[0:len(params)-2]
			pairsofparams=cleanedparams.split('&')
			param={}
			for i in range(len(pairsofparams)):
					splitparams={}
					splitparams=pairsofparams[i].split('=')
					if (len(splitparams))==2:
							param[splitparams[0]]=splitparams[1]
							
	return param   
	
def setupCacheEntries():
    entries = 5 #make sure this refelcts the amount of entries you have
    dialogName = ["WTF", "4oD", "BBC iPlayer", "Simple Downloader", "ITV"]
    pathName = ["special://profile/addon_data/plugin.video.whatthefurk/cache", "special://profile/addon_data/plugin.video.4od/cache",
					"special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache","special://profile/addon_data/script.module.simple.downloader",
                    "special://profile/addon_data/plugin.video.itv/Images"]
                    
    cacheEntries = []
    
    for x in range(entries):
        cacheEntries.append(cacheEntry(dialogName[x],pathName[x]))
    
    return cacheEntries


def clearCache():
    
    if os.path.exists(cachePath)==True:    
        for root, dirs, files in os.walk(cachePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("[COLOR limegreen]Delete WorldTV Cache Files[/COLOR]", str(file_count) + "[COLOR  limegreen] files found[/COLOR]", "[COLOR gold]Do you want to delete them?[/COLOR]"):
                
                    for f in files:
                        try:
                            if (f == "xbmc.log" or f == "xbmc.old.log"): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if os.path.exists(tempPath)==True:    
        for root, dirs, files in os.walk(tempPath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:
                dialog = xbmcgui.Dialog()
                if dialog.yesno("[COLOR  limegreen]Delete WorldTV Temp Files[/COLOR]", str(file_count) + "[COLOR  limegreen] files found[/COLOR]", "[COLOR gold]Do you want to delete them?[/COLOR]"):
                    for f in files:
                        try:
                            if (f == "xbmc.log" or f == "xbmc.old.log"): continue
                            os.unlink(os.path.join(root, f))
                        except:
                            pass
                    for d in dirs:
                        try:
                            shutil.rmtree(os.path.join(root, d))
                        except:
                            pass
                        
            else:
                pass
    if xbmc.getCondVisibility('system.platform.ATV2'):
        atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
        
        for root, dirs, files in os.walk(atv2_cache_a):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("[COLOR limegreen]Delete ATV2 Cache Files[/COLOR]", str(file_count) + "[COLOR gold] files found in 'Other'", "Do you want to delete them?[/COLOR]"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass
        atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
        
        for root, dirs, files in os.walk(atv2_cache_b):
            file_count = 0
            file_count += len(files)
        
            if file_count > 0:

                dialog = xbmcgui.Dialog()
                if dialog.yesno("[COLOR gold]Delete ATV2 Cache Files[/COLOR]", str(file_count) + "[COLOR gold] files found in 'LocalAndRental'[/COLOR]", "[COLOR gold]Do you want to delete them?[/COLOR]"):
                
                    for f in files:
                        os.unlink(os.path.join(root, f))
                    for d in dirs:
                        shutil.rmtree(os.path.join(root, d))
                        
            else:
                pass    
                
    cacheEntries = setupCacheEntries()
                                         
    for entry in cacheEntries:
        clear_cache_path = xbmc.translatePath(entry.path)
        if os.path.exists(clear_cache_path)==True:    
            for root, dirs, files in os.walk(clear_cache_path):
                file_count = 0
                file_count += len(files)
                if file_count > 0:

                    dialog = xbmcgui.Dialog()
                    if dialog.yesno("[COLOR  limegreen]ROCK CLEANER[/COLOR]",str(file_count) + "[COLOR  limegreen]%s [COLOR gold]cache files found[/COLOR]"%(entry.name), "[COLOR gold]Do you want to delete them?[/COLOR]"):
                        for f in files:
                            os.unlink(os.path.join(root, f))
                        for d in dirs:
                            shutil.rmtree(os.path.join(root, d))
                            
                else:
                    pass
                

    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR  limegreen]WorldTV Cleaner[/COLOR]", "[COLOR gold]Done Clearing All Cache files[/COLOR]")
    
    
def deleteThumbnails():
    
    if os.path.exists(thumbnailPath)==True:  
            dialog = xbmcgui.Dialog()
            if dialog.yesno("[COLOR red]Delete Thumbnails[/COLOR]", "[COLOR gold]This option deletes all WorldTV thumbnails[/COLOR]", "[COLOR gold]Are you sure you want to do this?[/COLOR]"):
                for root, dirs, files in os.walk(thumbnailPath):
                    file_count = 0
                    file_count += len(files)
                    if file_count > 0:                
                        for f in files:
                            try:
                                os.unlink(os.path.join(root, f))
                            except:
                                pass                
    else:
        pass
    
    text13 = os.path.join(databasePath,"Textures13.db")
    os.unlink(text13)
        
    dialog.ok("[COLOR  limegreen]Restart WorldTV[/COLOR]", "[COLOR gold]Please restart WorldTV to rebuild thumbnail library[/COLOR]")
        
def purgePackages():
    
    purgePath = xbmc.translatePath('special://home/addons/packages')
    dialog = xbmcgui.Dialog()
    for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
    if dialog.yesno("[COLOR  limegreen]Delete Package Cache Files[/COLOR]", "[COLOR  limegreen]%d [COLOR gold]packages found.[/COLOR]"%file_count, "[COLOR gold]Do you want to Delete Them?[/COLOR]"):  
        for root, dirs, files in os.walk(purgePath):
            file_count = 0
            file_count += len(files)
            if file_count > 0:            
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    shutil.rmtree(os.path.join(root, d))
                dialog = xbmcgui.Dialog()
                dialog.ok("[COLOR limegreen]WorldTV CLEANER[/COLOR]", "[COLOR gold]Deleting Packages all done[/COLOR]")
            else:
                dialog = xbmcgui.Dialog()
                dialog.ok("[COLOR blue]WorldTV CLEANER[/COLOR]", "[COLOR gold]No Packages to Purge[/COLOR]") 
                
def ForceUpdate():
  dialog = xbmcgui.Dialog()
  if dialog.yesno("[COLOR limegreen]WorldTV CLEANER[/COLOR]", "[COLOR gold]Update All Add-ons[/COLOR]", "[COLOR gold]And Repository ?[/COLOR]"):
     xbmc.executebuiltin('UpdateAddonRepos()')
     xbmc.executebuiltin('UpdateLocalAddons()') 
  dialog = xbmcgui.Dialog()
  dialog.ok("[COLOR limegreen]WorldTV CLEANER[/COLOR]", "[COLOR gold]Updating All Addons and Repos[/COLOR]")  
                
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

if mode==None or url==None or len(url)<1:
        mainMenu()
       
elif mode==1:
		clearCache()
        
elif mode==2:
        deleteThumbnails()

elif mode==3:
		purgePackages()
		
elif mode==4:
		ForceUpdate()



xbmcplugin.endOfDirectory(int(sys.argv[1]))


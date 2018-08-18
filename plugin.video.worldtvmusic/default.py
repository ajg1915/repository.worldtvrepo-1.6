# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Vevo Music Addon by coldkeys
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: coldkeys
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.worldtvmusic'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "RbmS3tQJ7Os&list=PLqYXv_L7NiEyYnfZhVHR7ixOTANxjes89"
YOUTUBE_CHANNEL_ID_2 = "PLWtAfhR9YD1wdKOTDqCFYoFUcThRCfAjp"
YOUTUBE_CHANNEL_ID_3 = "PLhQMRuwr-QN8KW5gp3EirCHdZTRCrAqfk"
YOUTUBE_CHANNEL_ID_4 = "PLhQMRuwr-QN8KW5gp3EirCHdZTRCrAqfk"
YOUTUBE_CHANNEL_ID_5 = "PLhS3DcL9XnJgGz07uMlGr5gJYE2w8rn_K"
YOUTUBE_CHANNEL_ID_6 = "PLTfrnDl20kIOmlwIT7LtUL8iX8UHAzqOw"
YOUTUBE_CHANNEL_ID_7 = "PLDC827E741DA933F0"
YOUTUBE_CHANNEL_ID_8 = "PLuK6flVU_Aj45QZ_A5ld0-pP3CIkoNQDk"
YOUTUBE_CHANNEL_ID_9 = "PL9WDw_HowNxwO43GcV9v1x4jGH7pAOrZI"
YOUTUBE_CHANNEL_ID_10 = "PLGBuKfnErZlAkaUUy57-mR97f8SBgMNHh"
YOUTUBE_CHANNEL_ID_11 = "PLCD0445C57F2B7F41"
YOUTUBE_CHANNEL_ID_12 = "PLE6rhv8iI_vJ48CbdqZqnr-6LT4A_Lxtq"
YOUTUBE_CHANNEL_ID_13 = "PLpuDUpB0osJmZQ0a3n6imXirSu0QAZIqF"
YOUTUBE_CHANNEL_ID_14 = "PLFgquLnL59ak1QNHmrUSjNM6WTegpgX__"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="Rock N Roll", 
        title="Rock N Roll",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://s4.evcdn.com/images/block/I0-001/020/077/171-2.jpeg_/rock-and-roll-bingo-71.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="Jazz", 
        title="Jazz",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://s4.evcdn.com/images/block/I0-001/034/262/959-5.jpeg_/back-bay-bistro-jazz-dinner-series-59.jpeg",
        folder=True )

    plugintools.add_item( 
        #action="Easy Listening", 
        title="Easy Listening",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://blb-thumb-img.s3.amazonaws.com/34648.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pop Now!",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://d3jlmdk6p3mr4i.cloudfront.net/images/concerts/album4.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="RAP",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://imgix.ranker.com/user_node_img/50080/1001591792/original/life-of-a-dark-rose-photo-u1?w=125&h=125&fit=crop&crop=faces&q=60&fm=jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Just Sing Karaoke",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://static.apkthing.com/uploads/posts/2016-04/thumbs/1461814138_sing3.png",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Big Bands",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://s1.evcdn.com/images/block/I0-001/032/463/784-6.jpeg_/society-beat-big-band-orchestra-84.jpeg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="50s",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://ecx.images-amazon.com/images/I/51-q8jYF8jL._SL125_.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="60s",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/236x/6f/25/ca/6f25ca8623609e8c784fa8b3da1816d4.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="70s",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://67.media.tumblr.com/avatar_db784cb07cb7_128.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="80s",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://www.cdjapan.co.jp/pictures/s/01/29/UICY-20430.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="90s",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://67.media.tumblr.com/avatar_13c7e358d249_128.png",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="2000s",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://s3-eu-west-1.amazonaws.com/singa-images-dev/media/images/modified/3/a89d22d7b267d4f229a3d69da8514282f558efcbd9eaffd0593043624919d4be.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="What's Trending",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://66.media.tumblr.com/avatar_978d1b4e00c1_128.png",
        folder=True ) 
	

run()

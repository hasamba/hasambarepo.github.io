# -*- coding: utf-8 -*-
import xbmcgui,xbmcaddon,time
import _strptime,xbmcvfs
import base64
Addon = xbmcaddon.Addon()

start_time_start=time.time()
time_data=[]
import xbmcaddon,os,xbmc,urllib,re,xbmcplugin,sys
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
from resources.modules import log

KODI_VERSION = int(xbmc.getInfoLabel("System.BuildVersion").split('.', 1)[0])
if KODI_VERSION<=18:
    xbmc_tranlate_path=xbmc.translatePath
    from urlparse import parse_qsl
else:
    import xbmcvfs
    from urllib.parse import parse_qsl
    xbmc_tranlate_path=xbmcvfs.translatePath
COLOR1         = 'gold'
COLOR2         = 'white'
DIALOG         = xbmcgui.Dialog()
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path=dir_path.replace('resources','')
mando_icon=os.path.join(dir_path,'icon.png')
ADDONTITLE='Mando 2'
global from_seek
import threading,json
from resources.modules import public
# from resources.modules import tmdbn
sort_by_episode=False
from_seek=False
all_jen_links=[]
play_status_rd_ext=''
break_window_rd=False
break_window=False
play_status=''
infoDialog_counter_close=False
all_other_sources_uni={}
aa_results={}
avg_f=''
stop_cpu=False

tvdb_results=[]
done1=0
done1_1=0
wait_for_subs=''
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
stop_window=False

once_fast_play=0
close_on_error=0
all_other_sources={}
all_hased=[]

if KODI_VERSION<=18:#kodi18
    if Addon.getSetting('debug')=='false':
        reload (sys )#line:61
        sys .setdefaultencoding ('utf8')#line:62
else:#kodi19
    import importlib
    importlib.reload (sys )#line:61
all_w_global={}
l_full_stats=''
po_watching=''
clicked_id=''
selected_index=-1
clicked=False
silent=False
break_jump=0
global list_index,str_next,sources_searching
global susb_data_next
susb_data_next={}
sources_searching=False
str_next=''
list_index=999
all_s_in=({},0,'','','')
close_sources_now=0
addonPath = xbmc_tranlate_path(Addon.getAddonInfo("path"))
user_dataDir = xbmc_tranlate_path(Addon.getAddonInfo("profile"))
if not os.path.exists(user_dataDir):
     os.makedirs(user_dataDir)
lang=xbmc.getLanguage(0)
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)

addNolink=public.addNolink
addDir3=public.addDir3
addLink=public.addLink

lang=public.lang
pre_mode=public.pre_mode
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time+999)

elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
from  resources.modules import cache
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)

elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)

art_folder='artwork'
    

BASE_LOGO=os.path.join(addonPath, 'resources', art_folder+'/')
file = open(os.path.join(BASE_LOGO, 'fanart.json'), 'r') 
fans= file.read()
file.close()
fanarts=json.loads(fans)
all_fanarts={}
for items in fanarts:
    if 'http' in fanarts[items]:
        all_fanarts[items]=fanarts[items]
    else:
        all_fanarts[items]=(os.path.join(BASE_LOGO, fanarts[items]))
    
global playing_text
elapsed_time = time.time() - start_time_start
time_data.append(elapsed_time)
playing_text=''


try:
    import urllib.parse
except:
    import urlparse
if KODI_VERSION<=18:
    que=urllib.quote_plus
    url_encode=urllib.urlencode
else:
    que=urllib.parse.quote_plus
    url_encode=urllib.parse.urlencode
if KODI_VERSION<=18:
    unque=urllib.unquote_plus
else:
    unque=urllib.parse.unquote_plus
if KODI_VERSION<=18:
    from urlparse import urlparse
    urp=urlparse
else:
    import urllib.parse as urlparse
    urp=urlparse.urlparse
if KODI_VERSION>18:
    def trd_alive(thread):
        return thread.is_alive()
    class Thread (threading.Thread):
       def __init__(self, target, *args):
        super().__init__(target=target, args=args)
        
       def run(self, *args):
          
          self._target(*self._args)
          return 0
else:
    def trd_alive(thread):
        return thread.isAlive()
    class Thread(threading.Thread):
        def __init__(self, target, *args):
           
            self._target = target
            self._args = args
            
            
            threading.Thread.__init__(self)
            
        def run(self):
            
            self._target(*self._args)
def replaceHTMLCodes(txt):
    try:
        import HTMLParser
        html_parser = HTMLParser.HTMLParser()
       
    except:
        import html as html_parser
    txt = re.sub("(&#[0-9]+)([^;^0-9]+)", "\\1;\\2", txt)
    txt = html_parser.unescape(txt)
    txt = txt.replace("&quot;", "\"")
    txt = txt.replace("&amp;", "&")
    txt = txt.replace("&#8211", "-")
    txt = txt.replace("&#8217", "'")
    txt = txt.strip()
    return txt
def get_params17_18():
        param=[]
        if len(sys.argv)>=2:
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
def get_params(user_params=''):
        
        if KODI_VERSION>18:
            param = dict(parse_qsl(user_params.replace('?','')))
        else:
            params=dict(parse_qsl(user_params.replace('?','')))
            param =  {k: v[0] for k, v in params.items()} 
            
        
        return param     
def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result+chr(ord(ch)^ord(next(temp)))
    return result
def main_menu(time_data):
    
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time+111)
    #show_updates()
    
            
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time+222)
    all_d=[]
   
    if Addon.getSetting('movie_world')=='true':
        aa=addDir3(Addon.getLocalizedString(32024),'www',2,BASE_LOGO+'movies.png',all_fanarts['32024'],'Movies')
        all_d.append(aa)

    if Addon.getSetting('tv_world')=='true':
        aa=addDir3(Addon.getLocalizedString(32025),'www',3,BASE_LOGO+'tv.png',all_fanarts['32025'],'TV')
        all_d.append(aa)
    #if Addon.getSetting('idan')=='true':
    #    aa=addDir3('ערוצי עידן פלוס','www',190,BASE_LOGO+'base.png',all_fanarts['32024'],'עידן')
    #    all_d.append(aa)
    if Addon.getSetting('trakt_world')=='true':
        aa=addDir3(Addon.getLocalizedString(32026),'www',21,BASE_LOGO+'trakt.png',all_fanarts['32026'],'No account needed)')
        all_d.append(aa)
    if Addon.getSetting('trakt')=='true':
        aa=addDir3(Addon.getLocalizedString(32027),'www',114,BASE_LOGO+'trakt.png',all_fanarts['32027'],'TV')
        all_d.append(aa)
    if Addon.getSetting('search')=='true':
        aa=addDir3(Addon.getLocalizedString(32020),'www',5,BASE_LOGO+'search.png',all_fanarts['32020'],'Search')
        all_d.append(aa)
    if Addon.getSetting('search_history')=='true':
        aa=addDir3(Addon.getLocalizedString(32021),'both',143,BASE_LOGO+'search.png',all_fanarts['32021'],'TMDB')
        all_d.append(aa)
    if Addon.getSetting('last_link_played')=='true':
        aa=addDir3(Addon.getLocalizedString(32022),'www',144,BASE_LOGO+'last.png',all_fanarts['32022'],'Last Played') 
        all_d.append(aa)
    if Addon.getSetting('whats_new')=='true':
        aa=addNolink(Addon.getLocalizedString(32028) , 'www',149,False,fanart=all_fanarts['32028'], iconimage=BASE_LOGO+'news.png',plot='',dont_place=True)
        all_d.append(aa)
    if Addon.getSetting('settings')=='true':
        aa=addNolink( Addon.getLocalizedString(32029), 'www',151,False,fanart=all_fanarts['32029'], iconimage=BASE_LOGO+'setting.png',plot='',dont_place=True)
        all_d.append(aa)
    if Addon.getSetting('resume_watching')=='true':		
        aa=addDir3(Addon.getLocalizedString(32030),'both',158,BASE_LOGO+'resume.png',all_fanarts['32030'],'TMDB')
        all_d.append(aa)
    if Addon.getSetting('debrid_select')=='0':
        if Addon.getSetting('my_rd_history')=='true':
            aa=addDir3(Addon.getLocalizedString(32031),'1',168,BASE_LOGO+'rd_history.png',all_fanarts['32031'],'TMDB')
            all_d.append(aa)
        if Addon.getSetting('rd_Torrents')=='true':
            aa=addDir3(Addon.getLocalizedString(32032),'1',169,BASE_LOGO+'rd_Torrents.png',all_fanarts['32032'],'TMDB')
            all_d.append(aa)
    if Addon.getSetting('actor')=='true':
        aa=addDir3(Addon.getLocalizedString(32033),'www',72,BASE_LOGO+'actor.png',all_fanarts['32033'],'Actor')
        all_d.append(aa)
    if Addon.getSetting('scraper_check')=='true':
        aa=addDir3( Addon.getLocalizedString(32034), 'www',172,BASE_LOGO+'basic.png',all_fanarts['32034'],'Test')
        
        all_d.append(aa)
    #place your Jen playlist here:
    #dulpicate this line with your address
    #aa=addDir3('Name', 'Your Jen Address',189,'Iconimage','fanart','Description',search_db='Your Search db Address')
    #all_d.append(aa)
    #aa=addDir3('סרטים בקליק', 'https://narcacist.com/Jen4k/4ksection.json',191,'https://www.wirelesshack.org/wp-content/uploads/2020/07/How-To-Install-Ghost-Kodi-Addon-2020.jpg','https://troypoint.com/wp-content/uploads/2020/07/ghost-kodi-addon.png','Ghost')
    #all_d.append(aa)
    
    
    
    if Addon.getSetting('debug')=='true':
        aa=addDir3( 'Unit tests', 'www',181,'https://lh3.googleusercontent.com/proxy/Ia9aOfcgtzofMb0urCAs8NV-4RRhcIVST-Gqx9GI9RLsx7IJe_5jBqjfdsJcOO3QIV3TT-uiF2nKmyYCX0vj5UPR4iW1iHXgZylE8N8wyNgRLw','https://i.ytimg.com/vi/3wLqsRLvV-c/maxresdefault.jpg','Test')
        
        all_d.append(aa)
    found=False
    for i in range(0,10):
        if Addon.getSetting('imdb_user_'+str(i))!='':
            found=True
            break
    if found:
        aa=addDir3(Addon.getLocalizedString(32309),'www',183,BASE_LOGO+'basic.png',all_fanarts['32309'],'Imdb')
        all_d.append(aa)
    
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time+333)
    if Addon.getSetting("stop_where")=='0':
            xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
    
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time+444)
    return time_data
def movie_world():
    all_d=[]
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""url TEXT, ""tv_movie TEXT);" % 'add_cat')
    
   
    dbcon.commit()
    dbcur.execute("SELECT * FROM add_cat")
    match = dbcur.fetchall()
    dbcur.close()
    dbcon.close()
    
    all_s_strings=[]
    for name,url,tv_movie in match:
        
        if (tv_movie=='movie'):
           aa=addDir3('[COLOR lightblue][B]'+name+'[/B][/COLOR]',url,14,BASE_LOGO+'int.png',all_fanarts['32295'],'Tmdb_custom')
           all_d.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32295),'http://api.themoviedb.org/3/movie/now_playing?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&page=1'%lang,14,BASE_LOGO+'int.png',all_fanarts['32295'],'Tmdb')
    all_d.append(aa)
    'Popular Movies'
    aa=addDir3(Addon.getLocalizedString(32036),'http://api.themoviedb.org/3/movie/popular?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&page=1'%lang,14,BASE_LOGO+'popular.png',all_fanarts['32036'],'Tmdb')
    all_d.append(aa)
    order_by='vote_count.desc'
    aa=addDir3('הכי מדורגים','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,BASE_LOGO+'movies.png',all_fanarts['32038'],'Columbia Pictures')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32037),'http://api.themoviedb.org/3/search/movie?api_key=34142515d9d23817496eeb4ff1d223d0&query=3d&language=%s&append_to_response=origin_country&page=1'%lang,14,BASE_LOGO+'3d.png',all_fanarts['32037'],'Tmdb')
    all_d.append(aa)
    
    #Genre
    aa=addDir3(Addon.getLocalizedString(32038),'http://api.themoviedb.org/3/genre/movie/list?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&page=1'%lang,18,BASE_LOGO+'genre.png',all_fanarts['32038'],'Tmdb')
    all_d.append(aa)
    #Years
    aa=addDir3(Addon.getLocalizedString(32039),'movie_years&page=1',14,BASE_LOGO+'years.png',all_fanarts['32039'],'Tmdb')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32040),'movie_years&page=1',112,BASE_LOGO+'networks.png',all_fanarts['32040'],'Tmdb')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32041),'advance_movie',14,BASE_LOGO+'content_s.png',all_fanarts['32041'],'Advance Content selection')
    all_d.append(aa)

    #Search movie
    aa=addDir3(Addon.getLocalizedString(32042),'http://api.themoviedb.org/3/search/movie?api_key=34142515d9d23817496eeb4ff1d223d0&query=%s&language={0}&append_to_response=origin_country&page=1'.format(lang),14,BASE_LOGO+'search_m.png',all_fanarts['32042'],'Tmdb')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32043),'movie',143,BASE_LOGO+'search.png',all_fanarts['32043'],'TMDB')
    all_d.append(aa)
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    
    table_name='lastlinkmovie'
    
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""o_name TEXT,""name TEXT, ""url TEXT, ""iconimage TEXT, ""fanart TEXT,""description TEXT,""data TEXT,""season TEXT,""episode TEXT,""original_title TEXT,""saved_name TEXT,""heb_name TEXT,""show_original_year TEXT,""eng_name TEXT,""isr TEXT,""prev_name TEXT,""id TEXT);"%table_name)
    
    dbcur.execute("SELECT * FROM lastlinkmovie WHERE o_name='f_name'")

    match = dbcur.fetchone()
    dbcon.commit()
    
    dbcur.close()
    dbcon.close()
    
    if match!=None:
       f_name,name,url,iconimage,fanart,description,data,season,episode,original_title,saved_name,heb_name,show_original_year,eng_name,isr,prev_name,id=match
       try:
           if url!=' ':
             if 'http' not  in url:
               import base64
               url=base64.b64decode(url)
              
             aa=addLink('[I]%s[/I]'%Addon.getLocalizedString(32022), url,6,False,iconimage,fanart,description,data=show_original_year,prev_name=name,original_title=original_title,season=season,episode=episode,tmdb=id,year=show_original_year,place_control=True)
             all_d.append(aa)
       except  Exception as e:
         log.warning(e)
         pass
    aa=addDir3(Addon.getLocalizedString(32044),'movie',145,BASE_LOGO+'history.png',all_fanarts['32044'],'History')
    
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32045),'0',174,BASE_LOGO+'classic.png',all_fanarts['32045'],'classic')
    
    all_d.append(aa)
    
    # aa=addDir3(Addon.getLocalizedString(32046),'0',176,BASE_LOGO+'westren.png',all_fanarts['32046'],'classic')
    
    # all_d.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32047),'0',178,BASE_LOGO+'3d.png',all_fanarts['32047'],'3D')
    
    all_d.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32313),'0',187,BASE_LOGO+'keywords.png',all_fanarts['32313'],'keywords')
    
    all_d.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))

def movie_prodiction():
    all_d=[]
    if Addon.getSetting("order_networks")=='0':
        order_by='popularity.desc'
    elif Addon.getSetting("order_networks")=='2':
        order_by='vote_average.desc'
    elif Addon.getSetting("order_networks")=='1':
        order_by='first_air_date.desc'
    
    
    aa=addDir3('[COLOR red]Marvel[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=7505&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://yt3.ggpht.com/a-/AN66SAwQlZAow0EBMi2-tFht-HvmozkqAXlkejVc4A=s900-mo-c-c0xffffffff-rj-k-no','https://images-na.ssl-images-amazon.com/images/I/91YWN2-mI6L._SL1500_.jpg','Marvel')
    all_d.append(aa)
    aa=addDir3('[COLOR lightblue]DC Studios[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=9993&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://pmcvariety.files.wordpress.com/2013/09/dc-comics-logo.jpg?w=1000&h=563&crop=1','http://www.goldenspiralmedia.com/wp-content/uploads/2016/03/DC_Comics.jpg','DC Studios')
    all_d.append(aa)
    aa=addDir3('[COLOR lightgreen]Lucasfilm[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=1&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://fontmeme.com/images/lucasfilm-logo.png','https://i.ytimg.com/vi/wdYaG3o3bgE/maxresdefault.jpg','Lucasfilm')
    all_d.append(aa)
    aa=addDir3('[COLOR yellow]Warner Bros.[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=174&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'http://looking.la/wp-content/uploads/2017/10/warner-bros.png','https://cdn.arstechnica.net/wp-content/uploads/2016/09/warner.jpg','SyFy')
    all_d.append(aa)
    aa=addDir3('[COLOR blue]Walt Disney Pictures[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=2&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://i.ytimg.com/vi/9wDrIrdMh6o/hqdefault.jpg','https://vignette.wikia.nocookie.net/logopedia/images/7/78/Walt_Disney_Pictures_2008_logo.jpg/revision/latest?cb=20160720144950','Walt Disney Pictures')
    all_d.append(aa)
    aa=addDir3('[COLOR skyblue]Pixar[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=3&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://elestoque.org/wp-content/uploads/2017/12/Pixar-lamp.png','https://wallpapercave.com/wp/GysuwJ2.jpg','Pixar')
    all_d.append(aa)
    aa=addDir3('[COLOR deepskyblue]Paramount[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=4&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/Paramount_Pictures_2010.svg/1200px-Paramount_Pictures_2010.svg.png','https://vignette.wikia.nocookie.net/logopedia/images/a/a1/Paramount_Pictures_logo_with_new_Viacom_byline.jpg/revision/latest?cb=20120311200405&format=original','Paramount')
    all_d.append(aa)
    aa=addDir3('[COLOR burlywood]Columbia Pictures[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=5&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://static.tvtropes.org/pmwiki/pub/images/lady_columbia.jpg','https://vignette.wikia.nocookie.net/marveldatabase/images/1/1c/Columbia_Pictures_%28logo%29.jpg/revision/latest/scale-to-width-down/1000?cb=20141130063022','Columbia Pictures')
    all_d.append(aa)
    aa=addDir3('[COLOR powderblue]DreamWorks[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=7&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://www.dreamworksanimation.com/share.jpg','https://www.verdict.co.uk/wp-content/uploads/2017/11/DA-hero-final-final.jpg','DreamWorks')
    all_d.append(aa)
    aa=addDir3('[COLOR lightsaltegray]Miramax[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=14&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://vignette.wikia.nocookie.net/disney/images/8/8b/1000px-Miramax_1987_Print_Logo.png/revision/latest?cb=20140902041428','https://i.ytimg.com/vi/4keXxB94PJ0/maxresdefault.jpg','Miramax')
    all_d.append(aa)
    aa=addDir3('[COLOR gold]20th Century Fox[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=25&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://pmcdeadline2.files.wordpress.com/2017/03/20th-century-fox-cinemacon1.jpg?w=446&h=299&crop=1','https://vignette.wikia.nocookie.net/simpsons/images/8/80/TCFTV_logo_%282013-%3F%29.jpg/revision/latest?cb=20140730182820','20th Century Fox')
    all_d.append(aa)
    aa=addDir3('[COLOR bisque]Sony Pictures[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=34&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Sony_Pictures_Television_logo.svg/1200px-Sony_Pictures_Television_logo.svg.png','https://vignette.wikia.nocookie.net/logopedia/images/2/20/Sony_Pictures_Digital.png/revision/latest?cb=20140813002921','Sony Pictures')
    all_d.append(aa)
    aa=addDir3('[COLOR navy]Lions Gate Films[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=35&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'http://image.wikifoundry.com/image/1/QXHyOWmjvPRXhjC98B9Lpw53003/GW217H162','https://vignette.wikia.nocookie.net/fanon/images/f/fe/Lionsgate.jpg/revision/latest?cb=20141102103150','Lions Gate Films')
    all_d.append(aa)
    aa=addDir3('[COLOR beige]Orion Pictures[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=41&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://i.ytimg.com/vi/43OehM_rz8o/hqdefault.jpg','https://i.ytimg.com/vi/g58B0aSIB2Y/maxresdefault.jpg','Lions Gate Films')
    all_d.append(aa)
    aa=addDir3('[COLOR yellow]MGM[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=21&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://pbs.twimg.com/profile_images/958755066789294080/L9BklGz__400x400.jpg','https://assets.entrepreneur.com/content/3x2/2000/20150818171949-metro-goldwun-mayer-trade-mark.jpeg','MGM')
    all_d.append(aa)
    aa=addDir3('[COLOR gray]New Line Cinema[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=12&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://upload.wikimedia.org/wikipedia/en/thumb/0/04/New_Line_Cinema.svg/1200px-New_Line_Cinema.svg.png','https://vignette.wikia.nocookie.net/theideas/images/a/aa/New_Line_Cinema_logo.png/revision/latest?cb=20180210122847','New Line Cinema')
    all_d.append(aa)
    aa=addDir3('[COLOR darkblue]Gracie Films[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=18&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://i.ytimg.com/vi/q_slAJmZBeQ/hqdefault.jpg','https://i.ytimg.com/vi/yGofbuJTb4g/maxresdefault.jpg','Gracie Films')
    all_d.append(aa)
    aa=addDir3('[COLOR goldenrod]Imagine Entertainment[/COLOR]','https://'+'api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&with_companies=23&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://s3.amazonaws.com/fs.goanimate.com/files/thumbnails/movie/2813/1661813/9297975L.jpg','https://www.24spoilers.com/wp-content/uploads/2004/06/Imagine-Entertainment-logo.jpg','Imagine Entertainment')
    all_d.append(aa)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def movie_db_menu():

    all_d=[]

    all_d.append(addDir3('סרטים מדובבים עמודים','0',204,BASE_LOGO+'movies.png','http://4k.com/wp-content/uploads/2014/11/toystory3_img10_720-790x442.jpg','סרטים מדובבים'))
    all_d.append(addDir3('סרטים מדובבים שנים','0',204,BASE_LOGO+'years.png','','לפי שנים'))
    all_d.append(addDir3(' סרטים מדובבים לפי א-ב','0',205,BASE_LOGO+'history.png','','סרטים מדובבים'))
    all_d.append(addDir3('סרטים שנצפו','0',204,BASE_LOGO+'item_jump.png','https://i.ytimg.com/vi/9FQgg_h_lcQ/maxresdefault.jpg','נצפו','נצפו'))
    
    all_d.append(addDir3('חפש','www',206,BASE_LOGO+'search.png','','חפש'))
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))

def adjusted_datetime(string=False, dt=False):
    from datetime import datetime, timedelta
    d = datetime.utcnow() + timedelta(hours=int(72))
    if dt: return d
    d = datetime.date(d)
    if string:
        try: d = d.strftime('%Y-%m-%d')
        except ValueError: d = d.strftime('%Y-%m-%d')
    else: return d
def main_trakt():
   all_d=[]
   aa=addDir3(Addon.getLocalizedString(32048),'movie?limit=40&page=1',116,BASE_LOGO+'lists.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Lists')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32049),'tv?limit=40&page=1',116,BASE_LOGO+'lists.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Lists')
   all_d.append(aa)
   import datetime
   current_date = adjusted_datetime()
   start = (current_date - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
   finish = 14
        
   aa=addDir3(Addon.getLocalizedString(32050),'calendars/my/shows/%s/%s?limit=40&page=1'%(start,finish),117,BASE_LOGO+'lists.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Lists')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32051),'users/me/watched/shows?extended=full&limit=40&page=1',115,BASE_LOGO+'progress.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Progress')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32052),'sync/watchlist/episodes?extended=full&limit=40&page=1',115,BASE_LOGO+'ep_watch.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Episodes')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32053),'users/me/watchlist/episodes?extended=full&limit=40&page=1',117,BASE_LOGO+'series_w.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Series')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32054),'users/me/collection/shows?limit=40&page=1',117,BASE_LOGO+'tv_col.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','TV')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32055),'users/me/watchlist/shows?limit=40&page=1',117,BASE_LOGO+'show_w.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Shows')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32056),'recommendations/shows?limit=40&ignore_collected=true&page=1',166,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
   all_d.append(aa)
   
   aa=addDir3(Addon.getLocalizedString(32057),'users/me/watchlist/movies?limit=40&page=1',117,BASE_LOGO+'movie_wl.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32058),'recommendations/movies?limit=40&ignore_collected=true&page=1',166,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
   all_d.append(aa)
   
   aa=addDir3(Addon.getLocalizedString(32059),'users/me/watched/movies?limit=40&page=1',117,BASE_LOGO+'movie_w.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Watched')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32060),'users/me/watched/shows?limit=40&page=1',117,BASE_LOGO+'series_wa.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Watched shows')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32061),'users/me/collection/movies?limit=40&page=1',117,BASE_LOGO+'movie_c.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','collection')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32062),'users/likes/lists?limit=40&page=1',118,BASE_LOGO+'liked_l.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Liked lists')
   all_d.append(aa)
   aa=addDir3(Addon.getLocalizedString(32063),'sync/playback/movies?limit=40&page=1',117,BASE_LOGO+'liked_l.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Liked lists')
   all_d.append(aa)
   
   aa=addDir3(Addon.getLocalizedString(32064),'sync/playback/episodes?limit=40&page=1',164,BASE_LOGO+'liked_l.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Liked lists')
   all_d.append(aa)
   
   xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
            
            
def tv_show_menu():
    all_d=[]
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""url TEXT, ""tv_movie TEXT);" % 'add_cat')
    
   
    dbcon.commit()
    dbcur.execute("SELECT * FROM add_cat")
    match = dbcur.fetchall()
    dbcur.close()
    dbcon.close()
    
    all_s_strings=[]
    for name,url,tv_movie in match:
        
        if (tv_movie=='tv'):
           aa=addDir3('[COLOR lightblue][B]'+name+'[/B][/COLOR]',url,14,BASE_LOGO+'int.png',all_fanarts['32295'],'Tmdb_custom')
           all_d.append(aa)
           
    import datetime
    now = datetime.datetime.now()
    aa=addDir3(Addon.getLocalizedString(32023),'tv',145,BASE_LOGO+'tracker.png',all_fanarts['32023'],'History')
    #Popular
    aa=addDir3(Addon.getLocalizedString(32012),'https://api.themoviedb.org/3/discover/tv/?api_key=34142515d9d23817496eeb4ff1d223d0&language={0}&sort_by=popularity.desc&include_null_first_air_dates=false&with_original_language={1}&page=1'.format(lang,'en'),14,BASE_LOGO+'popular.png',all_fanarts['32013'],Addon.getLocalizedString(32012))
    # aa=addDir3(Addon.getLocalizedString(32012),'http://api.themoviedb.org/3/tv/popular?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&page=1'%lang,14,BASE_LOGO+'popular.png',all_fanarts['32013'],'TMDB')
    all_d.append(aa)

    aa=addDir3(Addon.getLocalizedString(32013),'https://api.themoviedb.org/3/tv/on_the_air?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&page=1'%lang,14,BASE_LOGO+'on_air.png',all_fanarts['32013'],'TMDB')
    all_d.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32014),'https://api.themoviedb.org/3/discover/tv/?api_key=34142515d9d23817496eeb4ff1d223d0&language={0}&sort_by=popularity.desc&first_air_date_year='+str(now.year)+'&with_original_language={1}&language=he&page=1'.format(lang,'en'),14,'special://home/addons/plugin.video.telemedia/tele/Tv_Show/popular_tv.png','special://home/addons/plugin.video.telemedia/tele/tv_fanart.png','New Tv shows')
    # aa=addDir3(Addon.getLocalizedString(32014),'https://api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&language=en-US&sort_by=popularity.desc&first_air_date_year='+str(now.year)+'&timezone=America%2FNew_York&include_null_first_air_ates=false&language={0}&page=1'.format(lang),14,BASE_LOGO+'int.png',all_fanarts['32014'],'New Tv shows')
    all_d.append(aa)
    #new episodes
    aa=addDir3(Addon.getLocalizedString(32015),'https://api.tvmaze.com/schedule',20,BASE_LOGO+'new_ep.png',all_fanarts['32015'],'New Episodes')
    all_d.append(aa)
    #Genre
    aa=addDir3(Addon.getLocalizedString(32016),'http://api.themoviedb.org/3/genre/tv/list?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&page=1'%lang,18,BASE_LOGO+'genre.png',all_fanarts['32016'],'TMDB')
    all_d.append(aa)
    #Years
    aa=addDir3(Addon.getLocalizedString(32017),'tv_years&page=1',14,BASE_LOGO+'years.png',all_fanarts['32017'],'TMDB')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32018),'tv_years&page=1',101,BASE_LOGO+'networks.png',all_fanarts['32018'],'TMDB')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32019),'advance_tv',14,BASE_LOGO+'content_s.png',all_fanarts['32019'],'Advance Content selection')
    
    all_d.append(aa)
    #Search tv
    aa=addDir3(Addon.getLocalizedString(32020),'http://api.themoviedb.org/3/search/tv?api_key=34142515d9d23817496eeb4ff1d223d0&query=%s&language={0}&page=1'.format(lang),14,BASE_LOGO+'search.png',all_fanarts['32020'],'TMDB')
    all_d.append(aa)
    aa=addDir3(Addon.getLocalizedString(32021),'tv',143,BASE_LOGO+'search.png',all_fanarts['32021'],'TMDB')
    all_d.append(aa)
    
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    
    table_name='lastlinktv'
    
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""o_name TEXT,""name TEXT, ""url TEXT, ""iconimage TEXT, ""fanart TEXT,""description TEXT,""data TEXT,""season TEXT,""episode TEXT,""original_title TEXT,""saved_name TEXT,""heb_name TEXT,""show_original_year TEXT,""eng_name TEXT,""isr TEXT,""prev_name TEXT,""id TEXT);"%table_name)
    
    dbcur.execute("SELECT * FROM lastlinktv WHERE o_name='f_name'")

    match = dbcur.fetchone()
    dbcon.commit()
    
    dbcur.close()
    dbcon.close()
    
    if match!=None:
       f_name,name,url,iconimage,fanart,description,data,season,episode,original_title,saved_name,heb_name,show_original_year,eng_name,isr,prev_name,id=match
       try:
           if url!=' ':
             if 'http' not  in url:
               import base64
               url=base64.b64decode(url)
              
             aa=addLink('[I]%s[/I]'%Addon.getLocalizedString(32022), url,6,False,iconimage,fanart,description,data=show_original_year,original_title=original_title,season=season,episode=episode,tmdb=id,year=show_original_year,place_control=True)
             all_d.append(aa)
       except  Exception as e:
         log.warning(e)
         pass
         
    
    
    
    aa=addDir3(Addon.getLocalizedString(32023),'tv',145,BASE_LOGO+'tracker.png',all_fanarts['32023'],'History')
    all_d.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def tv_neworks():
    all_d=[]
    if Addon.getSetting("order_networks")=='0':
        order_by='popularity.desc'
    elif Addon.getSetting("order_networks")=='2':
        order_by='vote_average.desc'
    elif Addon.getSetting("order_networks")=='1':
        order_by='first_air_date.desc'
    aa=addDir3('[COLOR lightblue]Disney+[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=2739&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://lumiere-a.akamaihd.net/v1/images/image_308e48ed.png','https://allears.net/wp-content/uploads/2018/11/wonderful-world-of-animation-disneys-hollywood-studios.jpg','Disney')
    all_d.append(aa)
    aa=addDir3('[COLOR blue]Apple TV+[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=2552&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://ksassets.timeincuk.net/wp/uploads/sites/55/2019/03/Apple-TV-screengrab-920x584.png','https://www.apple.com/newsroom/videos/apple-tv-plus-/posters/Apple-TV-app_571x321.jpg.large.jpg','Apple')
    all_d.append(aa)
    aa=addDir3('[COLOR red]NetFlix[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=213&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://art.pixilart.com/705ba833f935409.png','https://i.ytimg.com/vi/fJ8WffxB2Pg/maxresdefault.jpg','NetFlix')
    all_d.append(aa)
    aa=addDir3('[COLOR gray]HBO[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=49&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://filmschoolrejects.com/wp-content/uploads/2018/01/hbo-logo.jpg','https://www.hbo.com/content/dam/hbodata/brand/hbo-static-1920.jpg','HBO')
    all_d.append(aa)
    aa=addDir3('[COLOR lightblue]CBS[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=16&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://cdn.freebiesupply.com/logos/large/2x/cbs-logo-png-transparent.png','https://tvseriesfinale.com/wp-content/uploads/2014/10/cbs40-590x221.jpg','HBO')
    all_d.append(aa)
    aa=addDir3('[COLOR purple]SyFy[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=77&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'http://cdn.collider.com/wp-content/uploads/syfy-logo1.jpg','https://imagesvc.timeincapp.com/v3/mm/image?url=https%3A%2F%2Fewedit.files.wordpress.com%2F2017%2F05%2Fdefault.jpg&w=1100&c=sc&poi=face&q=85','SyFy')
    all_d.append(aa)
    aa=addDir3('[COLOR lightgreen]The CW[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=71&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://www.broadcastingcable.com/.image/t_share/MTU0Njg3Mjc5MDY1OTk5MzQy/tv-network-logo-cw-resized-bc.jpg','https://i2.wp.com/nerdbastards.com/wp-content/uploads/2016/02/The-CW-Banner.jpg','The CW')
    all_d.append(aa)
    aa=addDir3('[COLOR silver]ABC[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=2&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'http://logok.org/wp-content/uploads/2014/03/abc-gold-logo-880x660.png','https://i.ytimg.com/vi/xSOp4HJTxH4/maxresdefault.jpg','ABC')
    all_d.append(aa)
    aa=addDir3('[COLOR yellow]NBC[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=6&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://designobserver.com/media/images/mondrian/39684-NBC_logo_m.jpg','https://www.nbcstore.com/media/catalog/product/cache/1/image/1000x/040ec09b1e35df139433887a97daa66f/n/b/nbc_logo_black_totebagrollover.jpg','NBC')
    all_d.append(aa)
    aa=addDir3('[COLOR gold]AMAZON[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=1024&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'http://g-ec2.images-amazon.com/images/G/01/social/api-share/amazon_logo_500500._V323939215_.png','https://cdn.images.express.co.uk/img/dynamic/59/590x/Amazon-Fire-TV-Amazon-Fire-TV-users-Amazon-Fire-TV-stream-Amazon-Fire-TV-Free-Dive-TV-channel-Amazon-Fire-TV-news-Amazon-1010042.jpg?r=1535541629130','AMAZON')
    all_d.append(aa)
    aa=addDir3('[COLOR green]hulu[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=453&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://i1.wp.com/thetalkinggeek.com/wp-content/uploads/2012/03/hulu_logo_spiced-up.png?resize=300%2C225&ssl=1','https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi677r77IbeAhURNhoKHeXyB-AQjRx6BAgBEAU&url=https%3A%2F%2Fwww.hulu.com%2F&psig=AOvVaw0xW2rhsh4UPsbe8wPjrul1&ust=1539638077261645','hulu')
    all_d.append(aa)
    aa=addDir3('[COLOR red]Showtime[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=67&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://res.cloudinary.com/wnotw/images/c_limit,w_1536,q_auto:best,f_auto/v1501788508/sci5cdawypsux61i9pyb/showtime-networks-logo','https://www.sho.com/site/image-bin/images/0_0_0/0_0_0_prm-ogseries_1280x640.jpg','showtime')
    all_d.append(aa)
    aa=addDir3('[COLOR red]BBC One[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=4&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://lh3.googleusercontent.com/proxy/LnjjtuGk_PErC5iaReOcy6EEvwjT9wzlyZBKhQHconLsyHWdVn1NHa-Bz3E0_Dev0KV_yJtGyQTlHDwvvm3zW3i0NFSmQVim5_hYOeZ-jWpD1Zs','https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/BBC_One_HD.svg/800px-BBC_One_HD.svg.png','BBC')
    all_d.append(aa)
    aa=addDir3('[COLOR teal]BBC Two[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=332&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://pbs.twimg.com/profile_images/1057914504321908736/06hkWvx__400x400.jpg','http://amirsaidani.co.uk/wp-content/uploads/2019/06/BBC_TWO_LOGO_ANIMATION.gif','BBC')
    all_d.append(aa)
    aa=addDir3('[COLOR pink]BBC Three[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=3&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/BBC_Three_%282020%29.svg/1200px-BBC_Three_%282020%29.svg.png','https://ichef.bbci.co.uk/news/1024/media/images/81061000/jpg/_81061920_bbcthreelogo.jpg','BBC')
    all_d.append(aa)
    aa=addDir3('[COLOR lightblue]ITV[/COLOR]','https://'+'api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&with_networks=9&language={0}&sort_by={1}&timezone=America%2FNew_York&include_null_first_air_dates=false&page=1'.format(lang,order_by),14,'https://sm.imgix.net/20/31/itv.jpg?w=1200&h=1200&auto=compress,format&fit=clip','https://www.imediaethics.org/wp-content/uploads/2018/11/SCfaQb9l_400x400-350x350.jpg','BBC')
    all_d.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def trakt_world():
    all=[]
    aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32124), id,27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
    all.append(aa)
    
    
    
    aa=addDir3(Addon.getLocalizedString(32125),'movies/trending?limit=40&page=1',117,BASE_LOGO+'people.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32126),'movies/popular?limit=40&page=1$$$noaut',166,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
    all.append(aa)
    aa=addDir3(Addon.getLocalizedString(32127),'movies/played/%s?limit=40&page=1',117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32128),'movies/watched/%s?limit=40&page=1',117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32129),'movies/collected/%s?limit=40&page=1',117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32130),'movies/anticipated?limit=40&page=1$$$noaut',117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32131),'movies/boxoffice?limit=40&page=1$$$noaut',117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Movies')
    all.append(aa)
    
    aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32025), id,27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
    all.append(aa)
    aa=addDir3(Addon.getLocalizedString(32132),'shows/trending?limit=40&page=1$$$noaut',117,BASE_LOGO+'people.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32133),'shows/popular?limit=40&page=1$$$noaut',166,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32134),'shows/played/%s?limit=40&page=1',117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32135),'shows/collected/%s?limit=40&page=1',117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32136),'shows/anticipated?limit=40&page=1$$$noaut',117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Tv')
    all.append(aa)
    
    import datetime
    datetime_get = (datetime.datetime.utcnow() - datetime.timedelta(days = 7))

    log.warning(datetime_get.strftime('%Y-%m-%d'))
    f_data=datetime_get.strftime('%Y-%m-%d')
    
    
    aa=addDir3(Addon.getLocalizedString(32307),'shows/updates/%s?limit=40&page=1$$$noaut'%f_data,117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Tv')
    all.append(aa)
    
    datetime_get = (datetime.datetime.utcnow() - datetime.timedelta(days = 30))

    log.warning(datetime_get.strftime('%Y-%m-%d'))
    f_data=datetime_get.strftime('%Y-%m-%d')
    
    
    aa=addDir3(Addon.getLocalizedString(32308),'shows/updates/%s?limit=40&page=1$$$noaut'%f_data,117,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Tv')
    all.append(aa)
    
    aa=addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32137), id,27,False,fanart=' ', iconimage=' ',plot=' ',dont_place=True)
    all.append(aa)
    aa=addDir3(Addon.getLocalizedString(32138),'lists/trending',119,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Tv')
    all.append(aa)
    
    aa=addDir3(Addon.getLocalizedString(32139),'lists/popular',119,BASE_LOGO+'trakt.png','https://seo-michael.co.uk/content/images/2016/08/trakt.jpg','Tv')
    all.append(aa)
    
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all,len(all))
def search_menu():
    all_d=[]

    if Addon.getSetting('search')=='true':
        aa=addDir3(Addon.getLocalizedString(32020),'www',5,BASE_LOGO+'search.png',all_fanarts['32020'],'Search')
        all_d.append(aa)
    if Addon.getSetting('search_history')=='true':
        aa=addDir3(Addon.getLocalizedString(32021),'both',143,BASE_LOGO+'search.png',all_fanarts['32021'],'TMDB')
        all_d.append(aa)
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_DATEADDED)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
def load_resolveurl_libs():
    path=xbmc_tranlate_path('special://home/addons/script.module.resolveurl/lib')
    sys.path.append( path)
    path=xbmc_tranlate_path('special://home/addons/script.module.six/lib')
    sys.path.append( path)
    path=xbmc_tranlate_path('special://home/addons/script.module.kodi-six/libs')
    sys.path.append( path)
    path1=xbmc_tranlate_path('special://home/addons/script.module.requests/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.urllib3/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.chardet/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.certifi/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.idna/lib')
    sys.path.append( path1)
    path1=xbmc_tranlate_path('special://home/addons/script.module.futures/lib')
    sys.path.append( path1)

def search_history(url,icon,fan):
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""free TEXT);" % 'search')
    dbcon.commit()
        
    dbcur.execute("SELECT * FROM search ORDER BY rowid DESC")
    
    # if Addon.getSetting("sync_mod")=='true' and Addon.getSetting("sync_search")=='true':
        # try:
            # all_db=read_firebase('search')
            # match_search=[]
            # for itt in all_db:
                
                # items=all_db[itt]

                # match_search.append((items['name'],items['free']))
        # except:
          # match_search = dbcur.fetchall()
          # # LogNotify("[COLOR %s]%s[/COLOR]" % (COLOR1, 'בעיה בסנכרון'),'[COLOR %s]מזהה ID שגוי[/COLOR]' % COLOR2)
    # else:
    
    match_search = dbcur.fetchall()
    import logging
    all_d=[]
    for nm,fr in match_search:
        aa=addDir3(nm,nm,14,BASE_LOGO+'search.png','https://www.york.ac.uk/media/study/courses/postgraduate/centreforlifelonglearning/English-Building-History-banner-bought.jpg','TMDB')
        # aa=addDir3(qua,'http://api.themoviedb.org/3/search/{0}?api_key=34142515d9d23817496eeb4ff1d223d0&query={1}&language={2}&page=1'.format(type,qua,lang),14,BASE_LOGO+'search.png','https://www.york.ac.uk/media/study/courses/postgraduate/centreforlifelonglearning/English-Building-History-banner-bought.jpg','TMDB')
        all_d.append(aa)
        

    aa=addNolink( '[COLOR orange]נקה היסטורייה[/COLOR]',url,148,False,fanart=fan, iconimage=icon,plot='Clear %s History'%url,dont_place=True)
    all_d.append(aa)
        
    dbcur.close()
    dbcon.close()
    xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_UNSORTED)
    xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))


def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass
    # if 'youtube' not in o_url:
        # from resources.default import jump_seek
        # thread.append(Thread(jump_seek,que(name),o_url,que(video_info),id,icon,fan,plot,table_name))
        
    
        # thread[0].start()
    # else:
       # playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
       # base_header = {
        # 'Connection': 'keep-alive',
        # 'Pragma': 'no-cache',
        # 'Cache-Control': 'no-cache',
        # 'Accept': '*/*',
        # 'DNT': '1',
        # 'X-Requested-With': 'XMLHttpRequest',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Sec-Fetch-Site': 'same-origin',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Dest': 'empty',
        
        # 'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
        # }
       # import requests,random
       # if KODI_VERSION<19:
            # x=requests.get(o_url,headers=base_header).content
       # else:
           # x=requests.get(o_url,headers=base_header).content.decode('utf-8')
       
       # matche = re.compile('ytInitialData = (.+?)};',re.DOTALL).findall(x)
       # all_j=json.loads(matche[0]+'}')
       # log.warning(json.dumps(all_j))
       # rand=random.randint(0,len(all_j['playerOverlays']['playerOverlayRenderer']['endScreen']['watchNextEndScreenRenderer']['results'])-1)
       # title=all_j['playerOverlays']['playerOverlayRenderer']['endScreen']['watchNextEndScreenRenderer']['results'][rand]['endScreenVideoRenderer']['title']['simpleText']
       # link_id=all_j['playerOverlays']['playerOverlayRenderer']['endScreen']['watchNextEndScreenRenderer']['results'][rand]['endScreenVideoRenderer']['videoId']
       # link='plugin://plugin.video.kids_new/?mode=5&description={0}&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D{1}&iconimage=&fanart=&video_info={2}&mode=5&id=&name={3}'.format('next',link_id,'',title)
       # listItem = xbmcgui.ListItem(title, path=link) 
       # playlist.add(url=link,listitem=listItem)
def special_url(url):
        global from_seek
        all_years=[]
        end_d=False
        if 'advance' in url:
            from resources.modules.tmdb  import adv_gen_window
            all_g,start_y,end_y,save_cat=adv_gen_window(url.split('_')[1])
           
            if len(all_g)==0:
                sys.exit(1)
            typee=url.split('_')[1]
            if typee=='movie':
                url='http://api.themoviedb.org/3/discover/%s?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&sort_by=popularity.desc&primary_release_date.gte=%s-01-01&primary_release_date.lte=%s-12-31&with_genres=%s&page=1'%(typee,lang,start_y,end_y,','.join(all_g))
            else:
                url='http://api.themoviedb.org/3/discover/%s?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&sort_by=popularity.desc&first_air_date.gte=%s-01-01&first_air_date.lte=%s-12-31&with_genres=%s&page=1'%(typee,lang,start_y,end_y,','.join(all_g))
            if (save_cat):
                try:
                    from sqlite3 import dbapi2 as database
                except:
                    from pysqlite2 import dbapi2 as database
                cacheFile=os.path.join(user_dataDir,'database.db')
                dbcon = database.connect(cacheFile)
                dbcur = dbcon.cursor()
                dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""url TEXT, ""tv_movie TEXT);" % 'add_cat')
                
               
                dbcon.commit()
                dbcur.execute("SELECT * FROM add_cat")
                match = dbcur.fetchall()
                all_s_strings=[]
                for name,url2,tv_movie in match:
                   all_s_strings.append(url2)
                from  resources.modules.client import get_html
                if typee=='movie':
                    html=get_html('http://api.themoviedb.org/3/genre/movie/list?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&page=1'%lang).json()
                else:
                    html=get_html('http://api.themoviedb.org/3/genre/tv/list?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&page=1'%lang).json()
                
                all_names=[]
                all_g_name={}
                for data in html['genres']:
                    all_g_name[data['id']]=data['name']
                    
                for items in all_g:
                    all_names.append(all_g_name[int(items)])
                log.warning(all_s_strings)
                log.warning(url)
                if url not in all_s_strings:
                    log.warning('saving')
                    dbcur.execute("INSERT INTO add_cat Values ('%s','%s','%s')"%(','.join(all_names),url,typee))
                    dbcon.commit()
                dbcur.close()
                dbcon.close()
        if url=='tv_years&page=1' and 'page=1' in url:
          import datetime
          all_d=[]
          now = datetime.datetime.now()
          for year in range(now.year,1970,-1):
                all_years.append(str(year))
          if Addon.getSetting("dip_dialog")=='0':
              ret=ret = xbmcgui.Dialog().select("Choose", all_years)
              if ret!=-1:
                url='https://api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&sort_by=popularity.desc&first_air_date_year=%s&include_null_first_air_dates=false&with_original_language=en&page=1'%(lang,all_years[ret])
               
              else:
                sys.exit()
          else:
            for items in all_years:
                url='https://api.themoviedb.org/3/discover/tv?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&sort_by=popularity.desc&first_air_date_year=%s&include_null_first_air_dates=false&with_original_language=en&page=1'%(lang,items)
                
                aa=addDir3(items,url,14,'https://www.techniquetuesday.com/mm5/graphics/00000001/Technique-Tuesday-Calendar-Years-Clear-Stamps-Large_329x400.jpg','https://images.livemint.com/rf/Image-621x414/LiveMint/Period2/2018/08/16/Photos/Processed/investment-knrG--621x414@LiveMint.jpg',items,collect_all=True)
                all_d.append(aa)
            xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
            end_d=True
        elif url=='movie_years&page=1':
              new_name_array=[]
              isr=0
              from_seek=False
              all_years=[]
              import datetime
              all_d=[]
              now = datetime.datetime.now()
              for year in range(now.year,1970,-1):
                    all_years.append(str(year))
      
              if Addon.getSetting("dip_dialog")=='0':
                  ret=ret = xbmcgui.Dialog().select("Choose", all_years)
                  if ret!=-1:
                    
                      url='https://api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year=%s&with_original_language=en&page=1'%(lang,all_years[ret])
                    
                  else:
                    return 0,0
              else:
                for items in all_years:
                    
                    url='https://api.themoviedb.org/3/discover/movie?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&sort_by=popularity.desc&include_adult=false&include_video=false&primary_release_year=%s&with_original_language=en&page=1'%(lang,items)
                    if 0:
                       if  name not in all_n:
                        all_n.append(name)
                        
                        aa=addDir3(items,url,14,'https://www.techniquetuesday.com/mm5/graphics/00000001/Technique-Tuesday-Calendar-Years-Clear-Stamps-Large_329x400.jpg','https://images.livemint.com/rf/Image-621x414/LiveMint/Period2/2018/08/16/Photos/Processed/investment-knrG--621x414@LiveMint.jpg',items,collect_all=True)
                        all_d.append(aa)
                    else:
                        aa=addDir3(items,url,14,'https://www.techniquetuesday.com/mm5/graphics/00000001/Technique-Tuesday-Calendar-Years-Clear-Stamps-Large_329x400.jpg','https://images.livemint.com/rf/Image-621x414/LiveMint/Period2/2018/08/16/Photos/Processed/investment-knrG--621x414@LiveMint.jpg',items,collect_all=True)
                        all_d.append(aa)
                xbmcplugin .addDirectoryItems(int(sys.argv[1]),all_d,len(all_d))
                end_d=True
        elif '/search' in url and 'page=1' in url and '%s' in url:
        
        
            from_seek=True
            search_entered =''
            keyboard = xbmc.Keyboard(search_entered, 'Enter Search')
            keyboard.doModal()
            if keyboard.isConfirmed() :
                   search_entered = keyboard.getText()
                   if search_entered=='':
                    sys.exit()
              
                   
                   url=url%que(search_entered)
                   if '/tv?' in url:
                    type_in='tv'
                   else:
                    type_in='movie'
                   
                  
              
            else:
              
              
              sys.exit()
        
        
        elif '/search/' in url and 'page=1' in url :
                from_seek=True
                from resources.modules.tmdb_n import tmdb as get_movies
                if '%' in url:
                    search_entered=''
                    keyboard = xbmc.Keyboard(search_entered, 'הכנס מילות חיפוש')
                    keyboard.doModal()
                    if keyboard.isConfirmed() :
                           search_entered = que(keyboard.getText().replace("'",""))
                           if search_entered=='':
                            sys.exit()
                    
                else:
                    
                    regex='&query=(.+?)&'
                    search_entered=re.compile(regex).findall(url.replace(' ','%20'))[0]
                from resources.default import search_tvdb
                #thread=[]
                #thread.append(Thread(search_tvdb,search_entered))
           
                #thread[0].start()
                if 'tv' in url:
                    tv_movie='tv'
                else:
                    tv_movie='movie'
                    
                search_entered=que(search_entered.replace('%20',' '))
               
                get_movies('get_movies','http://api.themoviedb.org/3/search/{0}?api_key=34142515d9d23817496eeb4ff1d223d0&query={1}&language={2}&page=1'.format(tv_movie,search_entered,lang))
             
                end_d=True
        if '/search' in url and 'page=1' in url:
               xbmcgui.Window(10000).setProperty('from_seek','true')
               if 'tv' in url:
                    tv_movie='tv'
               else:
                    tv_movie='movie'
               try:
                    from sqlite3 import dbapi2 as database
               except:
                    from pysqlite2 import dbapi2 as database
               cacheFile=os.path.join(user_dataDir,'database.db')
               dbcon = database.connect(cacheFile)
               dbcur = dbcon.cursor()
               dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""tmdb TEXT, ""season TEXT, ""episode TEXT,""playtime TEXT,""total TEXT, ""free TEXT);" % 'playback')
               dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT ,""tv_movie TEXT);" % ('search_string2'))
               
               dbcon.commit()
               dbcur.execute("SELECT * FROM search_string2")
               match = dbcur.fetchall()
               all_s_strings=[]
               for qu,tt in match:
                all_s_strings.append((qu+'$$$'+tt))
               from_seek=True
               search_entered=url.split('query=')[1]
               search_entered=search_entered.split('&')[0]
               
               if search_entered+'$$$'+tv_movie not in all_s_strings:
                 dbcur.execute("SELECT * FROM search_string2 where name='%s' and tv_movie='%s'"%(unque(search_entered.replace("'","%27")),tv_movie))
                 match = dbcur.fetchall()
                 
              
                 
                 if len(match)==0:
                     dbcur.execute("INSERT INTO search_string2 Values ('%s','%s')"%(unque(search_entered.replace("'","%27")),tv_movie))
                     dbcon.commit()
               dbcur.close()
               dbcon.close()
        return url,end_d
def update_all_w(url_o):
        import base64
        all_w={}
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile_trk = os.path.join(user_dataDir, 'cache_play_trk.db')
        dbcon_trk = database.connect(cacheFile_trk)
        dbcur_trk  = dbcon_trk.cursor()
        dbcur_trk.execute("CREATE TABLE IF NOT EXISTS %s ( ""data_ep TEXT, ""dates TEXT, ""fanart TEXT,""color TEXT,""id TEXT,""season TEXT,""episode TEXT, ""next TEXT,""plot TEXT);" % 'AllData4')
        
        dbcon_trk.commit()
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""url TEXT, ""icon TEXT, ""image TEXT, ""plot TEXT, ""year TEXT, ""original_title TEXT, ""season TEXT, ""episode TEXT, ""id TEXT, ""eng_name TEXT, ""show_original_year TEXT, ""heb_name TEXT , ""isr TEXT, ""type TEXT);" % 'Lastepisode')
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""tmdb TEXT, ""season TEXT, ""episode TEXT,""playtime TEXT,""total TEXT, ""free TEXT);" % 'playback')
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT,""id TEXT, ""season TEXT, ""episode TEXT);" % 'subs')
        
        dbcon.commit()
        
        all_o_data=[]
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""o_name TEXT,""name TEXT, ""url TEXT, ""iconimage TEXT, ""fanart TEXT,""description TEXT,""data TEXT,""season TEXT,""episode TEXT,""original_title TEXT,""saved_name TEXT,""heb_name TEXT,""show_original_year TEXT,""eng_name TEXT,""isr TEXT,""prev_name TEXT,""id TEXT);"%'lastlinktv')
        
        dbcur.execute("SELECT * FROM lastlinktv WHERE o_name='f_name'")

        match = dbcur.fetchone()
        dbcon.commit()
        
        
        
        if match!=None:
           f_name,name,url,iconimage,fanart,description,data,season,episode,original_title,saved_name,heb_name,show_original_year,eng_name,isr,prev_name,id=match
           try:
               if url!=' ':
                 if 'http' not  in url:
               
                   url=base64.b64decode(url)
                 dd=[]
                 if url_o!='tv':
                    data_ep=show_original_year
                    dbcur.execute("SELECT * FROM playback")
                    match_playback = dbcur.fetchall()
                    all_w={}
                      
                    for n,tm,s,e,p,t,f in match_playback:
                            ee=str(tm)
                            all_w[ee]={}
                            all_w[ee]['resume']=str(p)
                            all_w[ee]['totaltime']=str(t)
                    
                 else:
                    dbcur.execute("SELECT * FROM playback where tmdb='%s' and season='%s' "%(id,str(season)))
                    match_playback = dbcur.fetchall()
                    
                    all_w={}
                
                    for n,t,s,e,p,t,f in match_playback:
                        ee=str(e)
                        all_w[ee]={}
                        all_w[ee]['resume']=str(p)
                        all_w[ee]['totaltime']=str(t)
                 added_res_trakt=''
            
                 
                 #aa=addLink('[I]%s[/I]'%Addon.getLocalizedString(32022), url,6,False,iconimage,fanart,description,data=show_original_year,original_title=original_title,season=season,episode=episode,tmdb=id,year=show_original_year,place_control=True)
                 dd.append((name,show_original_year,original_title,id,season,episode,show_original_year))
                 
           except  Exception as e:
             log.warning('Error1:'+str(e))
             pass
        return all_w
def get_trakt_last():
    all_ids={}
    url='users/me/watched/shows?extended=full&limit=400&page=1'
            
    from resources.modules.general import call_trakt
    result = call_trakt(url)
    log.warning(result)
    for item in result:
            
        try:
            last_watched_at=None
            if 'last_watched_at' in item:
                last_watched_at=item['last_watched_at']
            num_1 = 0
            if 'seasons' in item:
                if last_watched_at:
                    found=0
                    for seasons in item['seasons']:
                        #if found==1:
                        #    break
                        for episodes in seasons['episodes']:
                            if episodes['last_watched_at']==last_watched_at:
                                season =str(seasons['number'])
                                episode=str(episodes['number'])
                                #found=1
                                #break
                else:
                    for i in range(0, len(item['seasons'])):
                        if item['seasons'][i]['number'] > 0: num_1 += len(item['seasons'][i]['episodes'])
                    num_2 = int(item['show']['aired_episodes'])
                    if num_1 >= num_2 and not sync: raise Exception()

                    season = str(item['seasons'][-1]['number'])

                    episode = [x for x in item['seasons'][-1]['episodes'] if 'number' in x]
                    episode = sorted(episode, key=lambda x: x['number'])
                    episode = str(episode[-1]['number'])
            else:
                season = str(item['episode']['season'])
                episode=str(item['episode']['number'])
            tmdb = item['show']['ids']['tmdb']
            
            tmdb = re.sub('[^0-9]', '', str(tmdb))
            all_ids[tmdb]={'season':season,'episode':episode}
            
        except Exception as e:
                import linecache
                exc_type, exc_obj, tb = sys.exc_info()
                f = tb.tb_frame
                lineno = tb.tb_lineno
                filename = f.f_code.co_filename
                linecache.checkcache(filename)
                line = linecache.getline(filename, lineno, f.f_globals)
                error='''\
                  line no:%s,
                  line:%s,
                  error:%s,
                  url:%s,
                  ep_no:%s,
                  '''%(str(lineno),line,str(e),url,episode_fixed)
                  
                  
                  
                  
                log.warning(error)
                log.warning('Error in trakt')
    return all_ids
def remove_custom(url):
    try:
        from sqlite3 import dbapi2 as database
    except:
        from pysqlite2 import dbapi2 as database
    cacheFile=os.path.join(user_dataDir,'database.db')
    dbcon = database.connect(cacheFile)
    dbcur = dbcon.cursor()
    dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT, ""url TEXT, ""tv_movie TEXT);" % 'add_cat')
    dbcur.execute("DELETE FROM add_cat where url='%s'"%url)
   
    dbcon.commit()
    dbcur.close()
    dbcon.close()
    xbmc.executebuiltin('Container.Refresh')
def refresh_list(user_params,sys_arg_1_data,Addon_id=""):
    # params=get_params()
    Addon = xbmcaddon.Addon()
    global elapsed_time,time_data,sys_arg_1,use_debrid#,description,original_title,iconimage,fanart,dd,url,name,resume,c_id,m_id,fast_link,data,id,saved_name,prev_name,isr,no_subs,season,episode,show_original_year,groups_id,heb_name,year,tmdbid,eng_name,dates,data1,file_name,fav_status,only_torrent,only_heb_servers,new_windows_only,meliq,tv_movie,last_id,nextup,read_data2,tmdb,o_name
    if KODI_VERSION>18:
        params=get_params(user_params=user_params)
    else:
        params=get_params17_18()

    selected_scrapers='All'
    url=None
    name=''
    o_name=''
    mode=None
    iconimage=None
    fanart=None
    description=''
    data=None
    original_title=''
    read_data2=''
    id='0'
    dates='0'
    season='0'
    episode='0'
    show_original_year='0'
    nextup='true'
    dd=''
    video_data={}
    get_sources_nextup='false'
    all_w={}
    use_filter='true'
    use_rejected='true'
    heb_name=''
    tmdbid=''
    has_alldd='false'
    prev_name=''
    search_db=''
    mypass=""
    page = 1
    video_info={}
    try:
            url=unque(params["url"])
    except:
            pass
    try:
            name=unque(params["name"])
    except:
            pass
    try:
            iconimage=unque(params["iconimage"])
    except:
            pass
    try:        
            mode=int(params["mode"])
    except:
            pass
    try:        
            fanart=unque(params["fanart"])
    except:
            pass
    try:        
            description=unque(params["description"])
    except:
            pass
    try:        
            data=(params["data"])
    except:
            pass
    try:        
            original_title=unque(params["original_title"])
    except:
            pass
            
    try:        
            id=(params["id"])
    except:
            pass
    try:        
            season=(params["season"])
    except:
            pass
    try:        
            episode=(params["episode"])
    except:
            pass
    try:        
            show_original_year=(params["show_original_year"])
    except:
            pass
    try:        
            dd=(params["dd"])
    except:
            pass
    try:        
            nextup=(params["nextup"])
    except:
            pass
    try:        
            dates=(params["dates"])
    except:
            pass
    try:        
            video_data=unque(params["video_data"])
    except:
            pass
    try:        
            get_sources_nextup=(params["get_sources_nextup"])
    except:
            pass
            
    try:        
            all_w=unque(params["all_w"])
    except:
            pass
            
    try:        
            use_filter=(params["use_filter"])
    except:
            pass
            
    try:        
            use_rejected=(params["use_rejected"])
    except:
            pass
    try:        
            heb_name=unque(params["heb_name"])
    except:
            pass
            
    try:        
            tmdbid=str(params["tmdbid"])
    except:
            pass
    try:        
            has_alldd=str(params["has_alldd"])
    except:
            pass
    prev_name=name
    try:        
            prev_name=unque(params["prev_name"])
    except:
            pass
    try:        
            search_db=unque(params["search_db"])
    except:
            pass

    try:        
            from_seek=(params["from_seek"])=='True'
    except:
            pass
    #html=cache.get(cfscrape_version,24, table='posters')
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time)

    public.pre_mode=mode
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time+777)
    log.warning('mode_mando:'+str(mode))
    sys_arg_1=int(sys.argv[1])
    if mode==None :
           elapsed_time = time.time() - start_time_start
           time_data.append(elapsed_time+555)
           time_data= main_menu(time_data)
            

    elif mode==2:
        movie_world()
    elif mode==3:
        tv_show_menu()
    elif mode==5:
        log.warning('Search all')
        from resources.modules.tmdb import get_movies
        search_entered=''
        keyboard = xbmc.Keyboard(search_entered, 'הכנס מילות חיפוש')
        keyboard.doModal()
        if keyboard.isConfirmed() :
               search_entered = que(keyboard.getText().replace("'",""))
        if search_entered=='':
         sys.exit()
        if len(Addon.getSetting("firebase"))>0:
            from resources.default import write_search
            thread=[]
            table_name='search_mando'
            free=''
            thread.append(Thread(write_search,unque(search_entered.replace("'","%27")),free,table_name))

            thread[0].start()
        # from resources.default import search_tvdb
        # search_tvdb(search_entered)
        # thread=[]
        # thread.append(Thread(search_tvdb,search_entered))
       
        # thread[0].start()
        try:
            dialog = xbmcgui.DialogBusy()
            dialog.create()
        except:
           xbmc.executebuiltin('ActivateWindow(busydialognocancel)')
        addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32024), id,27,False,fanart=' ', iconimage=' ',plot=' ')
        get_movies('http://api.themoviedb.org/3/search/movie?api_key=34142515d9d23817496eeb4ff1d223d0&query={0}&language={1}&append_to_response=origin_country&page=1'.format(search_entered,lang),global_s=True)
        
        addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32099), id,27,False,fanart=' ', iconimage=' ',plot=' ')
        log.warning('http://api.themoviedb.org/3/search/tv?api_key=34142515d9d23817496eeb4ff1d223d0&query={0}&language={1}&page=1'.format(search_entered,lang))
        get_movies('http://api.themoviedb.org/3/search/tv?api_key=34142515d9d23817496eeb4ff1d223d0&query={0}&language={1}&page=1'.format(search_entered,lang),global_s=True)
        # addNolink( '[COLOR blue][I]TVDB[/I][/COLOR]', id,27,False,fanart=' ', iconimage=' ',plot=' ')
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s ( ""name TEXT ,""free TEXT);" % ('search'))

        dbcur.execute("SELECT * FROM search ")
        match_search = dbcur.fetchall()
        all_pre_search=[]
        for nm,fr in match_search:
            all_pre_search.append(nm)
        if unque(search_entered) not in all_pre_search :
             
             dbcur.execute("INSERT INTO search Values ('%s','%s')"%(unque(search_entered.replace("'","%27")),' '))
             dbcon.commit()
             dbcon.close()

        xbmc.executebuiltin('Dialog.Close(busydialognocancel)')
        xbmcplugin .addDirectoryItems(int(sys.argv[1]),tvdb_results,len(tvdb_results))
    elif mode==6:
        from resources.default import play_link
        play_link(name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,dd,heb_name,prev_name=prev_name,has_alldd=has_alldd,nextup=nextup,video_data_exp=video_data,get_sources_nextup=get_sources_nextup,all_w=all_w,tvdb_id=tmdbid)
    elif mode==14:
        from resources.modules.tmdb_n import tmdb 
        log.warning(url)
        url,end_d=special_url(url)
        log.warning(url)
        log.warning(end_d)
        if not end_d:
            tmdb('get_movies',url.replace(' ','%20'))
                
        
    elif mode==15:
        if Addon.getSetting('new_scraper')=='true':
            from resources.find_sources import get_sources
            get_sources(name,iconimage,fanart,description,data,original_title,id,season,episode,heb_name)
        else:
            from resources.default import get_sources

            # original_title=original_title.replace('&','and').replace('?','')
            get_sources(name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,heb_name,video_data_exp=video_data,all_w=all_w,use_filter=use_filter,use_rejected=use_rejected,tvdb_id=tmdbid)
    elif mode==16:
        from  resources.modules.client import get_html
        if 'tvdb' in id :
            url2='https://'+'api.themoviedb.org/3/find/%s?api_key=34142515d9d23817496eeb4ff1d223d0&external_source=tvdb_id&language=%s'%(id.replace('tvdb',''),lang)
            pre_id=get_html(url2).json()['tv_results']
            
            if len(pre_id)>0:
                id=str(pre_id[0]['id'])
        elif 'imdb' in id:
            url2='https://'+'api.themoviedb.org/3/find/%s?api_key=34142515d9d23817496eeb4ff1d223d0&external_source=imdb_id&language=%s'%(id.replace('imdb',''),lang)
           
            pre_id=get_html(url2).json()['tv_results']
            
            if len(pre_id)>0:
                id=str(pre_id[0]['id'])
        else:
            url2='https://api.themoviedb.org/3/tv/%s?api_key=34142515d9d23817496eeb4ff1d223d0&language=%s&append_to_response=external_ids'%(id,lang)
        from resources.modules.tmdb_n import tmdb 
        #from resources.modules.tmdb import get_seasons
        #get_seasons(name,url,iconimage,fanart,description,data,original_title,id,heb_name)
        tmdb('get_seasons',url2)
        
    elif mode==18:
        from resources.default import get_genere
        get_genere(url)
    elif mode==19:
        
        #from resources.modules.tmdb import get_episode
        #get_episode(name,url,iconimage,fanart,description,data,original_title,id,season,tmdbid,show_original_year,heb_name)
        from resources.modules.tmdb_n import tmdb 
        #from resources.modules.tmdb import get_seasons
        #get_seasons(name,url,iconimage,fanart,description,data,original_title,id,heb_name)
        tmdb('get_episodes',url,heb_name=heb_name,original_title=original_title,id=id)
    elif mode==20:
        from resources.default import get_tv_maze
        get_tv_maze(url,iconimage)
    elif mode==21:
        trakt_world()
    elif mode==25:
        from resources.default import play_trailer
        play_trailer(id,url,description)
    elif mode==34:
        from resources.default import remove_from_trace
        remove_from_trace(name,original_title,id,season,episode)
    elif mode==35:
        from resources.default import ClearCache
        ClearCache()
    elif mode==65:
        from resources.default import add_remove_trakt
        add_remove_trakt(name,original_title,id,season,episode)
    elif mode==72: 
        from resources.default import by_actor
        by_actor(url,iconimage,fanart)
    elif mode==73: 
        from resources.default import actor_m
        actor_m(url,description)
    elif mode==74: 
        from resources.default import search_actor
        search_actor()
    elif mode==101:
        tv_neworks()
    elif mode==112:
        movie_prodiction()

    elif mode==114:
        main_trakt()
    elif mode==115:
        from resources.modules.trakt import progress_trakt
        progress_trakt(url)
    elif mode==116:
        from resources.modules.trakt import get_trakt
        get_trakt(url)
    elif mode==117:
        from resources.modules.trakt import get_trk_data
        get_trk_data(url)
    elif mode==118:
        from resources.modules.trakt import trakt_liked
        trakt_liked(url,iconimage,fanart)
    elif mode==119:
        from resources.modules.trakt import get_simple_trakt
        get_simple_trakt(url)
    elif mode==137:
        from resources.default import clear_rd
        clear_rd()
    elif mode==138:
        from resources.default import re_enable_rd
        re_enable_rd()
    elif mode==139:
        from resources.default import clear_pr
        clear_pr()
    elif mode==140:
        from resources.default import re_enable_pr
        re_enable_pr()
    elif mode==141:
        from resources.default import clear_all_d
        clear_all_d()
    elif mode==142:
        from resources.default import re_enable_all_d
        re_enable_all_d()
    elif mode==143:
        from resources.default import search_history
        search_history(url,iconimage,fanart)
    elif mode==144:
       from resources.default import last_played
       last_played()
    elif mode==145:
       all_w_fixed=update_all_w(url)
       #read_data2,enc_data,all_folders,url_o=last_viewed(url)
       from resources.default import last_viewed
       # read_data2,enc_data,all_folders,url_o=last_viewed(url)
       read_data2,enc_data,all_folders,url_o=cache.get(last_viewed,24,url, table='last_view')
       aa=[]
       import logging
       if len(all_folders)>0:
            #dp = xbmcgui.DialogProgressBG()

            #dp.create('Updating from trakt')
            if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_last_view")=='true' :
                all_ids=get_trakt_last()
                x=0
                from resources.modules.tmdb import get_episode_data
            from time import gmtime,strftime
            date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            try:
                from sqlite3 import dbapi2 as database
            except:
                from pysqlite2 import dbapi2 as database
            cacheFile=os.path.join(user_dataDir,'database.db')
            dbcon = database.connect(cacheFile)
            dbcur = dbcon.cursor()
            for name, url,mode, icon,added_res_trakt,all_w,heb_name,fanart,data_ep,plot,original_title,id,season,episode,eng_name,watched,show_original_year,dates,dd in all_folders:
                
                #dp.update(int((x*100.0)/len(all_folders)),name)
                if Addon.getSetting("trakt_access_token")!='' and Addon.getSetting("trakt_last_view")=='true':
                    x+=1
                    
                    if id in all_ids:
                      try:
                        season_n=all_ids[id]['season']
                        episode_n=all_ids[id]['episode']

                        if season_n!=season or episode_n>episode:
                            log.warning('Found not equal one:'+name)
                            
                            name,plot,fanart,season,episode=get_episode_data(id,season_n,episode_n,season_name=True)
                            dbcur.execute("UPDATE Lastepisode SET season='%s',episode='%s',image='%s',heb_name='%s',isr='%s' WHERE original_title = '%s' and type='%s'"%(season,episode,fanart,heb_name.replace("'","%27"),date_time,original_title.replace("'","%27"),'tv'))
                            
                            
                            dbcon.commit()
                
                      except:
                         log.warning('Not found:'+id)
                aa.append(addNolink(name, url,mode,False, iconimage=icon,all_w_trk=added_res_trakt,all_w=all_w_fixed,heb_name=heb_name,fanart=fanart,data=data_ep,plot=plot,original_title=original_title,id=id,season=season,episode=episode,eng_name=eng_name,watched=watched,show_original_year=show_original_year,dates=dates,dd=dd,dont_place=True))
            dbcon.commit()
            dbcur.close()
            dbcon.close()
            #dp.close()
            # if Addon.getSetting("trakt_access_token")!='' and url_o=='tv':
                # aa.append(addNolink( '[COLOR blue][I]---%s---[/I][/COLOR]'%Addon.getLocalizedString(32114), id,157,False,fanart='https://bestdroidplayer.com/wp-content/uploads/2019/06/trakt-what-is-how-use-on-kodi.png', iconimage=BASE_LOGO+'trakt.png',plot=' ',dont_place=True))
                
            xbmcplugin .addDirectoryItems(int(sys.argv[1]),aa,len(aa))
    elif mode==146:
        from resources.default import s_tracker
        s_tracker(name,url,iconimage,fanart,description,data,original_title,id,season,episode,show_original_year,dates,heb_name)
    elif mode==147:
        from resources.default import clear_trakt
        clear_trakt()
    elif mode==148:
        from resources.default import clear_search
        clear_search(url)
    elif mode==149:
        from resources.default import show_updates
        show_updates(force=True)
    elif mode==150:
        from resources.modules.trakt import manager
       
        manager(name, url, data)
    elif mode==151:
        Addon.openSettings()
    elif mode==157:
        if name=="Clean":
            ok=True
        else:
            ok=None
        #ok=xbmcgui.Dialog().yesno("Override",('%s (%s)'%(Addon.getLocalizedString(32150),Addon.getAddonInfo('name'))))
        remove_db=False
        show_msg=True
        if ok:
            remove_db=True
        from resources.default import sync_trk,ClearCache
        sync_trk(removedb=remove_db,show_msg=show_msg)
       
        ClearCache()

        xbmc.executebuiltin('Container.Refresh')
    elif mode==158:
        from resources.default import was_i
        was_i()
    elif mode==159:
        from resources.default import remove_was_i
        remove_was_i(name,id,season,episode)
    elif mode==160:
        from resources.modules.trakt import remove_trk_resume
        remove_trk_resume(name,id,season,episode,data,sys_arg_1=sys_arg_1)
    elif mode==162:
        clear_was_i()
    
    elif mode==164:
        from resources.modules.trakt import resume_episode_list
        resume_episode_list(url,sys_arg_1=sys_arg_1)
    elif mode==166:
        from resources.modules.trakt import get_simple_trk_data
        get_simple_trk_data(url,sys_arg_1=sys_arg_1)
    elif mode==167:
        from resources.default import set_view_type
        set_view_type(str(url))
    elif mode==168:
        from resources.default import rd_history
        rd_history(url)
    elif mode==169:
        from resources.default import rd_history_torrents
        rd_history_torrents()
    elif mode==170:
        from resources.default import simple_play
        simple_play(name,url)
    elif mode==171:
        from resources.default import remove_rd_history
        remove_rd_history(name,id)
    elif mode==172:
        from resources.default import server_test
        server_test()
    elif mode==173:
        from resources.default import en_dis_scrapers
        en_dis_scrapers(name,url)
    elif mode==174:
        from resources.default import classic_movies
        classic_movies(url)
    elif mode==175:
        listItem = xbmcgui.ListItem(name, path=url) 
        listItem.setInfo(type='Video', infoLabels={'title':name})
        ok=xbmcplugin.setResolvedUrl(handle=int(sys_arg_1), succeeded=True, listitem=listItem)
    elif mode==176:
        from resources.default import westwern_movies
        westwern_movies(url)
    elif mode==177:
        from resources.default import get_cast
        get_cast(url,id,season,episode)
    elif mode==178:
        from resources.default import get_3d
        get_3d(url)
    elif mode==179:
        from resources.default import collection_detials
        collection_detials(id)
    elif mode==180:
        try:
            path=xbmc_tranlate_path('special://home/addons/script.module.resolveurl/lib')
            sys.path.append( path)
            path=xbmc_tranlate_path('special://home/addons/script.module.six/lib')
            sys.path.append( path)
            path=xbmc_tranlate_path('special://home/addons/script.module.kodi-six/libs')
            sys.path.append( path)
            import resolveurl
            resolveurl.display_settings()
        except:
            pass
    elif mode==181:
        from resources.default import all_test_menu
        all_test_menu(iconimage,fanart)
    elif mode==182:
        from resources.default import run_system_test
        run_system_test(url)
    elif mode==183:
        from resources.default import imdb_menu
        imdb_menu(iconimage,fanart)
    elif mode==184:
        from resources.default import get_imdb_lists
        get_imdb_lists(url,iconimage,fanart)
    elif mode==185:
        from resources.default import fill_imdb_list
        fill_imdb_list(url)
    elif mode==186:
        xbmc.executebuiltin('Addon.OpenSettings(script.module.fenomscrapers)')
    elif mode==187:
        from resources.default import get_keywords_ab
        get_keywords_ab(iconimage,fanart)
    elif mode==188:
        from resources.default import  get_keywords
        get_keywords(url,iconimage,fanart,dates)
    elif mode==189:
        from resources.default import check_subs
        check_subs()
    elif mode==190:
        from resources.default import idan_chan
        idan_chan()
    elif mode==191:
        from resources.default import populate_json_playlist,populate_playlist
        if ".json" in url or ".m3u8" in url:
            populate_json_playlist(url,iconimage,fanart,search_db,mypass=mypass)
        else:
            populate_playlist(url,iconimage,fanart,search_db,mypass=mypass)
    elif mode==192:
        from resources.default import  search_jen_lists
        search_jen_lists(search_db)
    elif mode==193:
        from resources.default import master_addon
        master_addon(url,iconimage,fanart,heb_name,tmdbid,dates,description)
    elif mode==194:
        from resources.default import cat_select
        cat_select(iconimage,fanart,url)
    elif mode==196:
        from resources.default import play_youtube
        play_youtube(url,name )
    elif mode==197:
        from resources.default import cat_full_select
        cat_full_select(iconimage,fanart,url)
    elif mode==198:
        from  resources.list_module import m4ufree
        m4ufree.main_list()
    elif mode==199:
        from  resources.list_module import m4ufree
        m4ufree.m_list(name,url,iconimage,fanart)
    elif mode==200:
        from resources.default import showText
        from  resources.modules.client import get_html
        furl=re.compile('message\((.+?)\)').findall(url)
        if len(furl)==0:
            x=get_html(url.split('message/')[1]).content()
            showText(name,x)
        else:
            x=get_html(furl[0]).content()
            showText(name,x)
    elif mode==201:
        dp = xbmcgui . DialogProgress ( )
        dp.create('המתן','מרענן...')
        dp.update(0, 'המתן'+'מרענן...'+'סוגר הרחבה\n'+ '' )
        do_json = '{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}}' % (addon_id, "false")
        query = xbmc.executeJSONRPC(do_json)
        response = json.loads(query)
        
        ok_1=True
        dp.update(0, 'המתן'+'מרענן...'+'עכשיו נפתח\n'+ '' )
        do_json = '{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}}' % (addon_id, "true")
        query = xbmc.executeJSONRPC(do_json)
        response = json.loads(query)
        xbmcgui.Dialog().ok('סיימנו',str(response))
        
        dp.close()
    elif mode==202:
        from resources.default import upload_log
        upload_log()
    elif mode==203:
        remove_custom(url)
    elif mode==204:
        link=url.split('page=')[0]
        page_no=url.split('page=')[1]
        from_seek=True
        page_no = xbmcgui.Dialog().input('הכנס מספר עמוד', '', xbmcgui.INPUT_NUMERIC)#
        
        url=link+'page='+str(int(page_no)+1)
        from resources.modules.tmdb_n import tmdb 
        log.warning(url)
        url,end_d=special_url(url)
    
        if not end_d:
            tmdb('get_movies',url.replace(' ','%20'))
            
    match=[]
    elapsed_time = time.time() - start_time_start
    time_data.append(elapsed_time)
    if Addon.getSetting("display_lock")=='true':
        try:
            from sqlite3 import dbapi2 as database
        except:
            from pysqlite2 import dbapi2 as database
        cacheFile=os.path.join(user_dataDir,'database.db')
        dbcon = database.connect(cacheFile)
        dbcur = dbcon.cursor()
        dbcur.execute("CREATE TABLE IF NOT EXISTS %s (""mode TEXT,""name TEXT, ""id TEXT, ""type TEXT, ""free TEXT,""free2 TEXT);"%'views')
        try:
            dbcur.execute("SELECT * FROM views where (mode='%s' or free='global')"%(str(mode)))


                    
            match = dbcur.fetchall()
        except:
            match=[]
        dbcur.close()
        dbcon.close()
    all_modes=[]


    type='%s default'%Addon.getAddonInfo('name')
    for mode,name,id,type,free1,free2 in match:
            all_modes.append(mode)

    if mode=='global':
        type='%s default'%Addon.getAddonInfo('name')
    # log.warning('type:'+type)
    if type=='files' or type=='movies' or type=='tvshows' or type=='episodes':
        #log.warning('setContent:'+type)
        xbmcplugin.setContent(int(sys.argv[1]), type)
    else:
        if mode==2 or mode==3 or mode==114 or mode==112 or mode==101:
            xbmcplugin.setContent(int(sys.argv[1]), 'files')
        elif mode==16 :
           xbmcplugin.setContent(int(sys.argv[1]), 'seasons')
        elif mode==19 or mode==20 or sort_by_episode:
           xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
        else:
        
            if mode==14 and 'tv' in url:
                log.warning('Set Type:Tv shows')
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            else:
                log.warning('Set Type:movies')
                xbmcplugin.setContent(int(sys.argv[1]), 'movies')

    if len(all_modes)>0:
        
        #log.warning('Container.SetViewMode(%d)' % int(id))
        xbmc.executebuiltin('Container.SetViewMode(%d)' % int(id))

    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)


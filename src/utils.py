import pandas as pd 

def read_input(path, encod, **kwargs):
    dtype_values = kwargs.get('dtype_values', None)
    df = pd.read_csv(path, sep=';', encoding=encod, dtype=dtype_values)
    return df


technology=['technology','innovat','computer','high tech|high-tech','science','engineering']
consumer_protection=['privacy','data leak','leak','fake news',' safety','decept','defective','hack']
firms=['google','alphabet','apple','facebook','meta','amazon','microsoft']
products=['chrome','incognito','youtube','nexus','pixel','google drive','gmail','glass','street view','buzz','fitbit',
 'maps', 'doodle','play','translate','search', 'google news','nest hub','xl','nest','chromecast','stadia','hub',
 'marshmallow','lollipop','cloud','waymo','earth','engine',

'apple pay','apple watch','iphone','ipad','ipod','iwatch','macbook','macbook pro', 'macbook air','mac',
 'imac','airpods','ios','siri','icloud','apple tv','apple music','app store', 'safari','x','app','apple store',
 'xr', 'xs', 'se','iphones','itunes','ibook','plus','pro','max','mini','os','airtag','airtags','arcade','homepod',
'keynote','ipados','id','foxconn','facetime','beat','stalk',

'messenger','instagram', 'whatsapp','page','feed','oculus',

'prime', 'kindle',
'publishing','amazon prime','amazon drive','amazon video','amazon business','amazon web service',
'amazon cloud', 'alexa','echo dot','echo','dot', 'delivery', 'amazon uk','unlimited', 'episode','foods','grocery', 
'grand tour','grand','tour','viking', 'vikings','argo','argos','macmillan', 'dvd','clarkson','lord','ring','hair','skin','vacuum',
'pre','beer','drake','spark','kart','dog','twitch','cat','xo','matthew','stafford','ratchet','clank',
'swagway','album','mouse','showbiz','beauty','guardian','batman','arkham','gc','hair','skin','shirt',
'lovefilm','mirzapur','cast','audio','drama','movie','jack ryan','actor','character','lucifer','outlander',
'premier','super mario','sky','channel','voyage',


'windows','window','xp','surface','xbox','studio','microsoft office', 'office','word','cortana', 'surface pro','teams',  'playstation',
'microsoft edge', 'edge', 'gear','outlook','halo','skype','kinect','internet explorer','explorer','ie','bing','xcloud','hololens',
'forza','ori','scarlett','scorpio','wordperfect','valhalla','onedrive','games gold','lumia','azure',
'assassin creed','assassin','creed','minecraft','yammer','warcraft','tay']



ceos=['sundar','pichai','eric','schmidt','steve jobs','tim cook','mark zuckerberg','andy jassy','jeff','bezos','satya', 'nadella','bill gates',
      'gates','steve job','steve','tim', 'cook','zuckerberg','ceo','tim cook ','steve ballmer','ballmer','elop',
      'schiller','fadell','phil spencer','spencer','mcspirit','sandberg','paul','allen','larry hryb','hryb']
      

types=['tablet','mobile', 'laptop', 'pc', 'computer', 'desktop','smartphone', 'smartwatch', 'search engine', 'software','hardware',
               'machine', 'browser','ebook', 'book',  'reader',  'console', 'headphone', 'earbud','bud','store','music',
              'gaming', 'operating','streaming','title','chatbot']



competitor=['samsung', 'galaxy',  'twitter','tiktok', 'switch','sony', 'asos', 'activision blizzard', 'activision','blizzard',
            'nintendo','snes', 'netflix','android','yahoo','nokia','huawei','motorola','htc','blackberry','oppo','oneplus','rim','symbian','bbc','morrison','spotify'] 


configue=['device','feature','battery','screen','sound','gb','g','k','mm','chip','processor','design','display','touch','ram',
          'inch','keyboard','camera','handset','speaker','button','touchscreen','storage', 'data']


celebrity=['dubost','neymar','amanda','beyonce','blur','richard','hammond','ranj','jeremy clarkson', 'jeremy','momoa',
           'jared','aniston','smith','kim','tony','tom','sophie','oasis','trio','sharon','betty','raoul','moat','lauren','andrew',
           'samuel gibbs','samuel','gibbs','van','gaal']

topics = celebrity + configue + competitor + types + ceos + products + firms + consumer_protection + technology

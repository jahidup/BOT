# config.py
# Owner and Admins
OWNER_ID = 8104850843
ADMIN_IDS = [5987905091]

# Force Join Channels
CHANNELS = [-1003090922367, -1003698567122, -1003672015073]
CHANNEL_LINKS = [
    "https://t.me/all_data_here",
    "https://t.me/osint_lookup",
    "https://t.me/legend_chats_osint"
]

# Log Channels – अपनी चैनल IDs यहाँ डालें (बॉट को admin बनाना न भूलें.)
LOG_CHANNELS = {
    'num': -1003482423742,
    'ifsc': -1003624886596,
    'email': -1003431549612,
    'gst': -1003634866992,
    'vehicle': -1003237155636,
    'pincode': -1003677285823,
    'instagram': -1003498414978,
    'github': -1003576017442,
    'pakistan': -1003663672738,
    'ip': -1003665811220,
    'aadhar': -1003482423742,
    'family': -1003643170105,
    'tg2num': -1003642820243,
    'vehicle_chalan': -1003237155636,      # 🔥 NAYA
    'vehicle_to_number': -1003237155636,    # 🔥 NAYA
}

APIS = {
    'num': {
        'url': 'https://ayaanmods.site/number.php?key=annonymous&number={}',
        'param': 'number',
        'log': LOG_CHANNELS['num'],
        'desc': 'Mobile number lookup',
        'extra_blacklist': ['API_Developer', 'channel_name', 'channel_link', ]
    },
    'ifsc': {
        'url': 'https://ifsc-info-api-abhigyan-codes.onrender.com/ifsc?code={}',
        'param': 'ifsc',
        'log': LOG_CHANNELS['ifsc'],
        'desc': 'IFSC code lookup',
        'extra_blacklist': ['channel', 'developer']
    },
    'email': {
        'url': 'https://anon-email-info.vercel.app/email?key=tempe124&email={}',
        'param': 'email',
        'log': LOG_CHANNELS['email'],
        'desc': 'Email validation & domain info',
        'extra_blacklist': ['developer']
    },
    'gst': {
        'url': 'https://gst-info-api-by-abhigyan-codes-1.onrender.com/gst?number={}',
        'param': 'gst',
        'log': LOG_CHANNELS['gst'],
        'desc': 'GST number lookup',
        'extra_blacklist': ['meta']
    },
    'vehicle': {
        'url': 'https://api.b77bf911.workers.dev/vehicle?registration={}',
        'param': 'RC number',
        'log': LOG_CHANNELS['vehicle'],
        'desc': 'Vehicle registration details',
        'extra_blacklist': ['challan']
    },
    'vehicle_chalan': {                      # 🔥 NAYA
        'url': 'https://api.b77bf911.workers.dev/vehicle?registration={}',
        'param': 'RC number',
        'log': LOG_CHANNELS['vehicle_chalan'],
        'desc': 'Vehicle Challan Information',
        'extra_blacklist': []
    },
    'vehicle_to_number': {                    # 🔥 NAYA
        'url': 'https://anon-vehicle-info.vercel.app/rc?key=temp114&rc={}',
        'param': 'RC number',
        'log': LOG_CHANNELS['vehicle_to_number'],
        'desc': 'Vehicle Owner Mobile Number',
        'extra_blacklist': ['developer']
    },
    'pincode': {
        'url': 'https://api.postalpincode.in/pincode/{}',
        'param': 'pincode',
        'log': LOG_CHANNELS['pincode'],
        'desc': 'Pincode details',
        'extra_blacklist': []
    },
    'instagram': {
        'url': 'https://anon-insta-info.vercel.app/profile?key=temp104&username={}',
        'param': 'username',
        'log': LOG_CHANNELS['instagram'],
        'desc': 'Instagram user info',
        'extra_blacklist': ['developer']
    },
    'github': {
        'url': 'https://info-github-api.vercel.app/api/github?username={}',
        'param': 'username',
        'log': LOG_CHANNELS['github'],
        'desc': 'GitHub user info',
        'extra_blacklist': ['credits']
    },
    'pakistan': {
        'url': 'https://pak-number-and-cnic-info-api-by-abhigyan.onrender.com/api/lookup?query=92{}',
        'param': 'number',
        'log': LOG_CHANNELS['pakistan'],
        'desc': 'Pakistan mobile number lookup',
        'extra_blacklist': ['copyright']
    },
    'ip': {
        'url': 'https://anon-multi-info.vercel.app/ipinfo?key=temp104&ip={}',
        'param': 'ip',
        'log': LOG_CHANNELS['ip'],
        'desc': 'IP address geolocation',
        'extra_blacklist': ['developer']
    },
    'aadhar': {
        'url': 'https://anon-num-info.vercel.app/aadhar?key=temp104&id={}',
        'param': 'aadhaar number',
        'log': LOG_CHANNELS['aadhar'],
        'desc': 'Aadhaar info lookup',
        'extra_blacklist': ['developer']
    },
    'family': {
        'url': 'https://sbsakib.eu.cc/sab/?key=Demo&type=id_family&term={}',
        'param': 'aadhaar number',
        'log': LOG_CHANNELS['family'],
        'desc': 'Family info lookup',
        'extra_blacklist': ['owner']
    },
    'tg2num': {
        'url': 'https://sbsakib.eu.cc/api/Tg_username/?key=Premium_User&username={}',
        'param': 'telegram user ID',
        'log': LOG_CHANNELS['tg2num'],
        'desc': 'Telegram to number lookup',
        'extra_blacklist': ['developer', 'key_status', 'owner', '9277193139']
    },
}

DEV_USERNAME = "@Nullprotocol_X"
POWERED_BY = "NULL PROTOCOL"
BACKUP_CHANNEL = -1003740236326

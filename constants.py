# Rest API config
HOST = '0.0.0.0'
PORT = 8500

# MongoDB config
MONGO_HOST = '172.104.185.102'
MONGO_PORT = 8600
MONGO_DB = 'newsquiz'
MONGO_USER = 'newsquiz'
MONGO_PASS = 'grdVGACnq$2019'
MONGO_URI = 'mongodb://%s:%s@%s:%d/%s?authSource=admin' % (MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_DB)

# Public/static folder
STATIC_FOLDER = 'static'
PUBLIC_FOLDER = STATIC_FOLDER

# Models
Q_RECOMMENDER_MODEL = 'recommendation/models/q_recommeder.pkl'

# Others
TOPICS  = ['economy', 'society', 'sports', 'recommended', 'politics']
LEVELS = ['easy', 'medium', 'hard']
PUBLISHERS = ['wsj', 'bbc', 'kenh14']
TYPES = ['text', 'audio']
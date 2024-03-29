# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX


class Config(object):
    # Configuration class for the bot

    # Enable or disable logging
    LOGGER = True

    # <================================================ REQUIRED ======================================================>
    # Telegram API configuration
    API_ID = 20434292  # Get this value from my.telegram.org/apps
    API_HASH = "ea4683f64ac46aa1d6fb236638a0ac01"

    # Database configuration (PostgreSQL)
    DATABASE_URL = "postgres://uiktkvesrmrjmy:3061a4f38474806381c45607b29918f11c71945a40f5c8f74e84290fc8255ead@ec2-3-230-24-12.compute-1.amazonaws.com:5432/d7gggb2vcebk3o"

    # Event logs chat ID and message dump chat ID
    EVENT_LOGS = -1004176732118
    MESSAGE_DUMP = -1004176732118

    # MongoDB configuration
    MONGO_DB_URI = "mongodb+srv://anmol:anmol@cluster0.kh5am2k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Support chat and support ID
    SUPPORT_CHAT = "movies_samrajya"
    SUPPORT_ID = -1001619678735

    # Database name
    DB_NAME = "MikoDB"

    # Bot token
    TOKEN = "7043985048:AAEbqy8519urzcj07MO9lZ4BrlGVokX2U7c"  # Get bot token from @BotFather on Telegram

    # Owner's Telegram user ID (Must be an integer)
    OWNER_ID = 1663603208
    # <=======================================================================================================>

    # <================================================ OPTIONAL ======================================================>
    # Optional configuration fields

    # List of groups to blacklist
    BL_CHATS = []

    # User IDs of sudo users, dev users, support users, tiger users, and whitelist users
    DRAGONS = []  # Sudo users
    DEV_USERS = []  # Dev users
    DEMONS = []  # Support users
    TIGERS = []  # Tiger users
    WOLVES = []  # Whitelist users

    # Toggle features
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True

    # Modules to load or exclude
    LOAD = []
    NO_LOAD = []

    # Global ban settings
    STRICT_GBAN = True

    # Temporary download directory
    TEMP_DOWNLOAD_DIRECTORY = "./"
    # <=======================================================================================================>


# <=======================================================================================================>


class Production(Config):
    # Production configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True


class Development(Config):
    # Development configuration (inherits from Config)

    # Enable or disable logging
    LOGGER = True

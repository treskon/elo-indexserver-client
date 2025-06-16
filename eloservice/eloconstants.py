from enum import Enum

from eloclient.models import SordZ, SordC, EditInfoZ, EditInfoC, copy_sord_z, CopySordC, LockZ, CheckoutUsersZ, \
    CheckinUsersZ


class ElobitsetEditz(Enum):
    MASK_NAMES = "1"
    MB_ALL = "2196631817761587199"  # Results as a Bitshift, originates from java source code
    MB_OBJ_KEYS = "9007199254740992"
    MB_MASK = "8192"
    MB_NAME = "32"  # long mbName = (1L << 5);
    MB_ID_ONLY = "1"


SORD_Z_EMPTY = SordZ()  # Useful when you don't need any bitset, however the API requires it. This usually means that
# the indexserver will decide for you. One example is the ix_service_port_if_checkin_sord_path

SORD_Z_MB_ALL = SordZ(SordC.mb_all)
SORD_Z_MB_ALL.bset = ElobitsetEditz.MB_ALL.value

SORD_Z_MB_NAME = SordZ()
SORD_Z_MB_NAME.bset = ElobitsetEditz.MB_NAME.value

EDIT_INFO_Z_MB_ALL = EditInfoZ(EditInfoC().mb_all)
EDIT_INFO_Z_MB_ALL.bset = ElobitsetEditz.MB_ALL.value
EDIT_INFO_Z_MB_ALL.sord_z = SordZ(SordC.mb_all)
EDIT_INFO_Z_MB_ALL.sord_z.bset = ElobitsetEditz.MB_ALL.value

EDIT_INFO_Z_MASK_NAMES = EditInfoZ(EditInfoC().mb_mask_names)
EDIT_INFO_Z_MASK_NAMES.bset = ElobitsetEditz.MASK_NAMES.value
EDIT_INFO_Z_MASK_NAMES.sord_z = SordZ()
EDIT_INFO_Z_MASK_NAMES.bset = ElobitsetEditz.MASK_NAMES.value

EDIT_INFO_Z_MB_ID = EditInfoZ(EditInfoC().mb_only_id)
EDIT_INFO_Z_MB_ID.bset = ElobitsetEditz.MB_ID_ONLY.value
EDIT_INFO_Z_MB_ID.sord_z = SordZ()
EDIT_INFO_Z_MB_ID.bset = ElobitsetEditz.MB_ID_ONLY.value

COPY_SORD_C_MOVE = copy_sord_z.CopySordZ(CopySordC().move)
COPY_SORD_C_MOVE.bset = 1

# To retrieve the maskInfos + set mask values we need these bitsets
EDIT_INFO_Z_MB_MASK_INFOS = EditInfoZ(EditInfoC().mb_all)
EDIT_INFO_Z_MB_MASK_INFOS.bset = str(int(ElobitsetEditz.MB_OBJ_KEYS.value) + int(ElobitsetEditz.MB_MASK.value))
EDIT_INFO_Z_MB_MASK_INFOS.sord_z = SordZ(SordC.mb_all)
EDIT_INFO_Z_MB_MASK_INFOS.sord_z.bset = str(int(ElobitsetEditz.MB_OBJ_KEYS.value) + int(ElobitsetEditz.MB_MASK.value))

SordZ_INFO_MB_MASK_INFOS = SordZ(bset=EDIT_INFO_Z_MB_MASK_INFOS.bset)

LOCK_Z_YES = LockZ("1")
LOCK_Z_NO = LockZ("0")
LOCK_Z_IF_FREE = LockZ("2")
LOCK_Z_FORCE = LockZ("4")

CHECKOUT_USERS_Z_ALL_BY_ID = CheckoutUsersZ()
CHECKOUT_USERS_Z_ALL_BY_ID.bset = "1"

CHECKOUT_USERS_Z_ALL_USER = CheckoutUsersZ()
CHECKOUT_USERS_Z_ALL_USER.bset = "2"

CHECKOUT_USERS_Z_ALL_GROUPS = CheckoutUsersZ()
CHECKOUT_USERS_Z_ALL_GROUPS.bset = "3"

CHECKOUT_USERS_Z_MEMBERS_OF_GROUP = CheckoutUsersZ()
CHECKOUT_USERS_Z_MEMBERS_OF_GROUP.bset = "5"
# 1 = Gruppen Details der übergebenen ID
# 2 = Alle Benutzer von AC
# 3 = Alle Gruppen von AC
# 4 = Alle Gruppen und alle Benutzer von AC
# 5 = Benutzer Details der Gruppenmitglieder (übergebene ID)

CHECKIN_USER_UPDATE = CheckinUsersZ()
CHECKIN_USER_UPDATE.bset = "1" # Update an existing user

CHECKIN_USER_CREATE = CheckinUsersZ()
CHECKIN_USER_CREATE.bset = "5" # Create a new user


elo_text_mime_types = [
    "text/",
    "application/json",
    "application/javascript",
    "application/xml",
    "application/x-www-form-urlencoded",
    "application/xhtml+xml",
    "application/html",
    "application/xml",
    "application/yaml",
    "application/csv"
    # not complete
]


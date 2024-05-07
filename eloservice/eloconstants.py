from enum import Enum

from eloclient.models import SordZ, SordC, EditInfoZ, EditInfoC, copy_sord_z, CopySordC, LockC


class ElobitsetEditz(Enum):
    MASK_NAMES = "1"
    MB_ALL = "2196631817761587199"  # Results as a Bitshift, originates from java source code
    MB_OBJ_KEYS = "9007199254740992"
    MB_MASK = "8192"


SORD_Z_EMPTY = SordZ()  # Useful when you don't need any bitset, however the API requires it. This usually means that
# the indexserver will decide for you. One example is the ix_service_port_if_checkin_sord_path

SORD_Z_MB_ALL = SordZ(SordC.mb_all)
SORD_Z_MB_ALL.bset = ElobitsetEditz.MB_ALL.value

EDIT_INFO_Z_MB_ALL = EditInfoZ(EditInfoC().mb_all)
EDIT_INFO_Z_MB_ALL.bset = ElobitsetEditz.MB_ALL.value
EDIT_INFO_Z_MB_ALL.sord_z = SordZ(SordC.mb_all)
EDIT_INFO_Z_MB_ALL.sord_z.bset = ElobitsetEditz.MB_ALL.value

EDIT_INFO_Z_MASK_NAMES = EditInfoZ(EditInfoC().mb_mask_names)
EDIT_INFO_Z_MASK_NAMES.bset = ElobitsetEditz.MASK_NAMES.value
EDIT_INFO_Z_MASK_NAMES.sord_z = SordZ()
EDIT_INFO_Z_MASK_NAMES.bset = ElobitsetEditz.MASK_NAMES.value

COPY_SORD_C_MOVE = copy_sord_z.CopySordZ(CopySordC().move)
COPY_SORD_C_MOVE.bset = 1

# To retrieve the maskInfos + set mask values we need these bitsets
EDIT_INFO_Z_MB_MASK_INFOS = EditInfoZ(EditInfoC().mb_all)
EDIT_INFO_Z_MB_MASK_INFOS.bset = str(int(ElobitsetEditz.MB_OBJ_KEYS.value) + int(ElobitsetEditz.MB_MASK.value))
EDIT_INFO_Z_MB_MASK_INFOS.sord_z = SordZ(SordC.mb_all)
EDIT_INFO_Z_MB_MASK_INFOS.sord_z.bset = str(int(ElobitsetEditz.MB_OBJ_KEYS.value) + int(ElobitsetEditz.MB_MASK.value))

SordZ_INFO_MB_MASK_INFOS = SordZ(bset=EDIT_INFO_Z_MB_MASK_INFOS.bset)

LOCK_Z_YES = SordZ(LockC().yes)
LOCK_Z_NO = SordZ(LockC().no)

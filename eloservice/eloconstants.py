from enum import Enum

from eloclient.models import SordZ, SordC, EditInfoZ, EditInfoC, copy_sord_z, CopySordC


class ElobitsetEditz(Enum):
    MASK_NAMES = "1"
    MB_ALL = "2196631817761587199"  # Results as a Bitshift, originates from java source code


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

"""
Integration tests for keywording aspects (ELO 23 and newer).

Self-contained: the test aspect and the aspect mask are created on the server if they don't exist yet (they are kept
for later runs, as masks/aspects that were used can't be deleted easily). The documents of a run are created in a new
folder that is removed at the end.
"""
import os
import time
import unittest
import uuid
from datetime import date, datetime

from eloservice import elo_service
from eloservice.aspect_util import (ASPECT_LINE_TYPE_TEXT, ASPECT_LINE_TYPE_INTEGER, ASPECT_LINE_TYPE_DOUBLE,
                                    ASPECT_LINE_TYPE_ISO_DATE_ONLY, ASPECT_LINE_TYPE_ISO_DATE_TIME, ASPECT_Z_MB_ALL,
                                    EDIT_INFO_Z_MB_ALL, LOCK_Z_NO)

ASPECT_NAME = "PyClientTestAspect"
MASK_NAME = "PyClient Aspect Test"
ASSOC_MANY = "PYTEST_MANY"
ASSOC_SINGLE = "PYTEST_SINGLE"
LINES = {
    "TXT": ASPECT_LINE_TYPE_TEXT,
    "NUM": ASPECT_LINE_TYPE_INTEGER,
    "DBL": ASPECT_LINE_TYPE_DOUBLE,
    "DAY": ASPECT_LINE_TYPE_ISO_DATE_ONLY,
    "TS": ASPECT_LINE_TYPE_ISO_DATE_TIME,
}
DOC_MASK_Z_MB_ALL = {"bset": "72057594037927935"}  # DocMaskC.mbAll


def _service():
    return elo_service.EloService(url=os.environ["TEST_ELO_IX_URL"], user=os.environ["TEST_ELO_IX_USER"],
                                  password=os.environ["TEST_ELO_IX_PASSWORD"])


def _ensure_test_aspect(service) -> int:
    util = service.aspect_util
    existing = next((a for a in service.get_aspects() if a.name == ASPECT_NAME), None)
    if existing is not None:
        return existing.id
    errors = []
    # AspectLineC.TYPE_* (DocMaskLineC.TYPE_* + 100); some Indexserver versions only accept the DocMaskLineC types
    for offset in (0, -100):
        lines = [{"key": key, "type": line_type + offset, "displayName": key} for key, line_type in LINES.items()]
        try:
            aspect = util._call("createAspect", {"name": ASPECT_NAME, "lines": lines})
            return util._call("checkinAspect", {"aspect": aspect, "aspectZ": ASPECT_Z_MB_ALL, "unlockZ": LOCK_Z_NO})
        except ValueError as e:
            errors.append(str(e))
    version = util._call("getConstants", {}).get("STREAM_VERSION")
    raise ValueError(f"Could not create test aspect on Indexserver {version}: {errors}")


def _ensure_test_mask(service, aspect_id: int) -> str:
    util = service.aspect_util
    if service.mask_util.get_mask_name(MASK_NAME) is None:
        assocs = [
            util._call("createAspectAssoc", {"name": ASSOC_MANY, "aspectId": str(aspect_id),
                                             "cardinality": "OPTIONAL_MANY"}),
            util._call("createAspectAssoc", {"name": ASSOC_SINGLE, "aspectId": str(aspect_id),
                                             "cardinality": "OPTIONAL"}),
        ]
        mask = util._call("createAspectMask", {"name": MASK_NAME, "aspectAssocs": assocs})
        util._call("checkinDocMask", {"docMask": mask, "docMaskZ": DOC_MASK_Z_MB_ALL, "unlockZ": LOCK_Z_NO})
        service.mask_util.cache_get_all_masks_names.clear()
    return str(service.mask_util.get_mask_name(MASK_NAME).id)


def _create_sord(service, parent_id: str, mask_id: str, name: str) -> str:
    util = service.aspect_util
    sord = util._call("createSord", {"parentId": parent_id, "maskId": mask_id, "editInfoZ": EDIT_INFO_Z_MB_ALL})["sord"]
    sord["name"] = name
    return str(util._call("checkinSord", {"sord": sord, "sordZ": EDIT_INFO_Z_MB_ALL["sordZ"], "unlockZ": LOCK_Z_NO}))


class TestAspects(unittest.TestCase):
    service = None
    aspect_id = None
    mask_id = None
    folder = None

    @classmethod
    def setUpClass(cls):
        cls.service = _service()
        cls.aspect_id = _ensure_test_aspect(cls.service)
        cls.mask_id = _ensure_test_mask(cls.service, cls.aspect_id)
        cls.folder = cls.service.create_folder(f"¶aspect-test-{int(time.time() * 1000)}")

    @classmethod
    def tearDownClass(cls):
        if cls.folder is not None:
            cls.service.remove(cls.folder)

    def _new_sord(self):
        return _create_sord(self.service, self.folder, self.mask_id, f"aspect {uuid.uuid4().hex[:8]}")

    def test_get_aspects(self):
        aspects = self.service.get_aspects()
        self.assertIn(ASPECT_NAME, [a.name for a in aspects])

    def test_get_aspect(self):
        for identifier in [ASPECT_NAME, str(self.aspect_id)]:
            aspect = self.service.get_aspect(identifier)
            self.assertEqual(ASPECT_NAME, aspect.name)
            self.assertEqual(set(LINES), set(aspect.lines))

    def test_get_mask_aspect_assocs(self):
        assocs = self.service.get_mask_aspect_assocs(MASK_NAME)
        self.assertEqual({ASSOC_MANY, ASSOC_SINGLE}, set(assocs))
        self.assertEqual("OPTIONAL_MANY", assocs[ASSOC_MANY].cardinality)
        self.assertEqual("OPTIONAL", assocs[ASSOC_SINGLE].cardinality)
        self.assertEqual(self.aspect_id, assocs[ASSOC_MANY].aspect_id)
        self.assertEqual({}, self.service.get_mask_aspect_assocs("E-Mail"))

    def test_write_and_read_aspect_fields(self):
        sord_id = self._new_sord()
        objects = [
            {"TXT": "Grüß Gott", "NUM": 42, "DBL": 3.5, "DAY": date(2024, 1, 31),
             "TS": datetime(2024, 1, 31, 13, 45, 10)},
            {"TXT": "second", "NUM": -7},
        ]
        self.service.write_aspect_fields(sord_id, {ASSOC_MANY: objects, ASSOC_SINGLE: {"TXT": "single"}})
        fields = self.service.get_aspect_fields(sord_id)
        self.assertEqual(objects, fields[ASSOC_MANY])
        self.assertEqual([{"TXT": "single"}], fields[ASSOC_SINGLE])

        # only the given association is replaced
        self.service.write_aspect_fields(sord_id, {ASSOC_SINGLE: {"TXT": "changed"}})
        fields = self.service.get_aspect_fields(sord_id)
        self.assertEqual(objects, fields[ASSOC_MANY])
        self.assertEqual([{"TXT": "changed"}], fields[ASSOC_SINGLE])

        # an empty list removes the objects of an association
        self.service.write_aspect_fields(sord_id, {ASSOC_MANY: []})
        self.assertEqual([], self.service.get_aspect_fields(sord_id).get(ASSOC_MANY, []))

    def test_write_invalid(self):
        sord_id = self._new_sord()
        with self.assertRaises(ValueError):
            self.service.write_aspect_fields(sord_id, {"NOT_AN_ASSOC": {"TXT": "x"}})
        with self.assertRaises(ValueError):
            self.service.write_aspect_fields(sord_id, {ASSOC_SINGLE: {"NOT_A_LINE": "x"}})
        with self.assertRaises(ValueError):
            self.service.write_aspect_fields(sord_id, {ASSOC_SINGLE: [{"TXT": "a"}, {"TXT": "b"}]})

    def test_search_aspect_fields(self):
        sord_id = self._new_sord()
        other_id = self._new_sord()
        marker = f"search-{uuid.uuid4().hex}"
        self.service.write_aspect_fields(sord_id, {ASSOC_MANY: [{"TXT": marker, "NUM": 1001}]})
        self.service.write_aspect_fields(other_id, {ASSOC_MANY: [{"TXT": marker, "NUM": 5}]})

        found = self.service.search(search_aspect_fields={f"{ASSOC_MANY}¶{ASPECT_NAME}¶TXT": marker})
        self.assertEqual({sord_id, other_id}, set(found))
        # wildcard for the association
        found = self.service.search(search_aspect_fields={f"¶{ASPECT_NAME}¶TXT": marker,
                                                          f"¶{ASPECT_NAME}¶NUM": ("GREATER", 1000)})
        self.assertEqual([sord_id], found)
        # or
        found = self.service.search(search_aspect_fields={f"¶{ASPECT_NAME}¶TXT": marker,
                                                          f"¶{ASPECT_NAME}¶NUM": [1001, 5]})
        self.assertEqual({sord_id, other_id}, set(found))
        self.assertTrue(self.service.exists(search_aspect_fields={f"¶{ASPECT_NAME}¶NUM": 1001,
                                                                  f"¶{ASPECT_NAME}¶TXT": marker}))
        self.assertFalse(self.service.exists(search_aspect_fields={f"¶{ASPECT_NAME}¶TXT": marker + "-none"}))


if __name__ == '__main__':
    unittest.main()

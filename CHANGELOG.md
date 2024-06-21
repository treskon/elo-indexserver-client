## 20.0.0.111

generated client for 20.0.0.111

## 0.1.9

base version

## 0.1.10

Moved from private repo to public GitHub repo.

## 0.1.11

PR:

* https://github.com/treskon/elo-indexserver-client/pull/3

Details:

* Updated to OpenAPI Spec from elo
* Added write_map_fields method to EloService

## 0.1.12

PR:

* https://github.com/treskon/elo-indexserver-client/pull/6

Details:

* Added configurable caching for overwrite_mask_fields (caches get_all_masks_names and get_mask_detail)
* Fix a bug that caused a severe performance issue during overwrite_mask_fields

## 0.1.13

PR:

* https://github.com/treskon/elo-indexserver-client/pull/7

Details:

* Hotfix create_folder method; used wrong bitset (mb_all) resulted in indexserver trying to assign 'freie eingabe' mask
  to a folder which is not possible on some elo instances. We updated our elo testing server to be more strict on this
  so we prevent this issue in the future

## 0.1.14

PR:

* https://github.com/treskon/elo-indexserver-client/pull/10

Details:

* add optional parameter filename_objkey, filename_objkey_id for upload_file and update_file. Which sets the filename in
  the options tab (internally done via a predefined obj_key entry)

## 0.1.15

PR:

* https://github.com/treskon/elo-indexserver-client/pull/11

overwrite_mask_fields add optional param metadata_force #11

Details:

* Add metadata_force to method overwrite_mask_fields. This allows to set metadata by ID that is otherwise not assignable
  to a mask. Useful in certain cases like the special filename mask objkeys

## 0.1.16

PR:

* https://github.com/treskon/elo-indexserver-client/pull/13

file_util: guess mimetype based on the obj_key parameter instead of the filename



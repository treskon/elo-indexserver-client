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

## 0.1.17

PR:

* https://github.com/treskon/elo-indexserver-client/pull/14
    * update method upload_file and update_file.
* https://github.com/treskon/elo-indexserver-client/pull/15
    * Add a method to download a file by its sord_id

Details:
upload_file and update_file are now also setting the x_date_iso.
Automatically:

* the modified date of the file
  Manually:
* can be set by the caller of the function.

i_date_iso = Time of the archiving - technical date on which the file was uploaded
x_date_iso = Primary document date (optional) - usecase dependent date, e.g. invoice date, contract date, etc.

## 0.1.18

PR:

* https://github.com/treskon/elo-indexserver-client/pull/12
    * Read map fields

Details:

* Added read_map_fields method to EloService to read map fields from a sord
    * Can load all map fields or only specific ones
    * Can load strings or entire byte arrays
    * Can load a specific map domain

## 0.1.19

PR:

* https://github.com/treskon/elo-indexserver-client/pull/16
    * add a convenient method to automatically convert the obj_keys from a sord to a dict and cast them to their type
      according to the config in the docmask.

## 0.1.20

* https://github.com/treskon/elo-indexserver-client/pull/17
    * add serialize_map_fields_table and deserialize_map_fields_table:  Helper Method to serializes, given the raw elo
      map fields, a table like format. The table is represented as a list
      of dictionaries, where each dictionary represents a row in the table.
      All operations are done in memory and no ELO operations are performed.

## 0.1.21

* https://github.com/treskon/elo-indexserver-client/pull/18
    * maputils: serialize_table, deserialize_table remove table_name parameter as it was a wrong assumption that elo uses best practices

## 0.1.22

* https://github.com/treskon/elo-indexserver-client/pull/19
    * maputils: 'write_map_fields': change fallback behaviour when a value > 255 is stored


Previously if one value was larger all other values were also written as blob. 
Patched Version: Only the larger values are written as blobs. Other values are still written as strings.
This results in 2 API calls which reduces performance. However, in a real world scenario the old behaviour was not useful as ELO does not have that fallback build in. So most UIs would show just an empty field, even if the Map Blob field was filled.

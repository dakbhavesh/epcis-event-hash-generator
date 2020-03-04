from .epcis_event_hash_generator import xml_epcis_hash

from os import walk

TEST_FILE_PATH = "../testFiles/examples"
TEST_FILE_PATH_SAME_EVENT = "../testFiles/expected_equal/"


def test_distinct():
    """
    Assert that there are no collisions, i.e. different events must have different hashes.
    """
    all_hashes = []

    for (_, _, filenames) in walk(TEST_FILE_PATH):
        for filename in filenames:
            if filename.endswith("xml"):
                all_hashes += xml_epcis_hash(TEST_FILE_PATH + filename, "sha256")[0]
        break
    
    assert all_hashes
    assert len(all_hashes) == len(set(all_hashes))
    
def testEqual():    
    """
    Assert that different representations of the same events have the same hash.
    """
    for (_, _, filenames) in walk(TEST_FILE_PATH_SAME_EVENT):
        for filename in filenames:
            if filename.endswith("xml"):
                assert len(set(xml_epcis_hash(TEST_FILE_PATH_SAME_EVENT + filename, "sha256")[0])) == 1
        break

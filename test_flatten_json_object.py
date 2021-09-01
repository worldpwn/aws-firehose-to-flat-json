from flat import flatten_json_object
import json


def test_oneLevelObject_shouldSaveValue():
    obj = {"value": 12}
    result = flatten_json_object(obj)
    assert result == {"value": 12}


def test_oneLevelMultiValueObject_shouldSaveValue():
    obj = {"value": 12, "other": [1, 3]}
    result = flatten_json_object(obj)
    assert result == {"value": 12, "other": [1, 3]}


def test_twoLevelMultiValueObject_shouldFlattenValue():
    obj = {"value": 12, "other": {"otherVal": 23}}
    result = flatten_json_object(obj)
    assert result == {"value": 12, "other_otherVal": 23}


def test_threeLevelSingleValueObject_shouldStringify():
    obj = {"other": {"levelThree": {"threeVal": [1]}}}
    result = flatten_json_object(obj)
    assert result == {
        "other_levelThree": json.dumps({"threeVal": [1]}),
    }


def test_levelTwo_threeLevelMultiValueObject_shouldFlattenValue():
    obj = {"value": 12, "other": {"otherVal": 23, "levelThree": {"threeVal": [1]}}}
    result = flatten_json_object(obj)
    assert result == {
        "value": 12,
        "other_otherVal": 23,
        "other_levelThree": json.dumps({"threeVal": [1]}),
    }

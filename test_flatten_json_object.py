from flat import flatten_json_object
import json


def test_levelOne_oneLevelObject_shouldStringifyValue():
    obj = {"value": 12}
    level = 1
    result = flatten_json_object(obj, level)
    assert result == {"value": "12"}


def test_levelTwo_oneLevelObject_shouldSameValue():
    obj = {"value": 12}
    level = 2
    result = flatten_json_object(obj, level)
    assert result == {"value": 12}


def test_levelOne_oneLevelMultiValueObject_shouldStringifyValue():
    obj = {"value": 12, "other": [1, 3]}
    level = 2
    result = flatten_json_object(obj, level)
    assert result == {"value": 12, "other": [1, 3]}

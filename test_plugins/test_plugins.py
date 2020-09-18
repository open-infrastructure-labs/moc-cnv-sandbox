def test_false(value):
    return bool(value) is False


def test_has_kv(obj, key, val):
    return key in obj and obj[key] == val


def test_indirect_has_kv(target, obj, key, val):
    return target in obj and key in obj[target] and obj[target][key] == val


class TestModule(object):
    def tests(self):
        return {
            'false': test_false,
            'haskv': test_has_kv,
            'indirect_has_kv': test_indirect_has_kv,
        }

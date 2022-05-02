import sys


def vs():
    # 1
    print(sys.version)
    print(sys.version_info)

    # 3
    a = b'h\x65llo'
    print(list(a))
    print(a)


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # instance


if __name__ == '__main__':
    vs()
    print(repr(to_str(b'foo')))
    print(repr(to_str('bar')))
    print(repr(to_str(b'\xed\x95\x9c')))

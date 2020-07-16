import base64


def ignition_encode(val, content_type='text/plain', charset='utf-8'):
    content = base64.b64encode(val.encode(charset)).decode()
    return f'data:{content_type};charset={charset};base64,{content}'


def ignition_encode_files(val, content_type='text/plain', charset='utf-8'):
    '''Iterate through an ignition configuration and replace
    inline content with the base64 encoded version'''

    for filespec in val.get('spec', {}).get('config', {}).get('storage', {}).get('files', []):
        if 'contents' in filespec:
            if 'inline' in filespec['contents']:
                filespec['contents']['source'] = (
                    ignition_encode(filespec['contents']['inline']))
                del filespec['contents']['inline']

    return val


class FilterModule(object):
    def filters(self):
        return {
            'ignition_encode': ignition_encode,
            'ignition_encode_files': ignition_encode_files,
        }


if __name__ == '__main__':
    import argparse
    import sys
    import yaml

    p = argparse.ArgumentParser()
    p.add_argument('-o', '--output', dest='outputfile')
    p.add_argument('inputfile', nargs='?')
    args = p.parse_args()

    inputfile = open(args.inputfile) if args.inputfile else sys.stdin
    outputfile = open(args.outputfile, 'w') if args.outputfile else sys.stdout

    with inputfile:
        data = yaml.safe_load(inputfile)
        ignition_encode_files(data)

        with outputfile:
            yaml.safe_dump(data, stream=outputfile)

import os
from dataclasses import dataclass
import re

@dataclass
class dirTree:
    __slots__ = ['path', 'folders', 'files' ]
    def __init__( self, path : str = None ) -> None:

        self.files = dict()
        self.folders = dict()

        if path is None:
            self.path = os.getcwd()
        else:
            self.path = path

        self.files['all'] = list()
        with os.scandir( self.path ) as it:
            for entry in it:
                if not entry.name.startswith('.'):
                    if entry.is_file():
                        self.files['all'].append(entry.name)
                    elif entry.is_dir():
                        self.folders[ entry.name ] = dirTree( entry.path )
                    else:
                        pass
        
        for f in self.files['all']:
            if re.search('.', f) is None:
                continue
            elif len(f.split('.')) != 2:
                continue
            else:
                file_name, file_extention = f.split('.')
                if file_extention not in self.files:
                    self.files[ file_extention ] = list( [ file_name ] )
                else:
                    self.files[ file_extention ].append( file_name )
        return

def main():
    a = dirTree()
    print( a.files )
    return

if __name__ == '__main__':
    main()



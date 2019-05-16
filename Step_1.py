#
# Написать скрипт, который принимает в качестве аргументов ключи и значения и
# выводит информацию из хранилища (в нашем случае — из файла).
#
# Запись значения по ключу
# > storage.py --key key_name --val value
#
# Получение значения по ключу
# > storage.py --key key_name
#
# Ответом в данном случае будет вывод с помощью print соответствующего значения
# > value
# или
# > value_1, value_2
#
# если значений по этому ключу было записано несколько.
# Метрики сохраняйте в порядке их добавления. Обратите внимание на пробел после запятой.
#

import os
import tempfile
import argparse
import json
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="Take value by key")
parser.add_argument("--val", help="Write value by key")
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def key_loader(args, storage_path):
    def read_write(text=None):
        state = 'w' if text else 'r'
        with open(storage_path, state) as f:
            if not text: return json.loads(f.read())
            else: f.write(json.dumps(text))
    if os.path.exists(storage_path): # Read file if it not empty
        if os.path.getsize(storage_path):
            key_val = read_write()

            if not args.val: # Give value by key
                if args.key in key_val: print(reduce(lambda x, y: x + ", " + y, key_val[args.key]))
                else: print(None)

            else: # Write value by key
                if args.key in key_val:
                    key_val[args.key].append(args.val)
                    read_write(key_val)
                else:
                    key_val[args.key] = [args.val]
                    read_write(key_val)
        else: print(None)
    else: # If file empty or doesn't exists
        if not args.val: print(None)
        else: read_write({args.key : [args.val]})

if not args.key: print('\nInput some args like: "--key key_name --val value"\n')
else: key_loader(args, storage_path)
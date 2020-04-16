import json
from datetime import datetime

def return_args_list(*args, **kwargs):
    args_list = []

    if args and kwargs:
        args_list.append(args)
        args_list.append(kwargs)
    elif args and not kwargs:
        args_list.append(args)
    elif kwargs and not args:
        args_list.append(kwargs)
    return args_list

def save_json(path, log):
    with open(path, 'w', encoding='utf-8') as log_file:
        json.dump(log, log_file, ensure_ascii=False)

def save_log(path):
    def decor_log(funct):
        def new_funct(*args, **kwargs):
           
            log_dict = {
                'data': datetime.now().strftime("data:%Y-%m-%d time:%H.%M.%S"),
                'name': funct.__name__,
                'args_list': return_args_list(*args, **kwargs),
                'return_val': funct(*args, **kwargs)
            }

            save_json(path, log_dict)

        return new_funct
    return decor_log

# @save_log('log_file.json')
#     def my_function(*args, **kwargs):
#         return 4

# def if __name__ == "__main__":
#     my_function(5,6, z=7)
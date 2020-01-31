from contextlib import contextmanager
import datetime
import newsafr_json

# class MyDatetime:
#   def __init__(self, function):
#     self.start_time = datetime.datetime.now()
#     self.function = function
    
#   def __enter__(self):
#      return self.function

#   def __exit__(self, exp_type, exp_val, exp_tb):
#     self.end_time = datetime.datetime.now()
#     self.interval_time = self.end_time - self.start_time  

#     print(f"Время запуска кода: {self.start_time}") 
#     print(f"Время завершения кода: {self.end_time}")
#     print(f"Время работы: {self.interval_time}")

@contextmanager
def my_context_manager(function):
  try:
    start_time = datetime.datetime.now()
    yield function
  finally:
    end_time = datetime.datetime.now()
    interval_time = end_time - start_time  

    print(f"Время запуска кода: {start_time}") 
    print(f"Время завершения кода: {end_time}")
    print(f"Время работы: {interval_time}")    
    
if __name__ == '__main__':
  # with MyDatetime(get_json()) as my_datatime:
  #   my_datatime

  with my_context_manager(newsafr_json.get_json()) as my_datatime:
    my_datatime
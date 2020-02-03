import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(path_text, path_result, text_lang, to_lang):
    params = {
        'key': API_KEY,
        'text': reading_file(path_text),
        'lang': f"{text_lang}-{to_lang}",
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    text_result = ''.join(json_['text'])
    writin_file(path_result, text_result)

def reading_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        return text

def writin_file(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        return f.write(text)

if __name__ == '__main__':
    try:
        translate_it('FR.txt', 'result.txt', 'fr', 'ru')
    except Exception as e:
        print(f"Ошибка! {e}")
    else:   
        print('Перевод успешно завершен')
    
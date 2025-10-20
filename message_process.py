import json

"""Типы тегов сообщений
| Тег                                   | Назначение                               |
| ------------------------------------- | ---------------------------------------- |
| `<b>`                                 | Жирный текст                             |
| `<strong>`                            | Жирный текст                             |
| `<i>`                                 | Курсив                                   |
| `<em>`                                | Курсив                                   |
| `<u>`                                 | Подчеркнутый текст                       |
| `<ins>`                               | Подчеркнутый текст                       |
| `<s>`                                 | Зачеркнутый текст                        |
| `<strike>`                            | Зачеркнутый текст                        |
| `<del>`                               | Зачеркнутый текст                        |
| `<span class="tg-spoiler">`           | Спойлер                                  |
| `<a href="URL">`                      | Гиперссылка                              |
| `<code>`                              | Моноширинный фрагмент текста             |
| `<pre>`                               | Блок кода (однострочный / многострочный) |
| `<pre><code class="language-python">` | Подсветка кода (некоторые клиенты)       |

"""

class InputMessage:
    def __init__(self, file_name="message_input.txt"):
        self.file_name = file_name

    def input_message(self, command, json_path):
        with open(self.file_name, "r", encoding='utf-8') as f:
            message_data = f.read().strip()

        with open(json_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        json_data[command] = message_data
        print(*json_data.items(), sep="\n")
        with open(json_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False)


class MessageProcess:
    def __init__(self, file_path="handlers/messages.json"):
        self.file_path = file_path
        self.messages = self.get_messages()

    def get_messages(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        return json_data

    def get_message(self, command):
        return self.messages[command]

if __name__ == "__main__":
    input_message = InputMessage()
    input_message.input_message("messages_menu", "handlers/messages.json")
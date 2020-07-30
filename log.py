(Press CTRL+C to quit)
___TranslationMiddleware: on_turn
_____should_translate: user_language( en ) != TranslationSettings.default_language.value: False
___MicrosoftTranlator: translate: text_input = hi, language_output = en
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=en
_____json_response: [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': 'hi', 'to': 'en'}]}]
___Multilingual_bot: on_message_activity, turn_context = <botbuilder.core.turn_context.TurnContext object at 0x00000247C3623160>
_____aux_on_send()
___TranslationMiddleware: end  on_turn() 


___TranslationMiddleware: on_turn
_____should_translate: user_language( en ) != TranslationSettings.default_language.value: False
___MicrosoftTranlator: translate: text_input = list, language_output = en
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=en
_____json_response: [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': 'list', 'to': 'en'}]}]
___Multilingual_bot: on_message_activity, turn_context = <botbuilder.core.turn_context.TurnContext object at 0x00000247C3623A00>
_____aux_on_send()
___TranslationMiddleware: end  on_turn()


___TranslationMiddleware: on_turn
_____should_translate: user_language( en ) != TranslationSettings.default_language.value: False
___MicrosoftTranlator: translate: text_input = ja, language_output = en
___Multilingual_bot: on_message_activity, turn_context = <botbuilder.core.turn_context.TurnContext object at 0x00000247C35FBBE0>
nihongko_japanese:  ja
current_language:  ja
current_languate is nihongko_japanese lang:  ja
_____aux_on_send()
___MicrosoftTranlator: translate: text_input = Your current language code is: ja, type to translate., language_output = ja
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=ja
_____json_response: [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': 'あなたの現在の言語コードは次のとおりです: ja,翻訳するタイプ。', 'to': 'ja'}]}]
___TranslationMiddleware: end  on_turn()


___TranslationMiddleware: on_turn
_____should_translate: user_language( ja ) != TranslationSettings.default_language.value: True      
___MicrosoftTranlator: translate: text_input = hi, language_output = en
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=en
_____json_response: [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': 'hi', 'to': 'en'}]}]
___TranslationMiddleware: context.actitiy.text =  hi
___Multilingual_bot: on_message_activity, turn_context = <botbuilder.core.turn_context.TurnContext object at 0x00000247C366CB20>
_____aux_on_send()
___MicrosoftTranlator: translate: text_input = hi, language_output = ja
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=ja
_____json_response: [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': 'こんにちは', 'to': 'ja'}]}]
___TranslationMiddleware: end  on_turn() 


___TranslationMiddleware: on_turn
_____should_translate: user_language( ja ) != TranslationSettings.default_language.value: True      
___MicrosoftTranlator: translate: text_input = list, language_output = en
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=en
_____json_response: [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': 'list', 'to': 'en'}]}]
___TranslationMiddleware: context.actitiy.text =  list
___Multilingual_bot: on_message_activity, turn_context = <botbuilder.core.turn_context.TurnContext object at 0x00000247C35FB940>
_____aux_on_send()
___MicrosoftTranlator: translate: text_input = Choose your language:, language_output = ja
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=ja
_____json_response: [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': '言語を選択:', 'to': 'ja'}]}]
___TranslationMiddleware: end  on_turn() 


___TranslationMiddleware: on_turn
_____should_translate: user_language( ja ) != TranslationSettings.default_language.value: True
___MicrosoftTranlator: translate: text_input = zh-hant, language_output = en
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=en
_____json_response: [{'detectedLanguage': {'language': 'de', 'score': 1.0}, 'translations': [{'text': 'zh-hant', 'to': 'en'}]}]
___TranslationMiddleware: context.actitiy.text =  zh-hant
___Multilingual_bot: on_message_activity, turn_context = <botbuilder.core.turn_context.TurnContext object at 0x00000247C36239A0>
nihongko_japanese:  ja
current_language:  zh-hant
current_languate is chinese_t
lang:  zh-hant
_____aux_on_send()
___MicrosoftTranlator: translate: text_input = Your current language code is: zh-hant, type to translate., language_output = zh-hant
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=zh-hant
_____json_response: [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': '您目前的語言代碼是: zh -hant, 鍵入要翻譯。', 'to': 'zh-Hant'}]}]
___TranslationMiddleware: end  on_turn() 


___TranslationMiddleware: on_turn
_____should_translate: user_language( zh-hant ) != TranslationSettings.default_language.value: True
___MicrosoftTranlator: translate: text_input = こんにちは, language_output = en
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=en
_____json_response: [{'detectedLanguage': {'language': 'ja', 'score': 1.0}, 'translations': [{'text': 'Hello', 'to': 'en'}]}]
___TranslationMiddleware: context.actitiy.text =  Hello
___Multilingual_bot: on_message_activity, turn_context = <botbuilder.core.turn_context.TurnContext object at 0x00000247C36668B0>
_____aux_on_send()
___MicrosoftTranlator: translate: text_input = Hello, language_output = zh-hant
_____send request to:  https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=zh-hant
_____json_response: [{'detectedLanguage': {'language': 'en', 'score': 1.0}, 'translations': [{'text': '你好。', 'to': 'zh-Hant'}]}]
___TranslationMiddleware: end  on_turn() 
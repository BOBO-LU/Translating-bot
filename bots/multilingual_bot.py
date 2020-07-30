# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import json
import os

from botbuilder.core import (
    ActivityHandler,
    TurnContext,
    UserState,
    CardFactory,
    MessageFactory,
)
from botbuilder.schema import (
    ChannelAccount,
    Attachment,
    SuggestedActions,
    CardAction,
    ActionTypes,
)

from translation.translation_settings import TranslationSettings


class MultiLingualBot(ActivityHandler):
    """
    This bot demonstrates how to use Microsoft Translator.
    More information can be found at:
    https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-info-overview"
    """

    def __init__(self, user_state: UserState):
        print(f"MultiLingualBot: __init__ActivityHandler = {ActivityHandler}")
        if user_state is None:
            raise TypeError(
                "[MultiLingualBot]: Missing parameter. user_state is required but None was given"
            )

        self.user_state = user_state

        self.language_preference_accessor = self.user_state.create_property(
            "LanguagePreference"
        )

    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        # Greet anyone that was not the target (recipient) of this message.
        # To learn more about Adaptive Cards, see https://aka.ms/msbot-adaptivecards for more details.
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    MessageFactory.attachment(self._create_adaptive_card_attachment())
                )
                await turn_context.send_activity(
                    "This bot will introduce you to translation middleware. Say 'list' to get started."
                )

    async def on_message_activity(self, turn_context: TurnContext):
        print(f"___Multilingual_bot: on_message_activity, turn_context = {turn_context}")
        if self._is_language_change_requested(turn_context.activity.text):
            # If the user requested a language change through the suggested actions with values "es" or "en",
            # simply change the user's language preference in the user state.
            # The translation middleware will catch this setting and translate both ways to the user's
            # selected language.
            # If Spanish was selected by the user, the reply below will actually be shown in Spanish to the user.
            current_language = turn_context.activity.text.lower()
            if current_language in (
                    TranslationSettings.english_english.value, TranslationSettings.spanish_english.value
            ):
                print('_____current_languate is english')
                lang = TranslationSettings.english_english.value

            elif current_language == TranslationSettings.chinese_t.value:
                print('_____current_languate is chinese_t')
                lang = TranslationSettings.chinese_t.value

            elif current_language == TranslationSettings.nihongko_japanese.value:
                print('_____current_languate is nihongko_japanese ' , end="")
                lang = TranslationSettings.nihongko_japanese.value
                

            else:
                lang = TranslationSettings.english_spanish.value

            print("_____TranslationSettings.english_spanish.value :", lang)
            await self.language_preference_accessor.set(turn_context, lang)

            await turn_context.send_activity(f"Your current language code is: {lang}, type to translate.")

            # Save the user profile updates into the user state.
            await self.user_state.save_changes(turn_context)

        elif turn_context.activity.text.lower() in ( "list", "language", "l", "language.", "languages"):
         # Show the user the possible options for language. If the user chooses a different language
            # than the default, then the translation middleware will pick it up from the user state and
            # translate messages both ways, i.e. user to bot and bot to user.
            reply = MessageFactory.text("Choose your language:")
            reply.suggested_actions = SuggestedActions(
                actions=[
                    CardAction(
                        title="Español",
                        type=ActionTypes.post_back,
                        value=TranslationSettings.english_spanish.value,
                    ),
                    CardAction(
                        title="English",
                        type=ActionTypes.post_back,
                        value=TranslationSettings.english_english.value,
                    ),
                    CardAction(
                        title="繁體中文",
                        type=ActionTypes.post_back,
                        value=TranslationSettings.chinese_t.value,
                    ),
                    CardAction(
                        title="日本語",
                        type=ActionTypes.post_back,
                        # value=TranslationSettings.nihongko_japanese.value,
                        value = "ja"
                    ),
                ]
            )
            await turn_context.send_activity(reply)
        else:
            #Get the text send by user. While return it to user, the on_turn() function 
            # will activate the translator to translate the text.
            reply = turn_context.activity.text
            await turn_context.send_activity(reply)
           
        print(f"___Multilingual_bot: end     on_message_activity, turn_context = {turn_context}")
    def _create_adaptive_card_attachment(self) -> Attachment:
        print(f"___multilingual_bot: _create_adaptive_card_attachment , self = {self}")
        """
        Load attachment from file.
        :return:
        """
        card_path = os.path.join(os.getcwd(), "cards/welcomeCard.json")
        with open(card_path, "rt") as in_file:
            card_data = json.load(in_file)

        return CardFactory.adaptive_card(card_data)

    def _is_language_change_requested(self, utterance: str) -> bool:

        if not utterance:
            return False

        utterance = utterance.lower()
        

        return utterance in (
            TranslationSettings.english_spanish.value,
            TranslationSettings.english_english.value,
            TranslationSettings.spanish_spanish.value,
            TranslationSettings.spanish_english.value,
            TranslationSettings.nihongko_japanese.value,
            TranslationSettings.chinese_t.value,
            "ja"
        )

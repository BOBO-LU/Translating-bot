# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import Callable, Awaitable, List

from botbuilder.core import Middleware, UserState, TurnContext
from botbuilder.schema import Activity, ActivityTypes

from translation import MicrosoftTranslator
from translation.translation_settings import TranslationSettings


class TranslationMiddleware(Middleware):
    """
    Middleware for translating text between the user and bot.
    Uses the Microsoft Translator Text API.
    """
    user_text_message = "" #save the user's text in english every turn
    def __init__(self, translator: MicrosoftTranslator, user_state: UserState):
        print(f'___TranslationMiddleware: __init__')
        self.translator = translator
        self.language_preference_accessor = user_state.create_property(
            "LanguagePreference"
        )

    async def on_turn(
        self, context: TurnContext, logic: Callable[[TurnContext], Awaitable]
    ):
        """
        Processes an incoming activity.
        :param context:
        :param logic:
        :return:
        """
        print(f'___TranslationMiddleware: on_turn')
        translate = await self._should_translate(context)
        print(f'___TranslationMiddleware: context = {context}')
        
        # 如果要使用者語言不是英文，而且訊息類別是message，則送到翻譯器當中，把句子中的文字替換成預設語言
        if translate and context.activity.type == ActivityTypes.message:
            # context.activity.text = await self.translator.translate(
            #     context.activity.text, TranslationSettings.default_language.value
            # )
            user_text_message = await self.translator.translate(
                context.activity.text, TranslationSettings.default_language.value
            )
            print(f"___TranslationMiddleware: context.activity.type = {context.activity.type}, context.actitiy.text = {context.activity.text}")
        else :
            context.activity.text = await self.translator.translate(
                context.activity.text, TranslationSettings.default_language.value
            )
            print(f"___TranslationMiddleware:  ## DO NOTHING ##  context.activity.type = {context.activity.type}, context.actitiy.text = {context.activity.text}")
            
            # this function will be execute when send_activity happens
        async def aux_on_send(
            ctx: TurnContext, activities: List[Activity], next_send: Callable
        ):
            print(f'_____aux_on_send()')
            user_language = await self.language_preference_accessor.get(
                ctx, TranslationSettings.default_language.value
            )
            should_translate = (
                user_language != TranslationSettings.default_language.value
            )

            # Translate messages sent to the user to user language
            if should_translate:
                for activity in activities:
                    await self._translate_message_activity(activity, user_language)

            return await next_send()
        
        
        async def aux_on_update(
            ctx: aux_on_send, activity: Activity, next_update: Callable
        ):
            print(f'_____aux_on_update()')
            user_language = await self.language_preference_accessor.get(
                ctx, TranslationSettings.default_language.value
            )
            should_translate = (
                user_language != TranslationSettings.default_language.value
            )

            # Translate messages sent to the user to user language
            if should_translate and activity.type == ActivityTypes.message:
                await self._translate_message_activity(activity, user_language)

            return await next_update()

        context.on_send_activities(aux_on_send)
        context.on_update_activity(aux_on_update)
        
        await logic()
        print(f"___TranslationMiddleware: end  on_turn() \n ")
    async def _should_translate(self, turn_context: TurnContext) -> bool:
        user_language = await self.language_preference_accessor.get(
            turn_context, TranslationSettings.default_language.value)
        
        print(f'_____should_translate: user_language( {user_language} ) != TranslationSettings.default_language.value: {user_language != TranslationSettings.default_language.value}')
        
        # return False
        return user_language != TranslationSettings.default_language.value

    async def _translate_message_activity(self, activity: Activity, target_locale: str):
        if activity.type == ActivityTypes.message:
            activity.text = await self.translator.translate(
                activity.text, target_locale
            )

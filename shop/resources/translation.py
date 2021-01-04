from modeltranslation.translator import register, TranslationOptions

from .models import AboutUs, Contact, Rule, Terms


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'what_we_do', 'our_team')
    required_languages = ('en', 'hy')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address',)
    required_languages = ('en', 'hy')


@register(Rule)
class RuleTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('en', 'hy')


@register(Terms)
class RuleTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('en', 'hy')

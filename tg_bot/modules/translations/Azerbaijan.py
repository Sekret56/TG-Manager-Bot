RUN_STRINGS = (
"Sən hara getdiyini düşünürsən?",
    "Hə? Nə? Qaçdılar?",
    "ZZzzZZzz ... Hə? Nə? Oh, sadəcə yenə onlar, heç vaxt unutma.",
    "Buraya qayıt!",
    "O qədər də sürətli deyil...",
    "Divara baxın!",
    "Məni onlarla tək qoyma !!",
    "Sən qaçırsan, ölürsən.",
    "Səni zarafatcıl, mən hər yerdəyəm",
    "Buna görə peşman olacaqsan ...",
    "Siz də /kickme cəhd edə bilərsiniz, eşitdiyimə görə əyləncəlidir.",
    "Get başqasını narahat et, burada heç kimin vecinə deyil.",
    "Qaça bilərsən, amma gizlənə bilməzsən.",
    "Sən bütün bunlarmı?",
    "Sənin arxandayam ...",
    "Şirkətiniz var!",
    "Bunu asanlıqla və ya çətin bir şəkildə edə bilərik.",
    "Sən sadəcə anlamırsan, elə deyilmi?",
    "Bəli, qaçsan yaxşıdır!",
    "Xahiş edirəm, mənə nə qədər əhəmiyyət verdiyini xatırlat?",
    "Sən olsaydın daha sürətli qaçardım.",
    "Bu mütləq axtardığımız insandır.",
    "Oralar həmişə sizin xeyrinizə olsun.",
    "Məşhur son sözlər.",
    "Və onlar bir daha görünməyəcək qədər sonsuza qədər yox oldular.",
    "\" Mənə bax! Çox sərinəm, botdan qaça bilərəm! \ "- bu adam",
    "Bəli, bəli, get."
    "Budur, bu üzüyü götürün və başınızı qurtaran kimi Mordora aparın."
    "Əfsanə var, hələ də qaçırlar ...",
    "Harry Potter'dan fərqli olaraq, valideynləriniz sizi məndən qoruya bilməzlər.",
    "Qorxu qəzəbə səbəb olur. Qəzəb nifrətə səbəb olur. Nifrət əzab-əziyyətə səbəb olur. Qorxub qaçmağa davam etsəniz, ola bilər"
    "növbəti Vader olun.",
    "Daha sonra birdən çox hesablama apardığımda, sənin şenaniganlarınıza olan marağımın tam olaraq 0 olduğuna qərar verdim."
    "Əfsanə var, hələ də çalışırlar.",
    "Onu davam etdirin, onsuz da sizi burda istədiyimizə əmin deyilik.",
    "Sən bir wizasan - Oh. Gözlə. Harry deyilsən, hərəkətə davam et.",
    "HALLWAYS'DA YOXDUR!",
    "Əlvida, dostum.",
    "Köpəkləri kim buraxdı?",
    "Gülməli, çünki heç kimin vecinə deyil.",
    "Məndən xoşun gəldi.)",
    "Açığı, əzizim, mən heç bir əmr vermirəm.",
    "Mənim süd kokteylimi oğlanları həyətə gətirir ... Buna görə daha sürətli qaç!Səni görməsinlər)",
    "Həqiqəti idarə edə bilməzsən!",
    "Çoxdan əvvəl, uzaq bir qalaktikada ... Biri bununla maraqlanardı. Artıq deyil.",
    "Hey, onlara bax! Qaçılmaz banhammerdən qaçırlar ... Şirin.",
    "Əvvəlcə Han vurdu. Mən də edəcəm.",
    "Nə arxasınca qaçırsan, ağ dovşan?",
    "Doktorun dediyi kimi ... qaç!",
)

SLAP_TEMPLATES = (
    "{user1} {hit} {user2} ilə {item}.",
    "{user1} {hit} {user2} bir {item} ilə üzə.",
    "{user1} {hit} {user2} bir {element} ilə bir az.",
    "{user1} {user2} ünvanına bir {item} atır}.",
    "{user1} bir {item} götürür və {user2} - nin üzünə atır.",
    "{user1} {user2} -nin ümumi istiqamətində bir {item} işə salır.",
    "{user1} bir {item} ilə {user2} şillə vurmağa başlayır.",
    "{user1} sancaqlar {user2} aşağı və ardıcıl bir {item} ilə onları vurur.",
    "{user1} onunla bir {item} və {hits} {user2} tutur.",
    "{user1} {user2} kresloya bağlayır və onlara {item} atır.",
    "{user1}, {user2} lavada üzməyi öyrənməyə kömək etmək üçün bir təkan verdi."
)

ITEMS = (
    "dəmir skelet",
    "böyük alabalıq",
    "beysbol sopası",
    "yarasa",
    "taxta qamış",
    "dırnaq",
    "Printer",
    "kürək",
    "CRT monitor",
    "fizika kitabı",
    "toster",
    "Mona Lisa portreti",
    "televiziya",
    "beş tonluq yük maşını",
    "yapışqan lent",
    "kitab",
    "noutbuk",
    "köhnə televiziya",
    "qayalar kisəsi",
    "İsti çay",
    "rezin toyuq",
    "tırmanılmış yarasa",
    "yanğın Söndürən",
    "ağır qaya",
    "kir yığını",
    "arı pətəyi",
    "çürümüş ət parçası",
    "ayı",
    "ton kərpic",
)

THROW = (
    "atır",
     "çırpınmaq",
     "patronlar",
     "tullayır",
)

HIT = (
    "vurdu",
    "döydü",
    "şillələr",
    "tulladı",
    "Bağladı",
)

MARKDOWN_HELP = """
Markdown is a very powerful formatting tool supported by telegram. {} has some enhancements, to make sure that \
saved messages are correctly parsed, and to allow you to create buttons.

- <code>_italic_</code>: wrapping text with '_' will produce italic text
- <code>*bold*</code>: wrapping text with '*' will produce bold text
- <code>`code`</code>: wrapping text with '`' will produce monospaced text, also known as 'code'
- <code>[sometext](someURL)</code>: this will create a link - the message will just show <code>sometext</code>, \
and tapping on it will open the page at <code>someURL</code>.
EG: <code>[test](example.com)</code>

- <code>[buttontext](buttonurl:someURL)</code>: this is a special enhancement to allow users to have telegram \
buttons in their markdown. <code>buttontext</code> will be what is displayed on the button, and <code>someurl</code> \
will be the url which is opened.
EG: <code>[This is a button](buttonurl:example.com)</code>

If you want multiple buttons on the same line, use :same, as such:
<code>[one](buttonurl://example.com)
[two](buttonurl://google.com:same)</code>
This will create two buttons on a single line, instead of one button per line.
"""

EnglishStrings = {
    "kömək": """*Funksiyalarımız*:
 - /start: Botu başladın
 - /help və ya /help <funksiya adı>: start edəndən sonra.
 - /lang: Dil dəyişin
 - /settings:
 - PM-də: dəstəklənən bütün modullar üçün ayarlarınızı sizə göndərir.
    - qrupda: bütün söhbət parametrləri ilə sizi pm-ə yönləndirəcəkdir.
   {}
   """,

    "send-group-settings": """Hi there! There are quite a few settings for *{}* - go ahead and pick what
you're interested in.""",

#Misc
"RUNS-K": RUN_STRINGS,
"SLAP_TEMPLATES-K": SLAP_TEMPLATES,
"ITEMS-K": ITEMS,
"HIT-K": HIT,
"THROW-K": THROW,
"ITEMP-K": ITEMS,
"ITEMR-K": ITEMS,
"MARKDOWN_HELP-K": MARKDOWN_HELP,

#GDPR
"send-gdpr": """Your personal data has been deleted.\n\nNote that this will not unban \
you from any chats, as that is telegram data, not YanaBot data.
Flooding, warns, and gbans are also preserved, as of \
[this](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
which clearly states that the right to erasure does not apply \
\"for the performance of a task carried out in the public interest\", as is \
the case for the aforementioned pieces of data."""

}

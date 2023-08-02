import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot token
TOKEN = '6525819301:AAGHGytQkV3fh7HztiqpUJzZEvfnHMTKfLM'

# Create a TeleBot instance
bot = telebot.TeleBot(TOKEN)

# Function to handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    # Add your specific start message in Arabic here
    start_message_arabic = """أهلاً بك في بوت ArabiCoupon! أكتب اسم المتجر المراد بالعربية مثل نون، كارفور، امريكان ايجل.
تقدر تنسخ الكود من خلال الضغط على الكود نفسه مثال:
الكود: ArabiCoupon
لو مبتحبش الاشعارات تقدر تقفلها من اعدادات البوت."""
    bot.reply_to(message, start_message_arabic)

# Function to handle user messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text.lower()

 # Custom responses based on user input
    if user_input == 'Noon':
        response_hello = """الكود: TEA
الكود: RXF1
العرض: كاش باك للمستخدمين الجدد 10% كحد أقصى 50 ريال و للقديمين 5% كحد أقصى 10 ريال كل كود صالح للاستعمال 3 مرات
الدول:🇸🇦 🇦🇪 🇪🇬
الموقع: ... (أدخل الموقع الخاص بالمتجر)"""
        bot.reply_to(message, response_hello)
    elif user_input == 'نون':
        bot.reply_to(message, """الكود: TEA
الكود: RXF1
العرض: كاش باك للمستخدمين الجدد 10% كحد أقصى 50 ريال و للقديمين 5% كحد أقصى 10 ريال كل كود صالح للاستعمال 3 مرات
الدول:🇸🇦 🇦🇪 🇪🇬
الموقع: ... (noon.com)""")
    elif user_input == 'نمشي':
        bot.reply_to(message, """الكود: test2
الكود: test3
العرض: كاش باك للمستخدمين الجدد 10% كحد أقصى 50 ريال و للقديمين 5% كحد أقصى 10 ريال كل كود صالح للاستعمال 3 مرات
الدول:🇸🇦 🇦🇪 🇪🇬
الموقع: ... (ar-global.namshi.com)""")
    elif user_input == 'سيفى':
        bot.reply_to(message, """الكود: test4
الكود: test5
العرض: كاش باك للمستخدمين الجدد 10% كحد أقصى 50 ريال و للقديمين 5% كحد أقصى 10 ريال كل كود صالح للاستعمال 3 مرات
الدول:🇸🇦 🇦🇪 🇪🇬
الموقع: ... (sivvi.com)""")
    elif user_input == 'ممزورلد':
        bot.reply_to(message, """الكود: test60
الكود: test7
العرض: كاش باك للمستخدمين الجدد 10% كحد أقصى 50 ريال و للقديمين 5% كحد أقصى 10 ريال كل كود صالح للاستعمال 3 مرات
الدول:🇸🇦 🇦🇪 🇪🇬
الموقع: ... (mumzworld.com)""")
    elif user_input == 'امازون':
        bot.reply_to(message, """الكود: test8
الكود: test9
العرض: كاش باك للمستخدمين الجدد 10% كحد أقصى 50 ريال و للقديمين 5% كحد أقصى 10 ريال كل كود صالح للاستعمال 3 مرات
الدول:🇸🇦 🇦🇪 🇪🇬
الموقع: ... (amazon.com)""")
    elif user_input == 'كارفور':
        bot.reply_to(message, """الكود: test10
الكود: test11
العرض: كاش باك للمستخدمين الجدد 10% كحد أقصى 50 ريال و للقديمين 5% كحد أقصى 10 ريال كل كود صالح للاستعمال 3 مرات
الدول:🇸🇦 🇦🇪 🇪🇬
الموقع: ... (carrefour.com)""")
    elif user_input == 'امريكان ايجل':
        bot.reply_to(message, """الكود: test12
الكود: test13
العرض: كاش باك للمستخدمين الجدد 10% كحد أقصى 50 ريال و للقديمين 5% كحد أقصى 10 ريال كل كود صالح للاستعمال 3 مرات
الدول:🇸🇦 🇦🇪 🇪🇬
الموقع: ... (americaneagle.com)""")
    elif user_input == 'help':
        bot.reply_to(message, "اتأكد انك بتكتب اسم الموقع بالعربى، عندك اوبشانات كتير زى نون، نمشي، سيفى، ممزورلد، امازون، كارفور، امريكان ايجل")
    else:
        bot.reply_to(message, "أنا مش فاهم، حاول تكتب Help")

# Main function
def main():
    bot.polling()

if __name__ == '__main__':
    main()

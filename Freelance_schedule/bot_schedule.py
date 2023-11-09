from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from credits_token import bot_token
 
bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher
 
def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Это бот для расписания! Ничего не забывай!")
 
def help(update,context):
    context.bot.send_message(update.effective_chat.id, "Лишь попроси бота, и он поможет тебе с расписанием и некоторыми предметами")
    
def get_day(update, context):
    keyboard = [[InlineKeyboardButton("Monday", callback_data='1'),InlineKeyboardButton("Tuesday", callback_data='2'),InlineKeyboardButton("Wednsday", callback_data='3'), InlineKeyboardButton("Thursday", callback_data='4')],
                [InlineKeyboardButton("Friday", callback_data='5'), InlineKeyboardButton("saturday", callback_data='6')],
                [InlineKeyboardButton("sunday", callback_data='7')]]
    update.message.reply_text('Выбери день недели', reply_markup=InlineKeyboardMarkup(keyboard))
    
#функция для открытия файла
def get_data_from_file(day):
    f = open(day, "r", encoding = "utf-8")
    data = f.read()
    f.close()
    return data
def comm(update, context):
    context.bot.send_message(update.effective_chat.id, "Commands:/start,/help,/getday")
def button(update, context):
    query = update.callback_query
    query.answer()
    if query.data == "1":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("mon.txt"))
    elif query.data == "2":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("tue.txt"))
    elif query.data == "3":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("wed.txt"))
    elif query.data == "4":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("thu.txt"))
    elif query.data == "5":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("fri.txt"))
    elif query.data == "6":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("sat.txt"))
    elif query.data == "7":
        context.bot.send_message(update.effective_chat.id, get_data_from_file("sun.txt"))
    
def unknown(update, context):
    context.bot.send_message(update.effective_chat.id,"something wrong,check your command")
 
start_handler = CommandHandler('start', start)
help_handler = CommandHandler("help", help)
get_day_handler = CommandHandler('getday', get_day)
button_handler = CallbackQueryHandler(button)
comm_handler = CommandHandler("commands", comm)
unknown_handler = MessageHandler(Filters.text, unknown)

dispatcher.add_handler(button_handler)
dispatcher.add_handler(get_day_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(comm_handler)
dispatcher.add_handler(unknown_handler)
updater.start_polling()
updater.idle()
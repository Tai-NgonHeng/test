from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6329953520:AAGK1I2-runche60hz_QXcv61QHTgM4korg'
BOT_USERNAME: Final = '@InnovationAndconstructor_bot'

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Do you need some help?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a fixer! Please type about your problem so I can fix?')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command u can type anything you want')

async def fix_command(update: Update, wantcontext: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('what are you want to fix about?')

async def remake_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('what are you want to remake?')

async def repair_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('what are you want to repair?')

#Handle responses

def handle_responses(text: str) -> str:
    # processed: str = text.upper()
    if 'Hello' in text:
        return 'you are welcome!'
    if 'I have a problem.' in text:
        return 'what is your problem?'
    if 'My house' in text:
        return 'Your kitchen?'
    if 'can I have your phone number?' in text:
        return 'Yes I can tell you when u text mess words.'
    if 'What is your company name?' in text:
        return 'D PLUS'
    if 'who is your CEO?' in text:
        return 'Sir MAI VANTHA'
    if 'where is his address?' in text:
        return ' st 1988'
    if 'what is his gender?' in text:
        return 'Male'
    
    return 'contact us by: +855 89 295 599'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text:str = text.replace(BOT_USERNAME, '').strip()
            responses: str = handle_responses(new_text)
        else:
            return
    else:
        responses: str = handle_responses(text)

    print('Bot', responses)
    await update.message.reply_text(responses)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



if __name__== '__main__':
    print('starting bot...')
    app = Application.builder().token(TOKEN).build()

    #comands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('fix', fix_command))
    app.add_handler(CommandHandler('remake', remake_command))
    app.add_handler(CommandHandler('repair', repair_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(error)

    #polls the bot
    print('polling...')
    print('You Can Go To Telegram And Pick The Menu You Need.Thanks')
    app.run_polling(poll_interval=3)
    


















    
    

    
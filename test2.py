def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome to the Calories Counter Bot! Please enter the food you ate to get the calorie count.")

from handlers.vars_for_handlers.vars import get_temp_category
from utils.parser.web_requests import PictureGeter
from loader import bot

class ParserManager:
    @staticmethod
    async def process_settings_for_parser(count_in_message):
        try:
            count = int(count_in_message)
            return count
        except ValueError:
            return "Цифру пожалуйста )"

    @staticmethod
    async def run_parser(count: int):
        result = PictureGeter.get_list_with_urls_on_pictures(category=await get_temp_category(), count_of_pictures=int(count))
        return result
    
    
    async def get_returned_data(self, message):
        user_input = await self.process_settings_for_parser(message.text)
        input_type = type(user_input)
        if input_type is int:
            return await self.run_parser(message.text), message.chat.id
        elif input_type is str:
            return user_input, message.chat.id
         
    async def send_parsed_pictures(self, parsed_pictures: list, id: int):
        for url_link in parsed_pictures:
            try:
                await bot.send_photo(chat_id=id, photo=url_link)
            except:
                pass
    
    async def try_two_scenarios_block(self, data: list):
        if type(data[0]) is list:
            await self.send_parsed_pictures(data[0], data[1])
        elif type(data[0]) is str:
            await bot.send_message(text=data[0], chat_id=data[1])
            
            

from .logger import logger


async def process_updater_data(updater_data: list[dict]) -> int:
    last_update_id = -1
    for update in updater_data:
        last_update_id = update['update_id']
        logger.info(f'Process update #{last_update_id}')
        if update.get('message', None):
            logger.info('... Detect new message')
            ...
        if update.get('edited_message', None):
            logger.info('... Detect new version of message')
            ...

    return last_update_id

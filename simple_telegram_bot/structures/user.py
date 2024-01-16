from typing import Optional


class User:
    """This object represents a Telegram user or bot."""

    def __init__(
            self,
            id: int | str,
            is_bot: bool,
            first_name: str,
            last_name: Optional[str] = '',
            username: Optional[str] = '',
            language_code: Optional[str] = '',
            is_premium: Optional[bool] = False,
            added_to_attachment_menu: Optional[bool] = False,
            can_join_groups: Optional[bool] = False,
            can_read_all_group_messages: Optional[bool] = False,
            supports_inline_queries: Optional[bool] = False,
    ):
        self.id = id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
        self.is_premium = is_premium
        self.added_to_attachment_menu = added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.supports_inline_queries = supports_inline_queries


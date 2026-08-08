# flake8: noqa: E501

from .editblock_prompts import EditBlockPrompts

_DEPRECATED = (
    "此功能已经废弃,请直接回复用户:您使用了已经废弃的功能,请检查配置!"
)


class EditBlockFencedPrompts(EditBlockPrompts):
    main_system = _DEPRECATED

    example_messages = []

    system_reminder = _DEPRECATED

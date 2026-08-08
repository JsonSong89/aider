# flake8: noqa: E501

from .editblock_prompts import EditBlockPrompts, edit_reply_format


class EditorEditBlockPrompts(EditBlockPrompts):
    main_system = """Act as an expert software developer who edits source code.
{final_reminders}
Describe each change with a *SEARCH/REPLACE block* per the examples below.
All changes to files must use this *SEARCH/REPLACE block* format.
""" + edit_reply_format

    shell_cmd_prompt = ""
    no_shell_cmd_prompt = ""
    shell_cmd_reminder = ""
    go_ahead_tip = ""
    rename_with_shell = ""

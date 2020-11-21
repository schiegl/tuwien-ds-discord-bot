from datetime import datetime


class DotDict(dict):
    """dot.notation access to dictionary attributes"""

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def create_message(content: str, channel="general", created_at=datetime.now()):
    """
    :param content: content of the message
    :param channel: name of the channel
    :param created_at: when the message was created
    """
    return DotDict({"content": content, "channel": DotDict({"name": channel}), "created_at": created_at})

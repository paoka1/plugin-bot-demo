class Plugin:
    handle: object
    match: list
    property: int
    block: bool

    def __init__(self, handle, match, priority, block):
        self.handle = handle
        self.match = match
        self.priority = priority
        self.block = block


class Plugins:
    plugins: list

    def __init__(self):
        self.plugins = []

    def register(self, plugin: Plugin):
        self.plugins.append(plugin)

    def is_match(self, msg, match):
        pass

    def get_match(self, msg):
        for plugin in self.plugins:
            for match in plugin.match:
                if self.is_match(msg, match):
                    yield plugin

    def sort(self):
        self.plugins.sort(key=lambda x: x.priority)

    def get_num(self):
        return len(self.plugins)


class KwPlugins(Plugins):

    def __init__(self):
        super(KwPlugins, self).__init__()
        self.name = "OnKeyWordPlugins"

    def is_match(self, msg, match):
        if match in msg:
            return True
        return False


class FmPlugins(Plugins):

    def __init__(self):
        super(FmPlugins, self).__init__()
        self.name = "OnFullMatchPlugins"

    def is_match(self, msg, match):
        if msg == match:
            return True
        return False


class SwPlugins(Plugins):

    def __init__(self):
        super(SwPlugins, self).__init__()
        self.name = "OnStartWithPlugins"

    def is_match(self, msg, match):
        if msg.startswith(match):
            return True
        return False


class EwPlugins(Plugins):

    def __init__(self):
        super(EwPlugins, self).__init__()
        self.name = "OnEndWithPlugins"

    def is_match(self, msg, match):
        if msg.endswith(match):
            return True
        return False


kw_plugins = KwPlugins()
fm_plugins = FmPlugins()
sw_plugins = SwPlugins()
ew_plugins = EwPlugins()
plugins = [kw_plugins, fm_plugins, sw_plugins, ew_plugins]


def on_keyword(match: list, priority: int, block=False):
    def decorator(func):
        kw_plugins.register(Plugin(func, match, priority, block))
        return func
    return decorator


def full_match(match: list, priority: int, block=False):
    def decorator(func):
        fm_plugins.register(Plugin(func, match, priority, block))
        return func
    return decorator


def start_with(match: list, priority: int, block=False):
    def decorator(func):
        sw_plugins.register(Plugin(func, match, priority, block))
        return func
    return decorator


def end_with(match: list, priority: int, block=False):
    def decorator(func):
        ew_plugins.register(Plugin(func, match, priority, block))
        return func
    return decorator

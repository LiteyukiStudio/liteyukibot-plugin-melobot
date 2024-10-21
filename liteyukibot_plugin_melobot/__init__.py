from croterline.process import get_ctx
from liteyuki.plugin import PluginMetadata, PluginType
from liteyuki.core import sub_process_manager

from melobot import Bot

__plugin_meta__ = PluginMetadata(
    name="Melobot3",
    type=PluginType.APPLICATION,
)


def run_melobot():
    ctx = get_ctx()
    Bot("liteyuki-plugin").run()


sub_process_manager.add(func=run_melobot, name="melobot")

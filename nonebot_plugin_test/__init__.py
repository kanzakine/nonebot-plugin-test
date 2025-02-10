from nonebot.plugin import PluginMetadata
from .config import Config
from nonebot import on_command

__plugin_meta__ = PluginMetadata(
    name="test",
    description="测试用",
    usage="test",
    type="application",
    homepage="https://github.com/kanzakine/nonebot-plugin-test",
    config=Config,
    supported_adapters={"~onebot.v11", "~telegram"},
)

weather = on_keyword("test")
@weather.handle()
async def handle_function():
    await weather.finish("message")
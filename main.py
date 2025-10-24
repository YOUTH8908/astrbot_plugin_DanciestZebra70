from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import json

@register("websocket_subscribe", "author", "订阅 WebSocket 消息推送", "1.0.0", "repo url")
class WSSubscribePlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("订阅")
    async def subscribe(self, event: AstrMessageEvent):
        '''在当前群聊中订阅 WebSocket 消息推送。用法：/订阅'''
        if not event.is_group():
            yield event.plain_result("❌ 请在群聊中使用此命令。")
            return

        group_id = event.get_group_id()
        if not group_id:
            yield event.plain_result("⚠️ 无法获取群 ID，订阅失败。")
            return

        # 从存储中加载已订阅群组
        raw = self.context.storage.get("subscribed_groups", "[]")
        try:
            subscribed_groups = set(json.loads(raw))
        except:
            subscribed_groups = set()

        if group_id in subscribed_groups:
            yield event.plain_result("✅ 本群已订阅 WebSocket 消息推送。")
        else:
            subscribed_groups.add(group_id)
            self.context.storage.set("subscribed_groups", json.dumps(list(subscribed_groups)))
            logger.info(f"群 {group_id} 已订阅 WebSocket 推送")
            yield event.plain_result("✅ 订阅成功！本群将接收来自 ws://38.55.205.62:6678/ 的消息。")

    @filter.command("取消订阅")
    async def unsubscribe(self, event: AstrMessageEvent):
        '''取消本群的 WebSocket 消息订阅。用法：/取消订阅'''
        if not event.is_group():
            yield event.plain_result("❌ 请在群聊中使用此命令。")
            return

        group_id = event.get_group_id()
        if not group_id:
            yield event.plain_result("⚠️ 无法获取群 ID，操作失败。")
            return

        raw = self.context.storage.get("subscribed_groups", "[]")
        try:
            subscribed_groups = set(json.loads(raw))
        except:
            subscribed_groups = set()

        if group_id not in subscribed_groups:
            yield event.plain_result("ℹ️ 本群未订阅 WebSocket 消息推送。")
        else:
            subscribed_groups.discard(group_id)
            self.context.storage.set("subscribed_groups", json.dumps(list(subscribed_groups)))
            logger.info(f"群 {group_id} 已取消订阅")
            yield event.plain_result("✅ 已取消订阅 WebSocket 消息推送。")

    async def terminate(self):
        '''插件停用时调用'''
        logger.info("WebSocket 订阅插件已停用")
from aiohttp import web

async def web_server():
    app = web.Application()
    bot = app['bot']
    app.router.add_get('/update_channel', bot.handle_web_request)
    return app

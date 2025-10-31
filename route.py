from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    content="""<html>
    <head>
        <title>Tech freak tamil</title>
    </head>
    <body style="background-color:black">
        <center>
        <h1>Welcome to Tech freak tamil web page</h1><br>
        <h2>join our channel for more Bots</h2><br>
        <a href="https://t.me/tech_freak_tamil"><button>Join now</button></a><br>
        <h2>This our file store bot</h2>
        </center>
        <style>
            h1,h2,h3{
                color: white;
                text-shadow: 0 3px 6px rgb(9, 240, 78);
            }
            button{
                padding: 15px 40px;
                font-size: 20px;
                font-weight: bold;
                color: white;
                background: #111;
                border: 2px solid #0f0;
                border-radius: 10px;
                cursor: pointer;
                text-transform: uppercase;
                transition: 0.3s;
                box-shadow: 0 0 20px #0f0, 0 0 40px #0f0 ;

            }
            button:hover{
                background: #0f0;
                color:#111;
                box-shadow: 0 0 30px #0f0, 0 0 60px #0f0 , 0 0 100px #0f0;
            }
        </style>
    </body>
</html>"""
    return web.Response(text=content, content_type="text/html")



async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


# Tech freak 
# Don't Remove Credit!!!
# Telegram Channel @Tech_freak_tamil
# Developer @devilo7
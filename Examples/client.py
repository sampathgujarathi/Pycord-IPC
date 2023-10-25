from quart import Quart
from ipc.client import Client

app = Quart(__name__)
ipc = Client(secret_key="🐼")

@app.route('/user/<user>')
async def main(user):
    resp = await ipc.request("get_user_data", user_id=user)
    return str(resp.response)

if __name__ == '__main__':
    app.run()
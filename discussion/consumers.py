import json

from channels import Group
from channels.auth import channel_session_user


@channel_session_user
def ws_connect(message):
    print 'connecting..'
    message.reply_channel.send({
        'accept': True
    })


@channel_session_user
def ws_receive(message):
    data = json.loads(message.content.get('text'))
    con_name = str(data.get('contest'))
    con_name=con_name.replace(" ","_")
    print con_name,'added'
    Group(con_name).add(message.reply_channel)
    message.channel_session['con_group'] = con_name

@channel_session_user
def ws_disconnect(message):

    print 'disconnecting..'
    user_group = message.channel_session['con_group']
    Group(user_group).discard(message.reply_channel)

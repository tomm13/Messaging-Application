# Chat-Application
A chat application made with guizero, asymmetric encryption and sockets.

This is a project I've been working on since Mid-July 2022. My goal is to create a chat system with both safety and simplicity in mind.

## Safety

The safety of the chat application and it's users are one of it's most important aspects. The use of RSA encryption in this
application sets to make it far more challenging to break into the server, or to retrieve contents of the chat.

This is an example of what a person without the correct 6-10 digit key would see upon joining:

<img width="327" alt="Screenshot 2022-09-02 at 00 44 49" src="https://user-images.githubusercontent.com/42684333/188030658-8926c360-68bb-4e0e-9403-973d85490b6b.png">

## Simplistic UI

The UI has had major reworks since it's creation. I alwats wanted the UI to be as simplistic as possible, and I believe I achieved that:

<img width="800" alt="Screenshot 2022-09-02 at 00 52 49" src="https://user-images.githubusercontent.com/42684333/188031308-15258e9f-ae63-4821-9e9c-f155fdf6f038.png">
<img width="1198" alt="Screenshot 2022-09-02 at 00 53 20" src="https://user-images.githubusercontent.com/42684333/188031311-ecd2b404-064a-4087-89bd-dced5a2d653c.png">

## Additional Details

### Animations

These were created to simplify the UI and enhance the UX. These vary from output messages of an action to disconnection messages to commands.

<img width="1200" alt="Screenshot 2022-09-02 at 00 56 57" src="https://user-images.githubusercontent.com/42684333/188031791-5846d169-c022-4846-a588-389bdb6aff0d.png">
<img width="1197" alt="Screenshot 2022-09-02 at 00 56 40" src="https://user-images.githubusercontent.com/42684333/188031789-c3f95df2-b7e7-4b5d-8488-aded0c76e777.png">

### Moderators

In order for the chatroom to stay civilised, moderators were created. As of *2nd September 2022* moderators can only kick non-moderators.

<img width="1198" alt="Screenshot 2022-09-02 at 00 57 18" src="https://user-images.githubusercontent.com/42684333/188032032-0da64295-25fe-4cef-aa04-f7fe4ce9b67d.png">

### Commands

Commands are an essential part of the code, especially with linking animations and messages. However they can also be used to display information or execute functions.

#### List of commands:
- `/space` - Shows the maximum server capacity
- `/online` - Shows the number of online users
- `/modonline` - Shows the number of moderators online
- `/users` - Shows every online user
- `/mods` - Shows every online moderator
- `/spaceleft` - Shows the remaining server capacity
- `/ip` - Shows IP
- `/port` - Shows Port
- `/key` - Shows RSA Decryption Key
- `/theme` - Switches between light mode and dark mode
- `/filler` - When on, displays a useful message every 15 seconds after the last animation. (eg. time, messages sent, commands to use)
- `/color <color>` - Switches text color to `<color>`
- `/save <location>' - Saves the chat history to `<location>`
- `/mod <user>` - Sends a request to give the moderator role to `<user>` 
- `/kick <user>` - Kicks `<user>`. Only valid if sent by a moderator

### Code Details

In order for the chat to be detecting for input whilst detecting for other users' messages, threads had to be implemented. In fact, most animations and listening functions are run on a thread so the main thread can detect input from the user, and send it when necessary.



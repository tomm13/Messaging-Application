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

### Moderators (or Mods)

In order for the chatroom to stay civilised, moderators were created. Moderators are chosen to remove any user they deem unfit, with the approval of other moderators in most situations.

#### Moderator benefits:

- A unique *khaki* color that cannot be used by non-moderators, applied from the borders of the window to the animation fadeins:

<img width="1198" alt="Screenshot 2022-09-02 at 00 57 18" src="https://user-images.githubusercontent.com/42684333/188032032-0da64295-25fe-4cef-aa04-f7fe4ce9b67d.png">

- Automatic switching from light mode to dark mode.

- The right to assign any non-moderator as a moderator:

<img width="1197" alt="Screenshot 2022-09-03 at 00 04 36" src="https://user-images.githubusercontent.com/42684333/188244864-2df61d82-463f-48b6-b03d-8c677bda9977.png">

- VoteKicking, which grants the moderator rights to kick non-moderators (when there is only 1 moderator), or to call a vote which all moderators could participate, in which 2 moderators must vote for or against the removal of a specific user. When a vote is called, the moderator that called the vote will automatically cast their vote in favour of the removal.



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
- `/color <color>` - Switches text color to `<color>`
- `/save <location>' - Saves the chat history to `<location>`
- `/mod <user>` - Sends a request to give the moderator role to `<user>` 
- `/kick <user>` - Kicks/Starts a vote to kick `<user>`. Only valid if sent by a moderator
- `/vote <for/against>` - When a vote is active, choose either <for> or <against>. Only valid as a moderator
- `/vote details` - When a vote is active, the details for moderators in favour of and against the vote will be shown.

### Inputs upon joining

This step may seem complicated at first, but is anything but. The guidelines for the 5 inputs are:

- Username must not be "", Username, or contain spaces. More importantly your username must not already exist in the database.
- Colors should be text such as "lightblue" or "red"
- IP should have dots joining the integers and must not contain spaces
- Port should be a 4-5 digit number that contains no spaces
- The priavte key should be in the format `12345, 67890` with variable length.

This is what happens when a user joins with an existing username:

<img width="1198" alt="Screenshot 2022-09-02 at 23 39 26" src="https://user-images.githubusercontent.com/42684333/188244333-7d4be191-60c7-4cdf-a41a-657e9571680e.png">

They are also halted from connecting to the server, and a blinking red alert will appear.

### Code Details

In order for the chat to be detecting for input whilst detecting for other users' messages, threads had to be implemented. In fact, most animations and listening functions are run on a thread so the main thread can detect input from the user, and send it when necessary.



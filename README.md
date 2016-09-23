# 21.co-BitMon
A Bitcoin-powered MMORPG in the style of a large entertainment company's wildly popular intellectual property!

What is this?
--
BitMon will be a text-based MMO in which you battle other players, trade your bit-sized monsters, and train them up so that you can become the ultimate Monster Master!

What is done so far?
--
So far, you can only register your account username and password, log-in, and select your starting monster. Anyone who registers in this premature stage will be given a bonus 4000 BitCreds (in-game currency) on top of the usual, release-time registration bonus of 1000 BitCreds.

(Please note, that this game relies on the [21.co](https://21.co) platform, and only users of 21 will be able to register/play.)

How can I get it?
--
First, install the [21.co](https://21.co) software:
```
curl https://21.co | bash
```
Follow the instructions there to log-in and join the market. Then, download and run the BitMon client:
```
wget -O bitmon-client.py http://21.browntech.space:8383/client && python3 bitmon-client.py
```

What is planned?
==
Monsters
--
The plan is to incorporate at least 50 unique monsters with their own types, base stats, and attacks for users to collect, train and battle.
Battles
--
Battle will be done in a turn-based menu, and player-versus-player battles will be possible. However, these battles will require players to check up on their "Battles" page. Player-versus-player battles will require players to place a wager of 10% of their current BitCredits balance. The losing player will pay the winning player that wager. Random encounters will have a chance of occurring every time the player makes a "move" from one square on the map to the next. When presented with a random encounter, players can either attempt a capture if they have any BitTraps and earn experience for the player or send out one of their own monsters to fight against it, earning experience for the monster.
Experience
--
There are two types of experience, both contributing to "leveling up". Player experience is earned by winning player battles, capturing monsters, and leveling up own monsters. Player level contributes to success rate when attempting a capture, as well as applying discounts at the item shops scattered throughout the map. Monster experience is earned whenever a monster defeats another in a random encounter. As monsters level up, their stats increase.
Perma-death
--
If a monster is defeated in battle, that monster is removed from the player's roster. There are no revive items, there are no phoenix downs. This is not a bug. This not because of lazy development. This is an intended feature and will negatively impact the player's experience points. This means you *can* decrease in player level. I want to keep you guys on your toes.
Trading
--
Similar to battles, players will have access to a "Trading" menu. Each trade will cost each player involved 300 BitCredits. Players will be able to put up one of their captured monsters for trade with a specific trade in mind. Anyone viewing the trades board will be able to swap out their monster for one of the ones available for trade. Example:
```
There are no trades available.
AwesomePlaya puts Yursba up for trade for Jotunmar
MrTrainer visits Trading Board
MrTrainer takes Yursba from AwesomePlaya
AwesomePlaya receives Jotunmar from MrTrainer
There are no trades available.
```
Items
--
The game will have several items available to purchase in the item shop. These items will recover the HP of your monsters, temporarily boost a statistic, or change the rate of capture during wild encounters.
BitCredits
--
BitCredits are used to engage in player battles, trade monsters, and purchase items. BitCredits can be purchased from the system at an exchange rate of 3 satoshis per BitCredit. They can also be sold back to the system at a 1:1 exchange. You can also earn more BitCredits by winning player battles, or conquering special encounters.
Special Encounters
--
Throughout the map, there will be 10 "special encounters". This will involve an NPC mimicking a player battle with the player, and the player will have to defeat between 3 and 6 high-level monsters. These special encounters will award high amounts of BitCredit and player experience, as well as earn a medal for the player. Each special encounter can only be completed once.
How can I help?
==
Anyone who would like to help is welcome to fork the main code and start adding blocks to it. I'm only one guy, and I've got a rather busy work/academic/personal life. Any help would be greatly appreciated, and might possibly be rewarded with a digital high-five (If I had money, I swear I'd give it.)


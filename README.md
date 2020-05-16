# Allen Ginsberg Bot Flock

[ginsberg bot flock twitter list](https://twitter.com/charlesreid1/lists/ginsbergbotflock)

The Allen Ginsberg Bot Flock is a flock of Twitter bots
tweeting Allen Ginsberg poems in perpetuity.

`bot/` contains the code for the bot flock.

`pelican/` contains the Pelican files used to generate [the project web page](http://charlesreid1.github.io/ginsberg).

See [the project web page](http://charlesreid1.github.io/ginsberg) for more information,
or browse through the code.

## List of Bot Accounts

[Ginsberg Bot Flock members list](https://twitter.com/charlesreid1/lists/ginsbergbotflock/members)

## Required Software

This bot flock utilizes [rainbow-mind-machine](https://github.com/rainbow-mind-machine/rainbow-mind-machine),
the extensible bot flock framework authored by yours truly.

## Required Twitter Setup

You will need to set up some Twitter accounts for your bots, obviously.
Set up a new Gmail account, create a Google Voice number, and use that 
as a phone number if Twitter demands a phone number from you.
(Twilio phone numbers _will not work_ for Twitter registration. Don't blow $1.)

You will also need a bot-master account. This acount will be associated with
your application. You can have one bot-master that runs all of your bot flocks
under the same application, even if they are different flocks running on 
different machines.

You will need to create a Twitter app through the bot-master account.
This step must be done prior to running the bot.
This will give you a consumer token and a consumer secret token.

**Captain Obvious sez:** you should keep your consumer secret token a secret!

## Consumer Token and Secret

This section assumes you now have your consumer token and consumer secret token.

Put these in the file `bot/apikeys.json` as two key-value pairs, like so:

```
{
    "cosumer_token": "AAAAAAAAAAAAA",
    "consumer_token_secret": "BBBBBBBBB"
}
```

## Where Do I Put My Keys

Your keys should go in the same directory as
the bot script and (optionally) any data or 
external files used to initialize each bot.

For example:

```
bot/
    GinsbergBotFlock.py
    apikeys.json
    data/
        account1.txt
        account2.txt
        account3.txt
        ...
    keys/
        account1.json
        account2.json
        account3.json
        ...
```

While you can put the keys anywhere you'd like,
this is the recommended layout.

## Where Do I Put My apikeys.json

The file `apikey.json` should go next to `GinsbergBotFlock.py`:

```
bot/
    GinsbergBotFlock.py
    apikeys.json
    data/
        ...
    keys/
        ...
```


## Running The Bot Flock

(Note: take care of `apikeys.json` before you begin.)

Running the bot flock is a two-step process:

1. (One time) Authorize the program to tweet on behalf of your account 
    (i.e., log in with each user account). This requires `apikeys.json` be present
    next to your bot flock program. This step generates key files (JSON format).

2. Run the bot flock. Tweet! Sleep! Repeat!

Either way, run it with Python:

```
$ cd bot/
$ python GinsbergBotFlock.py
```


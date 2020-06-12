Betty
=====

.. image: https://github.com/Circlepuller/betty/workflows/build/badge.svg
   :alt Build status

Betty will help you locate anime and manga on MyAnimeList.net, *I suppose*.

This repository has batteries included, so you can easily deploy to Heroku or a dedicated Linux machine with minimal
configuration necessary.

Installation
------------

To install Betty, clone this repository, create a Python 3 virtual environment, and install dependencies like so:

.. code: sh

    git clone git@github.com:Circlepuller/betty.git
    cd betty
    python3 -m venv bot-env
    source bot-env/bin/activate
    pip install -r requirements.txt

Next, create a ``.env`` file where configuration data is stored. Make sure to keep it secure! You'll at the least need
a Discord bot token. Check out the Discord Developer Portal's
`Documentation page <https://discord.com/developers/docs/intro>` for more information on getting the Discord bot token.

.. code: sh

    BOT_TOKEN=discord-bot-token

Finally, start your bot by doing the following:

.. code: sh

    python betty.py

A message will appear once Betty has successfully conntected to Discord, *I suppose*. Now that you've successfully
installed Betty, you may want to deploy it - which can currently be done one of two ways.

Dedicated server or VPS (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The process of deploying Betty to a dedicated server or VPS is similar to a local machine. Once you've set Betty
up on your server, you can use the provided SystemD service, ``extra/betty.service`` to daemonize your bot and keep it
running.

Heroku
~~~~~~

Alternatively, you can deploy Betty to Heroku via the provided ``Procfile`` and ``runtime.txt``. Be aware that Heroku's
free plan will sleep the bot process if Betty's web frontend is not accessed every hour. Make sure to set ``BOT_TOKEN``
in your app's configuration. Support for Heroku will likely be removed in the future.
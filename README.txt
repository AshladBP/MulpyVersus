MulpyVersus - Wrapper for MultiVersus API
=========================================

::

   This library will help you to use the MultiVersus API with Python easily.
   It is still under development, please report any issue you encounter.

.. image:: https://cdn.discordapp.com/attachments/361240816397582336/1006703539365617674/mulpyversus.png
   :alt: mulpyversus

Usage
=====

With this version, you will need a **Steam Ecrypted App Ticket**. You
get get yours
`here <https://github.com/brianbaldner/multiversus-api-docs/tree/main/steam-ticket-generator>`__.
*Future* version should include **the possibility to use an API that
doesn't require any sort of token**.

Get the API working
-------------------

Initializing the MulpyVersus class is the first step. With this object,
you will be able to call any search function.

::

   mlp = MulpyVersus("youSteamEcryptedAppTicket")

By giving your Steam Ecrypted App Ticket, your access_token will
automatically be refreshed whenever it is no longer valid. **So no need
to manually change it every 24h !**

# To use a custom emoji in your Discord Embed, you need to make sure the emoji is accessible in the server the bot is deployed on. Here are the steps to achieve this:

# 1. Ensure that the emoji is uploaded to the server: Custom emojis are specific to each server and can be uploaded by someone with the "Manage Emojis" permission. Make sure the emoji you want to use is uploaded to the server where the bot is present.

# 2. Get the custom emoji's ID: Right-click on the custom emoji in a chat message and select "Copy Link" or "Copy Link Address" (the option may differ based on your Discord client). The copied link should look like this: `https://cdn.discordapp.com/emojis/EMOJI_ID.png`.

# 3. Use the custom emoji's ID in your code: Instead of using the emoji name (like `:YellowCred:`), you should use the emoji ID in your `discord.Embed()` call. For example:

# ```python
embed = discord.Embed(title="<:emoji_name:emoji_id> This is a custom emoji")
# ```

# Replace `emoji_name` with the actual name of the emoji, and `emoji_id` with the ID you obtained from the link.

# Note: Discord Nitro is not required to use a custom emoji in an Embed. As long as the emoji is accessible in the server where the bot is present, you can use it in your Embeds.
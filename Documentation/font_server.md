# Font Server

Getting ideas down for building a font server application.

## Problem

The problem we currently have is there's not good way to manage non-system fonts on a users computer. The current way we install fonts and managed fonts is by purchasing the fonts, downloading them locally, creating an installer package(.pkg) and handing that installer off the the user to install. Once the install is complete we ask the user to delete the installer. 

This isn't a great solution. If for whatever reason we can't use a font anymore there's not an easy way to rmeove that font so it can't be used. Furthermore there's not an easy way for people to get a new font on their computer or for us to deploy a new font to their computer. 

## Solution

Font servers exist(see [Universal Type Server](https://www.extensis.com/universal-type-server)) but they can be very expensive.

The idea here is to build our own that fits the needs that we have. Things like Universal Type Server may have a lot of features we will never use. 

Simply put I think a Django application will be suitable. Django provides a good admin interface that allows us to manage permissions such as various groups and users. Since Django is built with and utilizes Python, we're already in "familiar" territory.  

This web server would sit in AWS(EC2?) with the fonts living in an S3 bucket or something more reasonable since fonts don't need that much storage space. 

The server should be able to check-in and out fonts to users using a desktop app[1] who have access to the server[2].

#### Example permission structure

The model below defines a `Font` or a group of fonts, that font or group of fonts has a related `Access group` this access group contains a `Team group`(i.e. "mtos"), the team group contains the individual users. 

This way we can manage access to fonts via groups vs. assigning a single font to an individual. Of course there will be edge cases and that can be worked out later. 
```
Font
|
|__ Access group
	|
	|__ Team group
		|
		|__ Individual user
```

[1] See font_client.md to details on the desktop application. 
[2] Django allows you to create users and assign permissions out of the box. We just need to build out those permissions schemes.  


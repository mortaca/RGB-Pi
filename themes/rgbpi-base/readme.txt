=== EmulationStation Theme: Eudora ===
Eudora is a clean theme that displays both large preview images and all title-oriented metadata.  Eudora was also built to be easily modified, as demonstrated by the advanced features described below.

In the base theme, both portrait and landscape image layouts are used in order to best fit the preview images for a variety of systems.  A best-guess has been made for each system based on the shape of its typical preview image, or its games' box art.

All user-oriented metadata; rating, last played timestamp, and play count, have been omitted from the base theme and all variants.


== Variant: Eudora Concise ==
The Concise variant omits the description text.  A single layout is used with an image area similar to the base theme's, but squared.


== Variant: Eudora Bigshot == 
The Bigshot variant omits all metadata and uses a single layout with a large preview image.  The game list is also wider in this variant.



=== Preview Image Size ===
Since Eudora uses bigger preview images than normal, you may wish to set your scraper to pull larger image files.  If you are using sselph's scraper, you can use the -max_width parameter to do this, matching the width of each system's layout.

Rough maximum sizes are as follows for each layout template:
Portrait:	400x600px
Landscape: 	600x400px
Concise: 	600x600px
Bigshot: 	745x745px



=== Advanced Feature: Color Sets ===
Eudora comes with 13 different color sets, allowing you to easily change the look of the theme.  The Monodark color set is used by default.  To use a different color set, edit eudora/colorset.xml, and point the <include> tag at any of the xml files in eudora/common/colorsets/.

For example, to use the monolight color set, change:
<include>./common/colorsets/monodark.xml</include>
	to
<include>./common/colorsets/monolight.xml</include>

Creating new color sets is really simple, as there is only one file to edit.  Just make a copy of an existing colorset xml file, rename it, and edit away.  That one file is all you need.

Some system logos may look bad with certain color sets.  Better support for the .svg stroke property in EmulationStation would help but, until that happens, there's not much to do about this other than to change the logo or the color set.



=== Advanced Feature: Templates ===
In Eudora, all of the information for the Portrait, Landscape, Concise, and Bigshot layouts is contained in templates.  The system-specific xml just determines which template is used.  This means it's very easy to change, or to mix and match, layouts.

For example, if you're using the base theme, but you want MAME to use the Landscape layout instead of the Portrait layout, just edit eudora/mame/theme.xml and change this line:

<include>./../common/templates/portrait.xml</include>	
	to
<include>./../common/templates/landscape.xml</include>

Everything else, including the colorset, should apply to the new layout automatically.  You can also set a system to Concise or Bigshot in this way.  All of these templates are included with each of the theme variants.



=== Credits ===
All xml, all sounds, and some images created by AmadhiX.

Based on the "Carbon" theme by Eric Hettervik, which is in turn based on "Simple" by Nils Bonenberger.  Most system logos and line art images are borrowed from these themes.

The background images "Binding Dark" and "Binding Light" are by Tia Newbury, from www.subtlepatterns.com, used under the CC-BY-SA 3.0 license.

The background images "Stardust Dark" and "Stardust Light" are based on "Stardust" by Atle Mo, from www.subtlepatterns.com, used under the CC-BY-SA 3.0 license.

The following fonts are used under the licenses included with the font files:
"Lato Regular" and "Lato Black" by Lukasz Dziedzic.
"Open Sans" by Google.
"Adobe Blank" maintained by Dr. Ken Lunde.

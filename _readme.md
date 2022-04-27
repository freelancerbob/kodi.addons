# Install
https://github.com/drinfernoo/repository.example/blob/master/README.md

### Vytvorenie kodi repozitara
- vytvoris si adresar pre repository addon `repository.myaddons`
	- obsahuje `addon.xml`, ktoreho `addon id` musi byt rovnake ako adresar `repository.myaddons`

```XML
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addon id="repository.myaddons" name="[COLOR limegreen][B]myAddons[/B][/COLOR]Wizard Repository" version="0.0.2" provider-name="myaddons">
    <extension point="xbmc.addon.repository" name="[COLOR limegreen][B]myAddons[/B][/COLOR]Wizard Repository">
        <dir>
            <info compressed="false">https://raw.githubusercontent.com/freelancerbob/kodi.addons/main/zips/addons.xml</info>
            <checksum>https://raw.githubusercontent.com/freelancerbob/kodi.addons/main/zips/addons.xml.md5</checksum>
            <datadir zip="true">https://raw.githubusercontent.com/freelancerbob/kodi.addons/main/zips/</datadir>
        </dir>
    </extension>
    
    <extension point="xbmc.addon.metadata">
        <summary>[COLOR limegreen][B]mojeAddonySummary[/B][/COLOR]Wizard</summary>
        <description>The official home of [COLOR limegreen][B]mojeAddonyDescription[/B][/COLOR]Wizard.</description>
        <disclaimer>None</disclaimer>
        <platform>all</platform>
        <assets>
            <icon>icon.png</icon>
            <fanart>fanart.jpg</fanart>
        </assets>
        <source>https://github.com/freelancerbob/kodi.addons</source>
    </extension>
</addon>
```
	- 

### Vytvorenie kodi addonu a zaradenie do repozitara
- vytvoris si adresar pre kodi addon `plugin.video.helloworld.bob`
- v nom vytvoris `addon.xml` a vydefinujes `id` rovnake ako nazov foldra `plugin.video.helloworld.bob`

```XML
<addon id="plugin.video.helloworld.bob" name="helloWorld.bob" provider-name="freelancerbob" version="0.0.4">
  <requires>
    <import addon="xbmc.python" version="3.0.0"/>
    <import addon="inputstream.adaptive" version="19.0.0"/>
  </requires>
  <extension library="main.py" point="xbmc.python.pluginsource">
    <provides>video</provides>
  </extension>
  <extension point="xbmc.addon.metadata">
    <summary lang="cs_CZ">Ahoj Svet</summary>
    <description lang="cs_CZ">
Prvy addon
    </description>    
    <platform>all</platform>
    <source>https://github.com/freelancerbob/plugin.video.helloworld.bob</source>
    <news>
v1.0.0
- prva verzia
    </news>

  </extension>
</addon>

```
### Automaticke vytvorenie suborov a addonov v adresari zip
- script `_repo_xml_generator.py` vytvori v adresari `zip` potrebne subory:
	- `addons.xml`, `addons.xml.md5`
	- adresare so zip subormi `repository.myaddons`, `plugin.video.helloworld.bob`
### Finalna struktura
```
project
│   README.md
│   _repo_xml_generator.py  
│
└───plugin.video.helloworld.bob
└───repository.myaddons
└───zip
│   │   addons.xml.md5
│   │   addons.xml
│   │
│   └───repository.myaddons
│   │      addon.xml
│   │      repository.myaddons-0.0.2.zip
│   │      repository.myaddons-0.0.1.zip
│   │      icon.png
│   │      fanart.jpg
│   │ 
│   └───plugin.video.helloworld.bob
│         addon.xml
│         plugin.video.helloworld.bob-0.0.4.zip
│         plugin.video.helloworld.bob-0.0.3.zip
│         plugin.video.helloworld.bob-0.0.2.zip
│         icon.png
```

### Ako to funguje ?
- 1a) Zalozis si `Github Pages` (alebo iny web server)a na hlavnu stranku daj:
	- `index.html` ktory obsahuje repository.myaddons-0.0.1.zip zo zip suboru 
		```html
		<a href="repository.myaddons-0.0.1.zip">repository.myaddons-0.0.1.zip</a>
		```
	- nahraj `repository.myaddons-0.0.1.zip` na priamo na domovsku stranku, pripadne do hrefu daj cely cestu.
- 1b ) Alebo `repository.myaddons-0.0.1.zip` nahras priamo do KODI
- <span style="color:red">Ak budes chciet updatnut addony s novou funkcionalitou tak nezabudni vzdy povysit verziu aj na repozitari, addone. Potom treba spustit `_repo_xml_generator.py` , ktory vytvori nove zip subory do prislusnych zloziek</span>
- cez git vzdy pushni zmeny


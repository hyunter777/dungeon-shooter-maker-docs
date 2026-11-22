# Dungeon Shooter Maker

Dungeon Shooter Maker is a toolkit for making top-down, room-by-room dungeon shooters in Unity without writing
code. Guns, items, enemies, bosses, rooms, floors and the reward economy are all data, edited in dedicated windows
and tested with one click.

<!-- TODO(screenshot): Project Overview window, saved as assets/images/overview.png -->

## What ships with the package

The package ships with a complete sample game: **4 floors and a camp lobby, 4 heroes, 16 guns, 24 items, 12 enemies
and 6 bosses, 12 synergies, 38 upgrades, 33 rooms, chests, shops and shrines**. Change it, or use it as a reference for your own game.

Everything is a ScriptableObject asset in `Assets/DungeonShooterMaker/Content/Default/` and is listed in the
**Content Database** (`Resources/DungeonShooterMaker/DefaultContent`). Editors create, rename, duplicate and delete
those assets for you and keep the database list up to date.

## Start here

1. Follow the [quick start](quick-start.md) to play the sample and change one value.
2. Learn what each window makes in [The editors](editors.md).
3. Set the run's rules, offers, elites and lobby in [Run rules and progression](run-rules.md).
4. Build enemies, rooms, floors, props and mini-bosses in [Content and gameplay](content.md).
5. Add tracks, sounds and effect animations in [Music and sound](music-sfx.md).
6. Check tests, Project Check and common problems in [FAQ and troubleshooting](faq.md).

## Tested environment

- Unity 6 (the sample project is on **6000.0.47f1**) with the Universal Render Pipeline (**URP 17.0.4**).
- Heroes, enemies, guns, effects and UI frames ship as sprite sheets; floors, walls and props are drawn from small
  pixel maps in code. Your own sprites are optional (see [Your own art](editors.md#your-own-art)).
- Game text uses the pixel font **Galmuri** (Galmuri7, Galmuri9, Galmuri11 Bold, English and Korean), which may ship
  with your game under the SIL Open Font License. See [Support and licenses](support.md).

## How the manual is organised

- **Start here** — welcome and quick start.
- **Making your game** — the editor windows, run rules, content and gameplay, music and sound.
- **Help** — testing, Project Check, design notes, FAQ and support.

The pages are maintained prose taken from the package's `Documentation/UserGuide.md`; building this site does not
require Unity or the product source.
